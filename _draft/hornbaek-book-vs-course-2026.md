# How Hornbæk, Kristensson & Oulasvirta (2025) reads against COMP3900/6390

*Analysis July 2026. Compares* Introduction to Human-Computer Interaction *(OUP, open access, DOI 10.1093/oso/9780192864543.001.0001) against the 12 lectures, 10 workshops, and 4 assessments of the 2026 course. The course's inherited spine is Rogers/Preece* Interaction Design *and Shneiderman* Designing the User Interface*.*

---

## Overview

This book is not a competitor to Rogers/Preece — it is a different *kind* of textbook. Rogers/Preece organises around a design lifecycle; Shneiderman organises around interface categories and guidelines. Hornbæk et al. organise around **enduring, evidence-backed principles**, and they say so explicitly: the book focuses on insights "rather than analyzing current user interfaces or cataloging trends in contemporary HCI research" (§1.5.3), aiming for claims that "will outlive particular interaction problems, fashions, and fads."

That single sentence is where most of the friction with your course lives, and most of the support too.

Its nine parts are: Overview → Understanding People (8 ch) → User Research (6 ch) → Understanding Interaction (7 ch) → User Interfaces (7 ch) → Design (4 ch) → **Engineering (6 ch)** → Evaluation (5 ch) → Conclusion (2 ch).

---

## Where it backs you up

**1. The activity spine is the same one you teach.** Ch 1 summarises HCI practice as four activities: understand people, study what users need, design and engineer systems, evaluate their benefits. Your lecture order (design → prototype → gather → analyse → evaluate) is that spine. Nothing structural to defend here.

**2. "You are not the user" is a named principle, and it is the axiom of your A2.** It appears in the Ch 46 principle table as a Chapter 10 principle: "your intuition is insufficient for design; user research is needed." §10.6 goes further and asks *does user research work?* — presenting Norman's counter-argument that human-centred design can produce incoherent, feature-crept systems, and concluding user research has "not been proven to be necessary or sufficient." That section is close to ideal reading for the PG cohort: it models exactly the critical stance LO5 asks for, from inside a mainstream textbook.

**3. Design rationale is explicitly defined — which A1 currently assumes.** Your A1 rubric puts **50% on "sophistication and clarity of the design rationale in terms of HCI theories, perspectives, and concepts"**, but no lecture defines what a design rationale *is*. §32.2.1 does: a statement of why a decision was made, including why alternatives were rejected, whose benefit is that it "make[s] the chain of thought visible, exposing shaky assumptions." It also notes rationale "has not been adopted in design organizations, perhaps because of the amount of extra work it creates" — an honest framing that answers the inevitable "why do we have to write this?"

**4. It defends process discipline against the students who resist it.** §33.5 ("Following a process is better than ad hoc practices") argues via Parnas & Clements that even "faked" idealised processes beat ad hoc work, because they make the base of a design explicit and traceable: "Why is this feature here — in what way is it important for end-users?" This is direct support for holding students to the double diamond / lifecycle in A1 and A3.

**5. Personas get a criterion for quality, not just a template.** Personas are the single most-discussed technique in the book (~178 mentions, Ch 15). §15.5 splits their use into a **realist** route (a persona is a claim that can be true or false) and an **instrumentalist** route (whatever inspires design is fine), then insists on **traceability and verifiability** regardless: "when writing up personas, one should document the data and other knowledge they were based on." Your Week 2 lecture and Workshop 02 teach personas and scenarios without this distinction. It is a small addition that gives students a standard for a *good* persona and maps directly onto A2's requirement to derive "clearly articulated user needs" from data.

**6. It calibrates how much evaluation is enough — useful for A3.** §40.4 walks through "The Tyranny of Evaluation" and Greenberg & Buxton's "Usability Evaluation Considered Harmful (Some of the Time)", landing on: "the evidence provided should be proportional to the claims made." A3 asks students to evaluate early-stage prototypes of non-standard interactions, where a thoughtless usability test is exactly the wrong move. This gives them a principled way to scope it.

**7. Shneiderman survives intact.** 27 citations, Norman 53. Direct manipulation is treated as a *principle* with empirical support (Ch 28), and Shneiderman's HCAI guidelines paper is cited. Your Week 12 lineage is not undercut.

---

## Where it pushes back

**1. The wave narrative is absent — deliberately.** Your Lecture 01 teaches "HCI history: The 'wave' theory" and Lecture 12 revisits it in the wrap-up. In this book: "second wave" and "first wave" occur **zero** times; the single "third wave" is Weiser's ubicomp, not Bødker's. Bødker appears only in the reference list (1991, 2011). "Posthuman" is absent, "entanglement" appears once, "epistemology" once. The book uses the 1992 ACM SIGCHI definition and moves on.

This is a genuine intellectual disagreement, not an omission. The paradigm/wave literature you have assembled in `biblio/` — Bødker 2006, Kaptelinin et al. 2003, Frauenberger 2019, Petrick 2020, Chignell et al. 2023 — is a historiographic framing of HCI as a field with contested foundations. This book's §1.5.4 takes the opposite temperament: "there are known answers in HCI", "it depends" is used "less often in HCI than one might think", and the book "takes a critical position toward many popular beliefs in the field."

**Recommendation: keep the waves and name the disagreement.** It is the thing that delivers LO2's "multiple perspectives" and it is defensible. But if the book becomes a set text, students will notice, and it is better as a deliberate teaching moment than a contradiction they find alone.

**2. Reflexivity is the sharpest clash.** "Reflexiv-" occurs **zero times** in 800+ pages. "Grounded theory": zero. Thematic analysis gets **two pages** (211–212) as §11.5.3 — a technique *inside the Interviews chapter* — cited only to Braun & Clarke 2006, not the 2019/2022 reflexive turn you actually teach. It is presented as a six-step procedure with no epistemological commitments.

Your Lecture 06 is titled "Reflexivity and Thematic Analysis" and contains "What even is knowledge anyway?", epistemology, "themes do not emerge", thin vs thick themes, and code hierarchies. Workshop 06 and Workshop 10 build on it, A2 recommends reflexive TA, and PG LO5 is about the designer's own presence in the process. **You are several years ahead of this book on qualitative methodology**, and the previous course analysis was right to call this a strength.

The risk is specific: a student who reads the book as the authority will meet TA as a neutral procedure, which undercuts Lecture 06's central move. Two mitigations, and I'd do both:

- Note in Lecture 06 that the book's treatment is deliberately thin and why (its realism makes epistemology look optional).
- Use the book's own §15.5 **traceability** requirement as an unexpected ally. It demands documentation of the reasoning from data to claim — the same accountability reflexivity demands, reached from a realist direction. That is a strong argument for students who find reflexivity woolly.

**3. Understanding people comes first in the book, and it is eight chapters.** Perception, motor control, cognition, needs and motivations, experience, collaboration, communication — Part II, before user research, before design. Ch 2 states the reason: to call a choice human-centred "means that the choice is justified by reference to knowledge of how people feel, think, and behave."

Your cognitive/social/emotional material is **Lecture 09 of 12**. With semester starting 27 July, A1 is due Monday 24 August — the start of week 5 — so students write the rationale that carries 50% of A1's marks having seen only intro, design, prototype, and data gathering. Mental models, gulfs of execution and evaluation, and distributed cognition arrive four weeks *after* the assessment that most needs them.

The prior analysis flagged this as "block rather than thread". The book independently corroborates it and supplies the architecture: the material is prerequisite, not enrichment. **This remains the highest-value structural change available**, and it is now externally backed rather than just an internal opinion.

**4. Engineering is a whole pillar the course does not have — and this is a deliberate, defensible omission.** Part VII is six chapters (systems, design engineering, safety and risk, software, computational representations and models) on the premise that "a system cannot be 'just built', its construction needs to be designed."

The course has no implementation layer, and should not acquire one. Students arrive having done the programming sequence (COMP1100/1110/2100) and software engineering (COMP2120), and most go on to a group-based software project capstone. Construction is taught competently elsewhere in the degree; 12 weeks spent partially re-teaching it would displace HCI content that has no other home. The book is a whole-discipline reference, not a course specification, and Part VII is largely addressed to HCI *research on* engineering methods (§34.2) rather than to teaching students to build.

The longer-term view is that the natural implementation layer for this course is **agentic AI** rather than levelling students up in a particular framework — which sidesteps the framework-churn problem entirely.

One consequence worth thinking through, because the book supplies the answer: if implementation becomes cheap, Lecture 03's fidelity spectrum changes meaning. Buxton's "getting the right design vs getting the design right" is partly an *economic* argument — sketch first because sketching is cheap and building is dear. When a student can go from sketch to working artefact in an afternoon, that argument weakens and the case for low-fidelity work has to become cognitive instead. Ch 31 (design cognition) is where that case lives: **fixation**. Cheap generation raises fixation risk, because the first plausible artefact becomes the anchor that stops the search. That is a stronger reason to sketch than cost ever was, and it is the argument Lecture 03 will need once students can generate working prototypes on demand.

**5. Part IV claims interaction itself can be modelled.** Information and control, dialogue, tool use, automation, rationality, practice — seven chapters arguing interaction is formally tractable: information theory for interaction as messages over a noisy channel, control theory for feedback toward a goal state, dialogue as computation permitting analysis of consistency and reversibility, automation as a function-allocation problem, and interaction as utility maximisation. Your old README schedule mapped a week to the "Computational Interaction" CHI subcommittee; the current 12 lectures have no equivalent. Your theory content is the Norman/distributed-cognition/embodied lineage in Lecture 09 — compatible, but students never see that interaction can be predicted rather than only interpreted.

**6. The interfaces catalogue gets a re-cut.** Lecture 07 is "45 years of interface types!" — CLI, GUI, multimedia, AR/VR, web, mobile, appliances, voice, pen, touch, touchless, haptic. This is the pattern the book explicitly refuses. Its Part V cuts by *mechanism* instead: input devices, displays, interaction techniques, commands and navigation, GUIs, reality-based interaction. That reorganisation supplies the analytical throughline the earlier analysis found missing, and it generalises — a student who understands input devices and interaction techniques can reason about a modality invented after graduation.

(Lecture 07 also carries the research-skills content — Scholar, ACM DL, citation — which is unrelated to interfaces and, per the prior analysis, needed from week 1.)

---

## What the book does *not* do, that you do

Worth being clear about, so adoption isn't mistaken for wholesale replacement:

- **Statistics.** §43.7 states plainly: "In this book, we do not offer a comprehensive overview of statistical methods for HCI", referring out to Robertson & Kaptein. "t-test" appears once, "effect size" never, ANOVA five times. Your Lecture 10 — t-tests, ANOVA variants, assumptions, regression, non-parametric tests, ART ANOVA, with worked IMPSY/EMPI case studies — is substantially *more* than the book offers. This reframes the standing recommendation: the content is a differentiator, only its placement (week 10, after A2 is due week 9) is the problem.
- **Expressive and creative interaction.** Creativity in this book is the *designer's* creativity (Ch 31 design cognition). Creativity support tools appear once, as a citation. There is no counterpart to Lecture 11 — no NIME, no artistic practice, no gesture-to-sound mapping. That lecture is your own contribution to the field and the book does nothing to displace it.
- **A dedicated HCAI framework lecture.** The book handles AI as automation (Ch 20) and rationality (Ch 21); LLMs appear ~14 times, mostly as tools or exercise prompts. Shneiderman's two-dimensional HCAI framework and design metaphors — your Lecture 12 — have no equivalent chapter.

Conversely, the book covers ground the course currently drops: **accessibility (~71 mentions), ethics (~96), inclusivity (~24), sustainability (~21), participatory design (~20)**. LO2 promises "ethical and inclusive considerations" and the old Shneiderman-aligned schedule had a Universal Usability week; the current 12 lectures have no dedicated slot, though `_draft/` still holds unused `universal-usability.md`, `08-ethics.md`, and `09-sustainability.md`. The book would give any of those a citable spine.

---

## Practical adoption notes

- **It is open access (CC BY-NC-ND 4.0).** Unlike Rogers/Preece and Shneiderman, it can be set as a required text at zero cost to 179 students. That alone may justify adoption as a secondary reference.
- **38 chapters carry Exercises sections**, several already shaped like your pre-class tasks — e.g. Ch 1's "track your frustrations for an hour, then ask whether better design would have avoided them", and Ch 15's "prompt ChatGPT to generate a persona, then critique it", which is close to your A2 territory.
- **Ch 46 is a table of every principle in the book, typed as Observation / Model / Guidance.** That typology is worth stealing outright — see below.
- **Ch 45 ("Growing into the HCI discipline")** is the strongest chapter for this course's purposes — see below.

---

## Chapters 45 and 46 in detail

These two are the closest match to how this course already thinks, and at ~20 pages combined they are realistic as a set reading in a way that Part II is not. Ch 46 is explicitly addressed to "HCI teachers and students alike." Specific attachment points to existing course components:

**§45.1 gives Workshop 08 a rubric.** Five criteria for reading a paper critically — **Argumentation, Evidence, Contribution, Impact, Significance** — with the note that these "map well to the evaluation criteria used by reviewers at scientific conferences in HCI." Workshop 08 already has students analyse CHI and DIS papers against methodological criteria; this is a citable, discipline-standard version of those criteria. The section also supplies the motivating statistic (only ~5% of citations in HCI papers are critically engaged) and two teachable myth examples: "muscle memory", which psychology does not recognise, and the claim that 93% of communication is nonverbal, which came from a far narrower study. For a course requiring five-plus references per assessment, that is directly on point.

**§45.2 sharpens Lecture 08's research-question activity.** Lecture 08 has "Four steps to write a research question", a worked example, Research Question Bingo, and a write-your-own activity. §45.2 adds three named failure modes the activity can test against:

- *Wrong level of abstraction* — the memorable bad example is "Why do aging users make errors when using Microsoft Word version 17.3 when they are sitting near a pool in Belize?", raised to "What causes errors in the use of word processing software, and how do factors related to aging interact with those?"
- *Solution-confounded* — "What does the interview method tell us about children's motivation to use tablets in schools?" presupposes the method; the neutral form drops it.
- *Not refutable* — questions that presuppose their answer, including the pet-theory and pet-system cases.

Plus a line worth quoting at students directly: "Off-hand comments about a problem being novel are almost always wrong."

**§45.3 is the justification A2 already demands.** A2 requires "a clear study plan with justification from HCI academic research." §45.3 explains *why* in terms students will accept: "merely going and measuring things easily leads to results that cannot be properly explained; in other words, we do not understand the conditions in which our results hold." It also frames research plans as **boundary objects** — documents made to be handed to others for scrutiny — which is a good description of what an A2 submission actually is.

**§45.4 supplies the counterweight the expressive strand needs.** The core rule is the same as §40.4 ("claims must be commensurate with the evidence"), and it explicitly extends rigour to design: "the artifacts we present are justified, and key decisions are grounded in observations and theories about users" — which is A1's rubric in one sentence. But it then limits itself: "being rigorous for its own sake is dogmatic... the call for rigor should not throttle creative acts such as experimentation and envisioning." For a course carrying a Lecture 11 on expressive interfaces, that sentence matters as much as the rule it qualifies.

**§45.7 addresses a prior specific to CS students.** Table 45.1 lists Wobbrock & Kientz's seven contribution types — empirical, artifact, methodological, theoretical, survey, dataset, opinion — and then names the two mirror-image surprises: computer science and behavioural science students are surprised that "artifacts, often presented in the form of demonstrations or software, can be first-class contributions to HCI research", while design students are surprised by "HCI's emphasis on theories as the basis of decision-making." This cohort is the first group. The table legitimises A1 and A3's prototype-as-contribution framing, legitimises the NIME-style work in Lecture 11, and gives A3 students vocabulary for stating what kind of contribution they have made.

**§45.5 has a ready-made Lecture 12 activity.** The thought experiments about ultimate interfaces are structured as vision-plus-dilemma: the perfect display raises the question of replicating a user being shot dead; the mind-reading interface leaves no room for private thought; the perfect AI partner means "you would have no autonomy left — there would no longer be a need for humans at all." That last one is Shneiderman's autonomy argument compressed into a paragraph, and it lands in exactly the slot Lecture 12 occupies.

**§45.6 is the ethics content LO2 promises.** The ACM Code of Conduct's four moral principles, plus a Bunge quote on why being a student or subordinate is not an exemption: "The scientist, engineer or manager may well wash his hands but this will not free him from moral duties or social responsibilities." LO2 commits to "ethical and inclusive considerations" and `_draft/08-ethics.md` is still unbuilt; this is a spine for it.

**§45.8 describes what this course already does.** Open access, open data, open source, open educational resources — and the authors' own invitation: "this book is open access, and so are the materials we developed... we hope that educators who use this book in teaching will share their experiences and developed materials." The course site is already public and the materials openly licensed, so this is alignment rather than advice.

**Ch 46's typology is the transferable device.** Every principle in the book is typed as one of three things:

- **Observation** — a recurring aspect of HCI to take into consideration
- **Model** — a formal relationship that can be exploited to explain behaviour or make design decisions
- **Guidance** — a concrete suggestion for approaching a problem

That distinction is worth teaching on its own, independently of whether the book is adopted. A1's top rubric band asks for theory engagement "beyond learning materials", and the most common way students fall short is treating a piece of advice as though it were a finding. Giving them three labels makes the difference visible and gradeable. Fitts' law is a Model; "be human centered" is Guidance; "experiences cannot be designed directly" is an Observation — and a rationale that confuses those categories is exactly what the rubric is trying to catch.

---

## Lectures 2 and 3 in detail

Part VI (Design) is the book's closest engagement with these two decks, and Ch 31 (Design cognition) carries almost all of it. **An important constraint first:** the 2026 balance audit already flags lectures 2 and 3 as overlong, so what follows should mostly *reorganise or displace* rather than add. The single most valuable item below — the three-axis frame for ideation methods — is probably shorter than the slides it would replace.

### Lecture 02: the ideation block

**The organising frame the "Choosing a Technique" slide is reaching for.** §31.2.2 sets out the quantity-drives-quality principle (expansion, then selection, often alternating) and then gives three axes along which *any* ideation method varies:

1. **How far associations are sought.** Further associations yield more novel ideas — but "the proportion of valuable ideas decreases the more distant the ideas are from known solutions." That tradeoff is the useful part; it is what makes the choice of technique a judgement rather than a preference.
2. **How other people are involved.** Stated bluntly: "Having more people generating ideas does not automatically translate into more or better ideas."
3. **How different representations are used.** Sketching is visuospatial; brainstorming is mostly verbal.

This converts a list of seven techniques into a space students can reason about, and it carries forward into Lecture 03 (sketching is on axis 3) and into the tutorials.

**A divergence in which techniques count.** The book's list of the eight most-used methods comes from a survey of professional designers: brainstorming, function/morphological analysis, scenarios, conceptual maps, checklists, analogies, metaphors, storyboards. Against the current slides:

- Brainstorming is well covered (~34 mentions).
- **Braindump, brainwrite, brainwalk, worst possible idea, and mindmap have zero occurrences.** The book's implicit position is that these are procedural variants of brainstorming rather than distinct methods.
- **Analogy (~27) and metaphor (~69) are treated as first-class ideation moves and are missing from the ideation block.** Worth noting that `erickson-metaphors:1995` is already in `references.bib`, and metaphor returns in Lecture 12 as an HCAI design framing — so teaching it here as an ideation technique would connect the two ends of the course.

**A caution that lands on "Why bad is the new good".** Lateral thinking — the de Bono family that Worst Possible Idea belongs to — is explicitly flagged: "the merits of lateral thinking are unclear in the scientific literature, as there is a lack of solid evidence of the efficacy of such methods. As a consequence, lateral thinking techniques are controversial." The general warning is broader: "Methods forcing idea generation may fail to produce creative ideas... Ideas that are forcefully produced are often simple variations of existing solutions."

This is not a reason to drop the activity. The pedagogical case for Worst Possible Idea — it lowers the stakes and gets quiet students contributing — is a different claim from the efficacy case, and it holds regardless. But the book will not back the efficacy claim, and it is better to teach it as "this works as a way of loosening a group up" than as "this produces better designs."

**Three things directly usable:**

- **Individual ideation before group ideation.** "To avoid becoming biased by others' ideas when brainstorming in a team, individuals are often given some time alone to think about solutions." This applies to the tutorials more than the lecture, since that is where ideation is actually group work.
- **Kelley's seven rules** (Paper Example 31.2.1): sharpen the focus, playful rules, number your ideas — with ~100 ideas/hour as a stated benchmark — build and jump, the space remembers, stretch your mental muscle, get physical. Plus the brainstorm-killers: letting the most senior person speak first or most, insisting on experience, and not being playful. The numeric target is the most useful part for a timed tutorial activity.
- **Inspiration card workshops**: random pairings of *technology* cards with *domain* cards as ideation seeds. Mechanically the same idea as Rogerson, Sparrow & Freeman's SMeFT Decks, which is already in `biblio/` — a ready link from a taught method to a paper students can read.

**Also relevant here:** §15.5 on personas (realist vs instrumentalist, plus traceability and verifiability) belongs in this lecture — see "Where it backs you up" above — and §33.5's defence of following an idealised process is the answer to students who find the double diamond artificial.

### Lecture 03: sketch and prototype

**Sketching is classed as an ideation method, not a representation method.** §31.2.3 sits inside "Generating solutions" and says sketching "shares many characteristics with brainstorming." That is closer to Buxton than the current framing, and it ties the deck back to Lecture 02's ideation block rather than leaving the two as separate topics.

**Its criteria map onto the existing "What should a sketch include?" slide:** done quickly, quantity over quality, inexpensive and disposable *yet documented so they can be returned to later*, using clear visual conventions and established terminology. And one line worth putting on a slide verbatim:

> "A sketch should not be of higher resolution than required for the intended purpose."

That is the fidelity principle as a single rule, and it is a better formulation than a low-fi/high-fi binary because it makes fidelity a function of purpose.

**Fixation is the argument the fidelity spectrum will need.** Confirmed in the text (61 mentions, introduced in Ch 1: "In design fixation, a designer maintains an early identified solution... Even experienced designers suffer from design fixation"), with §31.2.2 giving the mechanism: suspending criticism and generating many alternatives "can prevent design fixation." As implementation gets cheaper — see the engineering note above — this replaces the economic case for sketching with a cognitive one, and it is the stronger argument of the two.

**A quantity benchmark.** Figure 31.2 documents a real project (a cashless-society concept for Singapore's Smart Nation programme): 50 preliminary designs, 25 intermediate designs, roughly 30 iterations. Concrete numbers answer "why make so many?" better than an assertion does.

**Design rationale (§32.2.1) needs a home in one of these two decks.** A1 weights it at 50% and no lecture currently defines it. Lecture 03 is the more natural fit if it is framed as "what you write down about the prototype you just made", Lecture 02 if framed as part of the process.

---

## Priorities

1. **Move a compact "understanding people" block before A1** (or re-weight A1's rubric toward the prototyping process it actually follows). The book's Part II architecture is the strongest external argument yet for a change already identified internally.
2. **Decide the reflexivity position explicitly and teach it as a position.** The book's silence is an opportunity — use §15.5 traceability as the realist ally, and keep your methodological lead.
3. **Set Ch 45 as a reading and steal Ch 46's typology.** These are the two chapters that fit the course as it stands rather than asking it to change shape: Ch 45 attaches to Workshop 08, Lecture 08, A2's justification requirement, and Lecture 12 at named points above, and Ch 46's Observation / Model / Guidance distinction is a gradeable device for the theory-engagement band of A1's rubric. Both are cheap to adopt.

**Done so far (July 2026):** the book is now cited in `references.bib` as `hornbaek-intro-hci:2025`. Workshop 08's pre-class task carries the §45.1 critical-reading rubric as five aspects (students pick two, to stay inside the 100–200 word forum post), and Task 1's group discussion uses it as its frame. Lecture 08 gained three slides from §45.2 between the worked example and Research Question Bingo — knowledge/capability gaps, then the three failure modes (abstraction level, solution-confounded, refutability) — and the RQ activity now asks students to test candidate questions against them. Verified through both the reveal.js and Beamer builds; lecture 08 is now 44 slides.

**Cheapest remaining change:** the Lecture 02 ideation reorganisation in the section above. It replaces a list of techniques with the three-axis frame, which should shorten a deck the balance audit already calls overlong.

*Not a priority: the Part VII engineering gap.* Construction is covered upstream in the degree (COMP1100/1110/2100, COMP2120) and downstream in the capstone; see the note above on why this is a correct omission rather than a hole, and on the fixation argument that Lecture 03 will need as implementation gets cheaper.
