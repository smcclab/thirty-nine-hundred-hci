# Landing S2 2026: weeks 11–12 and after

*Planning doc, 13 Oct 2026 (Tue, week 10). Companion to
`week-12-hcai-rewrite-plan.md`.*

## Where we are

- Week 10 (this week): the week 9 lecture was given live; the week 10 lecture
  (Statistical Analysis) is covered by the **2025 recording**.
- **Two live lectures left**: lecture 11 (Expressive Interfaces) in week 11,
  lecture 12 (Human-Centred AI) in week 12.
- Final project (A3, 40%) due **Thu 5 Nov 2026 23:59** (exam period).
- Tutorials: week 11 analysis (workshop 10), week 12 positionality
  (workshop 11, best 10 of 11 count), then drop-in.

## 1. Week 10 pre-record (do this week)

- [ ] Post the 2025 video link on Canvas/Ed with a note: dates and
      assignment names in the video are 2025's. In particular, the 2025
      announcements slide says "final project repo not available yet". The
      2026 repo is out.
- [ ] Remind students that the stats content is examinable *through A3*: if
      they run a t-test or ANOVA, lecture 10 + the analysis notebook are the
      reference.
- [ ] Optional: a short Ed post pointing at
      `comp3900_hci_analysing_data_examples.ipynb` for anyone doing quant
      analysis in A3.

## 2. Lecture 11 (Expressive Interfaces): small fixes only

The lecture is in good shape. **The PowerPoint recording demo is already
there** (announcement on line 16, section `# Recording a video in Powerpoint`
near the end). But the demo slide has fallen out of sync with the A3 spec as
updated on 12 Oct.

### Demo slide: bring in line with `assessments/03-prototype-and-evaluation.md`

| Slide says | Spec says (authoritative) |
| --- | --- |
| "no longer than 5.5 minutes (330 seconds)" | 5 min (300 s) + 10% buffer, so hard max 330 s. Say *aim for 5:00*. |
| "no larger than 1920 x 1080" | same, plus `.mp4` with **H.264 or H.265** |
| "narrated with your voice", "show video of you speaking" | same, plus face **clear and identifiable**; **no TTS / generative AI voice or avatar** |
| *(missing)* | file **under 100 MB**; export at Full HD 1080p, check the size, re-encode (HandBrake/ffmpeg, H.264 2000k + AAC 128k ≈ 88 MB at 330 s) only if ≥100 MB; **check before committing** because git keeps every version |
| *(missing)* | file named exactly `project-presentation.mp4`; CI must be green |

Proposed replacement (two slides, ~8 min including the live demo):

1. **"Your presentation video: the rules"**: the table above as bullets, with
   a warn-box: *check the file size before `git commit`; a 400 MB commit
   stays in your repo history for good.*
2. **"Live: record, export, check"**: demo in PowerPoint: Record tab → camera
   on, cameo/face visible → record two slides → Export → Create a Video /
   *File → Export → MP4* on Mac → Full HD 1080p → then show the file size in
   Finder, and show `ffprobe`/QuickTime info for codec + duration. Close with
   the template README's re-encode one-liner.
   - Note on the slide: Mac and Windows PowerPoint menus differ; the
     Microsoft support link covers both. Fallbacks if PowerPoint misbehaves:
     Keynote (export H.264), OBS, or Zoom local recording. All are fine as
     long as the output meets the rules.
- Fix typo: "record an upload" → "record and upload".

### Announcements slide

- [ ] Point at the week 10 pre-record (and that it is the 2025 recording).
- [ ] "User Research marks and feedback out later this week": confirm this is
      still true for the week 11 lecture date, or update.
- [ ] Mention the participant spot-check (A2 promise; A3 has the same
      `## Participants` section and CI check), so nobody is surprised.

### Decide and close

- [ ] The `TODO` on first-person methods (Desjardins 2021, Höök 2018). Too
      late for 2026. **Recommend leaving it as a TODO for 2027**; the week 12
      positionality workshop already points at the readings.
- [ ] Human-AI creative section (Autolume, Cobbie, holographic dancer): keep
      as is, but **add one forward-pointer line**: "next week we ask what
      happens when the AI isn't a performance partner but the thing you
      delegate your work to." This sets up week 12 without moving content.
- [ ] Run the slide-overflow check (headless Chrome + `pdftotext -bbox`)
      after edits.

## 3. Lecture 12 (Human-Centred AI): the real work

See `week-12-hcai-rewrite-plan.md`. Summary of decisions (13 Oct):

- **Spine:** keep Shneiderman, but as *the 2021 position under stress test*,
  with Hornbæk Ch 18/20 supplying the older automation theory and post-2022
  HCI evidence supplying the test.
- **Demo:** both, short: a small nanojam agent mode (supertool vs.
  autonomous) plus a brief live agentic-coding moment.
- **Revision block:** shrink from ~20 slides to an A3-oriented checklist
  (3–4 slides).
- **Own work:** include Choi, Andres, Hunter & Martin (2025) GenAI sound
  design as a worked HCAI research case.

Build budget: lecture rewrite ~1.5 days; nanojam agent mode ~1 day plus a
test run; references/images ~0.5 day. Lecture 12 is in week 12, so this
needs to be finished by the end of week 11.

## 4. Admin to land the course (not lecture content)

- [ ] `make canvas-assignments` to push the updated A3 description (still
      outstanding from 12 Oct).
- [ ] **A2 participant spot-check emails**: promised in the A2 spec
      (`{#verification}`); A2 closed 6 Oct. Run
      `3900-check-participants needs-finding`, sample, email. Do this
      *before* A2 marks are released if any finding would change a mark.
- [ ] A2 marks + feedback release.
- [ ] Tutorial marks entered for all 11 workshops (lecture 12's first slide
      claims they are; make it true before saying it).
- [ ] SELT: confirm the 2026 open dates (the slide has "(??)").
- [x] (23 Oct) **Course stats slide in lecture 12 is 2025's** (330 → ~295 students,
      565 slides, >370 commits, 3K Ed threads). Regenerate for 2026: student
      count from lucy `data/students.csv`, commit count
      (`git log --since=2026-06-01 | grep -c ^commit`), slide/word/image
      counts via `count_slides.sh`, Ed stats from the Ed analytics page
      (the 2026 Ed course id still needs confirming, since the link may point at
      2025's 24905).
- [ ] A3 marking setup in lucy: `marking.yml` for `final`, MOSS base
      `cd8343a` (already set), marker fork sharing after 5 Nov, A3 participant
      spot-check after 5 Nov.
- [x] Ed: pinned "final project FAQ" thread #1639 (13 Oct); submission
      logistics block drafted 21 Oct from the 2025 forum, mirrored in
      `resources/07-assessment-faqs.md`.

## 5. After semester (note for 2027, don't do now)

- Workshops/lecture balance audit items still open: lectures 2–3 overlong,
  stats lecture placed after A2.
- First-person methods section for lecture 11.
- Decide whether lecture 12's HCAI material should become a full week
  earlier in the course (agentic AI as the implementation layer; see
  `comp3900-scope-boundaries`), rather than living in the last lecture.
