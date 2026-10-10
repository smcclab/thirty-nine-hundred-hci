# Week 9 (Cognitive, Social, Emotional) cleanup plan

Written 2026-10-10 (Saturday) for whichever session picks this up. The
lecture is delivered **Monday 12 October**, which is calendar week 10:
Monday 5 October was ACT Labour Day, so the course is one Monday short.
Lecture 10 (Statistical Analysis) will be a live stream or last year's
recording, and lectures 11 and 12 take the remaining two Mondays (19 and
26 October). State as of commit `cfd544f` plus two uncommitted edits (the
PowerPoint recording link in this deck and in `assessments/03`; commit
those first, they are correct).

## Where things stand

- **Deck size**: 52 slides, 3686 words, 70 words/slide, 39 images. Of the
  52, 45 are content slides (6 admin, Questions, References). At the
  audit's 2 min/slide that is ~90 min of content plus 15 min admin plus the
  phone-vs-text poll, in a slot that ends at 2:55. Needs to lose about ten
  slides, the same job as week 7.
- **Already done**: the four case studies from `case-studies-weeks-7-12.md`
  (Snapchat ×2, Google Buzz, Replika) are in and each ends on "the test
  that would have caught it". The admin block was partly fixed on 3 Oct
  (`c1dab7f`): A2 is no longer "due today" and the Friday-lecture line is
  gone. The PowerPoint link is fixed in the working tree.
- **Not done, unlike weeks 7 and 8**: no frame slide, no nanojam thread,
  no speaker notes, no overflow check in either output, description not
  updated. Week 8 closed on "Activity: two ways to evaluate nanojam" and
  the three nanojam research questions; nothing in this deck picks that up.
- **nanojam**: v1 (`dcbd561`, 20 Sep) already ships the study mode the
  spec scheduled for Fri 2 Oct: cued round, session, counterbalancing,
  hidden-labels CLI flag, CSV download and summary-line fallbacks. It is
  deployed at `charlesmartin.au/nanojam` (week 8 linked it). Nothing has
  changed in the repo since 20 Sep, there is no study-build tag, and the
  repo records nothing about whether the tutor pilot ran or whether
  `VITE_LOG_ENDPOINT` is set on the deployed build. See open questions.
- **The live-arc plan for this week is out of reach.** It wants a 35-min
  "cognition you can feel" block (change blindness, digit span, Stroop) plus
  a 30-min study plus live plotting. None of the demos exist and the week 10
  consumer of the Stroop dataset is now a stream or a recording. Scope it
  down to a five-minute demo; the rest goes to the 2027 list at the end.

## Stale and wrong, slide by slide

- **Announcements** (`:7-11`): stray space in "marked ,"; the stream line
  should say *when* the statistics lecture is released and whether it is
  live; nothing about this week's tutorial (Prototyping for Evaluation,
  `workshops/09`) or that the A3 repo exists (`course_info.yml` has
  `comp3900-2026-A3-final-project`; lecture 10's announcements still say
  "repo not available yet").
- **Final project block** (`:20-88`, six slides): paraphrases the spec in
  full but never states the three things students need on Monday: due
  **5 November 23:59 AEDT**, video **no more than 330 seconds** (CI
  enforces it), and participants **must be current COMP3900/6390
  students, recruit 3-5 in your tutorial now**. The positionality link
  uses the old `smcclab.github.io` host (still redirects, but update).
- **"Questions on the Final Project"** (`:81`): "Next week, I'll
  demonstrate recording a presentation in powerpoint." Next Monday is
  either the stream or lecture 11. Move the promise to the correct date or
  cut it.
- **Information Processing** (`:378-384`): five-bullet wall of text, no
  image, plain-text "(Card et al., 1983)" instead of a cite key. Will spill
  in Beamer. `references.bib` has no Card/Moran/Newell entry.
- **"Video: What is a mental model?"** (`:342-345`): a YouTube link behind a
  thumbnail; dead in the PDF and a whole slide for one link.
- **"Expressive Interfaces and Emotional Design"** (`:618`): shares its
  title with lecture 11. Reframe as the week-11 teaser.
- **Closing slide** (`:696`): "cathchbox" and "up until 2:55", both fixed
  in week 7's copy (`07-interfaces.md:915`).
- **Frontmatter**: no title-slide background, unlike every other deck
  (fixed 2026-10-10: `2025-nime-remote-performance.jpg`, Charles's own
  photo, also used on the Remote Conversations slide). No `fontsize: 9pt` (week 7 needed it to stop ~14 Beamer
  frames spilling; week 8 did not). Description does not mention the case
  studies or the study.

## Cleanup, in priority order

1. **Settle the two open questions below** (both are announcements-slide
   facts, not blockers for the editing).
2. **No live data collection this year** (decided 2026-10-10: lecture 10
   is most likely last year's recording, so there is no consumer for a
   class dataset and no energy for running a study). Replace the planned
   block with a **5-minute front-of-room demo, one slide**, right after the
   "Cognitive Aspects" section slide: two volunteers, projected, one on
   pads, one on the CLI with `hidden_labels` on, same cued round, nothing
   logged. The room watches recognition beat recall and sees the CLI say
   nothing on a wrong command. That is all the later slides need to point
   at (Memory: "you watched this"; Gulfs: "the CLI said nothing";
   Mental Models: "what did the volunteer think `loop` did?"). No consent
   slide, no endpoint, no pilot dependency. If even that feels like too
   much on the day, the slide still works as a talk-through of the week 8
   screenshot; nothing downstream breaks.

3. **Cut to about 41 slides.** Keep all four case studies and the
   phone-vs-text poll. The cuts, with the count after each:
   - Merge "Cognition", "Cognitive processes" and "What are cognitive
     processes?" into one slide: OED line, fast/slow, the six-item list
     (−2, 50).
   - Merge each process with its Design Implications slide: Attention,
     Perception, Memory, Learning, Reading/Speaking/Listening (−5, 45).
     Problem Solving is already merged. The merged Memory slide is where
     the hidden-labels CLI result lands: "you just measured this".
   - Drop the mental-models video slide; put the link on the Mental
     Models slide (−1, 44).
   - Rewrite Information Processing to four short lines with the Card
     1983 cite and the NASA-TLX sentence; the TLX line is what the final
     project can use.
   - Merge Distributed and External cognition into one slide, keep
     Embodied as its own because it is the week-11 bridge (−1, 43).
   - Fold "Being Social" into the Social section slide and "Emotions and
     Behaviour" into the Emotional section slide (−2, 41).
   - Reframe "Expressive Interfaces and Emotional Design" as the week-11
     teaser: visceral/behavioural/reflective, "the numbers from today's
     study will not capture this; in two weeks we build for it".
   - Then `python3 find_unused_images.py` (the video thumbnail and the
     Being Social images become orphans).
4. **Fix the admin block.** Announcements: A2 being marked; the statistics
   lecture's delivery and date; tutorial this week is Prototyping for
   Evaluation; A3 repo link. Collapse the six final-project slides to four:
   challenge, what to submit (with due date, 330 s, participant rule in a
   warn-box), video rules, questions. Fix the "next week" PowerPoint demo
   promise. Since A3 is "the final project combines A1 and A2", one line
   on the demo as a miniature of the A3 method would not hurt.
5. **Housekeeping, same as week 7.**
   - `::: notes` on the demo slide: the two commands to have the CLI
     volunteer type, and what to say if nobody volunteers.
   - Add `card-psychology-hci:1983` to `references.bib` from publisher
     metadata (Lawrence Erlbaum; Crossref has it as a book), cite it on
     the Information Processing slide.
   - Typos on the closing slide; stray space in announcements.
   - Description: add the four cases and the in-class study.
   - `make reveal` and `make beamer`, then the headless overflow check on
     both outputs (week 7's procedure). Expect to need `fontsize: 9pt`.
   - `make canvas-lectures-dry`, then `make canvas-lectures`.

## Open questions

1. **Lecture 10 release date.** If it is last year's recording, decide
   when it goes up on Canvas and say so on the announcements slide. The
   recording's own announcements are stale (A2 timing, "repo not
   available yet"); a one-line Ed post with the current facts covers it.
2. **Usual two-hour slot on Monday?** The closing slide's "2:55" assumes
   it. The cut list assumes 15 admin + 5 demo + ~60 content + poll +
   questions, which leaves slack.

Settled: no live data collection (see item 2). The tutor pilot and the
logging endpoint no longer matter for this lecture.

## After the lecture, not before

- Rewrite the week 9 section of `weeks-7-12-live-arc.md` to match what
  ran, and mark the week 10 section as "not this year" with the reason.
- The nanojam study mode is built and untested in a lecture. Running it
  for real is a 2027 item, with the week 10 live-notebook plan it feeds.
- Add to a 2027 list (not `TODO-2027.md`, which is template-repo scoped;
  a section in the live-arc note is the right place): the deferred
  cognition demos (change blindness, digit span, Stroop on phones), the
  Sharp dilemma-box warm-ups, and `resources/case-studies.md`.
- The lecture 10 announcements slide ("final project repo not available
  yet", "marks out next week") is stale whichever way it is delivered.

## Status 2026-10-10 (Saturday)

Mechanical fixes done in the working tree (not committed): title-slide
background; `fontsize: 9pt`; announcements rewritten (A2 being marked, A3
repo link, statistics lecture as a Canvas recording, this week's tutorial);
due date, 330-second ceiling and participant rule in a warn-box on the
Final Project Specification slide; PowerPoint demo promise moved to
19 October; positionality link on `smcclab.au`; video slide folded into
Mental Models as a link; Information Processing rewritten to four lines
with `card-psychology-hci:1983` (added to `references.bib` from Crossref,
original 1983 Erlbaum edition with the CRC reissue DOI); closing-slide
typos. Deck is now 51 slides / 3780 words. Both outputs built; all 61 PDF
pages scanned for text past the page edge (none) and the three rewritten
slides screenshotted in headless Chrome at 1920x1080 (all fit).
`01_02_conceptualising_interaction_0.png` is now unused; left in place.

Still to do: item 2 (demo slide), item 3 (merges to ~41 slides), item 5's
speaker notes, and the Canvas dry run and push.

Snapchat case (same day): the opening line said the app was baffling
because friends and publishers shared a list. That was Spiegel's rationale
for the new structure, not the usability complaint, which was the
unlabelled gesture navigation ("difficult to understand or hard to use",
Q3 2017 earnings call, now `snap-q3-2017-call:2017` in the bib from Snap's
investor-relations transcript PDF). Slide rewritten, and the content-map
figure replaced by `figures/snapchat-gestures.py`: two phones showing only
the camera, dashed arrows for the four hidden swipes, destinations before
and after, with the changed ones in saffron. Old `snapchat-redesign.png`
removed with `git rm`. Both outputs rebuilt and checked.
