# nanojam: specification

Draft 2026-09-20. Companion to `weeks-7-12-live-arc.md`, which is the
pedagogical plan; this note is the build spec, written so that a fresh
session (or a student) can start hacking without the rest of the context.

## What it is

A tiny music web app with **one sound engine and several interchangeable
interfaces**. Every interface drives the same engine through the same
command API, so the only thing that varies between them is the interaction.
That makes it a design-space exercise in the mould of Cubing Sound
[@wang-cubing-sound:2022]: hold the sound world fixed, vary the interface,
ask what each one affords and constrains, and later measure it.

It is a lecture example first (week 7, "same task, different affordances"),
a study apparatus second (weeks 8 to 10), and a live-coding substrate third
(weeks 11 and 12). Build for the first two; leave seams for the third.

Working name only. "nanojam" nods at MicroJam, which is fine for now.

## The fixed core

**Synth.** One two-operator FM voice design, four instances with fixed
presets: a low percussive tone (kick-ish), a noisy mid hit (snare-ish), a
short bright tick (hat-ish), and a sustained pitched tone. Parameters:
carrier frequency, modulation ratio, modulation index, amplitude envelope
(attack, decay). Tone.js `FMSynth` is acceptable; a hand-rolled Web Audio
version is about 40 lines and has no dependency. Either way, the four
presets are data, not code, so the parameter panel can edit them.

**Sequencer.** One 16-step pattern, four tracks (one per sound), fixed
tempo default 100 bpm, loops forever once started. Steps are booleans;
optional per-step velocity later. Tone.js `Transport` handles scheduling;
if hand-rolled, use a lookahead scheduler on `AudioContext.currentTime`,
never `setInterval` alone.

**Command API.** The seam between engine and interfaces. Everything an
interface can do is one of these:

```
trigger(sound)                 play a sound now
setStep(track, step, on)       edit the pattern
clear()                        empty the pattern
setTempo(bpm)
start() / stop()
setParam(sound, name, value)   FM parameters, for week 11 mappings
```

Every command call also goes through the logger. Interfaces never touch
the audio graph directly. This rule is what makes the study valid and what
makes weeks 11 and 12 possible.

## The interfaces (v1)

Each interface is a module that takes the command API and returns nothing.
A mode switch in the page swaps them; the pattern keeps playing across the
switch (nice demo moment).

| Interface | Interaction type | What it affords | What it constrains |
|---|---|---|---|
| **Pads** (mouse and touch, same code) | manipulating | discoverable, simultaneous hits, rhythm by feel | limited to what fits on screen; no patterning without a second UI |
| **CLI** | instructing | patterning, looping, precision, repeatability | opaque to novices; can't play "by ear" |
| **Camera** (2D controller) | exploring | continuous, hands-free, expressive movement | imprecise; needs light and a still camera; tiring |

**Pads.** A grid of `n` pads (default 4, allow 2 to 16). Each pad triggers a
sound on pointer-down, not pointer-up. Pad size, gap, and label visibility
are parameters. A second "pattern" view shows the 16 × 4 step grid as
tappable cells; both views are the same interface type, so both count as
"pads" in the study.

**CLI.** A single text input with a scrolling transcript. Vocabulary:

```
play kick                  trigger
loop kick _ _ kick _ snare _ _     set a track from a 16-symbol (or 8, doubled) string
loop snare x...x...x...x...
tempo 120
clear
start / stop
help
```

Error messages must be real: unknown word → "no sound called 'kik'. Try:
kick snare hat tone". Autocomplete on/off and error verbosity are
parameters, because both change the recall/recognition balance and week 9
wants to demo that.

**Camera.** A Wekinator-style 2D controller [@fiebrink-wekinator-nime:2009; @fiebrink-ml-education:2019]:
the position of a tracked point in the webcam frame is a continuous (x, y)
pair. Two layers:

1. *Regions.* Divide the frame into a 2 × 2 (parameter: up to 4 × 4) grid;
   entering a region triggers its sound. This is the discrete, study-able
   layer and the one that makes camera comparable with pads and CLI.
2. *Continuous.* x and y also drive two `setParam` targets (default:
   modulation index and tempo, or nothing until week 11). Latent, not
   central, for v1.

Tracking: MediaPipe Hands via CDN gives an index-fingertip position in the
browser with no server and works on laptop webcams and phone front cameras.
Fallback if MediaPipe is a pain: brightest-pixel or colour-blob tracking
on a downsampled frame, which is 30 lines and a torch on a phone. Smooth
the point with a one-pole filter (parameter). Show the tracked point and the
region grid over the mirrored video so the person can see what the system
sees; this is the visibility principle as UI.

Why camera and not voice: no network, no recogniser latency, works offline
and in a noisy hall, and the onset of a region entry is timestampable.
Voice stays as a front-of-room demo or Wizard-of-Oz, per the arc note.

## The parameter panel

The construction-set move: rather than build the right interface, build the
controls to find it live. A collapsible panel (keyboard shortcut to toggle),
grouped:

- **Pads:** count, size (px), gap (px), labels on/off, layout (row, grid).
- **CLI:** autocomplete on/off, error verbosity (terse/helpful), history on/off.
- **Camera:** grid divisions, smoothing, mirror on/off, dwell time before a
  region counts as entered (ms).
- **Engine:** tempo, the four FM presets (each parameter a slider), master
  volume.
- **Study:** logging on/off, participant id, condition, cued-round settings
  (below).

All parameters live in one JSON object, serialise to the URL hash, and
load from it. A URL is then a complete configuration, so a lecture slide
can link to "the pads at 30 px" and the study can hand out condition URLs.

## Modes

**Free play** is the default and logs nothing unless logging is switched on.
This is the app's reason to exist and the first thing anyone sees.

**Cued round** (study mode). The app cues a sound (visual flash plus the
sound itself, parameter), the participant triggers it as fast as possible
on the current interface, and the app records the result. Per round:

- `n_trials` (default 12), `cue_interval_ms`, cue type.
- For pads: pad width and distance are varied per trial from a small design
  (default 3 widths × 3 distances, one rep per cell, plus warm-up), so a
  Fitts regression is possible within pads.
- For CLI: `hidden_labels` flag hides the sound names from the screen, so the
  round measures recall rather than transcription.
- For camera: the cue names a region; movement time is from cue to region
  entry.

A **session** runs the cued round on each interface in a counterbalanced
order derived from the participant id, then a two-item preference question
(which felt best, which was easiest), then shows the participant their own
summary line. Opt-out is a single tap and returns to free play.

## Logging

One row per trial:

```
participant_id, session_ts, condition_order, interface, trial, cue_sound,
response_sound, correct, pad_width_px, pad_distance_px, region,
movement_time_ms, asynchrony_ms, device_class, ua_hash
```

Plus one row per session for the preference items. `participant_id` is
self-generated by the app (random adjective-animal), stored in
`localStorage`, never entered by the person.

Endpoint: Google Apps Script web app appending to a Sheet, POST as JSON,
fire-and-forget with a local queue that retries. Fallbacks, both built in
from the start: a **CSV download** button, and a **summary line** the
participant can paste into an Ed thread. A tutor-collected pilot dataset
must exist before week 9.

Timing: **superseded — see `docs/timing.md` in the nanojam repo**, which is
also the week-10 codebook. Two corrections to the line above. "Use
`performance.now()` for everything" is not possible: the cue and the metronome
are scheduled on the audio clock, so the app samples a clock pair per trial and
logs it rather than subtracting the two clocks. And "comparable within device"
is too generous — the constant holds only within device x AudioContext instance
x output route x camera-on/off, because opening `getUserMedia` on iOS changes
the audio route and therefore the latency, mid-session.

The row set is also wider than the list above: reaction time and movement time
are separated (with a home position on each interface, or Fitts' law is being
fitted to reaction time plus movement time), and every row carries validity
flags rather than being silently dropped.

## Stack and repo

*Settled 2026-09-20, built at `github.com/cpmpercussion/nanojam`.* The "no build
step" line below was the original intention; it lost to wanting the project to
be clean to work in day to day, and students needing node is an accepted cost
(nobody needs node to *use* the deployed build).

- **Vite + npm.** `npm install && npm run dev`. Four Vite features are
  load-bearing rather than incidental: `import.meta.glob` builds the interface
  registry, so adding an interface is dropping a file; `import.meta.hot`
  re-mounts the edited interface while the AudioContext and Transport keep
  running; `define` bakes the git SHA into every logged row; `base` is
  `/nanojam/` for Pages.
- **Tone.js** for the engine. Note `Tone.now()` adds the context lookahead, so
  interactive triggers must use `Tone.immediate()` or every hit lands 100 ms
  behind the finger.
- **NexusUI** for the parameter panel and the step grid. It is UMD-only, which
  is easier under a bundler than it would have been on the CDN path.
- **MediaPipe Tasks Vision** for hand tracking, lazily imported and code-split,
  with its wasm from a pinned CDN — the one place the original CDN plan
  survives. A brightness-blob tracker is the automatic fallback.
- Plain-DOM modules for the interfaces; no framework. p5.js not needed.
- Own public GitHub repo (not the course content repo), deployed on GitHub
  Pages, MIT licence. Students may fork it.
- Must work on iOS Safari and Android Chrome over eduroam. Audio needs a
  first tap to unlock; camera needs a permission prompt; both must have a
  visible, unmissable "tap to start" affordance.

## Milestones

| By | Deliverable |
|---|---|
| Wed week 8 (30 Sep) | Engine + pads + CLI + parameter panel + logging to Sheet. Deployed. Tested on two phones. |
| Week 8 lecture | Camera regions layer. Heuristic evaluation happens on this build. |
| Fri week 8 (2 Oct) | Cued round + session + counterbalancing + summary/CSV fallbacks. Tutors run the pilot. |
| Week 9 lecture | Study runs (or the collection window opens). Freeze the study build; tag it. |
| Week 11 | `setParam` mappings from camera and pointer streams; Tone.js parameter targets. |
| Week 12 | Agent interface: an LLM with a tool that issues CLI commands; two variants (suggest-and-accept vs autonomous). |

## Non-goals for v1

Audio recording, sharing, accounts, MIDI, more than one pattern, more than
four sounds, mobile-specific layouts beyond "the pads scale to the screen".
Voice control beyond a Wizard-of-Oz shortcut key. Anything requiring a
server other than the Sheet endpoint.

## Acceptance checks

- Loads and plays a beat on iPhone Safari and Android Chrome on eduroam
  within 10 s of opening the URL.
- Switching interface mid-pattern keeps the pattern playing.
- A URL with a hash configuration reproduces the panel state exactly.
- 40 devices posting trials at once lands every row in the Sheet, or
  queues and retries visibly.
- The CSV download opens in pandas with the column names above and no
  cleaning needed except what week 10 wants to teach.
- With logging off, the app makes no network requests after load.

## Open questions

- Is the camera regions layer a fair "selection" comparison, or is dwell
  time doing all the work? **Leaning "demo", on four grounds found while
  building it.** (1) Dwell is not a constant that can be subtracted: an
  overshoot-and-re-enter restarts it, so the penalty is distributed and
  correlates with the skill being measured. (2) A region entry can happen *en
  route* to somewhere else, so camera has a false-positive mode with no
  analogue in pads or CLI, and those false positives cluster on regions
  between start and target. (3) Smoothing is an experimenter-controlled lag
  that the other conditions do not have. (4) Region area is fixed by the
  frame, so width and distance cannot be varied without changing `divisions`,
  which changes the recall load at the same time — the factors are confounded
  by construction. The build logs both entry time and dwell completion, so the
  call can still be made after the pilot. Setting `studyCondition: false` on
  the module is a one-line change.
- Does the pattern view count as a pads condition or its own interface?
  **Decided: neither — it is not a study condition at all** (`studyCondition:
  false`). It is a pattern editor, not a selection task.
- FM presets by hand or borrow a set from a known chip emulation?
