# Canvas push tooling

Push built course content to the ANU Canvas course
(<https://canvas.anu.edu.au/courses/11488>) using the Canvas REST API. Standard
library Python only — no extra dependencies.

Two independent pushes live here:

| What | Canvas target | Script |
|---|---|---|
| Lecture slide PDFs | course **files**, linked from the Home page | `push_lectures.py` |
| Assessment + workshop text | **assignment descriptions** | `push_assignments.py` |

The PDF story is next; the assignment-text story is under **Assignment
descriptions** further down.

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

## Assignment descriptions

`push_assignments.py` replaces the manual loop of *edit the markdown → build the
HTML → open the built page → copy the body → paste it into the Canvas
rich-content editor*. It writes the description of 14 Canvas Assignment pages
from `assessments/*.md` and `workshops/*.md`.

```sh
make canvas-assignments-dry   # build fragments, diff against live, upload nothing
make canvas-assignments       # build fragments, overwrite the descriptions

python3 canvas/push_assignments.py --list                  # source -> Canvas mapping
python3 canvas/push_assignments.py --dry-run --only 01-prototyping
python3 canvas/push_assignments.py --only workshops        # a whole directory
python3 canvas/push_assignments.py --dry-run --context 6   # more diff context
```

### Why the HTML is a fragment

Canvas stores a description as an HTML **fragment** — no `<html>`/`<head>`/`<body>`,
and no title, because the assignment name supplies that. So `make canvas-html`
builds these with pandoc **without `--standalone`** (the only target in the repo
that does), into `build/canvas/{assessments,workshops}/*.html`. `--wrap=none`
keeps one block per line so the dry-run diff is readable.

This works because the existing descriptions *are* pasted pandoc output, so
everything pandoc emits already survives Canvas's HTML sanitiser: `figure` /
`figcaption`, `section`, `div`, `span`, `id` / `class` / `role` / `data-*`
attributes, inline `style` on table `colgroup`s, footnote and citation
back-links. Verified on 2026-08-02 — the 2025 pages round-trip through this
script with a diff of nothing but genuine content changes.

### What the push changes on the way through

Three transforms are applied to the built fragment, each reported per assignment:

- **Images are rewritten.** `img/foo.jpg` means nothing to Canvas, so each local
  src is matched to a Canvas file **by display name** and rewritten to the same
  `/files/<id>/preview?verifier=…` form Canvas's own editor writes (the verifier
  is a stable per-file token, taken from the file's `url`). A local image with no
  counterpart on Canvas is uploaded to `Uploaded Media 2` first. This happens in
  the script, not the Makefile, because only the script knows the file ids.
- **A leading `<h1>` is dropped.** Every workshop source opens with a `# Title`
  repeating its frontmatter title. That is right for the website, but on Canvas
  it would sit directly under the assignment name saying the same thing.
- **HTML comments are stripped.** Pandoc passes them straight through, so
  commented-out draft tasks would otherwise ship inside the Canvas page source —
  invisible on the page but readable via view-source, which is not what
  "commented out" is meant to mean. Canvas drops them on save anyway, so keeping
  them would make every later dry run report a change that can never apply.

Nothing else is touched: due date, points, submission type and publication state
are left alone. The due date *is* compared against the `**Due date**:` bullet in
the markdown and a mismatch is reported, but never written.

### Sizing and alt text live in the markdown

The 2025 pages had image sizes and, on 5 of 13 images, hand-written descriptive
alt text that existed **only in Canvas**. A push would have overwritten it, so it
was moved into the markdown on 2026-08-02 using pandoc image attributes:

```markdown
![Caption shown under the image.](img/foo.jpg){alt="What a screen reader says." width=80%}
```

Give `alt` only when it should differ from the caption — pandoc then drops
`aria-hidden="true"` from the `figcaption`, which is what you want. Sizing comes
out as `style="width:80.0%"` rather than the RCE's `width="80%" height="80%"`;
both render the same, and the `style` form is the valid one (`height="80%"` is
not conforming HTML). That accounts for a one-line diff on first push.

### What Canvas's sanitiser does to the HTML

Canvas re-serialises every description it stores, so a raw diff of ours-against-
theirs is almost all noise. `normalise()` in the script models the following, all
established by pushing and re-reading on 2026-08-02 — **a second dry run after a
push reports all 14 unchanged**, which is what proves the model is complete:

| Canvas does | Handled by |
|---|---|
| Drops the XHTML `/` from void tags, reorders attributes | Tag rewrite + attribute sort |
| Adds `loading="lazy"` to every image | Dropped as volatile |
| Adds `data-api-endpoint` / `data-api-returntype` to **any** link into Canvas, not just embeds | Dropped as volatile |
| **Strips `tabindex`** — kills the line anchors in pandoc's numbered code blocks | Dropped as volatile |
| Decodes `&quot;`, `&#39;`, `&nbsp;`; keeps `&amp;`, `&lt;`, `&gt;` | Entity table |
| Adds a trailing `;` to inline `style` rules | Declaration-level compare |
| Breaks lines in its own places | Whitespace collapse, `<pre>` excepted |

It **keeps** everything else pandoc emits, which is why the fragment approach
works at all: `figure` / `figcaption`, `section`, `div`, `span`, `blockquote`,
`table` / `colgroup` / `col`, `id` / `class` / `role` / `data-cites`, inline
`style` on images and colgroups, in-page anchors (`href="#submission-process"`),
footnote and citation back-links.

Two of those are worth knowing about beyond the diffing:

- The `tabindex` stripping means numbered code blocks lose some keyboard
  accessibility on Canvas. It happens inside `<pre>`, so watch out that any
  future normalisation change keeps normalising tags *inside* `pre` even while
  leaving its whitespace alone.
- Because Canvas rewrites `data-api-*` on internal links, a link to a *previous
  year's* course id still gets enriched and still looks fine in the editor while
  being useless to current students. `workshops/06-thematic-analysis.md` and
  `workshops/07-evaluation.md` both link to `courses/2781/assignments/11550`,
  which is not this course.

### Mapping and safety

Assignments are **discovered by name**, so the mapping survives the yearly course
copy that renumbers every id. The names are not derivable from the markdown
titles — "AI Needs Finding" is *Assignment 2: User Research* on Canvas, and
workshop *N* is *Week N+1* — so `ASSIGNMENT_MAP` in the script is explicit. Rename
an assignment in Canvas and you must rename it there too; the script exits with
the unmatched names rather than guessing.

Every real push first saves the pre-push description to
`build/canvas/backup/<timestamp>/`, so a bad push can be undone by pasting the
saved HTML back. It is under `build/`, so `make clean` clears it.

Known gap: **workshop/assessment markdown with trailing double-spaces** produces
stray `<br>` at the end of list items (25 such lines in
`workshops/09-prototyping-2.md` alone). The push is deliberately faithful to what
the website builds, so those go across too — fix them in the markdown, not here.

## Files

| File | Purpose |
|---|---|
| `canvas_api.py` | Minimal Canvas API client + 3-step file upload |
| `inspect_course.py` | Read-only dump of front page, modules, pages, folders, files |
| `push_lectures.py` | Overwrite-in-place push of `build/lectures/*.pdf` |
| `push_assignments.py` | Overwrite of assignment descriptions from `build/canvas/**/*.html` |

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
- **Workshops / assessments** are now handled — see
  [Assignment descriptions](#assignment-descriptions) above. The images they
  reference all already existed on Canvas under matching display names, which is
  what made the name-discovery approach work there too.
