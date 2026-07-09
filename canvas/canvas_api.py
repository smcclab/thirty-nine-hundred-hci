"""Minimal Canvas LMS API client for the HCI 3900 course tooling.

Standard library only (matches the repo's other scripts). Reads the API token
from, in order of precedence:

  1. the CANVAS_TOKEN environment variable, or
  2. the file ~/.config/canvas/anu-token (chmod 600 recommended).

The token is NEVER stored in this repository.

Base URL defaults to https://canvas.anu.edu.au and can be overridden with the
CANVAS_API_URL environment variable. The course id defaults to 11488 (HCI 3900
Semester 2 2026) and can be overridden with CANVAS_COURSE_ID.
"""

import json
import mimetypes
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

DEFAULT_BASE_URL = "https://canvas.anu.edu.au"
DEFAULT_COURSE_ID = "11488"
TOKEN_FILE = Path.home() / ".config" / "canvas" / "anu-token"


def get_token():
    token = os.environ.get("CANVAS_TOKEN")
    if token:
        return token.strip()
    if TOKEN_FILE.exists():
        return TOKEN_FILE.read_text().strip()
    sys.exit(
        f"No Canvas token found. Set CANVAS_TOKEN or write your token to {TOKEN_FILE}.\n"
        "Create one in Canvas: Account -> Settings -> Approved Integrations -> "
        "'+ New Access Token'."
    )


def base_url():
    return os.environ.get("CANVAS_API_URL", DEFAULT_BASE_URL).rstrip("/")


def course_id():
    return os.environ.get("CANVAS_COURSE_ID", DEFAULT_COURSE_ID)


class Canvas:
    def __init__(self, token=None):
        self.token = token or get_token()
        self.base = base_url()

    def _auth_header(self):
        return {"Authorization": f"Bearer {self.token}"}

    def request(self, method, path, params=None, data=None, headers=None):
        """Call the Canvas REST API. `path` may be absolute or relative to /api/v1."""
        if path.startswith("http"):
            url = path
        else:
            url = f"{self.base}/api/v1/{path.lstrip('/')}"
        if params:
            url += "?" + urllib.parse.urlencode(params, doseq=True)
        body = None
        req_headers = self._auth_header()
        if data is not None:
            body = urllib.parse.urlencode(data, doseq=True).encode()
            req_headers["Content-Type"] = "application/x-www-form-urlencoded"
        if headers:
            req_headers.update(headers)
        req = urllib.request.Request(url, data=body, method=method, headers=req_headers)
        try:
            with urllib.request.urlopen(req) as resp:
                raw = resp.read()
                link = resp.headers.get("Link")
                payload = json.loads(raw) if raw else None
                return payload, link
        except urllib.error.HTTPError as e:
            detail = e.read().decode(errors="replace")
            sys.exit(f"Canvas API {method} {url} -> {e.code} {e.reason}\n{detail}")

    def get(self, path, params=None):
        return self.request("GET", path, params=params)

    def get_all(self, path, params=None):
        """GET with pagination, returning the concatenated list of results."""
        params = dict(params or {})
        params.setdefault("per_page", 100)
        results = []
        payload, link = self.get(path, params=params)
        if isinstance(payload, list):
            results.extend(payload)
        else:
            return payload
        while link:
            next_url = _next_link(link)
            if not next_url:
                break
            payload, link = self.get(next_url)
            if isinstance(payload, list):
                results.extend(payload)
            else:
                break
        return results

    # -- File upload (3-step Canvas flow) ------------------------------------

    def upload_file(self, local_path, folder_path=None, parent_folder_id=None,
                    on_duplicate="overwrite", display_name=None):
        """Upload a file to a course folder.

        Target the folder either by `parent_folder_id` (preferred — unambiguous)
        or by `folder_path` (relative to the course root "course files", created
        if missing). Exactly one should be given.

        Uses on_duplicate='overwrite' so re-uploading the same filename replaces
        the existing file *in place*, preserving its Canvas file id (and therefore
        any module items / page links pointing at it). Returns the final file JSON.
        """
        local_path = Path(local_path)
        size = local_path.stat().st_size
        name = display_name or local_path.name
        content_type = mimetypes.guess_type(str(local_path))[0] or "application/octet-stream"

        data = {
            "name": name,
            "size": size,
            "content_type": content_type,
            "on_duplicate": on_duplicate,
        }
        if parent_folder_id is not None:
            data["parent_folder_id"] = parent_folder_id
        elif folder_path is not None:
            data["parent_folder_path"] = folder_path
        else:
            raise ValueError("Provide either parent_folder_id or folder_path")

        # Step 1: notify Canvas of the pending upload.
        step1, _ = self.request("POST", f"courses/{course_id()}/files", data=data)
        upload_url = step1["upload_url"]
        upload_params = step1["upload_params"]

        # Step 2: POST the file as multipart/form-data to the returned upload_url.
        # upload_params fields MUST come before the file field.
        with open(local_path, "rb") as fh:
            file_bytes = fh.read()
        body, ctype = _multipart(upload_params, "file", name, content_type, file_bytes)
        req = urllib.request.Request(upload_url, data=body, method="POST",
                                     headers={"Content-Type": ctype})
        # Do not attach the Canvas auth header to the (often S3/inst-fs) upload_url.
        try:
            with urllib.request.urlopen(req) as resp:
                code = resp.getcode()
                location = resp.headers.get("Location")
                raw = resp.read()
        except urllib.error.HTTPError as e:
            sys.exit(f"File upload POST failed: {e.code} {e.reason}\n{e.read().decode(errors='replace')}")

        # Step 3: confirm. inst-fs may return the file JSON directly (201), or a
        # 3xx redirect to a confirmation URL that must be GET'd with the token.
        if location:
            payload, _ = self.get(location)
            return payload
        if raw:
            return json.loads(raw)
        return {"status": code}


def _next_link(link_header):
    for part in link_header.split(","):
        segs = part.split(";")
        if len(segs) < 2:
            continue
        url = segs[0].strip().strip("<>")
        for rel in segs[1:]:
            if rel.strip() == 'rel="next"':
                return url
    return None


def _multipart(fields, file_field, filename, content_type, file_bytes):
    boundary = uuid.uuid4().hex
    crlf = b"\r\n"
    out = []
    for key, value in fields.items():
        out.append(b"--" + boundary.encode())
        out.append(f'Content-Disposition: form-data; name="{key}"'.encode())
        out.append(b"")
        out.append(str(value).encode())
    out.append(b"--" + boundary.encode())
    out.append(
        f'Content-Disposition: form-data; name="{file_field}"; filename="{filename}"'.encode()
    )
    out.append(f"Content-Type: {content_type}".encode())
    out.append(b"")
    out.append(file_bytes)
    out.append(b"--" + boundary.encode() + b"--")
    out.append(b"")
    body = crlf.join(out)
    return body, f"multipart/form-data; boundary={boundary}"
