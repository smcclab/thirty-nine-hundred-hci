# Case studies for weeks 7–12

Draft plan, revised 2026-09-19. Written in response to the week-6 pulse survey
(`~/src/hci/pulse-survey/report.md`, §3B): four students independently asked
for **real-world examples and consequences** — "stories of what happened when
a product did or didn't apply a principle" — and one specifically proposed a
20–30 minute case-study analysis inside a lecture. §4.2 of that report made it
an action.

Weeks 7–12 are lectures 07–12 (`week_7_monday: 2026-09-21` in
`lucy/data/course_info.yml`), so all six slots are still ahead of us.

## Selection rule

**Every case must turn on a decision about an application or an interface,
made by people doing the job these students are training for.** This is a
tighter rule than it sounds, and it rules out most of the famous
"technology disaster" canon. Air France 447, Therac-25 and Three Mile Island
are systems-engineering and safety-case failures; the interface is a
contributing factor but the decisions were about hardware interlocks,
certification and training, and the students are not aeronautical engineers.
Robodebt is a policy and governance failure — its defect is the income-averaging
rule and the reversed burden of proof, neither of which is an interface
decision, and *none of the methods in this course would have caught it*. Using
such a case teaches the opposite of what we want: that HCI is a lens you wave
at any disaster, rather than a discipline with methods that catch specific,
findable defects.

The six below each hinge on a choice a student could plausibly face in their
own final project, and each ends on a method from this course that would have
surfaced the problem before shipping.

## Relationship to the live-arc plan

`_draft/weeks-7-12-live-arc.md` proposes rebuilding the same six lectures
around a live-built instrument (nanojam). The two plans are compatible but
compete for the same minutes, so treat the case study as a **modular 12–15
minute block** droppable into either version of the deck:

- **If the live arc happens**, the case is the theory anchor for the live
  build — *before* the build in weeks 7, 9 and 12 ("here is what this choice
  cost someone real; now we make the same choice ourselves") and *after* it in
  weeks 8, 10 and 11 ("we just did this at toy scale; here it is at
  consequence scale").
- **If the live arc doesn't happen**, each case still works standalone, paid
  for by compressing the slides named under "Where it goes".

Nothing here depends on the arc being adopted.

## Why a fixed structure

The gap the survey describes is not "no examples" — the decks are full of
research examples. It is that students can't see how a principle becomes a
*decision* someone had to make without hindsight. So every case runs the same
six beats, and after two weeks students should be able to run them unprompted.
That repeatability is the point: it is the analytic move we want in the A2
rationale and the final project, taught by repetition rather than by a rubric
line.

1. **Situation** (~1 min). Who, when, what they were building.
2. **The fork** (~2 min). The two options actually on the table, presented
   *without* the answer. Both must be defensible.
3. **Vote / think-pair-share** (~3 min). Which would you have picked, and what
   would you need to know to decide? Uses the existing discussion-break format
   students named as a strength (§2.2 of the report).
4. **What they chose, and why it was reasonable** (~2 min). Steelman it. A
   case where the designers were idiots teaches nothing.
5. **The consequence** (~3 min). Documented outcome with numbers and a
   citation — not an anecdote.
6. **The concept that explains it, and the test that would have caught it**
   (~3 min). Ties to a slide already in that deck and ends on a method from
   this course. This beat is the direct answer to the COMP6390 student who
   asked how you know whether a usability attribute is actually achieved
   rather than merely felt.

Beat 6 accumulates. By week 12 the class has a six-item inventory of
"evaluation that would have caught it" — the menu the final project's
evaluation plan has to choose from.

## The arc

Read down the fork column and there's a spine worth saying out loud in week
12: **who does the learning** (Newton/Palm) → **can it be undone** (Hawaii) →
**what did you break that people had memorised** (Snapchat) → **does the
measurement justify the change** (Bing/Facebook) → **is faster even the goal**
(Ocarina) → **are you responsible for what your interface says** (Air Canada).
Six decisions, all of which a student could face in their own project.

| Wk | Lecture | Case | The fork | Source |
|---|---|---|---|---|
| 7 | 07 Interfaces | Newton MessagePad vs Palm Pilot | machine learns your handwriting / you learn its alphabet | external (new refs) |
| 8 | 08 Evaluation | Hawaii false missile alert, 2018 | two adjacent menu items, one confirm dialog, no undo | external (FCC report) |
| 9 | 09 Cognitive/social/emotional | Snapchat's 2018 redesign (+ Buzz, Replika) | reorganise for new users / preserve the old users' muscle memory | external |
| 10 | 10 Statistical analysis | Bing's ad headline test (+ Facebook contagion) | ship on judgement / measure it; and when is a *p*-value a reason to ship | external (HBR/PNAS) |
| 11 | 11 Expressive interfaces | Reactable + Ocarina, then the NIME longevity survey | build for the stage / build for the paper — and does anyone still play it? | **biblio** `jorda2010reactable`, `wang2014ocarina` + McPherson/Morreale |
| 12 | 12 Human-centred AI | Air Canada's chatbot (+ Google Photos) | let the bot answer policy questions / constrain it to retrieval | external (BCCRT) |

Week 11 comes ready-made from the biblio, which is the honest answer to
"is there a sequence already in the collection": the biblio is a research
library, deep in method and design-research exemplars and thin in
*consequence*, because CHI papers are not written about shipped products that
hurt their users. The five external cases are therefore additions, not
replacements, and each has a biblio-sourced alternative listed.

## What the textbooks in `hci-biblio` already give us

Checked directly against the PDFs (2026-09-19). The short answer: **yes, there
are case studies, but almost none of them are the kind the students asked
for** — with one exception that is genuinely useful and one that we should
copy the *format* of.

**1. "Case study" in these books usually means the research method, not a
teaching exemplar.** Lazar, Feldman & Hochheiser, *Research Methods in HCI*
(`lazar-2017-research-methods-hci.pdf`) devotes the whole of **Chapter 7** to
it — including §7.2 "Observing Sara: a case study of a case study", and §§7.4–7.5
on goals (exploration, explanation, description, demonstration) and types
(intrinsic/instrumental, single/multiple, embedded/holistic). This is good
teaching content, and week 8 or the final-project support could use it, but it
answers "how do I *do* a case study", not "what happened when someone shipped
the wrong thing". Chapter 10 carries two industry case studies contributed by
Gary Moulton (Yahoo!) and Laura Granka (Google).

**2. Sharp, Rogers & Preece (6th ed., `sharp-2023-interaction-design-textbook.pdf`)
has case studies, but they are worked research studies, not consequences.**
§14.4 "Evaluation Case Studies" runs two deliberately contrasting ones —
§14.4.1 **DeepTake**, predicting when drivers of automated cars must take
over (Pakdamanian et al., 2021), and §14.4.2 **Ethnobot**, an in-the-wild
ethnographic chatbot that prompted visitors at the Royal Highland Show
(Tallyn et al., 2018) — followed by §14.5 "What Did We Learn from the Case
Studies?" and an in-depth activity comparing the evaluation methods. Chapter
15 adds an iPad usability test and a remote expert VR evaluation conducted
under COVID conditions. **Worth lifting straight into week 8**: §14.4–14.5 are
already structured as a compare-two-studies activity, they are on the
students' own textbook, and they cost nothing to prepare. They are not
substitutes for the Hawaii case — DeepTake and Ethnobot are studies that went
*well* — but they pair with it nicely: one segment on what a good evaluation
looks like, one on what it costs to skip it.

**3. The thing actually worth copying is Sharp's "Dilemma" boxes.** The book
describes them as encouraging "readers to weigh the pros and cons of
controversial issues", roughly one per chapter — which is independently the
same structure as beats 2–4 above, already written, already keyed to the right
chapters. Relevant ones, by our week:

| Our week | Sharp chapter | Dilemma |
|---|---|---|
| 9 (cognitive) | 4 | "Is It OK to Use a Phone While Driving?" — with Caird et al. (2018) on reaction times, and Lou et al. (2022) on wrong-patient errors rising with electronic-health-record load |
| 9 (social) | 5 | social technologies for remote communication |
| 9 (emotional) | 6 | affective computing and emotional-AI sensing |
| 7 | 7 | robots as an interface type |
| 8 | 16 | heuristic evaluation, Budd's heuristics and WCAG |

Use these as the 3-minute warm-up *before* the main case in weeks 7, 8 and 9,
run live in the room. **Not as pre-class tasks** — those are tracking fine and
don't need more loaded onto them. The Chapter 4 dilemma is the strongest: it
has real numbers and a real clinical consequence, and it sits exactly where
week 9's attention material goes.

**4. Shneiderman's *Human-Centered AI* (`shneiderman-2022-human-centered-ai.pdf`)
is full of real incidents, and mostly they are the kind we ruled out** — the
two Boeing 737 MAX crashes, Patriot missile batteries in the 2003 Iraq War,
stock-market flash crashes, Chernobyl, Challenger. Shneiderman uses them
exactly the way the selection rule above warns against, which is a useful thing
to notice out loud rather than imitate. **The exception is Tesla** (25
mentions, and the best-developed example in the book), and specifically the
*naming* decision: Shneiderman quotes the NTSB report on the 2016 fatal crash
— "automation 'because we can' does not necessarily make the human-automation
system work better... an example of what can happen when automation is
introduced 'because we can' without adequate consideration of the human
element" — and then makes the HCI point directly, that calling the feature
"Autopilot" overstates its capability and encourages drivers to stop watching.
That *is* an interface decision: what you name a capability sets the user's
mental model of it. **Add it to week 12 as a 4-minute companion**, sourced from
the course's own HCAI textbook, alongside the Air Canada case — the pair gives
"the interface overclaimed" and "the interface was taken at its word".

**5. Norman's *Design of Everyday Things* PDF is a scan with no text layer**
(261 characters extracted across 261 pages), so it can't be searched, and its
famous examples are anecdotes rather than documented consequences anyway.
Edmonds, *The Art of Interaction*, has a genuine case-study chapter (ch. 5:
art and play, beta-testing and experience design, engagement and research,
social mixed-reality play space) which is relevant to **week 11** if you want a
biblio-native alternative to Ocarina — though they are practice accounts, not
decision-and-consequence stories.

**Net effect on this plan:** three free additions, no substitutions. Sharp
§14.4–14.5 into week 8, the Dilemma boxes as warm-ups in weeks 7–9, and
Shneiderman's Tesla-naming passage into week 12. The six main cases stay as
they are, because the collection genuinely does not contain them — which is
the finding, not a gap in the search.

---

## Week 7 — Interfaces: Newton vs Palm (1993–1996)

**Fork.** Apple's MessagePad (1993) shipped Calligrapher: unconstrained cursive
recognition, trained on the user, no new alphabet to learn — the machine adapts
to the human. Palm (1996) shipped Graffiti: a single-stroke alphabet derived
from Xerox PARC's Unistrokes, which the *user* has to learn — the human adapts
to the machine. In 1993 Apple's is obviously the better idea, and is the one
the class will vote for.

**Consequence.** Newton's recognition errors were public and funny enough to
reach a Doonesbury strip and a *Simpsons* gag; the reputation outlived the
later models whose recognition was genuinely fixed, and the line was
discontinued in 1998. Graffiti was learnable in about half an hour and
accurate, and the Palm Pilot took the market Newton had created.

**Concept + test.** Punctures the deck's own closing slide, *Natural User
Interfaces and Beyond* (line 930): "natural" describes the user's starting
state, not a measurable property of the interface, and one that demands
learning can beat one that doesn't. The test is plain and is week 8 arriving
early: measure recognition accuracy on unconstrained adult cursive, against a
threshold agreed *before* the ship decision.

**Where it goes.** Replaces about half the *Pen-Based* slide (line 561) plus
the *Natural User Interfaces* coda. Under the live arc, it's the opener that
motivates building the same instrument four ways.

**Sources (new `references.bib` entries).**
- Goldberg, D. & Richardson, C. (1993). Touch-typing with a stylus. *INTERCHI
  '93*, 80–87. <https://doi.org/10.1145/169059.169093> — the Unistrokes paper
  Graffiti derives from; states the constrained-alphabet rationale outright.
- MacKenzie, I. S. & Zhang, S. X. (1997). The immediate usability of Graffiti.
  *Graphics Interface '97*, 129–137 — the learnability evidence.
- Newton's reception is press and folklore, not research. Keep it to one
  slide and cite the cultural artefacts as cultural evidence.

**Biblio alternative (positive-outcome version).** `morrison2020torino` —
Microsoft Research's Torino tangible programming language for children with
visual disabilities, shipped as the American Printing House's Code Jumper.
Already cited in lecture 07. Fork: screen-reader-plus-text vs physical beads;
consequence: a product in schools. Use it if you want a case where the careful
choice won, or run it as a 4-minute companion.

---

## Week 8 — Evaluation: the Hawaii false missile alert (13 Jan 2018)

This one is a genuine interface case despite the dramatic setting: the
artefact is an ordinary internal web app, and the defect is entirely in its
widgets. Keep the segment on the screen, not on emergency management.

**Fork.** The alert-origination tool listed drill and live templates in the
same dropdown with near-identical labels ("DRILL - PACOM (CDW) STATE ONLY"
directly adjacent to "PACOM (CDW) STATE ONLY"), behind one generic
confirmation dialog. There was no cancellation template at all. The fork is
the one every student will face: do you distinguish a destructive action from
a safe one by *label text in a shared list*, or by making them structurally
different and reversible?

**Consequence.** A statewide alert telling 1.4 million people to seek
immediate shelter, and no way to retract it for 38 minutes. The FCC's Public
Safety and Homeland Security Bureau found a lack of reasonable safeguards and
controls.

**Concept + test.** This is the deck's *Evaluation by Inspection* section
(line 570) with stakes, and unusually clean: Nielsen's heuristic 5 (error
prevention) and 9 (help users recover from errors) are violated on the face of
the screen. Run it as the activity — put the reconstructed interface up and
have the room log violations against Nielsen's 10 *before* revealing what
happened. One evaluator, one hour, would have caught it. The cheapest method
in the course versus the largest consequence in it is the whole segment.

**Where it goes.** Becomes the worked example inside *Evaluation by
Inspection*, absorbing the *Heuristic Evaluations of User Interfaces (video)*
slot (line 585), which currently outsources the same job to a video.

**Source.** FCC PSHSB, *Report and Recommendations: Hawaii Emergency
Management Agency False Alert* (2018),
<https://docs.fcc.gov/public/attachments/DOC-350119A1.pdf>. Redraw the
dropdown rather than lifting a screenshot — projects better and dodges the
rights question.

**Alternative, if you'd rather it be something students would build.**
GitLab's 2017 production database incident: an engineer ran the removal
command in one of several identical terminal windows, deleting ~300 GB from
the live primary; five of six backup procedures turned out not to work. The
postmortem is public and blameless, and the interface defect — no visual
distinction between a production and a staging shell — is one every student
has in their own setup right now. Less vivid, much closer to home.

**Biblio alternative.** `schaadhardt-blind-screenreader-artboards:2021` —
a documented, current accessibility failure with named consequences for
working designers.

---

## Week 9 — Cognitive/social/emotional: three app decisions

The lecture has three sections, so it takes three short cases rather than one
long one. All three are consumer apps; none requires any domain knowledge.

### Cognitive (8 min): Snapchat's February 2018 redesign

**Fork.** Snapchat's growth problem was that new and older users found it
baffling. The redesign separated friends' content from publisher content and
reorganised where Stories lived — cleaner information architecture, defensible
on every principle in the deck. The alternative was to leave an
acknowledged-confusing structure alone because the existing users had
*memorised* it.

**Consequence.** A Change.org petition against the update reached 1.2 million
signatures; Snap declined to revert, then partly rolled back by May. In Q2
2018 Snapchat recorded its first-ever decline in daily active users — 188
million, down from 191 million — which Evan Spiegel attributed primarily to
"the disruption caused by our redesign".

**Concept + test.** The single best illustration of the deck's *Mental Models*
(line 331) and *Learning* (line 220) slides: an interface people use dozens of
times a day is operated from memory, not from reading, so a better structure
can still be a worse interface. Also *Recognition vs recall* and the *Design
Implications for Memory* slide (line 207). The test is one the course already
teaches and Snap arguably skipped for incumbent users: evaluate the change
with *existing expert users* on their own habitual tasks, timed, not just with
new users on first-run tasks.

### Social (4 min): Google Buzz, February 2010

**Fork.** Launch a social network inside Gmail with a default that
auto-follows your most-emailed contacts and publishes that list, versus
requiring people to build the graph themselves and accept a cold start.

**Consequence.** A user's most-frequent email contacts — which for some people
included an abusive ex-partner, a therapist or a source — were published on
their profile within days of launch. The FTC charged deceptive practices and
imposed a consent order requiring a comprehensive privacy program and 20 years
of independent audits, its first such order. Buzz was retired in December 2011.

**Concept + test.** Lands on the *Being Social* / *Co-Presence* slides (lines
441, 485): a contact list is a model of a *behaviour*, not of a relationship,
and publishing it discloses things people never chose to say. The test is a
cheap one the course teaches: run the default configuration past a handful of
real users with real data and ask what they would not want visible — the
critical-incident and interview methods from week 4, applied to a default
rather than to a feature.

### Emotional (4 min): Replika, February 2023

**Fork.** Withdraw the erotic-roleplay feature in response to a regulator, or
keep it and take the regulatory risk. Nobody in the room will argue with the
compliance decision, which is what makes it a good case: the fork isn't
*whether* to remove it, but whether a company that encouraged emotional
attachment owes its users anything in *how* it removes it.

**Consequence.** Documented grief and acute distress in a user base that had
formed attachments; r/Replika's moderators pinned suicide-prevention lines;
the feature was partly restored in May 2023 for pre-February users.

**Concept + test.** Directly on *Anthropomorphism* (line 599) and *Affective
Computing and Emotional AI* (line 567): emotional design creates obligations
that outlast the product decision, and there is no usability metric that shows
this coming. Closes the lecture on the limit of the course's own methods,
which sets up week 11.

**Sources.** Snapchat: Snap Inc. Q2 2018 results (SEC 10-Q) for the DAU
figure, plus TechCrunch/CNBC for the petition and rollback. Buzz: FTC press
release and consent order, March/October 2011, <https://www.ftc.gov> — primary
and quotable. Replika: Hanson, K. R. & Bolthouse, H. (2024), *Socius* 10,
<https://doi.org/10.1177/23780231241259627> — peer-reviewed, so citable.

**Biblio alternative.** `ambe-technology-individuation:2017` (the foibles of
augmented everyday objects) for a domestic, low-stakes version of the same
mental-model mismatch.

---

## Week 10 — Statistics: two experiments, opposite lessons

Both are experiments on an interface, which is what makes the statistics feel
like a design tool rather than a maths unit.

### The case for measuring (7 min): Bing's ad headline, 2012

**Fork.** A Bing engineer proposed a small change to how ad headlines were
displayed. A few days' work. It sat in the backlog for over six months because
experienced people judged it unimportant — the ordinary way software decisions
get made.

**Consequence.** When someone finally ran it as an A/B test, revenue rose
about 12%, triggering a "too good to be true" alert because the effect was so
large. It became Bing's best revenue idea, on the order of $100M a year.

**Concept + test.** The motivation for the deck's whole *Significance Test
Menu* (line 140): expert judgement ranked this idea near the bottom, and the
only thing that found it was measurement. Note the symmetric lesson — most
tested ideas *fail*, and the same mechanism that surfaced this one is what
stops the other ideas shipping on somebody's confidence.

### The case for reading the effect size (7 min): Facebook contagion, 2014

**Fork.** Having run a real News Feed manipulation on 689,003 users for a
week, report it as a finding, or conclude the effect is too small to mean
anything.

**Consequence.** Suppressing positive posts changed the proportion of positive
words by B = −0.1% (*p* < 0.001, *d* = 0.02) and negative words by B = +0.04%
(*p* = 0.007, *d* = 0.001). PNAS published an Editorial Expression of Concern
about consent.

**Concept + test.** *What's a p-value?* (line 106) doing actual work. Hand the
room the numbers before the interpretation and ask: is this a finding? Then
give them the authors' own defence, which is genuinely good — at that scale
*d* = 0.001 is hundreds of thousands of expressions a day, and the
manipulation was minimal while the DV is hard to move. There is no gotcha,
which is what makes it teach: the answer depends on the decision the number is
being used for. Put next to the Bing case, the pair gives the rule the lecture
wants — report an effect size with every *p*, and state in advance the
smallest effect that would change what you build.

**Where it goes.** Bing immediately before *A Significance Test Menu* (line
140) as its motivation; Facebook immediately after *What's a p-value?* (line
106). The IMPSY/EMPI case study (line 353) stays as the "done properly, at
research scale" close.

**Sources.** Kohavi, R. & Thomke, S. (2017), The surprising power of online
experiments, *Harvard Business Review* 95(5) — the Bing headline account, from
the person who ran the platform; Kohavi, Tang & Xu (2020), *Trustworthy Online
Controlled Experiments* (CUP) for the textbook version. Kramer, Guillory &
Hancock (2014), *PNAS* 111(24), 8788–8790,
<https://doi.org/10.1073/pnas.1320040111>, plus the Expression of Concern,
<https://doi.org/10.1073/pnas.1412469111>.

**Biblio alternative.** `caine-2016-local-sample-sizes` turns the same
question inward — what our own field actually does about N and power. Pairs
with either rather than replacing.

---

## Week 11 — Expressive interfaces: two survivors and the denominator

This is the one week where the biblio does the work, and it supports a
three-part segment rather than a single case. The structure is the point:
**two instruments that made it out of the lab, and then the survey that says
how rare that is.** Ending on the denominator is what stops the segment being
a highlight reel, and it is the most honest thing the course can say about the
convenor's own field.

### 1. The Reactable (5 min) — `jorda2010reactable`, already in `references.bib`

**Fork.** Jordà's group at Pompeu Fabra had a tangible tabletop synthesiser: a
round table, physical pucks, a camera underneath, projected visual feedback
showing the connections between objects. The conventional move for a research
prototype is a paper, a demo, and a corridor at the next conference. They
instead built it as a *performable instrument* — round, so players face each
other with no "front"; visible, so an audience can see the causality that a
laptop performance hides; robust enough to be moved and re-set-up.

**Consequence.** In the paper's own words, it "accomplished unparalleled mass
popularity if we consider its academic origin" — demos watched millions of
times on YouTube, and then "handpicked by Icelandic songstress Björk for her
2007 world tour". Jordà names the outcome precisely: it "turned into one of
the very few new digital instruments that have successfully passed the
research prototype state". It went on to a company and a mobile version.

**Why it's a good story to tell.** It is the rare case where the HCI research
decision *is* the commercial decision. The round table, the visible causality
and the shared control surface are tangible-interaction arguments from Ishii
and Fishkin — all cited in lecture 07 — and they are also exactly why it works
on a stadium stage and why the YouTube video is watchable. The design rationale
and the reason for its fame are the same rationale.

### 2. Smule Ocarina (5 min) — `wang2014ocarina`, already in `references.bib`

Currently cited only in lecture 07; belongs here.

**Fork.** Ge Wang had an iPhone, a microphone and a multitouch screen. The
efficient design is tap-a-note: instant, learnable, zero error. He instead made
the microphone a breath sensor and required four-finger covering of on-screen
holes — deliberately harder, slower and more error-prone to play — and added a
globe showing other players around the world.

**Consequence.** A top-selling paid app with millions of users, a design
rationale publishable in *Computer Music Journal*, and a company. Everything
that made it succeed would have scored as a defect in week 8.

**The pair.** Reactable made the instrument *legible* to an audience; Ocarina
made it *effortful* for the player. Neither optimised the thing weeks 8–10
taught us to optimise, and the deck can say so plainly: this is the bridge the
live-arc plan identifies — weeks 8–10 treat variability as noise to minimise,
week 11 treats it as signal — delivered by two cases rather than asserted.

### 3. Framing vs practice (5 min) — McPherson, Morreale & Harrison

**The corrective.** Both cases above are survivors, and a lecture that stops
there is teaching survivorship bias. McPherson, Morreale & Harrison's chapter
"Musical Instruments for Novices: Comparing NIME, HCI and Crowdfunding
Approaches" is the denominator: it surveys digital instruments released through
NIME, HCI venues, accessible-instrument research, and Kickstarter/Indiegogo
campaigns, and finds "striking differences in approach between commercial and
academic projects, with less pronounced differences between each of the
academic communities".

The framing-versus-practice gap is the teaching content, and it is sharp:

- **What the campaigns claim.** Marketing promises that the new technology
  could produce "any sound imaginable", and that music is made *accessible* by
  the device. The pitch is always removal of difficulty.
- **What the designs actually do.** Most crowdfunded instruments are MIDI
  controllers with a keyboard-oriented musical outlook, and the usual
  mechanism for "easier" is **limiting the pitch space or quantising the
  timing** — that is, deciding in advance what the player is allowed to play.
  McPherson et al.'s point is that these are unstated assumptions with a strong
  *aesthetic* influence on the performer: the instrument has opinions, and the
  marketing says it doesn't.
- **What the field's own record shows.** Morreale & McPherson (2017) surveyed
  the makers of the 97 NIME papers from 2010–2014 that introduced a new
  instrument; 70 responded (72%). Of the 51 built for prolonged performance
  use, **47.1% were not ready to perform on**, two thirds of those needing more
  than a few hours of work to become so, and **15.7% no longer existed at all**.
  The commonest stated reasons are mundane and worth reading out: "I don't have
  the opportunity at the moment" (22), "I turned my attention to building other
  DMIs" (14), "the hardware needs too much maintenance" (10), "it was a
  collaborative effort which has stopped" (9).

**Concept + test.** This lands on *Designing Constraints*
(`magnusson2010designconstrain`, already cited) with teeth — every "easy"
instrument is a constraint decision presented as an absence of one — and it
gives beat 6 an unusually concrete answer. The test is *longevity*: not "did
people like it in a one-hour study" but "was anyone still playing it in two
years", which is a measurable claim, almost never made, and directly relevant
to the final-project students who will want to claim their prototype is
accessible to novices. Ask the room what their own project would look like on
Morreale & McPherson's survey in 2028.

It also quietly does something the deck currently doesn't: it applies the
course's critical apparatus to the convenor's own research community, which is
a better answer to "how do I know whether this actually works" than any
individual method.

**Where it goes.** Reactable and Ocarina open *Music Interaction* (line 203),
ahead of the convenor's portfolio — external, independently validated cases
first make the research that follows land as "the same idea at research scale"
rather than as a showcase. The framing-versus-practice segment closes the
section, before *Human-AI Creative Interaction* (line 396), where it also sets
up the AI-creativity claims to be read sceptically.

**New `references.bib` entries.**
- McPherson, A., Morreale, F. & Harrison, J. (2019). Musical Instruments for
  Novices: Comparing NIME, HCI and Crowdfunding Approaches. In Holland, Mudd,
  Wilkie-McKenna, McPherson & Wanderley (eds.), *New Directions in Music and
  Human-Computer Interaction*, Springer Series on Cultural Computing.
  <https://doi.org/10.1007/978-3-319-92069-6_12>
- Morreale, F. & McPherson, A. (2017). Design for Longevity: Ongoing Use of
  Instruments from NIME 2010-14. *NIME 2017*.
  <https://www.nime.org/proceedings/2017/nime2017_paper0036.pdf> — open access,
  and the source of the numbers above.

Neither is in `hci-biblio` yet; both are worth adding there too, since the
longevity paper is the kind of thing A3 students will want.

**Biblio alternatives if the three-part structure is too much.**
`marshall2011chi` (Breath Control of Amusement Rides — the Broncomatic,
deployed to the paying public, already cited in this deck) is the best single
swap for Ocarina; Edmonds's *The Art of Interaction* ch. 5 has four practice
case studies if you want something from the art side.

---

## Week 12 — Human-centred AI: Air Canada's chatbot (2022–2024)

**Fork.** Put a generative chatbot on your website that answers policy
questions in its own words, or constrain it to retrieving and linking the
policy page. The first is better UX by every conventional measure — fewer
clicks, plain language, no navigation.

**Consequence.** The chatbot told Jake Moffatt he could apply for a
bereavement fare retroactively. Air Canada's actual policy, on another page of
the same site, said the opposite. In *Moffatt v. Air Canada*, 2024 BCCRT 149,
the tribunal rejected the airline's argument that the chatbot was a separate
entity responsible for its own actions, held that the chatbot is part of Air
Canada's website and that the company is responsible for all information on
it, and awarded damages for negligent misrepresentation. Small money, large
precedent.

**Concept + test.** This is the deck's *Design Metaphors* section (line 328)
adjudicated in court: Air Canada's defence was pure *intelligent agent*
metaphor — the bot as an actor with its own agency — and it lost to the
*supertool* view that it is a component of a product its owner is answerable
for. Plot it on the *Two Dimensional HCAI Framework* (line 251): high
automation, low human control, on a surface where a wrong answer is a
representation by the company. The eight design guidelines (line 268) become a
live checklist, and *Towards supertool designs* (line 385) acquires a concrete
meaning — the retrieval-and-link version is the supertool, and it is the
boring option that would have worked.

The test is one students can actually run on their own final projects: adopt a
"no ungrounded claims" rule for any generated text that states policy or fact,
and evaluate the bot against a set of known-answer questions where the correct
behaviour is a link, not a paragraph.

**Companion (5 min): Google Photos, 2015.** The app labelled photographs of
Jacky Alciné and a friend, both Black, as "gorillas". Google apologised, and
the fix it shipped was to remove the "gorilla" label from the product; a *New
York Times* test in 2023 found the label, and several related primate labels,
still absent eight years later. The fork is the one every AI feature will hit:
fix the model, or remove the failing capability from the interface. Google
chose the interface-level mitigation, permanently. Whether that is engineering
honesty or a cover-up is a genuinely open question and a good closing
discussion for the course.

**Where it goes.** Anchors *Design Metaphors* and gives *Governing Structure*
(line 528) a concrete referent. Under the live arc, it's the counterweight to
the agent-mode build: the same "let it answer in its own words" decision, at
toy scale and at company scale, in the same lecture.

**Sources.** *Moffatt v. Air Canada*, 2024 BCCRT 149 — the decision text is
public and short enough to quote directly; cite the case, not the law-firm
commentary. Google Photos: contemporaneous coverage for 2015, and the 2023
*New York Times* investigation for the follow-up.

**Optional 2-minute contrast: Robodebt.** Worth naming exactly once, precisely
*because* it is not an interface failure — the defect was in the
income-averaging rule and the reversed burden of proof, and no usability
method in this course would have found it. That boundary is worth drawing on
the last day: HCI has methods that catch specific, findable defects, and
knowing which failures they don't reach is part of knowing the discipline.
Your call whether this lands as clarity or as a detour.

**Biblio alternative.** `satchell-beyond-user:2009` (Beyond the User: Use and
Non-Use in HCI) — the theory, not a case; use it as the reading.

---

## Production checklist

1. **New `references.bib` entries.** Goldberg & Richardson 1993; MacKenzie &
   Zhang 1997; FCC 2018 (`@techreport`); Snap Q2 2018 10-Q (`@misc`); FTC
   Buzz consent order 2011 (`@misc`); Hanson & Bolthouse 2024; Kohavi &
   Thomke 2017; Kramer et al. 2014; *Moffatt v. Air Canada* 2024 BCCRT 149
   (`@misc` with the neutral citation); McPherson, Morreale & Harrison 2019
   (`@incollection`); Morreale & McPherson 2017 (`@inproceedings`). Source them
   from Crossref/publisher metadata, not by hand — same rule as `hci-biblio`.
   `wang2014ocarina` and `jorda2010reactable` are already there and need
   nothing; the two McPherson/Morreale items should go into `hci-biblio` too.
2. **Slide template.** No new SCSS needed: the beats map onto existing classes
   — `.info-box` for the fork, `.talk-box` for the vote, `.warn-box` for the
   consequence, `.success-box` for the test that would have caught it. A
   `.case-box` in `css/_palette.scss` + `charles_reveal_dark.scss` is a
   ten-line addition if you want the segments visually identifiable across
   the six decks.
3. **Images.** One or two per case. Prefer redrawn diagrams (the Hawaii
   dropdown, the Snapchat before/after navigation, the Air Canada two
   contradictory pages side by side) over lifted screenshots — they project
   better and dodge the rights question. Images can't be shared across content
   directories.
4. **A `resources/case-studies.md` page.** Six one-page write-ups with
   sources, built by `make resources` and linked from Canvas. This is the
   cheap half of survey action §4.1 — students asked for "more examples of
   good HCI designs and assignment expectations", and a page they can read
   before the A2 and final-project rationales is worth more than the lecture
   segment alone.
5. **Assessment hooks.** Weeks 8, 9, 10, 11 and 12 each end on a method the
   final project's evaluation plan could use — week 11's is longevity, which is
   the one most final-project prototypes will have no answer for. Say so explicitly, and consider one
   line in the final-project spec inviting students to name a case study their
   design would have to avoid repeating.
6. **Check the References slides.** Each deck gains 1–3 citations;
   `filters/reveal-refs-split.lua` handles overflow, but per the repo
   CLAUDE.md the fullest deck was at 794px of 1080 as of 2026-08-02, so
   eyeball the rendered HTML after the additions.

## Budget

12–15 minutes per lecture, paid for by the compressions named in each "Where
it goes" — none of which is new content loss, since all six displace
descriptive slides in favour of the same material applied. Inside what the
survey asked for (20–30 minutes was the ask; 15 minutes plus the discussion it
seeds is the realistic version), and it moves in the direction two students
independently requested when they asked for fewer slides and more activity.

## Open questions

- Week 9 carries the heaviest load already (final-project details, three
  sections, and under the live arc the main data collection). Three short
  cases may be one too many — Snapchat is the one to keep if only one fits.
- Whether to run these as lecture segments only, or also as a tutorial
  activity. The tutorials are already full and §3C of the survey says pacing
  is uneven, so the default should be lecture only.
- Newton/Palm is the weakest on primary sources: Graffiti's side is well
  covered by research, Newton's failure is press and folklore. The
  Torino/Code Jumper alternative is fully cited from the biblio if that
  bothers you.

## Revision note (2026-09-19)

The first draft of this plan used Air France 447 (week 9) and Robodebt (week
12). Both were cut: they are systems-safety and public-policy failures
respectively, and the decisions at their centre were not interface decisions.
Replaced with Snapchat's redesign, Google Buzz and Replika (week 9) and Air
Canada's chatbot with Google Photos (week 12) — all applications, all decisions
a graduate of this course could be the one making. Robodebt survives as an
optional two-minute contrast whose job is to mark the *edge* of what HCI
methods reach.

Also revised 2026-09-19: added the "What the textbooks already give us"
section after checking the PDFs directly, which added Sharp §14.4–14.5 to week
8, the Dilemma boxes as warm-ups in weeks 7–9, and Shneiderman's Tesla-naming
passage to week 12.

Refined 2026-09-19 (2): week 11 rebuilt as Reactable + Ocarina + the
framing-versus-practice corrective from McPherson, Morreale & Harrison (2019)
and Morreale & McPherson (2017). Dilemma boxes confirmed as in-lecture
warm-ups only, not pre-class tasks.

## Implementation note (2026-09-19)

Drafted into lectures 07 to 12 on the `case-studies-weeks-7-12` branch:
3 slides in 07 (Newton vs Palm), 2 in 08 (Hawaii, replacing the heuristic
evaluation video slot), 5 in 09 (Snapchat x2, Buzz, Replika), 3 in 10 (Facebook
x2, Bing), 4 in 11 (Reactable, Ocarina, longevity, framing vs practice), 4 in
12 (Air Canada x2, Google Photos, Autopilot). Every case ends on the
evaluation that would have caught it, using the existing box classes; no new
SCSS. Twenty-one new `references.bib` entries, DOI ones from Crossref, the
rest checked against the primary document. Redrawn diagrams for Hawaii,
Snapchat, Buzz, Replika, Air Canada and Google Photos; Commons photos (CC
BY-SA) for the Newton and Palm; matplotlib charts for the Facebook effect
sizes, Snap DAUs and the NIME longevity survey. Not done from the checklist:
the `resources/case-studies.md` page and the final-project spec hook. The
Sharp "Dilemma" warm-ups and the optional Robodebt contrast were left out to
keep the segments to the minimum slides.
