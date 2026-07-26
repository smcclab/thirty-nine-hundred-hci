# Canvas push tooling

Push built course PDFs to the ANU Canvas course
(<https://canvas.anu.edu.au/courses/11488>) using the Canvas REST API. Standard
library Python only — no extra dependencies.

## How it works

The 2025 Home page links each lecture PDF **by Canvas file id** (e.g.
`01-intro-to-hci.pdf` is file `1900986`, linked as
`/courses/11488/files/1900986?...&wrap=1`). The files live in the folder
`course files/Uploaded Media 2`.

The push uses **`on_duplicate=overwrite`**. When you re-upload a PDF with the
same filename, Canvas replaces its contents and builds a *replacement chain*: the
original file id redirects to the new upload. So **every existing Home-page link
automatically serves the refreshed slides** — no page editing, no re-linking.

To stay robust across yearly course copies (file/folder ids change on each copy),
`push_lectures.py` **discovers the target file by display name** and overwrites it
in whatever folder it currently lives in. A PDF with no match on Canvas is
uploaded to the fallback folder `Uploaded Media 2`.

## Setup (one time)

1. In Canvas: **Account → Settings → Approved Integrations → + New Access Token**.
   Purpose `hci-course-tooling`. Copy the token.
2. Save it (never commit it):

   ```sh
   printf %s 'PASTE_TOKEN_HERE' > ~/.config/canvas/anu-token
   chmod 600 ~/.config/canvas/anu-token
   ```

   Alternatively export `CANVAS_TOKEN` in your shell. The base URL
   (`CANVAS_API_URL`, default `https://canvas.anu.edu.au`) and course id
   (`CANVAS_COURSE_ID`, default `11488`) can also be overridden by env var.

## Usage

```sh
# See the current Canvas structure (read-only):
make canvas-inspect          # or: python3 canvas/inspect_course.py

# Preview the push plan — reads Canvas, uploads nothing:
make canvas-lectures-dry     # or: python3 canvas/push_lectures.py --dry-run

# Build the lecture PDFs, then push them:
make canvas-lectures         # runs `make beamer` first

# Push without rebuilding, or push a subset / the mega-bundle:
python3 canvas/push_lectures.py
python3 canvas/push_lectures.py --only 07 12
python3 canvas/push_lectures.py --mega      # also overwrites all_lectures.pdf
```

## Files

| File | Purpose |
|---|---|
| `canvas_api.py` | Minimal Canvas API client + 3-step file upload |
| `inspect_course.py` | Read-only dump of front page, modules, pages, folders, files |
| `push_lectures.py` | Overwrite-in-place push of `build/lectures/*.pdf` |

## Notes & gotchas

- **Course file quota.** The 12 lecture PDFs total ~119 MB (largest,
  `07-interfaces.pdf`, is ~34 MB). Course 11488 was observed on 2026-07-26 with
  a 2000 MB quota and 125 MB used, so a full push has ample room. Don't rely on
  that figure — quotas differ per course and per year, and `make canvas-inspect`
  prints the live `used / quota` so you never have to guess. If a push ever does
  fail with a quota error, ask the edtech team to raise it.
- **Replacement chains accumulate.** Each overwrite leaves the superseded file
  object behind (hidden) with the id redirecting forward. This is harmless and
  invisible to students; Canvas resolves the original linked id to the latest
  content every time.
- **`hidden: true` is normal here.** The edtech team loaded the lecture PDFs
  hidden from the student *Files* browser but reachable via the Home-page links
  (`hidden_for_user: false`). The push preserves this state.
- **Verifier tokens.** Home-page links include a `verifier=` query param. Enrolled
  students accessing through the course context don't depend on it, so overwrites
  don't break the links.
- **Workshops / assessments (later).** Tutorials and assessments on Canvas are
  *Assignment* pages with HTML pasted in, and reference images — pushing those
  cleanly is a separate task (image handling), not covered here yet.
```
