"""Push built lecture slide PDFs to the Canvas course.

Strategy (matches the 2025 site, keeps front-page links live):

  * The Home page links each lecture PDF by Canvas *file id*.
  * `on_duplicate=overwrite` replaces a file's bytes while keeping its id, so
    re-uploading a PDF with the same name updates the slides everywhere they're
    linked, with zero page editing.
  * To stay robust across yearly course copies (ids change), we DISCOVER the
    existing file by display name and overwrite it in its current folder. If a
    PDF has no counterpart on Canvas yet, we upload it to the fallback folder.

Usage:
    python canvas/push_lectures.py --dry-run      # show plan, change nothing
    python canvas/push_lectures.py                # upload/overwrite
    python canvas/push_lectures.py --only 07 12   # just those lectures
    python canvas/push_lectures.py --mega         # also push the all-lectures bundle

Environment: CANVAS_TOKEN / CANVAS_API_URL / CANVAS_COURSE_ID (see canvas_api.py).
"""

import argparse
import sys
from pathlib import Path

from canvas_api import Canvas, course_id

REPO_ROOT = Path(__file__).resolve().parent.parent
LECTURES_DIR = REPO_ROOT / "build" / "lectures"

# Fallback folder (relative to course root "course files") used only when a PDF
# is not already present on Canvas. Matches where the 2025 copy landed.
FALLBACK_FOLDER_PATH = "Uploaded Media 2"

# Optional all-in-one bundle: local bigfile -> Canvas display name to overwrite.
# The local path must match `make bigfiles` output ($(OUTPUT_DIR)/all_lectures.pdf).
MEGA_FILE = (REPO_ROOT / "build" / "all_lectures.pdf", "all_lectures.pdf")


def lecture_pdfs(only):
    pdfs = sorted(LECTURES_DIR.glob("*.pdf"))
    if only:
        pdfs = [p for p in pdfs if any(p.name.startswith(pre) for pre in only)]
    return pdfs


def build_name_index(c, cid):
    """Map display_name -> file object for every file in the course."""
    files = c.get_all(f"courses/{cid}/files", params={"per_page": 100})
    return {f["display_name"]: f for f in files}


def main():
    ap = argparse.ArgumentParser(description="Push lecture PDFs to Canvas.")
    ap.add_argument("--dry-run", action="store_true", help="show the plan, upload nothing")
    ap.add_argument("--only", nargs="*", default=None,
                    help="filename prefixes to include, e.g. 07 12")
    ap.add_argument("--mega", action="store_true",
                    help="also push the concatenated all-lectures bundle")
    args = ap.parse_args()

    c = Canvas()
    cid = course_id()

    pdfs = lecture_pdfs(args.only)
    if not pdfs:
        sys.exit(f"No lecture PDFs found in {LECTURES_DIR}. Run `make beamer` first.")

    jobs = [(p, p.name) for p in pdfs]
    if args.mega:
        mega_path, mega_name = MEGA_FILE
        if mega_path.exists():
            jobs.append((mega_path, mega_name))
        else:
            print(f"! --mega requested but {mega_path.name} not found (run `make bigfiles`); skipping")

    index = build_name_index(c, cid)

    print(f"Course {cid} — planning {len(jobs)} upload(s):\n")
    plan = []
    for local, canvas_name in jobs:
        existing = index.get(canvas_name)
        size_mb = local.stat().st_size / 1_048_576
        if existing:
            target = ("overwrite", existing["folder_id"], existing["id"])
            print(f"  OVERWRITE  {canvas_name:<38} {size_mb:6.1f} MB  "
                  f"-> file id {existing['id']} (folder {existing['folder_id']})")
        else:
            target = ("new", None, None)
            print(f"  NEW        {canvas_name:<38} {size_mb:6.1f} MB  "
                  f"-> folder '{FALLBACK_FOLDER_PATH}'")
        plan.append((local, canvas_name, target))

    if args.dry_run:
        print("\nDry run — nothing uploaded.")
        return

    print()
    for local, canvas_name, (kind, folder_id, _file_id) in plan:
        print(f"Uploading {canvas_name} ...", end=" ", flush=True)
        if kind == "overwrite":
            result = c.upload_file(local, parent_folder_id=folder_id,
                                   display_name=canvas_name, on_duplicate="overwrite")
        else:
            result = c.upload_file(local, folder_path=FALLBACK_FOLDER_PATH,
                                   display_name=canvas_name, on_duplicate="overwrite")
        rid = result.get("id") if isinstance(result, dict) else "?"
        print(f"done (file id {rid})")

    print("\nAll uploads complete. Existing Home-page links now point at the new slides.")


if __name__ == "__main__":
    main()
