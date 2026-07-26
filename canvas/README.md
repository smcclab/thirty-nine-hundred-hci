# Canvas push tooling

Push built course PDFs to the ANU Canvas course
(<https://canvas.anu.edu.au/courses/11488>) using the Canvas REST API. Standard
library Python only — no extra dependencies.

## How it works

The Home page links each lecture PDF **by Canvas file id**, e.g.
`/courses/11488/files/1969776?...&wrap=1`.

The push uses **`on_duplicate=overwrite`**, and the net effect is that **every
existing Home-page link serves the refreshed slides** — no page editing, no
re-linking. Measured across two pushes on 2026-07-26:

- **The replacement chain works.** Querying the *pre-push* id of a bundle
  (`1900987`) after overwriting it returned the **new** content — 110.6 MB,
  `modified=2026-07-26`, where before it was 111 MB from 2025-12-11. So an old id
  captured earlier keeps resolving, and resolves *forward*. This is the property
  the whole approach rests on.
- **But the upload response returns a different id when the bytes change.** First
  push (content genuinely changed): 7 of 12 lectures came back with a new id, 5
  kept theirs. Second push minutes later (identical lecture bytes): all 12 kept
  their ids, while the two bundles — whose bytes *had* changed — both got new
  ones. So a new id tracks a content change, not randomness.
- Re-reading the Home page afterwards showed it referencing the **new** ids, and
  all 15 ids it references resolved. Both the old and new ids work.

Practical rule: don't hardcode a file id, and don't assume the id an upload
returns matches the one you saw before it. Old ids stay valid, so a stale id is
not a broken link — but it is a misleading label. `inspect_course.py` prints
current ids.

To stay robust across yearly course copies (file/folder ids change on each copy),
`push_lectures.py` **discovers the target file by display name** and overwrites it
in whatever folder it currently lives in. A PDF with no match on Canvas is
uploaded to the fallback folder `Uploaded Media 2`. On the 2026 course copy the
lecture PDFs were found in folder `297917`, not the 2025 `Uploaded Media 2` — the
name-discovery path handled that automatically, which is the point of it.

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

# As above PLUS the all_lectures.pdf / all_workshops.pdf bundles the Home page
# links. Use this for a full refresh — canvas-lectures alone leaves them stale:
make canvas-lectures-mega    # runs `make beamer bigfiles` first

# Push without rebuilding, or push a subset / preview the bundles:
python3 canvas/push_lectures.py
python3 canvas/push_lectures.py --only 07 12
python3 canvas/push_lectures.py --dry-run --mega   # preview incl. bundles
```

## Files

| File | Purpose |
|---|---|
| `canvas_api.py` | Minimal Canvas API client + 3-step file upload |
| `inspect_course.py` | Read-only dump of front page, modules, pages, folders, files |
| `push_lectures.py` | Overwrite-in-place push of `build/lectures/*.pdf` |

## Notes & gotchas

- **Course file quota.** The 12 lecture PDFs total ~119 MB (largest,
  `07-interfaces.pdf`, is ~34 MB); the two bundles add ~115 MB. Course 11488 has
  a 2000 MB quota, so a full `canvas-lectures-mega` fits comfortably. Quotas
  differ per course and per year — `make canvas-inspect` prints the live
  `used / quota`, so don't trust a figure written down here. If a push ever does
  fail with a quota error, ask the edtech team to raise it.
- **Expect a one-time step up in usage on the first real push, and don't measure
  it too early.** Observed on 2026-07-26:

  | point | reported used |
  |---|---|
  | before any push | 125 MB |
  | immediately after pushing 119 MB | 124 MB |
  | after both pushes, settled | 245 MB |

  Two things are going on. First, **the accounting lags** — the 124 MB reading was
  taken seconds after a 119 MB upload and was simply stale, so a before/after
  comparison right around a push proves nothing. Second, a freshly copied course
  reports far less than its files actually weigh: 125 MB against 246 MB of files,
  because course-copy files still share storage with the source course. Your first
  real upload converts them into this course's own bytes, which is the step up.

  Superseded objects are *not* billed: settled usage (245 MB) matches the sum of
  the 35 current files (246 MB), so repeated pushes should hold roughly steady
  rather than creep. Verify with `make canvas-inspect` a few minutes afterwards,
  not immediately.
- **The bundles go stale unless you ask for them.** `all_lectures.pdf` and
  `all_workshops.pdf` are linked from the Home page but are *not* touched by a
  plain `make canvas-lectures` — use **`make canvas-lectures-mega`**, which builds
  `bigfiles` too and pushes both. This bit us: on 2026-07-26 the live
  `all_lectures.pdf` (file `1900987`) was 111 MB with `modified=2025-12-11`, so
  students clicking it got the *previous year's* slides while the 12 individual
  PDFs were current. Refreshed the same day.
- **`all_assessments.pdf` is built but not pushed.** `make bigfiles` produces it,
  but there is no counterpart on Canvas to overwrite, so pushing it would create
  an unlinked file rather than refresh anything. Add it to `MEGA_FILES` in
  `push_lectures.py` if a Canvas link for it is ever created.
- **`--dry-run` and `--mega` compose, but the make targets don't.**
  `canvas-lectures-dry` previews lectures only. To preview the bundles too, call
  the script directly: `python3 canvas/push_lectures.py --dry-run --mega`.
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
