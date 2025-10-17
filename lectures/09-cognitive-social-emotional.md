---
title: Cognitive, Social, and Emotional Interaction
author: Dr Charles Martin
---

## Announcements

- Assignment 2 Due today!
- Next week lecture is on Friday (???)
- Course now shifts to support final project.

## Plan for the class

1. Final Project Details
2. Cognitive Aspects of Interaction
3. Social Interaction
4. Emotional Interaction

# Final Project Details

:::::::::::::: {.columns}
::: {.column width="50%"}
- a complete design and evaluation process for a prototype interactive system.
- design a prototype in response to a real-world problem
- evaluate this system using HCI research methods
- report on the results

**primary submission document: a 5-minute recorded presentation**
:::
::: {.column width="50%"}
![Two users evaluating an interface in an office foyer.](img/2020-ar-interaction.jpg)
:::
::::::::::::::

## Final Project Research Challenge

> **Sustainable living through technology**: You woke up this morning, checked your email, and found that you have a new job---_ANU Student Lead for Sustainable Living_! 

> Your challenge is to help university students adopt sustainable behaviours in their everyday lives guided by the [UN Sustainable Development Goals (SDG)](https://sdgs.un.org/goals) which call for urgent action on climate change, responsible consumption, and sustainable communities. 

> You will need to _choose a focus_ (e.g., energy use, waste reduction, transportation, consumption), _prototype_ and _evaluate_ an interface to make sustainable living more accessible, engaging or effective. Your system should involve a level of non-standard interaction, either through unusual use of standard computer IO hardware, or a novel interface. 

## Final Project Specification

- include documentation of a testable prototype, research question, evaluation plan, data collection, data analysis, and articulation of findings
- include a **video recording** of a presentation which follows the provided headings: `project-presentation.mp4`
- include documentation in `project-documentation.md` which follows the provided headings (**N.B.:** this text may be a transcript of your spoken presentation with references and images, it may also be a slightly different text.)

## Final Project Sections

Your presentation and documentation will have the following sections:

1. **Research Question, Plan, and Conclusions**

2. **Prototype Design and Features**

3. **Research Data, Analysis and Findings**: N.B. you can choose to collect either qualitative, quantitative, or both

4. **COMP6390 Only---Positionality Statement**: critically reflect on your presence and influence within the technology design process in a [statement of positionality](https://smcclab.github.io/thirty-nine-hundred-hci/lectures/06-reflexive-thematic-analysis.html#/reflexivity).

## Video Presentation

:::::::::::::: {.columns}
::: {.column width="50%"}
- clear and concise covering the section headings above
- understandable audio **spoken by you**
- must include **video of your face** while presenting in the presentation
- must include at least 5 but no more than 10 slides
- title slides, personal introductions, tables of contents, reference slides are **not required** (waste of time!)
:::
::: {.column width="50%"}
Suggested recording method: [Microsoft Powerpoint's built-in recording tool](https://support.microsoft.com/en-au/office/record-a-presentation-2570dff5-f81c-40bc-b404-e04e95ffab33)

**no genAI or text-to-speech allowed for the video presentation!**
:::
::::::::::::::

## Questions on the Final Project

Who has a question about the final project? (Or anything else?)

# Cognitive Aspects

:::::::::::::: {.columns}
::: {.column width="60%"}
The way we think affects how we act and interact in our life.

We can design systems to cope well with human cognition to fit well with our capacity for remembering, deciding, perceiving, and attending.
:::
::: {.column width="50%"}
![COGNITION (Photo by Stefano Bucciarelli on Unsplash)](img/stefano-bucciarelli-59HOF9zHKNs-unsplash.jpg)
:::
::::::::::::::

## Cognition

:::::::::::::: {.columns}
::: {.column width="50%"}
A definition from Oxford English Dictionary:

> The action or faculty of knowing taken in its widest sense, including sensation, perception, conception, etc., as distinguished from feeling and volition...
:::
::: {.column width="50%"}
![(Photo by Mathilda Khoo on Unsplash)](img/mathilda-khoo-HLA3TAFQuQs-unsplash.jpg){width=50%}
:::
::::::::::::::

## Cognitive processes

Cognitive processes can change depending on the problem:

- **Experiential Cognition**: 2 + 2 =
- **Reflective Cognition**: 312 x 56 =

A famous frame for this difference is "fast and slow thinking" [@kahneman-fast-slow-thinking:2011].

## What are cognitive processes?

:::::::::::::: {.columns}
::: {.column width="60%"}
1. Attention
2. Perception
3. Memory
4. Learning
5. Reading, speaking, listening
6. Problem solving, planning, reasoning, decision making

[@eysenck-brysbaert:2023]
:::
::: {.column width="40%"}
![(Photo by Luke Jones on Unsplash)](img/luke-jones-DHR8LQRY-fU-unsplash.jpg){width=50%}
:::
::::::::::::::

## Attention

:::::::::::::: {.columns}
::: {.column width="60%"}
Selecting things to focus on, relevant to our needs,  from possibilities.

- clear goals (directed searching vs browsing)
- information presentation (structure and layout in the interface)
- multitasking and attention
  - depends on individuals and context
  - relevance of distractions
  - effort to task switch
  - designing to support effective multitasking
:::
::: {.column width="40%"}
![Structured and Unstructured information text [@rogers-beyond-hci:2023]](img/structuring-information.jpg){width=50%}
:::
::::::::::::::

## Design Implications for Attention

:::::::::::::: {.columns}
::: {.column width="60%"}
- consider context to make information salient when required
- techniques: animation, colour, ordering, spacing
- avoid cluttered visual interfaces
- support switching and returning (but how?)
:::
::: {.column width="40%"}
![Some interfaces need to be very careful about attention... (Photo by milan degraeve on Unsplash)](img/milan-degraeve-89sXVIkgYnI-unsplash.jpg)
:::
::::::::::::::

## Perception

:::::::::::::: {.columns}
::: {.column width="60%"}
- how we sense information and transform it into experience
- proprioception: Awareness of position and movement of body through muscles and joints
- vision dominant for sighted folks
- followed by hearing and touch
- important to present information so that it can be readily perceived
:::
::: {.column width="40%"}
![How does our perception influence design? (image: Mathilda Khoo on Unsplash)](img/mathilda-khoo-HLA3TAFQuQs-unsplash.jpg){width=80%}
:::
::::::::::::::

## Design Implications for Perception

:::::::::::::: {.columns}
::: {.column width="60%"}
- design icons and graphics to be distinguished
- white space and separators to group information
- sounds (earcons!) can help distinguish information
- colour contrast is important for perception (and accessibility)
- haptic feedback: use carefully, perhaps in response to user initiated actions
:::
::: {.column width="40%"}
![The layout of music controls in AR affects perception [@wang-cubing-sound:2022]](img/2022-cubing-sound-designs.jpg){width=100%}
:::
::::::::::::::

## Memory

:::::::::::::: {.columns}
::: {.column width="60%"}
- brain filters what to remember and what to forget to avoid overload – but not always in the way we want to!
- filtering into memory – depends on encoding process (e.g., active vs passive learning) and context (e.g., seeing someone in a different context)
- people are better at **recognition** than recall
- relying on technology rather than memory (e.g., car navigation system, “let's ask Claude..”)
- personal information management
- remembering passwords and multifactor authentication
:::
::: {.column width="40%"}
![Photo by Piotr Miazga on Unsplash](img/piotr-miazga-xOZXquhp7RA-unsplash.jpg){width=50%}
:::
::::::::::::::

## Design Implications for Memory

:::::::::::::: {.columns}
::: {.column width="60%"}
- avoid long and complex procedures for carrying out tasks
- design interfaces for **recognition** rather than recall (familiar patterns and consistency)
- provide ways to label digital information for identification
:::
::: {.column width="40%"}
![This is a bad pun, but memory cards are hard to recognise! File management systems help us to use recognition rather than recall to sort stored data. (Image: Denise Jans on Unsplash)](img/denise-jans-d9aVAvr5NVo-unsplash.jpg)
:::
::::::::::::::

## Learning

:::::::::::::: {.columns}
::: {.column width="60%"}

accumulation of skills and knowledge through memory [@rogers-beyond-hci:2023 p.119]

- incidental learning vs intentional learning
- learning by reading vs learning by doing
- learning through collaboration
- micro-learning
- multimodal learning through new and emerging technologies e.g., augmented reality and virtual reality
:::
::: {.column width="40%"}
![[@hooper-french-kitchen:2012]](img/02_theory_and_concepts_10.jpg){width=50%}

![[@cheng-language-culture:2017]](img/02_theory_and_concepts_11.jpg){width=50%}
:::
::::::::::::::

## Design Implications for Learning

:::::::::::::: {.columns}
::: {.column width="60%"}
- design to encourage exploration
- design constraints and guide users to appropriate actions

Learning theory concept: "zone of proximal development"---we should get users into that state!
:::
::: {.column width="40%"}
![How do we encourage exploration and embed guidance into systems! Games are awesome at this. (Image: Philippe Bout on Unsplash)](img/philippe-bout-93W0xn4961g-unsplash.jpg)
:::
::::::::::::::

## Reading, Speaking, Listening

:::::::::::::: {.columns}
::: {.column width="60%"}
- communication skills
- meaning the same across modes
- writing is permanent, speaking is transient
- reading quicker than listening
- listening less cognitive effort than reading
- some more grammatical than others
- interactive books, speech technologies, natural language processing, tactile interfaces, assistive technologies
:::
::: {.column width="40%"}
![Our experience of the same information changes depending on the context, reading a book, chatting with a friend, listening to a meeting (Image: Chris Montgomery on Unsplash)](img/chris-montgomery-smgTvepind4-unsplash.jpg)
:::
::::::::::::::

## Design Implications for Communication

:::::::::::::: {.columns}
::: {.column width="60%"}
- keep length of speech menus to minimum (less than 3-4 options)
- extra intonation on artificial speech
- provide options for making text large
:::
::: {.column width="40%"}
![Source: [Design Boom](https://www.designboom.com/technology/blind-maps-for-iphone-interactive-braille-interface/)](img/02_theory_and_concepts_12.png){width=50%}

![Photo by [Nicolas J Leclercq](https://unsplash.com/@nicolasjleclercq)](img/02_theory_and_concepts_13.jpg){width=50%}
:::
::::::::::::::

## Problem Solving, Planning, Reasoning, Decision Making

:::::::::::::: {.columns}
::: {.column width="60%"}
- Involve “reflective cognition” in relation to actions, choices, consequences
- How do you make purchasing decisions? What role does technology play?

:::
::: {.column width="40%"}
### Design Implications

- Provide information and help for users to improve their performance.
- Use simple and memorable functions for rapid decision making.
- Let users set their own configuration and options.
:::
::::::::::::::

# Cognitive Frameworks

- **Mental models**
- **Gulfs of Execution and Evaluation**
- **Information Processing**
- **Distributed Cognition**
- **External Cognition**
- **Embodied Interaction**

## Mental Models

:::::::::::::: {.columns}
::: {.column width="60%"}
A mental model is our internal understanding of how a system works.

- used to reason about unfamiliar technology or troubleshoot problems
- develop through experience; often incomplete or incorrect
- common errors from misapplying logic of a system: thermostat/oven vs. water tap
- poor mental models lead to difficulty identifying problems and explaining system behavior
- interfaces can help through clear instructions, contextual help, and appropriate metaphors
:::
::: {.column width="40%"}
![[Mental Models (nngroup)](https://www.nngroup.com/articles/mental-models/)](img/mental-models-nngroup.jpg){width=80%}
:::
::::::::::::::

## Gulfs of Execution and Evaluation

:::::::::::::: {.columns}
::: {.column width="50%"}
influential early HCI framework describing gaps between user and interface [@norman-cognitive-engineering:1986]

- gulf of [evaluation](https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/): understanding state
- gulf of [execution](https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/): understanding controls
- design challenge is bridging these gulfs to reduce cognitive effort
- framework explores mappings between system design and user understanding
- provides discourse for identifying mismatches in user-system interaction
:::
::: {.column width="50%"}
![Problem with switches: how do you know what happens when you switch it!](img/02_theory_and_concepts_18.png)
:::
::::::::::::::

## Information Processing

- **Mind as information processor**: (1980s metaphor) mind processes information through ordered stages (input, processing, output) involving mental representations like images, models, and rules
- **Human processor model**: conceptualized cognition as series of perceptual, cognitive, and motor processors to predict user interaction times with computers (Card et al., 1983)
- **Reaction time predictions**: The information processing approach enabled hypotheses about user response times and cognitive bottlenecks when overloaded with information
- **Shift to external cognition**: Modern HCI focuses on understanding cognitive activities in context, analyzing how environmental structures support cognition and reduce cognitive load
- **Cognitive load measurement**: Mental effort required for learning is assessed through methods like NASA-TLX survey, which measures mental demand, physical demand, temporal demand, performance, effort, and frustration

## Distributed Cognition

:::::::::::::: {.columns}
::: {.column width="60%"}
- interactions between multiple people and artefacts
- event-driven, systems as the unit of analysis, collective behaviours
- information flows and transformations through the system
- different levels of granularity
- analysis addresses problem solving, communication (verbal and non-verbal), coordination mechanisms, accessing and sharing knowledge
- analysis can inform design implications and decision-making in designing to support distributed cognition
:::
::: {.column width="40%"}
![Image: @rogers-beyond-hci:2023 p.128](img/02_theory_and_concepts_23.png)
:::
::::::::::::::

## External Cognition

:::::::::::::: {.columns}
::: {.column width="60%"}
- internal representations (in the head) and external representations (artefacts in the world) and how they interact
- combined with tools (e.g., pens, calculators, spreadsheets) to support cognitive activities
- the cognitive processes involved when we interact with different external representations
- cognitive offloading, computational offloading, annotating and cognitive tracing
:::
::: {.column width="40%"}
![Cognitive Offloading](img/02_theory_and_concepts_21.jpg){width=30%}

![Computational Offloading](img/02_theory_and_concepts_22.jpg){width=30%}

![Cognitive Tracing](img/02_theory_and_concepts_20.jpg){width=30%}
:::
::::::::::::::

## Embodied Interaction

our bodies and experiences shape how we perceive, feel, and think [@hornecker2005design]

- artifacts indicate usage through coupling to the world (e.g., open book as task reminder)
- sensorimotor experiences enable abstract thinking (inside-outside, up-down concepts)
- body mediates interactions with technology and shapes emotional responses
- movement instrumental in thought evolution and spatial thinking development
- abbreviated actions more effective than full simulation for learning skills

# Social Interaction

## Activity: Social human computer interactions

:::::::::::::: {.columns}
::: {.column width="60%"}
Let's consider one angle on social computer use.

> What are the kinds of situations in which you would phone someone (rather than text)?

**Write** for 2-3 minutes, **vote** for 1 minute, then let's discuss.
:::
::: {.column width="40%"}
![PollEverywhere link: <https://pollev.com/charlesmarti205>](img/polleverywhere-charles-qr.png)
:::
::::::::::::::

## Being Social

fundamental part of everyday life; how does technology mediate this?

- social media transformed how people connect across time and space
- COVID-19 accelerated videoconferencing adoption (and highlighted limitations)
- excessive phone use raises wellbeing concerns
- digital etiquette (muting, virtual hand-raising, emoji reactions)
- social coordination shifted to texting; added complexity!

## Face-to-Face Conversations

:::::::::::::: {.columns}
::: {.column width="50%"}
conversation may seem effortless but is a skilled collaborative achievement. how do these unfold?

- turn-taking rules: speaker chooses next, someone else starts, or current speaker continues [@sacks-simplest-systematics:1978]
- adjacency pairs: first utterance sets expectation for response
- repair mechanisms: repetition, gestures, and clarifications
- nonverbal cues coordinate conversation flow
- interfaces that emulate human conversational patterns are a long term goal! recent progress with AI.
:::
::: {.column width="50%"}
![Conversation is a key human capability that can be used in HCI (Photo by Aarón Blanco Tejedor on Unsplash)](img/aaron-blanco-tejedor-aocUkMcxeqI-unsplash.jpg)
:::
::::::::::::::

## Remote Conversations

:::::::::::::: {.columns}
::: {.column width="60%"}
- **video conferencing:** early research (1980s-90s) showed people spoke louder, took longer turns, interrupted less
- mainstream adoption via Skype, FaceTime, then Zoom/Teams
- virtual 2D spaces (e.g., Gather.Town) aim to recreate social presence and community
- **telepresence** creates perception of being present in a physical location while actually elsewhere
- **telepresence** through robots, rooms, virtual reality, games
- **social presence:** the feeling of _being there_ in a virtual space
- features of interaction design can establish a sense of presence and facilitate remote conversation
:::
::: {.column width="40%"}
![Telepresence in music at NIME2025 with a live pianist and two remote musicians (Photo by Charles)](img/2025-nime-remote-performance.jpg)
:::
::::::::::::::

## Co-Presence

:::::::::::::: {.columns}
::: {.column width="60%"}
supporting people in activities when they are interacting in the same physical space

- supporting effective collaboration
- hand gestures, body language, use of objects
- awareness: knowing what is going on around you, functioning as “close-knit teams”
- shareable interfaces: whiteboards, touch screens
- social translucence: enabling participants and activities to be visible
:::
::: {.column width="40%"}
![The Reflect Table: Pierre Dillenbourg in @rogers-beyond-hci:2023 p.55](img/02_theory_and_concepts_29.png){width=50%}

![musical instrument holograms to aid collaboration [@wang2025seeingsound]](img/aisee-holo-view.jpg){width=50%}
:::
::::::::::::::

## Social Games

:::::::::::::: {.columns}
::: {.column width="60%"}
games designed to facilitate social interaction between two or more players who are aware of each other's presence and actions

- can be cooperative or competitive, played with or without technology (board games, video games, online platforms)
- three heuristics: synchronous vs asynchronous interaction, symmetrical vs asymmetrical relationships, strong vs weak social ties [@ricchetti-social-games:2022]
- unconventional approaches, e.g. Journey (shared exploration)
- communities through live streaming (Twitch) foster social bonds
:::
::: {.column width="40%"}
![[Journey (2011)](https://www.gamespot.com/articles/journey-co-op-impressions/1100-6297312/) had an unconventional coop mode with almost no communication possible and little gameplay gain except the feeling of shared experience.](img/journey-game-coop.jpg)
:::
::::::::::::::

# Emotional Interaction

:::::::::::::: {.columns}
::: {.column width="60%"}
How do our emotions manifest in interaction?

Can designing for emotions help us in our tasks, or help us manage them?
:::
::: {.column width="40%"}
![Pepper Robot (Photo by [Alex Knight](https://unsplash.com/@agk42)](img/02_theory_and_concepts_49.jpg)
:::
::::::::::::::

## Emotions and Behaviour

- emotions affect behavior but relationship is complex and context-dependent
- emotional interaction design considers what makes users feel happy, sad, anxious or motivated
- users express emotions through facial expressions, body language and tone of voice
- automatic emotions happen rapidly while conscious emotions develop slowly
- interfaces can detect emotional states but decisions needed on appropriate responses

## A Model of Emotional Design

:::::::::::::: {.columns}
::: {.column width="60%"}
Understanding emotions assists with design. Positive and negative emotional states have different effects on creativity and tolerance [@norman-emotional-design:2005]

@ortony2012affect model of emotional design:

- visceral: look, feel, sound
- behavioural: use (usability)
- reflective: meaning, personal value, culture
:::
::: {.column width="40%"}
![[@ortony2012affect]](img/02_theory_and_concepts_50.png){width=100%}
:::
::::::::::::::

## Expressive Interfaces and Emotional Design

:::::::::::::: {.columns}
::: {.column width="60%"}
- design features that seek to create an emotional connection with users or elicit emotional responses in users
- expressivity through animation, sonification, vibrotactile feedback (e.g., mobile phone or watch buzzing)
- aesthetics affects perceptions of usability and pleasure of use
- annoying interfaces elicit negative responses 
:::
::: {.column width="40%"}
![Duolingo Reminders](img/02_theory_and_concepts_51.png){width=50%}

![Windows Blue Screen of Death](img/02_theory_and_concepts_52.png){width=50%}
:::
::::::::::::::

## Affective Computing and Emotional AI

:::::::::::::: {.columns}
::: {.column width="60%"}
- computers recognising and expressing emotions ([Rosalind Picard: Affective Computing, Engineering Emotion](https://www.youtube.com/watch?v=_86GQiEOjp4))
- measuring of feelings using facial expressions, voice, and physiological data
- sensing technologies: cameras, biosensors, speech analysis, motion capture, accelerometer sensors
- typical ML task classify emotions (anger, joy, sadness) as percentages from facial markers
- mood tracking apps: help manage emotions, moods, and mental health
:::
::: {.column width="40%"}
![Analysing emotion from a camera image.](img/02_theory_and_concepts_55.png)
:::
::::::::::::::

## Persuasive Technologies

:::::::::::::: {.columns}
::: {.column width="60%"}
persuasive design uses interface techniques to change user behavior and thinking

- pop-ups, recommendations, prompts, and one-click purchasing
- playful interventions ([piano stairs](https://youtu.be/2lXh2n0aPyw), [echoing bins](https://youtu.be/cbEKAwCoCKw))
- fitness trackers use dashboards, leaderboards, and social comparison for motivation
- social norms influence consumption - households adjust behavior based on neighborhood comparisons
- effective persuasion balances being noticeable without being intrusive or overly abstract
:::
::: {.column width="40%"}
![The world's deepest bin (2009) a playful bin that sounds like dropping an rubbish in a deep hole.](img/worlds-deepest-bin.png)
:::
::::::::::::::

## Anthropomorphism

:::::::::::::: {.columns}
::: {.column width="60%"}
anthropomorphism is the human tendency to attribute human qualities to animals and objects, widely applied in technology design

- applied in software designs, as well as hardware such as robots
- e.g., _"ChatGPT"_ vs _"Claude"_. 
- personalized first-person interaction ("Hi Charles!") proves more engaging than impersonal third-person commands
- robot dolls incorporate sensors, speech recognition, and servos
- should robots be hard (Sony AIBO) or soft designs that enhance emotional connection through touch? (e.g., haptic creature, @yohanan-haptic-creature:2008)
:::
::: {.column width="40%"}
![The haptic creature [@yohanan-haptic-creature-assessment:2011]](img/haptic-creature-2011.png)
:::
::::::::::::::

## Questions: Who has a question?

:::::::::::::: {.columns}
::: {.column width="60%"}
**Who has a question?**

- I can take _cathchbox_ question up until 2:55
- For after class questions: meet me outside the classroom at the bar (for 30 minutes)
- Feel free to ask about **any aspect of the course**
- Also feel free to ask about **any aspect of computing at ANU**! I may not be able to help, but I can listen.

:::
::: {.column width="40%"}
![Meet you _at the bar_ for questions. 🍸🥤🫖☕️ Unfortunately no drinks served! 🙃](img/kambri-bar.jpg)
:::
::::::::::::::

# References {.allowframebreaks}
