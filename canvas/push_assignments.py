"""Push assessment / workshop text to the Canvas Assignment pages.

This replaces the manual loop of "edit the markdown, `make html`, open the built
page, copy the body, paste it into the Canvas rich-content editor".

Strategy:

  * Canvas stores an assignment description as an HTML **fragment** — no <html>,
    <head> or <body> wrapper, and no title (the assignment name provides that).
    `make canvas-html` builds exactly that: pandoc without --standalone. The
    existing descriptions in course 11488 are pasted pandoc output, so the tag
    and attribute vocabulary pandoc emits (figure/figcaption, section, div,
    span, id/class/role/data-* attributes, inline styles on table colgroups)
    all survives Canvas's HTML sanitiser unchanged. Verified against the live
    2025 pages, which round-trip through this script with an empty diff.

  * Images are the one thing that cannot survive verbatim. The markdown says
    `img/foo.jpg`, which means nothing to Canvas, so at push time each local src
    is resolved to a Canvas file (matched by *display name*) and rewritten to
    the same absolute /files/<id>/preview?verifier=... form that Canvas's own
    editor produces. A local image with no counterpart on Canvas is uploaded to
    the fallback folder first. Rewriting happens here rather than in the
    Makefile because only this script knows the Canvas file ids.

  * Assignments are DISCOVERED BY NAME, not by id, so the mapping below keeps
    working across the yearly course copy (which renumbers everything). The
    names are the ones a student sees, so if you rename an assignment in Canvas
    you must rename it here too — the script fails loudly rather than guessing.

  * Only the description is touched. Due dates, points, submission types and
    publication state are left exactly as they are; the due date is *compared*
    against the "Due date" bullet in the markdown and a mismatch is reported,
    but never written.

Usage:
    python canvas/push_assignments.py --list           # mapping + live status
    python canvas/push_assignments.py --dry-run        # diff, change nothing
    python canvas/push_assignments.py                  # overwrite descriptions
    python canvas/push_assignments.py --only 01-prototyping
    python canvas/push_assignments.py --only workshops # whole directory

Run `make canvas-assignments-dry` / `make canvas-assignments` to build the
fragments first. Environment: CANVAS_TOKEN / CANVAS_API_URL / CANVAS_COURSE_ID
(see canvas_api.py).
"""

import argparse
import datetime as dt
import difflib
import html
import re
import sys
import urllib.parse
from pathlib import Path

from canvas_api import Canvas, base_url, course_id

REPO_ROOT = Path(__file__).resolve().parent.parent
CANVAS_OUT = REPO_ROOT / "build" / "canvas"
# Every push writes the pre-push description here first, so a bad push can be
# undone by pasting the saved HTML back into Canvas. Under build/, so `make
# clean` clears it — copy anything you want to keep.
BACKUP_DIR = CANVAS_OUT / "backup"

# Folder used when a local image is not on Canvas yet. Matches push_lectures.py
# and where the 2025 course copy put its media.
FALLBACK_FOLDER_PATH = "Uploaded Media 2"

# source markdown (repo-relative) -> Canvas assignment name.
#
# The Canvas names are NOT derivable from the markdown titles ("AI Needs
# Finding" is "Assignment 2: User Research" on Canvas; workshop N is Week N+1),
# so the mapping is explicit. Confirmed against the live course on 2026-08-02 by
# comparing heading sets between each built fragment and each description.
ASSIGNMENT_MAP = [
    ("assessments/00-pre-and-in-class-tasks.md", "Pre and In-Class Task Instructions"),
    ("assessments/01-prototyping.md", "Assignment 1: Prototyping"),
    ("assessments/02-needs-finding.md", "Assignment 2: User Research"),
    ("assessments/03-prototype-and-evaluation.md",
     "Final Project: Prototype Design and Research Project"),
    ("workshops/01-making.md", "Week 2: Making"),
    ("workshops/02-scenarios.md", "Week 3: Personas and Scenarios"),
    ("workshops/03-prototyping.md", "Week 4: Prototyping"),
    ("workshops/04-interviews.md", "Week 5: Interviewing"),
    ("workshops/05-surveys.md", "Week 6: Surveys"),
    ("workshops/06-thematic-analysis.md", "Week 7: Thematic Analysis"),
    ("workshops/07-evaluation.md", "Week 8: Planning Evaluations"),
    ("workshops/08-research-design.md", "Week 9: Research Design"),
    ("workshops/09-prototyping-2.md", "Week 10: More Prototyping"),
    ("workshops/10-analysis-2.md", "Week 11: From Theme to Implication"),
]

# Australian eastern time, for checking the markdown due date against Canvas.
TZ_OFFSETS = {"AEST": 10, "AEDT": 11}
DUE_RE = re.compile(
    r"\*\*Due date\*\*:\s*(\d{4}-\d{2}-\d{2})\s+(\d{2}):(\d{2})\s*(AEST|AEDT)")


# -- Fragment tidying --------------------------------------------------------

LEADING_H1_RE = re.compile(r"\A\s*<h1\b[^>]*>(.*?)</h1>\s*", re.I | re.S)
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)


def strip_comments(fragment):
    """Remove HTML comments. Returns (html, count).

    Pandoc passes markdown HTML comments straight through, so commented-out
    draft tasks would ship inside the Canvas page source — invisible on the
    page, but readable by anyone who views source, which is not what "commented
    out" is meant to mean. Canvas's sanitiser drops them on save anyway, so
    leaving them in would also make every subsequent dry run report a change
    that can never be applied.
    """
    return COMMENT_RE.subn("", fragment)


def strip_leading_h1(fragment):
    """Drop a leading <h1>, which Canvas already shows as the assignment name.

    Every workshop source opens with a `# Title` heading that repeats the
    frontmatter title. That reads correctly on the built website, but on Canvas
    it would sit directly under the assignment name saying the same thing — so
    the hand-pasted pages all dropped it, and so do we. Returns (html, title).
    """
    match = LEADING_H1_RE.match(fragment)
    if not match:
        return fragment, None
    title = re.sub(r"<[^>]+>", "", match.group(1)).strip()
    return fragment[match.end():], title


# -- Image rewriting ---------------------------------------------------------

IMG_TAG_RE = re.compile(r"<img\b[^>]*>", re.I)
SRC_RE = re.compile(r'\bsrc\s*=\s*"([^"]*)"', re.I)


def canvas_image_attrs(base, cid, file_obj):
    """Build the src/data-api-* attributes Canvas's own editor writes for a file.

    The verifier is a stable per-file token (it is the same one embedded in the
    file's `url`), and it is what the existing hand-pasted pages carry, so
    reproducing it keeps the dry-run diff free of spurious image churn.
    """
    fid = file_obj["id"]
    verifier = None
    url = file_obj.get("url") or ""
    if url:
        qs = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
        verifier = (qs.get("verifier") or [None])[0]
    src = f"{base}/courses/{cid}/files/{fid}/preview"
    if verifier:
        src += "?" + urllib.parse.urlencode({"verifier": verifier})
    endpoint = f"{base}/api/v1/courses/{cid}/files/{fid}"
    return src, endpoint


def rewrite_images(fragment, source_dir, resolve_file):
    """Point every local <img src> at its Canvas file. Returns (html, [names])."""
    used = []

    def fix(match):
        tag = match.group(0)
        src_match = SRC_RE.search(tag)
        if not src_match:
            return tag
        src = html.unescape(src_match.group(1))
        if src.startswith(("http://", "https://", "data:", "//")):
            return tag
        local = (source_dir / src).resolve()
        file_obj = resolve_file(local)
        if file_obj is None:
            print(f"    ! image not found locally or on Canvas: {src}", file=sys.stderr)
            return tag
        used.append(file_obj["display_name"])
        new_src, endpoint = canvas_image_attrs(base_url(), course_id(), file_obj)
        tag = SRC_RE.sub(lambda _: f'src="{html.escape(new_src, quote=True)}"', tag, count=1)
        # Canvas's editor attaches these; they let the RCE recognise the embed
        # as a course file if the page is ever edited by hand afterwards.
        tag = re.sub(r'\s*/?>$', "", tag)
        tag += (f' data-api-endpoint="{html.escape(endpoint, quote=True)}"'
                f' data-api-returntype="File" />')
        return tag

    return IMG_TAG_RE.sub(fix, fragment), used


# -- Normalisation, for diffing against what Canvas stored -------------------
#
# Canvas re-serialises whatever it is given: it drops the XHTML self-closing
# slash, reorders attributes, and adds loading="lazy" to images. None of that is
# a content change, so a raw diff of ours-vs-theirs is all noise. Normalising
# both sides the same way makes the dry-run diff show only real edits.

# Entities Canvas decodes to literal characters when it stores a description.
# Pandoc escapes quotes and apostrophes, so a pushed page would otherwise report
# a difference forever (37 lines of the surveys code samples). The three that
# must stay encoded — &amp;, &lt;, &gt; — Canvas keeps, since decoding them would
# change the markup, so they are safely absent here.
#
# &nbsp; maps to the character rather than a plain space: outside <pre> the
# whitespace collapse below turns it into one anyway, and inside <pre> both sides
# then hold the same character.
TEXT_ENTITIES = {
    "&quot;": '"',
    "&#39;": "'",
    "&#x27;": "'",
    "&nbsp;": "\u00a0",
}

PRE_RE = re.compile(r"(<pre\b.*?</pre>)", re.I | re.S)
NORM_TAG_RE = re.compile(
    r"<(/?)([a-zA-Z][a-zA-Z0-9]*)"
    r"((?:\s+[^\s=<>/]+(?:\s*=\s*(?:\"[^\"]*\"|'[^']*'|[^\s>]+))?)*)"
    r"\s*(/?)>")
ATTR_RE = re.compile(
    r"([^\s=<>/]+)(?:\s*=\s*(\"[^\"]*\"|'[^']*'|[^\s>]+))?")

# Attributes Canvas bolts on at save time, all derived from the src/href beside
# them, so they never carry content the comparison doesn't already cover:
# loading="lazy" on every image, and data-api-* on any link or embed pointing
# back into Canvas. We emit the data-api-* pair ourselves for images (that is
# what the RCE expects to see) but must not diff on it, or a pushed page would
# report a change forever.
#
# `tabindex` goes the other way — Canvas's sanitiser *strips* it, so pandoc's
# numbered-code-block line anchors can never round-trip it (117 of them in
# workshops/05-surveys.md alone). Nothing we can do about that from this side.
VOLATILE_ATTRS = {"loading", "data-api-endpoint", "data-api-returntype", "tabindex"}


def _norm_style(value):
    """`width:80.0%` and `width: 80.0%;` are the same rule; Canvas writes the latter."""
    decls = []
    for decl in value.split(";"):
        decl = decl.strip()
        if not decl:
            continue
        prop, sep, val = decl.partition(":")
        decls.append(f"{prop.strip().lower()}: {val.strip()}" if sep else decl)
    return "; ".join(decls)


def _norm_tag(match):
    closing, name, attrs, _self = match.groups()
    if closing:
        return f"</{name.lower()}>"
    pairs = []
    for am in ATTR_RE.finditer(attrs or ""):
        key = am.group(1).lower()
        if key in VOLATILE_ATTRS:
            continue
        val = am.group(2)
        if val is None:
            pairs.append(key)
            continue
        val = val[1:-1] if val[:1] in "\"'" else val
        val = " ".join(val.split())
        # Pandoc escapes an apostrophe in an attribute as &#39;; Canvas stores it
        # literally. Compare the decoded characters so the two agree.
        val = html.unescape(val)
        if key == "style":
            val = _norm_style(val)
        pairs.append(f'{key}="{val}"')
    pairs.sort()
    joined = (" " + " ".join(pairs)) if pairs else ""
    return f"<{name.lower()}{joined}>"


def normalise(fragment):
    """Canonical form of an HTML fragment, for content comparison only."""
    out = []
    for chunk in PRE_RE.split(COMMENT_RE.sub("", fragment or "")):
        # Tags are normalised everywhere, <pre> included — pandoc's numbered code
        # blocks carry per-line anchors whose tabindex Canvas strips, and those
        # live inside <pre>. Only the whitespace rules below have to skip it.
        chunk = NORM_TAG_RE.sub(_norm_tag, chunk)
        for entity, char in TEXT_ENTITIES.items():
            chunk = chunk.replace(entity, char)
        if chunk[:4].lower() == "<pre":
            out.append(chunk)  # whitespace is significant here — leave it alone
            continue
        # A newline against a tag boundary is pure source formatting — pandoc and
        # Canvas break lines in different places, and a browser collapses it away
        # either way. Drop it, but keep a newline *inside* a text run as a space.
        chunk = re.sub(r"[ \t]*\n[ \t\n]*", "\n", chunk)
        chunk = re.sub(r">\n", ">", chunk)
        chunk = re.sub(r"\n<", "<", chunk)
        chunk = re.sub(r"[ \t\n]+", " ", chunk)
        out.append(chunk)
    # One tag per line, so difflib reports useful hunks.
    text = "".join(out)
    text = re.sub(r">\s*<", ">\n<", text)
    return [line.strip() for line in text.strip().splitlines()]


# -- Due-date consistency check (read-only) ----------------------------------

def markdown_due(source_path):
    match = DUE_RE.search(source_path.read_text(encoding="utf-8"))
    if not match:
        return None
    date, hh, mm, tz = match.groups()
    naive = dt.datetime.strptime(f"{date} {hh}:{mm}", "%Y-%m-%d %H:%M")
    return naive.replace(tzinfo=dt.timezone(dt.timedelta(hours=TZ_OFFSETS[tz])))


def due_mismatch(source_path, assignment):
    """Return a warning string if markdown and Canvas disagree on the due date."""
    want = markdown_due(source_path)
    canvas_due = assignment.get("due_at")
    if want is None or not canvas_due:
        return None
    got = dt.datetime.strptime(canvas_due, "%Y-%m-%dT%H:%M:%SZ").replace(
        tzinfo=dt.timezone.utc)
    # Canvas stores 23:59:59 where the markdown says 23:59; a minute of slack.
    if abs((got - want).total_seconds()) < 60:
        return None
    local = got.astimezone(want.tzinfo)
    return (f"due date differs — markdown says {want:%Y-%m-%d %H:%M %z}, "
            f"Canvas has {local:%Y-%m-%d %H:%M %z} (not changed)")


# -- Main --------------------------------------------------------------------

def fragment_path(source_rel):
    return CANVAS_OUT / Path(source_rel).with_suffix(".html")


def build_file_index(c, cid):
    return {f["display_name"]: f for f in c.get_all(f"courses/{cid}/files")}


def main():
    ap = argparse.ArgumentParser(
        description="Push assessment/workshop text into Canvas assignment descriptions.")
    ap.add_argument("--dry-run", action="store_true",
                    help="show a diff against the live descriptions, change nothing")
    ap.add_argument("--list", action="store_true",
                    help="show the source -> Canvas mapping and exit")
    ap.add_argument("--only", nargs="*", default=None,
                    help="substrings of the source path to include, e.g. 01-prototyping workshops")
    ap.add_argument("--context", type=int, default=2,
                    help="lines of diff context in --dry-run (default 2)")
    args = ap.parse_args()

    c = Canvas()
    cid = course_id()

    jobs = ASSIGNMENT_MAP
    if args.only:
        jobs = [j for j in jobs if any(pat in j[0] for pat in args.only)]
        if not jobs:
            sys.exit(f"--only {' '.join(args.only)} matched no sources.")

    assignments = {a["name"]: a for a in c.get_all(f"courses/{cid}/assignments")}

    if args.list:
        print(f"Course {cid} — {len(jobs)} mapped assignment(s):\n")
        for source_rel, name in jobs:
            a = assignments.get(name)
            frag = fragment_path(source_rel)
            status = f"id {a['id']}, {'published' if a.get('published') else 'unpublished'}" \
                if a else "NOT FOUND ON CANVAS"
            built = "built" if frag.exists() else "not built"
            print(f"  {source_rel:<44} -> {name}\n"
                  f"  {'':<44}    ({status}; fragment {built})")
        return

    missing = [n for _, n in jobs if n not in assignments]
    if missing:
        sys.exit("These assignment names are not in the Canvas course — rename them "
                 "in Canvas or fix ASSIGNMENT_MAP:\n  " + "\n  ".join(missing))

    unbuilt = [s for s, _ in jobs if not fragment_path(s).exists()]
    if unbuilt:
        sys.exit("Missing built fragments (run `make canvas-html`):\n  "
                 + "\n  ".join(str(fragment_path(s)) for s in unbuilt))

    file_index = build_file_index(c, cid)
    uploaded = {}
    # Canvas's course files are one flat namespace, but each content directory
    # has its own img/ (they can't share). So two different local images with the
    # same basename would both resolve to a single Canvas file and one page would
    # silently show the wrong picture. Not the case today — worth catching if it
    # ever becomes so.
    seen_basenames = {}

    def resolve_file(local_path):
        """Canvas file object for a local image, uploading it if it's not there."""
        name = local_path.name
        clash = seen_basenames.setdefault(name, local_path)
        if clash != local_path:
            print(f"    ! '{name}' also came from {clash} — Canvas has one file per "
                  f"name, so these two images collide. Rename one.", file=sys.stderr)
        if name in file_index:
            return file_index[name]
        if name in uploaded:
            return uploaded[name]
        if not local_path.exists():
            return None
        if args.dry_run:
            print(f"    (dry run) would upload {name} to '{FALLBACK_FOLDER_PATH}'")
            return {"id": "NEW", "display_name": name, "url": ""}
        print(f"    uploading new image {name} ...", end=" ", flush=True)
        result = c.upload_file(local_path, folder_path=FALLBACK_FOLDER_PATH,
                               display_name=name, on_duplicate="overwrite")
        print(f"file id {result.get('id')}")
        uploaded[name] = result
        return result

    backup_dir = BACKUP_DIR / dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    if not args.dry_run:
        backup_dir.mkdir(parents=True, exist_ok=True)

    print(f"Course {cid} — {len(jobs)} assignment description(s)"
          f"{' (dry run)' if args.dry_run else ''}:\n")

    changed, unchanged, pushed = [], [], []
    for source_rel, name in jobs:
        assignment = assignments[name]
        source_path = REPO_ROOT / source_rel
        fragment = fragment_path(source_rel).read_text(encoding="utf-8")

        print(f"  {name}  (id {assignment['id']})")
        # Comments first: a comment ahead of the title would hide the <h1>.
        fragment, n_comments = strip_comments(fragment)
        if n_comments:
            print(f"    stripped {n_comments} HTML comment(s)")
        fragment, dropped_title = strip_leading_h1(fragment)
        if dropped_title:
            print(f"    dropped leading <h1>{dropped_title}</h1> "
                  f"(the assignment name already shows it)")
        new_html, images = rewrite_images(fragment, source_path.parent, resolve_file)
        if images:
            print(f"    images: {', '.join(images)}")

        warning = due_mismatch(source_path, assignment)
        if warning:
            print(f"    ! {warning}")

        old_norm = normalise(assignment.get("description") or "")
        new_norm = normalise(new_html)
        if old_norm == new_norm:
            print("    unchanged\n")
            unchanged.append(name)
            continue

        changed.append(name)
        diff = list(difflib.unified_diff(old_norm, new_norm, "canvas", "local",
                                         n=args.context, lineterm=""))
        adds = sum(1 for d in diff if d.startswith("+") and not d.startswith("+++"))
        dels = sum(1 for d in diff if d.startswith("-") and not d.startswith("---"))
        print(f"    CHANGED  (+{adds} / -{dels} normalised lines)")
        if args.dry_run:
            for line in diff[2:]:
                print(f"      {line}")
        print()

        if not args.dry_run:
            backup = backup_dir / f"{Path(source_rel).stem}.html"
            backup.write_text(assignment.get("description") or "", encoding="utf-8")
            c.request("PUT", f"courses/{cid}/assignments/{assignment['id']}",
                      data={"assignment[description]": new_html})
            pushed.append(name)

    print(f"{len(unchanged)} unchanged, {len(changed)} changed.")
    if args.dry_run:
        print("Dry run — nothing written to Canvas.")
    elif pushed:
        print(f"Updated {len(pushed)} description(s): " + ", ".join(pushed))
        print(f"Previous versions saved to {backup_dir.relative_to(REPO_ROOT)}/")
    else:
        print("Nothing to update.")


if __name__ == "__main__":
    main()
