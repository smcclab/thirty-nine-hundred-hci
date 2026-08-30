# Weeks 7–12: the live study arc

Draft plan, 2026-08-30. Goal: convert the back six lectures from textbook
recitals into the making/live-coding format used in weeks 1–6 and other
courses. The device is **one small app, built live in week 7, that carries
every remaining lecture**: it gets built (7), evaluated (8), studied (9),
analysed (10), made expressive (11), and made agentic (12). The class are
the participants; every week generates or consumes real data. This works at
any attendance level — 15 people is a real sample — and gives the lecture
recording a payoff the PDF can't reproduce.

## The artifact: "nanojam" (working name)

A tiny instrument — a sample-pad / pattern app: a handful of sounds you
trigger and loop. Its raison d'être is art: making music together, not
being measured. The measurement rides along in a *cued round* (study
mode): the app cues a sound, you trigger it fast and accurately — a
rhythm-game practice mode, which is the selection task in diegetic form.

Implemented in several interaction types, each a real instrument paradigm:

| Week | Interface | Lineage / role |
|---|---|---|
| 7 | GUI (pad grid, mouse) | Launchpad/MPC; pads are Fitts targets with width + position |
| 7 | Touch (same page on a phone) | pocket instrument — the MicroJam lineage, said out loud |
| 7 | CLI (`play kick`, `loop kick snare _ hat`) | micro live-coding language — TidalCycles/Sonic Pi; "CLIs are avant-garde again" |
| 7 | Voice: beatbox-to-sequencer | vocal percussion → drum triggers (Dubler, query-by-beatboxing); a mapping problem in the sonic domain — foreshadows week 11 |
| 11 | Continuous gesture → sound | discrete triggering deepens to continuous mapping |
| 12 | LLM agent ("make me a beat") | bandmate — the interface type Shneiderman didn't see coming |

Every cued-round trial logs: `participant_id (self-generated, anonymous),
interface, trial, pad_width, pad_distance, movement_time_ms, asynchrony_ms
(vs metronome cue), errors, timestamp`. Plus a Stroop block
(congruent/incongruent RT pairs) and a 2-item Likert preference at the end.
One tidy CSV is the week-10 dataset. (Web-audio latency on phones means
asynchrony is comparable within-device only — note this in the deck; it's
a measurement-validity lesson.)

The study is therefore a genuine NIME-style instrument evaluation —
"which interface makes a better instrument?" — not a toy psych experiment,
and it's the convenor's actual research field performed on the room.

**Logging infrastructure**: simplest zero-server option is a Google Apps
Script web-app endpoint writing to a Sheet (free, anonymous, exports CSV).
Fallbacks if wifi/endpoint dies live: (a) the page computes each
participant's summary line and they paste it into an Ed thread; (b) a
pre-collected pilot dataset from tutors is *always* on hand so week 10 works
even if week 9 collection fails. Host the page under the course site or a
scratch GitHub Pages repo — it must be reachable from student phones.

## Week 7 — Interfaces: build it (detailed)

- Compress the ~35-slide interface-type catalogue to a 10–15 min
  "45 years of interfaces" flip-through. Move the per-type *Research and
  Design considerations* into a `resources/` page (same move as the
  interview question cards) — students actually need it when choosing a
  final-project platform, not read aloud.
- Keep the research-skills/referencing opener (it's doing real work
  before A2).
- Main event (~60 min): live-build **nanojam** (see "The artifact" above):
  the same tiny instrument as pad grid → touch → CLI → voice.
- Close: "Which of these is the better *instrument*? How would we know?"
  → week 8 hook.

### Why an instrument and not a task app

The app's reason to exist is making music, not being measured — a lecture
artifact that exists only as a stimulus would contradict six weeks of
needs-finding ideology. The instrument framing also upgrades every mode:

- **Same sounds, four channels.** The sound set is identical across
  modes, so weeks 8–9 vary *only* interaction type — exactly the IV the
  study needs. Clicking vs typing is still the original HCI comparison
  (keystroke-level model, Card/Moran/Newell), quietly re-run on the room.
- **Fitts geometry for free.** Pad size and layout are the designer's to
  vary; a cued round supplies the width × distance manipulation.
- **Free-play = engagement.** A class-jam moment (everyone's phone at
  once) is chaos, but on-brand chaos — and a live demo of
  shareable/social interaction that week 9 can cite.
- **CLI nuance:** typing while reading pad labels is transcription, not
  recall. Build a flag for a CLI round where the sound names must be
  remembered — that round is week 9's recognition-vs-recall demo.
- **No bait-and-switch in week 11.** Expression is present-but-latent
  from day one; week 11 deepens discrete triggering into continuous
  mapping rather than revealing that a game was secretly music.

### Stack

Single static HTML page. **p5.js** for the canvas (native idiom, pairs
with Tone.js in week 11), plain DOM for the CLI input and mode switch,
**Web Speech API** for voice, `performance.now()` for timing. No build
step — the edit-save-reload loop is the existing VS Code + Live Server
workflow, so nothing new sits between the code and the projector.

Lives in its **own small public GitHub repo** (not this one — it must not
enter the `build/` pipeline), deployed on GitHub Pages so week 9 is
"phones visit a URL", and forkable by students who want to play.

Known risks, both teachable:

- **Voice will half-work in the hall** (Chrome-only, needs network + mic
  permission, hostile acoustics). Narrate the failure as content (gulf of
  evaluation, error recovery) and keep a keyboard-triggered
  **Wizard-of-Oz fallback** where the lecturer "recognises" the speech —
  a live callback to week 3's WoZ prototyping, not an apology.
- **Voice RTs are unmeasurable** (recogniser latency swamps human
  latency). That's a finding, delivered a week early: measure what you
  can interpret. Voice contributes error/preference data only.

**Framing voice honestly** (say this in lecture): the *idea* —
beatbox-to-sequencer — is genuinely good, with real lineage (Vochlea's
Dubler commercially, query-by-beatboxing in music-IR research) and a real
accessibility thread (voice/breath-controlled instruments for
motor-impaired and hands-busy musicians). What's dubious is whether a
*cheap implementation* of it is usable — "is this version a good idea?
Probably not. Can we test it? Yes." A condition intuition predicts will
lose is what gives the week-8 experiment stakes, and negative results
are results.

Study-mode caveat: a lecture hall of people beatboxing at their phones
in week 9 is glorious but acoustically hopeless — voice is tested as a
front-of-room demo condition (or small-N volunteers), contributing
error/preference data only, and that sampling compromise is itself
week-8 teaching material.

### The hour (cooking-show discipline)

Pre-written scaffold (~100 lines: page, sample player, logging module)
plus numbered checkpoint files (`01-scaffold.html` … `05-voice.html`).
Live-code the deltas between checkpoints; a typo or overrun means jumping
to "one I prepared earlier", never dying on stage. Big font, dark theme.

1. **Scaffold tour (5 min)** — *read*, don't write. The sounds already
   play (audio plumbing is not lecture content); reading the logging
   module aloud is the point: "log everything, with timestamps" is the
   research skill of the whole back six.
2. **Pad grid (15 min)** — draw pads, hit-test, trigger sounds, per-hit
   timing. Payoff: play a beat on it.
3. **Touch (5 min)** — open it on a phone: "it already works — except for
   everything that doesn't." Hover is gone, fat fingers, pad sizes →
   the mobile considerations land as debrief.
4. **CLI (15 min)** — input field + a micro live-coding parser (`play`,
   `loop`). Command syntax, error messages, the hidden-names flag.
   Live coding as artistic practice → CLI considerations debrief.
5. **Voice: beatbox mode (15 min)** — two tiers. Tier 1 (the gag): Web
   Speech API transcribing "boots and cats" as words. Tier 2 (the real
   idea): Web Audio onset detection + spectral centroid classifying vocal
   hits into kick/snare/hat — ~30 lines with an analyser node. Build
   tier 2 live; it half-working is the content. WoZ fallback if it
   fully fails. Considerations debrief.
6. **Debrief (5 min)** — four interfaces, one instrument, visibly
   different feel. "Which is the better instrument? How would we know?"
   → week 8.

## Week 8 — Evaluation: plan the study

- Research-question section stays (it's already activity-shaped).
- Live heuristic evaluation of the week-7 app using Nielsen's 10 as the
  coding scheme — the room logs violations in a shared doc; this *is* the
  "Evaluation by Inspection" section, performed.
- Then design next week's experiment together, live, using the deck's own
  machinery (variables, hypotheses, experimental designs table):
  RQ: does interface type affect selection speed and errors?
  IVs: interface (CLI/GUI/touch/voice, within-subjects, counterbalanced);
  target width × distance within GUI. DVs: movement time, error rate,
  preference. Pilot it on a volunteer at the front.
- Dovetails with Tutorial 7 "Planning Evaluations" the same week.

## Week 9 — Cognitive, Social, Emotional: run it (detailed)

Current deck: 48 slides, five sections. Restructure (nominal 2h):

**1. Announcements + Final Project details (15 min).** Keep as-is — this
is load-bearing scheduling content.

**2. Cognition you can feel (35 min).** Each cognitive process becomes a
30–60 s live demo on the class, followed by its existing *Design
Implications* slide — the implications slides survive, the descriptive
slides mostly go:

- *Attention*: selective-attention / change-blindness demo (flicker task
  can live in the app; the gorilla video also works).
- *Perception*: contrast/colour legibility demo (existing slides adapt).
- *Memory — recognition vs recall*: the week-7 app IS the demo. Time the
  room recalling CLI commands vs recognising GUI buttons. This is the
  classic textbook claim, demonstrated on their own data.
- *Working memory*: digit-span task on phones.
- *Stroop task* on phones: automaticity + attention, and it quietly
  manufactures the paired-samples dataset week 10's t-test needs.

**3. The main study (30 min).** Run the experiment designed in week 8:
cued rounds on nanojam (interface comparison + pad width × distance),
everyone on their own device,
counterbalancing assigned by the app. Open a consent slide first and say
why — modelling ethics practice is itself the content. End by live-plotting
the incoming data (scatter of movement time vs index of difficulty, means
per interface) but **do no statistics**: "these two means look different —
are they? Next week." That cliffhanger is the week-10 attendance pitch.

**4. Cognitive frameworks, through the task (20 min).** Gulfs of
execution/evaluation, mental models, information processing — each
illustrated by something the room just experienced (the voice interface's
lag = gulf of evaluation; CLI errors = mental-model mismatch). Distributed
/ external / embodied cognition compress to a slide each.

**5. Social + Emotional (10 min or cut).** Social interaction → pointed
reading (it resurfaces in A2 and final-project contexts). Emotional
interaction → reframe as the week-11 teaser: Norman's
visceral/behavioural/reflective, "usability numbers won't capture this —
in two weeks we build for it."

**Tutorial alignment**: Tutorial 8 that week is "Research Design" — the
lecture experiment is the worked example tutors can dissect.

**Risk management**: pilot dataset pre-collected (tutors/convenor), demo
videos as backup for any live demo, and the app deployed + tested on eduroam
before the lecture.

## Week 10 — Statistics: analyse it

The lecture is a live Jupyter session on the class's own CSV. Every item on
the existing "significance test menu" gets fed by week-9 data:

- Descriptives + data preparation: cleaning the real (messy!) class CSV.
- Paired t-test: Stroop congruent vs incongruent RTs.
- One-way repeated-measures / ART ANOVA: interface type (4 levels) on
  movement time.
- Regression: movement time vs Fitts index of difficulty — the law appears
  out of their own data.
- Nonparametric: Likert preferences.
- IMPSY/EMPI case study stays as the "this at research scale" close.

## Week 11 — Expressive Interfaces: what the numbers missed

Narrative fit (the piece that was unclear): **weeks 8–10 treated movement
variability as noise to minimise; week 11 treats it as signal.** After
three weeks of optimising time-and-error, the question "is the fastest
interface the best one?" has an obvious counterexample: an instrument. The
usability framing saturates exactly where expression begins — that's the
bridge, and students don't need to be told it's the point for it to land.

- Live: deepen nanojam from discrete triggering to continuous mapping —
  the pointer stream (position, velocity, timing: the same fields week 9
  logged) now drives sound parameters (Tone.js). Perform the *Steps in
  Mappings* slides: one-to-one → nonlinear → many-to-many, feeling each
  get more instrument-like. "In week 9 this wiggle was error; today it's
  phrasing."
- CST principles land as debrief of the live build.
- The portfolio case studies (MicroJam, PhaseRings, Co/da, Dinosaur Choir…)
  compress to ~10 min of "the same idea at research scale."
- Also seeds the final project's experience-goals framing: evaluation
  beyond usability.

## Week 12 — Human-Centred AI: stress-testing Shneiderman

Reframe honestly: Shneiderman wrote HCAI in 2021, just before LLM agents
worked. Instead of reciting a framework the field has partly outgrown, the
lecture **applies the course's own evaluation skills to the newest
interface type and tests whether the framework holds** — which is both
better scholarship and a live demo.

- Live: add the final interface to nanojam — an LLM agent given the same
  command language and a natural-language goal ("make me a beat"): the
  agent as bandmate. Build the feature twice: supertool style (it
  suggests/completes a pattern, human auditions and accepts) vs agent
  style (it jams autonomously, opaque). The HCAI critique becomes a
  co-creativity critique — links straight to the Cobbie/IMPSY material.
- Evaluate both against the 2D HCAI framework and the eight guidelines,
  live: where does an agentic system sit? Can high automation and high
  human control coexist the way the diagram promises? The reverse-centaur
  slide becomes a demonstration, not an assertion.
- Course wrap writes itself: the one instrument has now been played by
  pad grid, touch, CLI, voice, continuous gesture, and agent — 45 years
  of interface types, one artifact.
  The revision section hangs off that timeline instead of re-listing
  every deck.

## What to build (implementation checklist)

1. The nanojam app: single static page (p5.js + a small sample set), four
   interface modes, free-play + cued-round modes, trial logging,
   participant-id generation, counterbalancing.
2. Logging endpoint: Apps Script → Sheet, plus "paste your summary line"
   fallback and CSV download.
3. Stroop + digit-span pages (tiny, same logging).
4. Week 10 notebook skeleton in `notebooks/` (loads the Sheet CSV,
   sections matching the significance-test menu).
5. Continuous-mapping layer for week 11 (Tone.js parameters driven by
   the same pointer events).
6. Agent mode for week 12 (Claude API with a tool that issues nanojam
   commands — pattern-suggest supertool variant and autonomous variant).
7. Pilot dataset collected from tutors before week 9.
8. `resources/` page: interface types + research/design considerations
   (extracted from lecture 07).
