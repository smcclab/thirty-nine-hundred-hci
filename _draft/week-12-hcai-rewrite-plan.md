# Week 12 rewrite: stress-testing Shneiderman's HCAI against 2026

*Planning doc, 13 Oct 2026. Lecture delivered in week 12; finish the build by
the end of week 11. Companion to `landing-2026-weeks-11-12.md`. Builds on the
week 12 section of `weeks-7-12-live-arc.md` and the Hornbæk comparison in
`hornbaek-book-vs-course-2026.md`.*

## Decisions (Charles, 13 Oct)

1. **Spine:** keep Shneiderman (2022), presented as *the 2021 position*, and
   test it claim by claim against what happened after ChatGPT. Hornbæk et
   al. (2025) Ch 18 and Ch 20 supply the older automation theory underneath;
   post-2022 HCI research supplies the test.
2. **Demo:** both, short: nanojam agent mode (supertool vs. autonomous) plus a
   brief live agentic-coding moment.
3. **Revision block:** cut from ~20 slides to a 3–4 slide A3 checklist (there
   is no exam).
4. **Own work:** Choi, Andres, Hunter & Martin (2025), GenAI sound design via
   scenario-based design, as one worked HCAI-process case.

## The problem, stated precisely

`shneiderman-2022-human-centered-ai.pdf` contains **zero** occurrences of
"GPT" or "language model". Its chatbots are Tay, Woebot, Replika and
customer-service bots (Ch 16, pp. 133–4). It has no account of:

- natural language as the *primary* interface to general-purpose AI
  (prompting, the empty text box);
- a mass-market product that is anthropomorphic *by design* and sycophantic
  by training;
- generative output (text, code, images) as the thing users must evaluate;
- agents that act across tools and the web for minutes or hours on a
  delegated goal;
- adversaries hiding in the *data* the AI reads (prompt injection), rather
  than attacking the system from outside;
- the measured effects on productivity, skill and critical thinking that
  2023–26 studies now report.

Hornbæk et al. (2025) **does not fill this gap either**. It was written in
the early 2020s; LLMs appear ~14 times, mostly as exercise prompts. What it
does give us is a **theory layer that predicts most of what went wrong**,
which Shneiderman's book only gestures at: function allocation, types and
levels of automation, the ironies of automation, mixed-initiative
principles, dialogue as turn-taking with repair. That is the case for the
stress-test framing. The old theory works and the 2021 framework was
incomplete, and that can be demonstrated, not just asserted.

## What Hornbæk gives us (page refs to the OUP open-access PDF)

| Section | Content | Use in week 12 |
| --- | --- | --- |
| Paper Ex. 20.0.1 (p. 340) | Shneiderman vs. Maes 1997 debate; Maes's agent = knows habits, proactive, long-lived; Shneiderman = predictability, overview, don't confuse human and machine responsibility; both converged on mixed initiative; "more than 20 years later, a similar discussion was held" | **The opening frame.** Maes's three agent properties read like a 2026 product spec (memory, proactivity, persistence). Ask: who won? |
| §20.1.1 (p. 342) | Shared control via **extension** (power steering), **relief** (auto gearbox, autocomplete), **partitioning** (spell-check highlights, user fixes) | Quick taxonomy for students to classify AI features in their A3 |
| Paper Ex. 20.3.1 (pp. 342–3) | **H-metaphor**: shared control like riding a horse; loose-rein vs. tight-rein control; both agents need models of each other; 4 levels: strategic/tactical/operational/execution | Pair with Doctorow's **centaur/reverse centaur** slide (already in the deck). The horse metaphor is the positive version: you must be able to tighten the rein. |
| §20.1.2 (p. 343) | Allocation strategies: maximum automation (leaves humans the leftovers), most-capable agent (Fitts lists), economic; **authority problem** | Explains reverse centaurs: maximum automation *defines* the human role as whatever the machine can't do |
| §20.1.3 (pp. 343–6), Tables 20.1–20.2 | Parasuraman et al. levels **and types** (acquisition / analysis / decision / action / adaptive) | The deck has the levels table only. **Add the types**: an LLM agent spans all four, which is why one "autonomy level" no longer describes it |
| §20.2 (pp. 346–8), Fig 20.1 | Evaluation criteria: **mental workload, situation awareness, complacency, skill degradation**; system-level: reliability (TP/FP rates), cost of outcomes; six-step workflow | The four primary criteria become the **evaluation lens for the demo** and an A3 tool |
| §20.3 (pp. 348–9) | Interactive AI as augmentation, dialogue, monitoring, recommendations; "interactive AI is already ubiquitous… users do not realize" | Replaces the "practical robots / washing machine" slides with one line |
| §20.4 (pp. 350–1) | **Ironies of automation** (Bainbridge 1983): deskilling, vigilance, **agency**; Boeing 737 MAX; "attempts to automate do not replace the human; they only change the type of engagement" | The theory under the Tesla case, and the bridge to 2023–26 evidence on skill and critical thinking |
| Paper Ex. 20.3.2 (pp. 351–3) | Explainable AI: saliency, counterfactuals; explainability-accuracy trade-off; Wang et al.'s five design implications (forward reasoning, coherent factors, source data, **show uncertainty**, multiple explanations) | One slide on reliance: "show uncertainty, link the source" (connects to the Air Canada "link the source" test) |
| §18 intro + Paper Ex. 18.0.1 (pp. 309–11) | Dialogue = turns, context, shared state, initiative; **Liu & Chilton prompting** ("brute-force trial and error") | The interaction-paradigm slide: chat is a dialogue interface, so dialogue theory applies |
| §9.2.2–9.2.3 (pp. 166–7) | Turn adjacency and **repair**; "conversational agents struggle with adjacency" | Why chat errors are hard to repair; links to week 9 conversation content |
| §18.4 (pp. 318–20) | **Horvitz's mixed-initiative principles** (12, incl. "only automate if direct manipulation would be inferior", uncertainty → ask, efficient invocation *and termination*, minimise cost of poor guesses, socially appropriate behaviour, working memory, keep learning) | **A 1999 guideline set that has aged better than the 2021 one.** Run it head-to-head with Shneiderman's eight in the scorecard activity |
| §18.5 (pp. 322–3) | Kirsh's critique: users explore and *don't know the options*; discoverability | The empty prompt box is the extreme case: zero discoverability |
| Ch 15 exercise 3 (p. 275) | LLM-generated personas: "discuss how valid and informative" | One-line link to A2/A3 (and to the A2 data-integrity rules) |
| §41 (p. 720) | Langevin et al. heuristic evaluation for conversational agents | A3 pointer: if your prototype has an AI feature, here is a method |
| §45.5 (pp. 788–9) | Thought experiments; "the perfect AI partner… you would have no autonomy left" | **Closing think-box** before the wrap |
| §45.6 (p. 789) | ACM code; Bunge: engineers "cannot… disclaim all responsibility" | Pairs with the governance slide and the Air Canada verdict |

## Progress

- [x] **23 Oct: mechanical pass done** (commit on `main`): 2026 course stats
      slide (students from lucy, commits from git, slide/word/image counts
      from `count_slides.sh`, Ed numbers from the discussion-analytics CSV
      export); "Plan for the class" reframed as the stress test;
      announcements updated; revision block cut from 18 slides to a
      3-slide A3 checklist plus concept map and key challenges. Deck is 48
      slides. Still open on those slides: regenerate `img/hci-commits.jpg`
      (2025 screenshot), confirm tutorial marks entered and SELT dates
      (TODO comments in the source).
- [x] **25 Oct: core rewrite, additive pass** (uncommitted on `main`): 18 new
      slides inserted next to the existing slide each one argues with, nothing
      cut or moved. Added: 1997 debate opener; "five claims to test" bridge;
      Parasuraman *types*; H-metaphor; Bainbridge ironies; section slide +
      A1–A2 (text box, gulf of envisioning); B1–B2 (anthropomorphism,
      sycophancy/persuasion) before Air Canada; D1–D2 (Maes's agent as product
      with Feng's user roles, prompt injection) after Designs for Tele-bots;
      C1–C4 (ironies restated, METR perception gap, skill/productivity,
      design responses) after the Autopilot case; "what held / what broke"
      scorecard before Takeaways. Deck is 62 slides, ~6,800 words, 81 PDF
      pages. All new slides checked for overflow in headless Chrome at
      1920x1080. Hornbæk quotes and page numbers verified against the OUP PDF;
      Shneiderman 2022 confirmed to contain zero "GPT"/"language model".
      **Compress pass still to do** (verdict table below): the 2021-position
      section is now 8 slides; "Towards supertool designs" duplicates the new
      opener; blocks run A, B, D, C because the Autopilot slide sits where it
      does; old Takeaways overlaps the new scorecard slide.
- [ ] Scorecard *activity* (the slide exists; the pairs exercise does not).
- [ ] Demos (nanojam agent mode not started; source is `~/src/hci/nanojam`,
      which already has `api.js`/`logger.js` hooks commented for it).
- [x] References for blocks A–D into `references.bib` (25 Oct): 22 entries,
      16 from Crossref by DOI, 5 arXiv `@misc` with a preprint note, 1 Medium
      post (`shneiderman-muller-ai-anthropomorphism:2023`). Not yet copied to
      `hci-biblio/biblio.bib`, and no PDFs saved.

## Slide-by-slide verdict on the current deck

Legend: **Keep** (as is or light edit) · **Reframe** (keep content, change its
job) · **Compress** · **Cut** · **New**.

| Current slide | Verdict | Notes |
| --- | --- | --- |
| Announcements, Final Project | Keep | Update counts/dates (see landing doc) |
| Plan for the class | Reframe | "Today we will (try) to cover *all* of Shneiderman" → "Today we test a 2021 framework against 2026" |
| Course stats | Done 23 Oct | 2026 numbers in; commits screenshot still 2025's |
| What is HCAI? / HCAI | Keep, compress | One slide. The definition holds up. |
| Why is this important? | Reframe | "CLI (chatGPT)… confusing magical tools (agentic coding)" was written as a 2025 aside; make it the lecture's thesis |
| How is HCAI different (process/product, supertools) | Keep | The process/product split is still the best part of the book |
| White Robot vs Supertool | Keep, sharpen | Tropes critique now applies to *products*: chat assistants are given names, personas and first-person voice by design |
| HCAI structure | Compress | Merge into "the 2021 position" summary slide |
| People and Computers (anti-anthropomorphism) | Keep, strengthen | Shneiderman's warning was right and industry ignored it: sycophancy, companions (week 9 Replika case), role-play framing |
| Why start with a framework? | Cut | Merge into the levels slide |
| Rising above levels of automation | Keep, extend | Add Parasuraman's **types**, via Hornbæk §20.1.3 |
| Reverse Centaurs | Keep, pair | Add H-metaphor (loose/tight rein) as the positive counterpart |
| Reliable, Safe, Trustworthy | Compress | Fold into governance |
| 2D HCAI framework | Keep, **the thing under test** | Open question: can high automation and high control coexist for agents? Bring in human-AI team evidence |
| Eight design guidelines (+3 detail slides) | Reframe → **scorecard activity** | See below. Several map strikingly onto agentic tools (preview first → plan mode; audit trails → transcripts/diffs); others broke (control panels → empty text box); one was blindsided (adversarial attacks → prompt injection) |
| Design Metaphors / Science vs Innovation | Compress | One slide; keep the Pepper photo |
| Intelligent Agents and Supertools (thinking-machine myth, Turing, Natale) | Keep, update | Punchline: industry adopted the *agent* metaphor wholesale ("AI agents", "agentic"); the metaphor Shneiderman warned against won the naming war |
| **Case: Air Canada** | Keep | Strongest slide in the deck. Now the anchor for "anthropomorphism won the market" |
| **Case: Google Photos** | Keep | Move to the end as the closing think (already framed as "good last question") |
| Towards supertool designs (Licklider, 1997 debate, Maes) | Keep, move earlier | Becomes the opening frame, with Hornbæk Paper Ex. 20.0.1 |
| Teammates and Tele-bots | Keep | The existing think-box ("is agentic coding a telebot or teammate?") becomes the demo's question |
| Designs for Tele-bots | Compress | Merge with above |
| Assured Autonomy | Compress | Merge into ironies of automation |
| **Case: Autopilot (Williston)** | Keep | Now explicitly an *irony of automation* (vigilance) and a naming lesson: compare "Autopilot" with "Copilot" and "agent" |
| Control centres | Cut (or 1 line) | Possible one-liner: multi-agent "mission control" dashboards are the 2026 version |
| Social Robots / AIBO | Cut | Least relevant in 2026; week 9 covers anthropomorphism and Replika |
| Practical Robots (washing machine) | Cut → 1 line | Replace with Hornbæk §20.3: "interactive AI is already ubiquitous; users don't notice" |
| Governing Structure (Bryson quote, 4 levels) | Keep, update | Add EU AI Act via `rozgonyi-2026-ethics-eu-ai-regulation.pdf` (already in biblio); one line on Australia's position (verify current status before stating) |
| Traditional AI vs HCAI table | Keep | Good closing contrast |
| Takeaways | Rewrite | Around "what held / what broke / what to do in your project" |
| Revision: waves, usability goals, design stages, sketch, prototype, data gathering, quant, RTA, thin/thick themes, interface types, CSE, eval plan, stats, expressive, research challenges | Done 23 Oct | Cut to concept map + 3 A3-checklist slides + "Key challenges of HCI research" |
| So long, and thanks for all the fish | Keep | |

Net: roughly 61 → ~45 slides, with two activities and two demos added and
~25 minutes freed from revision.

## New material: four things the book didn't see

Each block is 1–3 slides and leads with a claim that **can be checked**,
following the case-study selection rule in `case-studies-weeks-7-12.md`.
All citations below were verified against Crossref/arXiv on 13 Oct (see the reading list); ‡ marks a preprint, which should be presented as early evidence.
**Do not put an unverified figure on a slide.**

### A. The interface became a conversation

- Chat is a *dialogue* interface (Hornbæk Ch 18), so turns, shared context
  and **repair** apply, and conversational agents are weak at adjacency and
  repair (Hornbæk §9.2).
- The empty prompt box is Kirsh's discoverability problem taken to the limit:
  every option is available and none is visible. Non-experts prompt by trial
  and error (Liu & Chilton 2022; Zamfirescu-Pereira et al. 2023).
- Link back to **week 9's gulfs**: the new difficulty is earlier than
  execution, in forming the intention at all, which Subramonyam et al.
  (2024) call the *gulf of envisioning*.
- Shneiderman's guideline 3 ("steer by way of interactive control panels")
  is the casualty: the market shipped a text box.

### B. Anthropomorphism won the market

- Shneiderman argued *against* systems that equate computers with people.
  The dominant 2023–26 product is a first-person, named, conversational
  persona.
- Sycophancy (Sharma et al. 2024) is a measurable consequence of training on
  human approval: the model tells you what you want to hear. Shanahan et al.
  (2023) "role play" as the better mental model.
- Air Canada stays here: the *agent* metaphor lost in court.
- Jakesch et al. (2023): co-writing with an opinionated model shifts the
  writer's own stated views. Persuasive technology (week 9) without anyone
  intending it.

### C. Reliance, and the ironies come back

- Bainbridge's ironies (via Hornbæk §20.4) apply directly: deskilling,
  vigilance, agency. Simkute et al. (2024) restate them for generative AI.
- **The perception gap (the strongest slide for this course):** Becker et
  al. (METR, 2025)‡: 16 experienced developers, 246 tasks in their own
  repos. With AI allowed, tasks took **19% longer**. They had forecast a 24%
  speed-up and afterwards believed they had been 20% faster. That is a lesson about **self-report vs.
  measurement**, which students learned in weeks 8 and 10. Use it as a
  "which would you trust: the survey or the stopwatch?" talk-box.
- Learning and skill: Shen & Tamkin (2026)‡ RCT (52 developers learning Trio): AI group 50% vs 67% on the quiz, worst on debugging, and those who delegated code-writing scored lowest. Bastani et al. (2025, PNAS) find the same in high-school maths, and that a hint-giving tutor largely prevented the drop. Lee et
  al. (2025) on knowledge workers' critical thinking. Frame as early
  evidence, not settled.
- Productivity is uneven: gains concentrate on novices and on tasks inside
  the "jagged frontier"; outside it, AI help makes people worse (Noy & Zhang
  2023; Brynjolfsson et al. 2025; Dell'Acqua et al. 2026). Vaccaro et al.
  (2024) meta-analysis: human+AI teams on average underperform the best of
  either alone, but gain on *creation* tasks. This bears directly on the
  2D framework's promise.
- Design responses with evidence: show uncertainty and source (Hornbæk
  Paper Ex. 20.3.2), cognitive forcing functions (Buçinca et al. 2021; effective but disliked). Note that explanations alone *raise* acceptance whether or not the AI is right (Bansal et al. 2021), and that first-person hedges ("I'm not sure, but…") reduce over-reliance (Kim et al. 2024).

### D. Agents: delegation at scale

- Maes's 1997 agent properties (knows you, proactive, long-lived) are now
  shipping features: memory, background tasks, agents that run for hours.
- One "level of automation" no longer describes a system: an agent does
  acquisition, analysis, decision *and* action (Parasuraman types).
  Feng et al. (2025)‡ recast autonomy as the **user's role**: operator,
  collaborator, consultant, approver, observer. Students can place their
  own tools on it.
- **Prompt injection** is the guideline the book couldn't anticipate: the
  adversary is in the content the agent reads, not attacking from outside.
- Counter-position for balance: Mitchell et al. (2025)‡, "fully autonomous
  AI agents should not be developed".

### E. HCAI as research: the "LLM wrapper" critique (2–3 slides, ~6 min)

The research-culture view of the same problem, and the most useful block
for students who want to do HCI research. The phrase "LLM box" turned out
not to exist in print; the critique circulates as **"LLM wrapper"**. Present
"a box in the system diagram" as your own framing.

1. **Scale (Pang et al., CHI '25).** Of 153 CHI papers that engage with LLMs
   (2020–24), ~63% use the LLM as a *system engine*. Most contributions are
   artifacts or empirical studies, models are overwhelmingly closed GPT-family
   and their choice mostly unjustified, and 40% of prompting papers don't
   release prompts. Their §5.1.3 question: "Is it a system contribution, if
   the implementation is straightforward, given LLMs' capabilities?"
2. **The provocation (Arawjo 2024, blog).** As a CHI 2024 reviewer, he found
   about half his pile were "LLMs applied to X", where the novelty was that
   nobody had done it yet. His five tests for getting past wrapper status:
   real engagement with prior work; a reason for an LLM over a non-AI
   approach; design/architecture iteration; a contribution beyond "we
   applied an LLM"; a study beyond a Likert usability test or a contrived
   ablation. **This is your "faster and preferred" critique**, and it is
   Greenberg & Buxton (2008) and Olsen (2007) again: the weak usability
   study is standing in for the contribution.
3. **The twist (Felix Navarro, Syriani & Arawjo, CHI '26).** Interviews with
   18 authors of LLM-system papers: almost all had heard "wrapper", always in
   rejections, and no one could define it consistently. In one set of
   reviews it decided a rejection. The label became a lazy reviewer shortcut. **Talk-box:** "Is your A3
   prototype a wrapper? Apply Arawjo's five tests to it."

Optional companion line (ties to A2's participant verification): the other
way an LLM replaces part of a study is as the *participant*. See Hämäläinen
et al. (CHI '23 Best Paper: synthetic answers are believable, so crowdsourced
self-report may become unreliable), Agnew et al. (CHI '24, "illusion of
artificial inclusion"), Wang et al. (*NMI* 2025: LLMs misportray and flatten
identity groups). This is the research-side reason our A2/A3 participant
lists are verified.

## Activities

1. **Scorecard (10 min, talk-box, pairs).** Hand out Shneiderman's eight
   guidelines and Horvitz's mixed-initiative principles (Hornbæk §18.4).
   Each pair grades one guideline against a 2026 system they use (ChatGPT,
   Copilot, Claude Code, Gemini in Gmail…): **held / broke / blindsided**.
   Collect on the board. Expected result: preview-first and audit-trail
   held (plan mode, diffs); control panels broke; adversarial attacks was
   blindsided; Horvitz's "efficient invocation and termination" and
   "minimise cost of poor guesses" are the most violated. This
   is also the evidence for the lecture's claim that the 1999 principles
   aged better.
2. **Perception gap talk-box (3 min)**, in block C.
3. **Closing think (2 min)**: Hornbæk §45.5's perfect-AI-partner dilemma,
   then Google Photos as the final unresolved question.

## Demos

### Demo 1: nanojam agent mode (~10 min)

nanojam is live at <https://charlesmartin.au/nanojam/> and is already the
weeks 7–9 throughline. Add two modes on the same six-command engine:

- **Supertool** (`#ui.interface=assist`): type a goal ("make me a
  four-on-the-floor beat with offbeat hats"); the model returns a *proposed*
  pattern shown as CLI text with a preview button; human **auditions,
  edits, accepts or rejects**. This is guideline 2 in miniature (preview
  first, select and initiate, then manage execution).
- **Autonomous** (`#ui.interface=agent`): the model is given the goal and a
  `nanojam_command` tool and jams on its own every N bars, changing the
  pattern as it sees fit. Show two versions: (a) opaque, with no log and no
  stop; (b) with a visible **command log (audit trail)** and a **stop
  button (efficient termination)**. The difference between (a) and (b) is
  the lecture's argument made audible.
- Evaluate live with Hornbæk's four criteria: ask the room about workload,
  situation awareness ("what's it doing now?"), complacency, and **agency**
  ("whose beat is this?"). Agency connects directly to week 11 and
  co-creativity.

Build notes:

- Model: `claude-haiku-5-5` for latency (one tool, tiny context). One tool:
  `nanojam_command(command: string)` that accepts the existing six commands.
  System prompt lists the command grammar from the CLI help.
- **API key must never ship in the static page.** For a lectern-only demo,
  a paste-in key held in `sessionStorage` is acceptable, or a 20-line local
  proxy. Default the agent modes to hidden unless a key is present, so the
  public page is unchanged for students.
- Fallback: screen-record a clean run of both modes in week 11 and keep the
  video on the lectern laptop (venue network has failed before).
- Source location: confirm where the nanojam source lives. It is not in
  `~/src/hci`.

### Demo 2: agentic coding moment (~5 min)

Claude Code (as used in COMP4020) on a tiny, safe nanojam task, e.g. "add a
clap sample and a `clap` command":

1. **Plan mode**: the agent proposes steps before touching anything
   (preview first).
2. Approve (select and initiate). Permission prompts appear as it runs
   (manage execution).
3. Show the **diff and transcript** (audit trail).
4. Ask the teammate-or-telebot question from the existing think-box.

Run it on a throwaway branch. Have the finished result pre-built on a second
branch in case it takes too long live.

## Own-work case (3–4 min)

Choi, Andres, Hunter & Martin (2025), *Scenario-Based Design to Envision How
GenAI Can Support Sound Design Practices* (`choi2024scenario` in
`references.bib`; PDF `choi-2024-genai-sound-design.pdf`). Use it as
**HCAI's "process" claim done properly**: start from a prior needs study of
sound/UX designers, write practitioner scenarios, *then* decide which
GenAI capabilities belong in the tool (four applications, four supporting
features). It is the opposite of "add a chatbot", and the method (week 2
scenarios) is one students already have. Place it right after block D as
"what HCAI design looks like when you do it".

## A3 checklist (replaces revision; 3–4 slides)

Built from the A3 rubric, one line per course concept:

- Needs → design: trace each design decision to a finding (Hornbæk §15.5
  traceability; week 2, A2).
- Prototype fidelity matches the question (week 3).
- Evaluation plan: goal, participants, data, method, analysis (week 8 slide,
  reused).
- Analysis appropriate to data: descriptive first; RTA themes not buckets
  (weeks 5, 6, 10).
- Claims proportional to evidence (Hornbæk §40.4/§45.4).
- If your prototype uses AI: say which type/level of automation it is, and
  how the user can preview, stop, and check it (today).
- Video rules + participants section + raw data (A3 spec).

## Proposed running order (~110 min incl. questions)

| Min | Block |
| --- | --- |
| 0–8 | Announcements, 2026 stats, plan |
| 8–20 | The 2021 position: HCAI, supertool vs white robot, 2D framework, eight guidelines (as claims to test) |
| 20–32 | The older theory: 1997 debate → levels *and types* → ironies → H-metaphor / centaur / reverse centaur |
| 32–57 | Four things the book didn't see (A–D), Air Canada and Autopilot cases inside B and C, perception-gap talk-box |
| 57–72 | Demos: nanojam supertool vs agent; agentic-coding moment |
| 72–82 | Scorecard activity |
| 82–86 | Own-work case (Choi et al.) |
| 86–92 | Block E: LLM-wrapper critique + "is your A3 a wrapper?" talk-box |
| 92–96 | Governance update + Trad AI vs HCAI table + Google Photos closing think |
| 96–102 | A3 checklist, SELT, thanks |
| 102–112 | Questions |

That is over the 104-minute estimate if everything runs long. **Cut order
if it runs over:** own-work case → governance detail → block E slide 1 (keep the five tests) → demo 2.

## Reading list / references to add

Already in `references.bib`: Shneiderman 2022, Shneiderman 1997 (debate),
Parasuraman 2000, Moffatt v Air Canada, Klein 2004, Licklider 1960, Martin
1993, Natale 2021, Bryson 2020, Choi et al. 2025, Lin 2020 (Cobbie).

Already in `hci-biblio/` but not cited in week 12: Hornbæk et al. 2025,
`rozgonyi-2026-ethics-eu-ai-regulation`, `klein-2004-ten-challenges-automation`,
`landay-2019-smart-interfaces-hai` (news piece; probably skip).

**Missing from the biblio entirely: no post-2022 HCI paper on LLM
interaction is in the library.** To add: see the verified list
below.

### Verified references (13 Oct 2026)

Checked against Crossref (DOIs) and publisher/arXiv abstracts. ‡ =
preprint/not peer-reviewed. Add the BibTeX to `references.bib` and the PDFs
to `hci-biblio/` (`author-year-slug.pdf`) as each one is used.

**Theory layer (pre-LLM, still holds)**

- Bainbridge, L. (1983). Ironies of automation. *Automatica* 19(6), 775–779. doi:10.1016/0005-1098(83)90046-8
- Horvitz, E. (1999). Principles of mixed-initiative user interfaces. CHI '99, 159–166. doi:10.1145/302979.303030 (OA: erichorvitz.com/chi99horvitz.pdf)
- Amershi, S. et al. (2019). Guidelines for human-AI interaction. CHI '19. doi:10.1145/3290605.3300233. 18 guidelines grouped *initially / during / when wrong / over time*. A possible third guideline set for the scorecard, or an A3 checklist.
- Bansal, G. et al. (2021). Does the whole exceed its parts? CHI '21. doi:10.1145/3411764.3445717
- Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think. *PACM HCI* 5(CSCW1). doi:10.1145/3449287
- Langevin, R. et al. (2021). Heuristic evaluation of conversational agents. CHI '21. doi:10.1145/3411764.3445312
- Bender, E. M. et al. (2021). On the dangers of stochastic parrots. FAccT '21. doi:10.1145/3442188.3445922

**A. Conversation as interface**

- Liu, V., & Chilton, L. B. (2022). Design guidelines for prompt engineering text-to-image generative models. CHI '22. doi:10.1145/3491102.3501825
- Zamfirescu-Pereira, J. D. et al. (2023). Why Johnny can't prompt. CHI '23. doi:10.1145/3544548.3581388
- Subramonyam, H. et al. (2024). Bridging the gulf of envisioning. CHI '24. doi:10.1145/3613904.3642754. Capability, instruction and intentionality gaps.
- Tankelevitch, L. et al. (2024). The metacognitive demands and opportunities of generative AI. CHI '24 (Best Paper). doi:10.1145/3613904.3642902
- Weisz, J. D. et al. (2024). Design principles for generative AI applications. CHI '24. doi:10.1145/3613904.3642466. Six principles; a good post-LLM counterpart to Shneiderman's eight.

**B. Anthropomorphism and persuasion**

- Shanahan, M., McDonell, K., & Reynolds, L. (2023). Role play with large language models. *Nature* 623, 493–498. doi:10.1038/s41586-023-06647-8
- Sharma, M. et al. (2024). Towards understanding sycophancy in language models. ICLR 2024. arXiv:2310.13548
- Jakesch, M. et al. (2023). Co-writing with opinionated language models affects users' views. CHI '23. doi:10.1145/3544548.3581196 (n = 1,506)
- Shneiderman, B., & Muller, M. (2023). On AI anthropomorphism. *Medium, Human-Centered AI*. medium.com/human-centered-ai/on-ai-anthropomorphism-abff4cecc5ae. **Shneiderman's own post-ChatGPT update**, prompted by GPT-4 saying "I". It is not peer-reviewed, but it is the best way to let him speak for himself in 2023. No peer-reviewed Shneiderman paper on LLMs/agents was found. OUP's 2025 paperback of the book apparently has no new LLM content (unconfirmed).
- Moffatt v. Air Canada, 2024 BCCRT 149 (already cited; slide's C$812 total is right: $650.88 damages + interest + fees).

**C. Reliance, skill, productivity**

- Simkute, A. et al. (2024/2025). Ironies of generative AI. *IJHCI* 41(5), 2898–2919. doi:10.1080/10447318.2024.2405782
- Becker, J., Rush, N., Barnes, E., & Rein, D. (2025). Measuring the impact of early-2025 AI on experienced open-source developer productivity. arXiv:2507.09089 ‡
- Lee, H.-P. et al. (2025). The impact of generative AI on critical thinking. CHI '25. doi:10.1145/3706598.3713778 (319 workers, self-report)
- Shen, J. H., & Tamkin, A. (2026). How AI impacts skill formation. arXiv:2601.20245 ‡
- Bastani, H. et al. (2025). Generative AI without guardrails can harm learning. *PNAS* 122(26). doi:10.1073/pnas.2422633122
- Kosmyna, N. et al. (2025). Your brain on ChatGPT. arXiv:2506.08872 ‡. Small sample (54, then 18). **Mention only with caveats, or skip**, because it is widely over-reported.
- Noy, S., & Zhang, W. (2023). *Science* 381, 187–192. doi:10.1126/science.adh2586 (−40% time, +18% quality, narrower gap between workers)
- Brynjolfsson, E., Li, D., & Raymond, L. (2025). Generative AI at work. *QJE* 140(2), 889–942. doi:10.1093/qje/qjae044 (**15%**, not the working paper's 14%; biggest gains for novices)
- Dell'Acqua, F. et al. (2026). Navigating the jagged technological frontier. *Organization Science* 37(2), 403–423. doi:10.1287/orsc.2025.21838 (cite this, not the 2023 HBS WP). Inside the frontier: +12.2% tasks, 25.1% faster, ~40% higher quality. **Re-check the "−19 points outside the frontier" figure against the paper before using it.**
- Vaccaro, M., Almaatouq, A., & Malone, T. (2024). When combinations of humans and AI are useful. *Nature Human Behaviour* 8, 2293–2303. doi:10.1038/s41562-024-02024-1 (106 experiments; g = −0.23 vs best alone; losses in decisions, gains in creation)
- Doshi, A. R., & Hauser, O. P. (2024). *Science Advances* 10(28), eadn5290. doi:10.1126/sciadv.adn5290 (more creative individually, less diverse collectively; links to week 11)
- Agarwal, D., Naaman, M., & Vashistha, A. (2025). AI suggestions homogenize writing toward Western styles. CHI '25. doi:10.1145/3706598.3713564
- Kim, S. S. Y. et al. (2024). "I'm not sure, but…". FAccT '24. doi:10.1145/3630106.3658941
- Steyvers, M. et al. (2025). What large language models know and what people think they know. *Nature Machine Intelligence* 7, 221–231. doi:10.1038/s42256-024-00976-7 (calibration gap: longer explanations raise confidence, not accuracy)
- Sarkar, A. (2024). AI should challenge, not obey. *CACM* 67(10), 18–21. doi:10.1145/3649404. A design stance for the takeaways slide.

**D. Agents and delegation**

- Feng, K. J. K., McDonald, D. W., & Zhang, A. X. (2025). Levels of autonomy for AI agents. arXiv:2506.12469 ‡ (Knight First Amendment Institute)
- Mitchell, M., Ghosh, A., Luccioni, A. S., & Pistilli, G. (2025). Fully autonomous AI agents should not be developed. arXiv:2502.02649 ‡ (position paper)
- He, G., Demartini, G., & Gadiraju, U. (2025). Plan-then-execute: user trust and team performance with LLM agents as a daily assistant. CHI '25. doi:10.1145/3706598.3713218. **Directly supports demo 2**: involvement in planning helps, but users trusted plausible bad plans. Plan mode isn't a guarantee.
- Mozannar, H. et al. (2024). Reading between the lines: modeling user behavior and costs in AI-assisted programming. CHI '24. doi:10.1145/3613904.3641936 (CUPS: much Copilot time goes to *verifying*)
- Handa, K. et al. (2025). Which economic tasks are performed with AI? arXiv:2503.04761 ‡ (57% augmentation / 43% automation). Later Index (Appel et al., arXiv:2511.15080) shows directive delegation rising 27% → 39%. **Quote the latest Anthropic Economic Index figures, not the 2025 split.** The trend toward delegation is the point.

**E. Research culture: LLM wrappers and synthetic participants** (verified 13 Oct)

All of block E is now in `hci-biblio/biblio.bib` (13 Oct). Keys:
`pang-llmification-chi:2025`, `arawjo-llm-wrapper-papers:2024`,
`felixnavarro-reporting-llm-systems:2026`, `crisan-assess-llm-contributions:2024`,
`dierk-evaluating-llms-experiential:2025` (CHI '25 HEAL workshop: names an
"evaluation crisis" across 23 CHI LLM papers),
`greenberg-usability-evaluation-harmful:2008`, `olsen-evaluating-ui-systems:2007`,
`lee-evaluating-human-lm-interaction:2023`, `hamalainen-synthetic-hci-data:2023`,
`agnew-illusion-artificial-inclusion:2024`, `wang-llms-replace-participants:2025`,
`kapania-simulacrum-stories:2025`, `kapania-llm-productivity-tool:2025`
(CSCW: how HCI researchers themselves use LLMs), and
`schoning-ai-accelerated-papers:2026` (*Interactions*: CHI submission growth from
AI-accelerated papers). Copy entries into `references.bib` under the same keys when
cited. PDFs still to save by hand (ACM DL, IEEE and Medium block scripted
downloads): Arawjo, Crisan, Greenberg & Buxton, Olsen, Hämäläinen, Schöning.

- Pang, R. Y., Schroeder, H., Smith, K. S., Barocas, S., Xiao, Z., Tseng, E., & Bragg, D. (2025). Understanding the LLM-ification of CHI. CHI '25, Art. 456. doi:10.1145/3706598.3713726 (OA, arXiv:2501.12557)
- Arawjo, I. (2024, 6 June). LLM wrapper papers are hurting HCI research. *Medium*. ianarawjo.medium.com/llm-wrapper-papers-are-hurting-hci-research-8ad416a5d59a
- Felix Navarro, K., Syriani, E., & Arawjo, I. (2026). Reporting and reviewing LLM-integrated systems in HCI: Challenges and considerations. CHI '26. doi:10.1145/3772318.3790439 (OA, arXiv:2602.05128). **Best single source.**
- Crisan, A. (2024). We don't know how to assess LLM contributions in VIS/HCI. IEEE BELIV '24, 115–118. doi:10.1109/BELIV64461.2024.00018
- CHI 2026 revised desk-reject process (8 Aug 2025): chi2026.acm.org/2025/08/08/revised-chi-2026-papers-desk-reject-process/ (not LLM-specific; cites +58% submissions since 2023)
- Greenberg, S., & Buxton, B. (2008). Usability evaluation considered harmful (some of the time). CHI '08, 111–120. doi:10.1145/1357054.1357074
- Olsen, D. R. (2007). Evaluating user interface systems research. UIST '07, 251–258. doi:10.1145/1294211.1294256
- Lee, M. et al. (2023). Evaluating human-language model interaction. *TMLR*. arXiv:2212.09746
- Hämäläinen, P., Tavast, M., & Kunnari, A. (2023). Evaluating large language models in generating synthetic HCI research data. CHI '23. doi:10.1145/3544548.3580688
- Agnew, W. et al. (2024). The illusion of artificial inclusion. CHI '24. doi:10.1145/3613904.3642703
- Wang, A., Morgenstern, J., & Dickerson, J. P. (2025). LLMs that replace human participants can harmfully misportray and flatten identity groups. *Nature Machine Intelligence* 7, 400–411. doi:10.1038/s42256-025-00986-z
- Kapania, S., Agnew, W., Eslami, M., Heidari, H., & Fox, S. (2025). "Simulacrum of stories": Examining LLMs as qualitative research participants. CHI '25. arXiv:2409.19430 (DOI unconfirmed)

**Governance (already in biblio)**

- Rozgonyi, K., & Conde Jiménez, R. (2026). Research ethics in regulating AI: EU legislation overview (`rozgonyi-2026-ethics-eu-ai-regulation.pdf`; check the venue and add the BibTeX).

## Open questions for Charles

- Lecture slot length: is 110 min realistic, or is the hard stop earlier?
- Where does the nanojam source live, and is a local key-paste acceptable
  for the agent modes?
- Scorecard: Shneiderman's eight vs Horvitz's twelve, or vs Weisz et al.'s
  six (post-LLM)? Two lists is plenty for 10 minutes; three is too many.
