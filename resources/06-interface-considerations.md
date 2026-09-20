---
title: Interface Considerations
author: Dr Charles Martin
description: "Research and design considerations for each interface type in the week 7 catalogue, organised around the five affordance-analysis questions, for choosing a final-project platform."
---

In week 7 we looked at a catalogue of interface types and a method, _affordance analysis_, for looking at any of them. The lecture slides keep the catalogue short. This page holds the research and design considerations that used to sit on a slide after each type. Use it when you are choosing a platform for the final project, or when you need a starting point for the literature on a particular kind of interface.

The considerations are uneven. For some types (command lines, voice, tangibles) there are decades of research and settled design advice. For others (holograms, brain-computer interfaces) the honest summary is "people are still finding out". I have tried to say which is which rather than pad the thin ones.

## How to use this page {#how-to}

Run the five questions from the lecture on the interface you are considering:

1. What **interaction type** does it support: instructing, conversing, manipulating, exploring, or responding [@rogers-beyond-hci:2023]?
2. What does it **afford**, and are those affordances perceptible [@Norman:2013; @gaver-technology-affordances:1991]?
3. What does it **constrain**, and is the constraint a feature or a bug [@magnusson2010designconstrain]?
4. What is **hidden**: what can you do that nothing on the surface tells you about?
5. What is **false**: what does it look like you can do that you cannot?

Then read the section below for the type you are considering. Each section gives the main design tension for that type, the questions researchers are still asking, and one or two places to read further. If a section does not answer your question, that is a gap in the literature you could name in your project rationale.

## Command line interfaces {#cli}

**Main tension:** power versus discoverability. Everything is hidden; nothing is false. Users who have learned the commands are fast, and users who have not are stuck.

**What we know:** the 1980s produced a lot of research on the form of commands (abbreviations, full names, familiar words), on syntax (how commands combine) and on how to organise options [@shneiderman-designing-ui:1992]. The finding was that there is no universally best naming scheme. What matters is _consistency_: the same verb should mean the same thing everywhere, and the same argument order should hold across commands.

**Design considerations:** name consistently, give error messages that name the fix, provide help that can be read without leaving the interface, and offer completion so the hidden vocabulary becomes partly perceptible.

## Graphical user interfaces {#gui}

**Main tension:** the WIMP model (windows, icons, menus, pointer) makes affordances perceptible at the cost of screen space and pointer travel.

**What we know:** visual design of information, colour, typography and imagery has a mature design literature [@mullet1996designing]. Window management research asks how to support rapid attention shifts between windows and displays without distraction, which is why keyboard shortcuts, task bars and auto-fill exist. Menu research is largely about which words to use for options and how deep a hierarchy can be before people get lost.

**Design considerations:** use an established icon set rather than drawing your own (for example [Font Awesome](https://fontawesome.com) or [The Noun Project](https://thenounproject.com)), keep menu vocabulary consistent with the user's task language, and check that every icon has a text equivalent for both accessibility and learnability.

## Multimedia {#multimedia}

**Main tension:** offering many representations of the same information is only useful if people engage with more than one of them.

**What we know:** multimedia interfaces were developed largely for training, education and entertainment. The open research questions are whether they actually improve learning or play, and what people do when they have unlimited access to diverse media and simulations. The design advice is thin: provide diverse hands-on interactivity and find ways to encourage people to use all of it.

This is a weak section. If your project is a multimedia learning tool you will get more from the learning sciences literature than from HCI.

## Websites {#web}

**Main tension:** designers plan a web page as if it will be read; users treat it as a billboard passing at highway speed [@krug2014don].

**What we know:** early web research asked how to structure information so people could navigate and find things quickly. The field then shifted toward aesthetics and visual design. Breadcrumb navigation and Keith Instone's three questions ("Where am I? What's here? Where can I go?") remain the core of wayfinding on the web.

**Design considerations:** assume scanning, not reading. Design for the phone first, for small displays and infinite scrolling. Make the current location and the available exits perceptible on every page.

## Mobile devices {#mobile}

**Main tension:** a rich sensor package and a tiny control surface.

**What we know:** the affordances of embedded sensors (accelerometer, GPS, camera, microphone) led to genuinely new applications, but the screen and control space are limited and shared with the user's hand. Touch targets have to be large enough for every finger, and the placement and integration of hardware controls matters more than on a desktop.

**Design considerations:** follow a platform guideline rather than inventing your own conventions; there are good general summaries [@babich2018mobileux] and each platform publishes its own. Decide early what the phone's hidden affordances (gestures, sensors) buy you and whether they are worth the learning cost.

## Appliances {#appliances}

**Main tension:** interaction is short and infrequent, so nothing can depend on learning.

**What we know:** @cooper2014face describe appliance interfaces as _transient_: people want to do one thing and walk away. The two design principles are simplicity and visibility. Adding internet connectivity and remote apps to appliances raises the question of whether that helps the transient use case or just adds a second, hidden interface.

## Smart interfaces {#smart}

**Main tension:** automation removes people from the loop, and people notice when they want back in.

**What we know:** smart devices are ordinary now. A house with a robot vacuum, a video doorbell and a few smart speakers that are supposed to talk to each other is not a research prototype. These systems are context-aware, network-connected, often AI-driven, and learn from behaviour. The aim is usually to automate and reduce error, as in buildings that manage their own lighting and heating. Over-automation frustrates people by taking away control: sealed windows, no manual override, a separate app for every device. Human-building interaction is a recent framing that puts occupant needs and values first [@alavi2019introduction].

**Design considerations:** decide whether the system should _amplify_ what people do or act _autonomously_ [@landay2019smartinterfaces], and make that choice visible. Almost everything a smart system can do is a hidden affordance, and much of what it appears to promise (the devices "talking to each other") turns out to be false. Design the manual override first.

## Voice interfaces {#voice}

**Main tension:** conversation is natural for humans and hard for machines, so every voice interface is choosing how human-like to pretend to be.

**What we know:** voice interfaces rely on either command-based or conversation-based interaction. The main structural choices are the conversational mechanism (natural conversation versus directed dialogue where the system asks specific questions), whether users can interrupt the system ("barge-in"), how the system recovers from mishearing, and the character of the synthesised voice (gender, dialect, pronunciation). The design literature on dialogue structure, error handling and etiquette [@cohen2004voice] predates the current assistants and is still relevant to them. Known current limits include children's speech, distinguishing speakers in a group, and the need for a wake word.

**Design considerations:** a voice interface has almost no perceptible affordances. Users have to guess what they can say. Decide how you will tell them, and design the failure case (mishearing) as carefully as the success case.

## Pen-based interfaces {#pen}

**Main tension:** the pen affords writing and drawing, but the computer has to recognise what was written.

**What we know:** the Newton versus Palm case study in the lecture is the main lesson. Recognising natural handwriting was the "natural" choice and it failed. Constraining the user to a learnable alphabet (Unistrokes, Graffiti) worked [@goldberg-unistrokes:1993; @mackenzie-graffiti-usability:1997]. The constraint was the feature.

## Touchscreens {#touch}

**Main tension:** direct manipulation with no tactile feedback.

**What we know:** touch supports new interactions (swiping, carousels, virtual keyboards, multitouch zoom and rotate) that can be less precise or slower than a keyboard and mouse. Gestures beyond tap and swipe are hidden affordances: they must be learned, and the screen gives no physical feedback that they exist or that they worked.

**Design considerations:** compensate for missing tactile feedback with visual and audio cues, keep gestures few and conventional, and never make a gesture the only way to reach a function.

## Touchless and gestural interfaces {#touchless}

**Main tension:** the body is always moving, so the system has to decide which movements are input.

**What we know:** gesture recognition must detect when a gesture starts and ends and separate intentional gestures from unconscious movement. Depth cameras in phones, laptops and smart speakers make 3D gesture sensing common. Gesture can also be _output_, for example an avatar mirroring the user's movement, which raises the question of how realistic the mirror must be to feel connected to the user. A webcam plus a trained mapping is enough to make a gestural instrument [@fiebrink-wekinator-nime:2009], which is what the nanojam project builds on.

## Haptic interfaces {#haptic}

**Main tension:** touch feedback grabs attention very effectively, which is also why it becomes annoying.

**What we know:** vibrotactile feedback works for sensory-motor skill training (sport, musical instruments) and for signalling events. The design variables are actuator placement, the type and timing of the touch, and its intensity and frequency. Continuous feedback fails through habituation and annoyance; intermittent buzzes are better at grabbing attention, and different patterns can signal different events. Mid-air ultrasound haptics (Ultrahaptics) can simulate buttons and sliders that can be felt but not seen, which is an interesting case for the affordance questions: perceptible by touch, invisible to the eye.

## Multimodal interfaces {#multimodal}

**Main tension:** combining modalities promises natural interaction and costs a great deal of design complexity.

**What we know:** the most researched combinations are speech with gesture, eye-gaze with gesture, and pen with speech. Speech plus vision is the most common in products. The open research question is the honest one: what are the actual benefits of combining modalities, and is human-like interaction (talk plus gesture) effective when applied to a computer? Design guidelines are collected in @oviatt2017handbook.

**Design considerations:** a multimodal system must recognise multiple things at once (speech, gesture, gaze, body movement), and errors in one channel confuse the others. Start with one modality and add a second only when you can say what it affords that the first did not.

## Shareable interfaces {#shareable}

**Main tension:** a shared surface gives a group a shared point of reference, and takes away each person's private space.

**What we know:** tabletops and wall displays support simultaneous input by co-located groups and are used in museums, galleries and classrooms for group-based learning [@clegg2020community]. The key design issues are display layout, balancing participation (who gets to touch what), and the split between personal and shared space. Software shareables (Google Docs, Miro) move the same questions to remote collaboration.

## Tangible interfaces {#tangible}

**Main tension:** _coupling_, meaning how a physical action is linked to a digital effect.

**What we know:** tangibles link physical objects to digital representations through embedded sensors [@ishii1997tangible; @fishkin2004taxonomy]. Conceptual frameworks [@shaer2010tangible; @ullmer2005token] set out what makes them distinct. The design decisions are which physical artefacts to use (cubes, tokens, clay), where digital feedback appears (on the object, beside it, elsewhere), and how tight the coupling should be for the purpose, whether learning, play or collaboration. For the history and aims of the field see @ullmer2022weaving.

**Design considerations:** prototype with sticky notes and cardboard tokens before building anything. Physical objects have strong perceptible affordances of their own, and the digital coupling can contradict them.

## Wearables {#wearables}

**Main tension:** the device has to be worn all day by a body that has other things to do.

**What we know:** comfort (light, small, unobtrusive), hygiene (washable, removable electronics, manageable batteries) and control (touch, voice or physical controls that work without looking) come before anything else. Fashionable design reduces the stigma of assistive wearables. Sensor data such as heart rate has to be presented in a way that is meaningful and actionable, whether visually, haptically or multimodally.

## Robots and drones {#robots}

**Main tension:** how human-like or animal-like should the machine appear?

**What we know:** the research questions are largely ethical. Should a robot mimic humans emotionally and physically, or clearly be a machine with a functional role? Many people prefer pet-like robots as comforting and less unsettling. Interaction design ranges from human-like engagement (talking, gesturing) to conventional controls. Drones raise privacy concerns (observing people without consent) and the debate about autonomous weapons and meaningful human control.

## Frontier interfaces {#frontier}

The lecture groups brain-computer, shape-changing and holographic interfaces as a frontier because the design knowledge is still forming. Briefly:

- **Brain-computer interfaces.** Mental privacy and consent are the central concerns, followed by accuracy (misreading intention). For assistive use the practical design challenge is how to arrange on-screen targets so selection is easy and accurate, and how predictive text can speed up communication.
- **Shape-changing interfaces.** Physical form as input and output [@alexander2018grand]. Open questions: do they improve understanding and engagement over 2D or 3D on-screen charts, and what grid size or object count is easy to learn?
- **Holographic interfaces.** Most of the research is in industry and asks how to represent people in shared space in ways that feel natural and not creepy. Design variables are hologram size and how people interact with a projection in their own room.

## Which interface? {#which}

The lecture's closing answer is "it depends", and the things it depends on are the type of task, the people using the system, the context, reliability, social acceptability, privacy, ethics and location. That list is a checklist for your final-project rationale. Run the five questions, pick a type, and then write down which of these factors made you choose it over the alternatives. The week 8 question follows immediately: which is the better one, and how would we know?

## References
