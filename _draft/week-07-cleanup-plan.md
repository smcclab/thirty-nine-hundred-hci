# Week 7 (Interfaces) cleanup plan

Written 2026-09-20 for whichever session picks this up. Lecture is in
week 7 (Mon 21 Sep onward). State as of commit `e4f42c8`.

## Where things stand

- **Frame settled**: the week teaches *affordance analysis* as a method
  (Norman 2013 affordance/signifier, Gaver 1991 perceptible/hidden/false,
  Magnusson 2010 constraints, Rogers interaction types), then walks the
  interface catalogue as bundles of affordances. Six new slides sit between
  "45 years of interface types!" and "Command Line Interfaces": the frame,
  the five-question method, a live worked example (empty table), a 15-min
  phone activity ("tell someone you're running late": type / dictate /
  choose), and a debrief that hands into the catalogue.
- **No live build in week 7.** nanojam is specified in `nanojam-spec.md` and
  is due Wed week 8. `weeks-7-12-live-arc.md` still describes a 60-min
  week-7 live build; its week 7 section is stale and should be rewritten to
  match the above (not urgent for the lecture).
- **References added**: `gaver-technology-affordances:1991`,
  `fiebrink-wekinator-nime:2009`, `fiebrink-human-model-eval:2011`,
  `fiebrink-ml-education:2019`. Lecture 11 gained a Wekinator slide.
- **Deck size**: 68 slides, 6821 words, 100 words/slide (densest deck in the
  course; the audit's rule of thumb is 2 min/content slide, so ~130 min of
  content plus a 15-min activity plus 15 min of admin in a 2-hour slot).

## Cleanup, in priority order

1. **Cut to time.** Target roughly 45 slides. Keep at full length the types
   nanojam and the final project actually use: CLI, GUI, Touchscreens,
   Touchless, Voice, Mobile, and the three Newton vs Palm slides. Merge or
   drop: the two Multimedia slides, the two Augmented Reality slides, the
   two Website Design slides, the two Haptic slides, Shareable + its
   considerations slide, Tangible + its considerations slide. Collapse Smart,
   Shape-changing, Holographic and Brain-computer into one "frontier" slide.
   The mid-deck "Activity: Thinking about AR and VR" (3-min talk) competes
   with the new 15-min activity: cut it or make it a one-line pulse check.
2. **Move the per-type Research and Design considerations to a resources
   page** (`resources/interface-considerations.md`, built by `make
   resources`). Leave one slide in the deck pointing at it: "each type has a
   considerations page; use it when choosing your final-project platform".
   Images cannot be shared across directories, so copy any needed ones into
   `resources/img/`. This was already planned in the arc note.
3. **Sequence check.** The slides must make temporal sense. Already fixed:
   the method slide no longer names the Newton before students have seen it;
   the debrief slide points forward explicitly. Still check: the coda's
   "Which Interface?" slide should call back to the five questions and the
   running-late activity, and end on the week-8 hook ("which is the better
   one, and how would we know?"). The Newton slide's "Norman makes the same
   point in today's coda" is fine as a forward pointer.
4. **Worked example prep.** Decide the object (lectern, phone, or door) and
   put a pre-filled version of the six-row table in speaker notes (`::: notes`)
   so the live fill has a floor if the room is quiet.
5. **Poll Everywhere.** Create an open-response poll for "most surprising
   hidden or false affordance" before the lecture; the QR slide already
   points at `pollev.com/charlesmarti205`.
6. **Frontmatter.** The `description` field still describes the old
   catalogue lecture; add the affordance-analysis method to it (it feeds the
   SEO filter and the index page). The "Plan for the class" slide has a
   bullet already.
7. **Build both outputs.** `make reveal` is clean. Run `make beamer` too: the
   Gaver 2×2 table and the six-row worked-example table sit inside columns
   and may overflow in the PDF. Then `make canvas-lectures-dry` and push with
   `make canvas-lectures` (see memory note on the Canvas workflow).

## After the lecture, not before

- Rewrite the week 7 section of `weeks-7-12-live-arc.md` to match what ran.
- Start the nanojam repo from `nanojam-spec.md` (own public repo, not this
  one; GitHub Pages; milestones in the spec).
- Verify that Fiebrink 2019 actually describes the webcam/coloured-object
  demo before leaning on that claim in week 11.
- Decide whether the week 9 study collects in one lecture or over a window;
  Monday 5 Oct (week 9) is ACT Labour Day.

## Status 2026-09-21 (morning of the lecture)

Items 1–3 and 6–7 done. Deck is 47 content slides. Worked-example floor is in
`::: notes` on that slide (object: the lectern; fallbacks: door, phone lock
screen). Deck now sets `fontsize: 9pt` in its frontmatter so the Beamer PDF
stops spilling off the bottom of ~14 frames; every reveal slide was checked
for vertical overflow in headless Chrome and every PDF page for text past the
bottom/right edge. Item 5 (Poll Everywhere open-response question) is manual
and still to do before class.
