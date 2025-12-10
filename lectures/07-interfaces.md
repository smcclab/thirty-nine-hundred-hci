---
title: Interfaces
author: Dr Charles Martin
title-slide-attributes:
    data-background-image: img/yichen-cube.jpg
    data-background-size: cover
---

## Announcements

<!--  data-background-image: img/caustic-interface.jpg
 -->
<!-- ![AR musical instrument cube. Yichen Wang. 2022.](img/yichen-cube.jpg){width=80%}
 -->

- Assignment 2 template and rubric updated
- Next two tutorials include assignment support baked into the activities.
- Still processing a few queries related to Assignment 1, should be finished soon.
- Final project will be released soon. Likely to involve thinking about alternative _interfaces_ so this is an important lecture!

**Who has a question about assignment 2?**

## Plan for the class

- Research skills (how to use Google Scholar and cite references)
- Overview of the diversity of interfaces in use and in research!
- Outline key design and research considerations
- Think about _natural_ user interfaces
- Think about which interface is _best_ for a given application or activity

# Research Skills

![Finding information when you need it (Source: Charles 2024)](img/2024-seoul-library.jpg){width=50%}

## Finding a source

- Assignments in this class require you to make independent choices
- Your choices should be backed by a source of knowledge, e.g.,
    - _what_ abilities does a particular animal have?
    - _what_ research plan makes sense for particular interface?
    - _why_ do human-AI interfaces have usability problems?

In scholarly writing, we need to **support** every statement we make. Support can be: either (1) a citation to a scholarly source _or_ (2) evidence from a study. 
**Where do you find these sources?**

## Google Scholar

:::::::::::::: {.columns}
::: {.column width="60%"}
- search engine for scholarly sources
- add more search terms to get more specific
- you can use the "time" selector on the left column to find recent work

**Careful:** 

- Google Scholar indexes anything that _looks_ like scholarly research (e.g., any PDFs on a website in a conference/journal format). Need to use critical thinking to decide whether sources are good quality or not.
- Google Scholar can give you a formatted citation but it may not have all information (e.g., URL, DOI)
:::
::: {.column width="40%"}
![Finding sources with Google Scholar](img/sources-google-scholar.png)
:::
::::::::::::::

## ACM Digital Library

:::::::::::::: {.columns}
::: {.column width="60%"}
- ACM Digital Library archives proceedings of ACM conferences and journals.
- not as good at searching, but will show you only peer-reviewed works

**Careful:** 

- Works best on-campus or via `virtual.anu.edu.au` so that you can access all papers.
- CHI and ACM are centres of HCI research, but there are other non-ACM venues that could be missed.
:::
::: {.column width="40%"}
![Finding sources with ACM Digital Library](img/sources-acm-dl.png)
:::
::::::::::::::

## Citations

In this class, we are going to standardise on numerical citations. When you state something in your text that needs support, you put the citation at the end of the sentence [1].

### References

- [1] Kazuhiro Wada, Masaya Tsunokake, and Shigeki Matsubara. 2025. Citation-Worthy Detection of URL Citations in Scholarly Papers. Proceedings of the 24th ACM/IEEE Joint Conference on Digital Libraries. Association for Computing Machinery, New York, NY, USA, Article 28, 1–5. <https://doi.org/10.1145/3677389.3702570>

### Write the references in Markdown like this:

```
- [1] Kazuhiro Wada, Masaya Tsunokake, and Shigeki Matsubara. 2025. Citation-Worthy Detection of URL Citations in Scholarly Papers. Proceedings of the 24th ACM/IEEE Joint Conference on Digital Libraries. Association for Computing Machinery, New York, NY, USA, Article 28, 1–5. <https://doi.org/10.1145/3677389.3702570>
```

## Metadata vs citation format

:::::::::::::: {.columns}
::: {.column width="50%"}
- metadata for a reference can be used with any citation format
- academics often use special tools for storing reference metadata
- computer scientists tend to use `BibTeX` format
- `BibTeX` is part of the venerable (`La`)[`TeX` ecosystem originally developed by CS luminary Donald Knuth](https://en.wikipedia.org/wiki/TeX) in the late 70s
- in LaTeX you can select citation format (e.g., ACM, IEEE, Chicago, Harvard, APA)
:::
::: {.column width="50%"}
```
@inproceedings{adiwangsa-charades:2025,
author = {Adiwangsa, Michelle and Bransky, Karla and Wood, Erika and Sweetser, Penny},
title = {A Game of ChARades: Using Role-Playing and Mimicry with and without Tangible Objects to Ideate Immersive Augmented Reality Experiences},
year = {2025},
isbn = {9798400714863},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3715668.3736382},
abstract = {Using tangible objects for immersive augmented reality (AR) experiences offers various benefits, such as providing a physical means of interacting with virtual objects and enhancing the functionality of everyday objects. However, designing AR experiences with tangible objects presents unique challenges, particularly due to the diverse physical properties that can influence user interactions. In this provocation, we explore effective approaches for ideating such AR experiences, by designing two exergames intended for AR head-mounted displays (HMDs). We found that role-playing and mimicry, both with and without tangible objects, provide valuable benefits in the design of such experiences. Building on this insight, we introduce ChARades, an iterative and playful gamestorming technique that incorporates role-playing and mimicry in both forms, to ideate immersive AR experiences involving tangible objects.},
booktitle = {Companion Publication of the 2025 ACM Designing Interactive Systems Conference},
pages = {440–445},
numpages = {6}
}
```

The metadata entry for @adiwangsa-charades:2025 which is cited using `[@adiwangsa-charades:2025]` in this Markdown document. In LaTeX you would cite it like this: `\cite{adiwangsa-charades:2025}`.
:::
::::::::::::::

## Big BibTeX files

:::::::::::::: {.columns}
::: {.column width="50%"}
Big reference libraries are part of academic work.

- Charles' "main" `.bib` file has ~1300 entries (started in 2013, first year of Charles' PhD!)
- `references.bib` for [this course](https://github.com/smcclab/thirty-nine-hundred-hci/blob/main/references.bib) has about 100 entries.
- Charles uses [BibDesk](https://bibdesk.sourceforge.io) to manage the big file, but usually just VSCode for smaller bibtex libraries.
- Other popular reference managers are Zotero, Mendeley and Endnote.
- Opinion time: Bibdesk is nice because the database is just a text file.
:::
::: {.column width="50%"}
![References listed in Bibdesk](img/bibdesk.png)
:::
::::::::::::::

## In this class...

:::::::::::::: {.columns}
::: {.column width="60%"}
- Not expecting you to use BibTeX (yet)
- Expecting you to list references in "ACM format".
- ACM format is inspired by APA referencing
    - supports both numerical [1, 2] and author-date (Martin, 2020) referencing.
    - includes _full_ names of authors and publication details for clarity
    - includes DOI as a full URI
- [ACM page](https://www.acm.org/publications/authors/reference-formatting) plain text examples for references to different types of source
- [CSL version](https://github.com/citation-style-language/styles/blob/master/association-for-computing-machinery.csl) (Citation Style Langauge)
- [BST version](https://github.com/borisveytsman/acmart/blob/primary/ACM-Reference-Format.bst) (BibTeX Style)
:::
::: {.column width="40%"}

:::
::::::::::::::

## Rules for this course:

1. all references **must exist!** (!!!)
2. use ACM format
3. use numerical citation (not author date) -- saves words in your word count
4. all references in your list should be cited in text
5. you have actually read references and that they are relevant to your work
6. at least two references should be _scholarly_ (so not a medium article) and _external_ (so not course lecture notes or textbook)
7. expectation: ✨✨_perfection_✨✨

## Who has a question about referencing and finding sources?

🙋🏽‍♀️🤷💁🏻🧠🗣️

Mucking up citations is a risk to lose marks unnecessarily.

Easy to do, but looks really bad to markers.

Let's clear up some questions now if you have them!

_I commit to finding ways to help you do this better!_

# Interface Types

:::::::::::::: {.columns}
::: {.column width="60%"}
How would you describe a computer interface?

> graphical, command, speech, ambient, intelligent, tangible, touch free, natural, etc.

Focus of interface can change:

- **function** e.g., *smart*phones
- **interaction style** used e.g., command, graphical or multimedia
- **input/output device** e.g., pen-based, speech-based, or gesture-based
- **platform** e.g., tablet, mobile, PC, or wearable

<!-- now with ML algorithms that are intended to recognise faces, objects, and the like 🤖! -->
  
:::
::: {.column width="40%"}
![Yichen Wang using a touchless, natural, AR interface, 2021.](img/07_yichen_hololens.jpg){width=60%}
:::
::::::::::::::

## 45 years of interface types!

:::::::::::::: {.columns}
::: {.column width="50%"}
- Command Line
- Graphical
- Multimedia
- Virtual reality
- Web
- Mobile
- Appliance
- Voice
- Pen
- Touch
- Touchless
:::
::: {.column width="50%"}
- Haptic
- Multimodal
- Shareable
- Tangible
- Augmented reality
- Wearables
- Robots and drones
- Brain-computer
- Smart
- Shape-changing
- Holographic
:::
::::::::::::::

## Command Line Interfaces

:::::::::::::: {.columns}
::: {.column width="50%"}

- Type in commands (e.g., `ls`)
- pressing certain combinations of keys (e.g., `Ctrl + V`)
- fixed from the keyboard (e.g., `delete`, `enter`, `esc`) or user-defined
- largely superseded by graphical interfaces such as menus, icons, predictable text commands 
- still useful for complex software (e.g., CAD), scripting batch operations, coding
- _is chatGPT a CLI?_
  
:::
::: {.column width="50%"}
![Charles editing a lecture in neovim (`:w`)](img/charles-neovim.png){width=100%}
:::
::::::::::::::

## Research and Design for CLIs

Back in 1980s, much research investigated command interfaces' optimisation:

- form of the commands such as the use of abbreviations, full names, and familiar names;
- syntax (e.g., how best to combine different commands), and organisation (e.g., how to structure options), are examples of some of the main areas that have been investigated [@scneiderman1992designing].
- Findings showed no universal optimal methods on command naming!

**Design principle**: labeling/naming the commands should be chosen to be as *consistent* as possible!

## Graphical User Interfaces

:::::::::::::: {.columns}
::: {.column width="50%"}

- Information represented within a graphical interface 
- use of color, typography, and imagery [@mullet1996designing]
- interface features abbreviated as WIMP
    - Windows
    <!-- lecture notes for charles -->
    <!-- overcome physical display constraints; enable concurrent task operations. -->
    - Icons
     <!-- objects as part of desktop metaphor; easier to learn and remember. -->
    - Menus
     <!-- support navigation; different styles such as flat lists, drop-down, pop-up, contextual, etc. -->
    - Pointer
  
:::
::: {.column width="50%"}
![Apple's first GUI: Lisa. Source: The Lisa: Apple's Most Influential Failure, Computer History Museum.](img/Lisa-desktop-screen.jpg){width=90%}
:::
::::::::::::::

## Research and Design for GUIs

- window management
    - enabling fluid movement and rapid attention shifts between windows and displays without distraction
    - e.g., keyboard shortcuts and task bars design; auto-fill in online forms
- menu design consideration: decide which terms to use for menu options
- consistent icon libraries for developer: e.g., [fontawesome.com](fontawesome.com) or [thenounproject.com](thenounproject.com)

## Multimedia

:::::::::::::: {.columns}
::: {.column width="50%"}
A single interface combines different media such as graphics, text, video, sound, and links them together with various forms of interactivity. E.g., Wikipedia.

- better information presentation.
- facilitate rapid access to multiple representations of information.

:::
::: {.column width="50%"}
![multimedia learning app for tablets. Source: KidsDiscover “Roman Empire for iPad”](img/multimedia-learning-app-example.png
){width=80%}
:::
::::::::::::::

## Multimedia

- developed for training, educational, and entertainment purposes. 
- To what extent do multimedia interfaces improve learning and play?
- What happens when users have unlimited access to diverse media and simulations?

### Research and Design Considerations

- How to encourage interaction with all aspects?
- provide a diversity of hands-on interactivities and simulations
- employ dynalinking, where changes in one window directly update another [@rogers1996search].
- how to best combine multiple media to support different kinds of tasks?

## Augmented and Virtual Reality

:::::::::::::: {.columns}
::: {.column width="60%"}
Interfaces can sit on a spectrum between fully virtual and fully real interaction [@milgram-mr:1994].

- The big middle area includes "mixed reality" (MR) interfaces
- Augmented reality usually closer to "real" reality.
- eXtended reality (XR) is a more recent term.

Has often seemed like a great idea, but hasn't cracked mainstream yet (or has it??)
:::
::: {.column width="40%"}
![The reality-virtuality continuum](img/reallity-virtuality-continuum.jpg)
:::
::::::::::::::

## Augmented Reality

:::::::::::::: {.columns}
::: {.column width="50%"}
- blending of digital content with the physical world to create an enhanced real-world experience
- 1960s: Ivan Sutherland’s development of the first head-mounted three-dimensional display
:::
::: {.column width="50%"}
![First augmented reality head-mounted display system. Source: [@sutherland1967ar].](img/wk11-ivan-sutherland-headset.jpg){width=80%}
:::
::::::::::::::

## Augmented Reality
:::::::::::::: {.columns}
::: {.column width="60%"}
- AR systems have evolved significantly, particularly displays and interaction models [@speicher2019mixed;@billinghurst-2015-ar-survey]
- displays: see-through, screen-based, projection-based.
- "spatial Computing", another way of thinking about it, defined by @greenwold-2003-spatial-computing
    -  *“human interaction with a machine in which the machine retains and manipulates referents to real objects and spaces."*
-  emphasising not only the augmentation of reality but also the *meaningful* interaction between digital and physical elements.
:::
::: {.column width="40%"}
![AR smartphone game Pokémon Go.](img/pokemon-go.jpg){width=80%}

![AR musical instrument (Yichen Wang, 2022).](img/yichen-cube.jpg){width=80%}
:::
::::::::::::::

## Virtual Reality

:::::::::::::: {.columns}
::: {.column width="60%"}
Emerged in 1970s with computer-generated graphical simulations.

**Goal**: to create user experiences that feel real when interacting with an artificial environment. 

- stereoscopically displayed image.
- interact with objects through input devices such a joystick within the field of vision.
- higher level of fidelity compared to other graphical interfaces, provides immersion.
- different viewpoints: first-person perspective, third-person perspective, etc.

:::
::: {.column width="40%"}
![Avatars for the “We Wait” VR experience [@steed-we-wait:2018] (CC-BY 4.0)](img/vr-example.png){width=80%}
:::
::::::::::::::

## Research and Design for Virtual Reality

:::::::::::::: {.columns}
::: {.column width="60%"}
- learning and training for specific skills.
    - driving, pilot training, surgery, medicine, complex/confronting environments.
    - build up skills with lower costs and low risk.
- navigation for accessibility, treatment (e.g, mental health)
- **entertainment**.
- virtual body to enhance the feeling of presence; reduce cybersickness; support natural user experience; the level of realism to target, etc.
:::
::: {.column width="40%"}
![iFire Networked Visualisation System. [UNSW Center for Interactive Cinema Research, 2025](https://www.unsw.edu.au/research/icinema/our-research/projects/ifire)](img/2024-06-ifire-networked-visualisation-system.png){width="100%"}
:::
::::::::::::::

## Activity: Thinking about AR and VR

🙋🏽‍♀️🤷💁🏻🧠🗣️

Find someone near you, and discuss these questions:

1. Have you ever tried an AR VR system? (phone, headset, audio-only, whatever)
2. What was the experience like? Do you see it as a useful technology?

Chat for 3 minutes and we'll hear a few responses.

## Website Design

:::::::::::::: {.columns}
::: {.column width="60%"}

- early websites were largely text-based, with hyperlinks to different places or pages of text.  
    - *"how best to structure information at the interface level to enable users to navigate and access it easily and quickly?"*
- shift from information usability to aesthetics and visual design.

> Much of the content on a web page is not read. Web designers are “thinking great literature” (or at least “product brochure”), while the viewer's reality is much closer to a “billboard going by at 60 miles an hour” [@krug2014don].
:::
::: {.column width="40%"}
![[Web Design history (source)](https://lionsheaddesigns.com/Web-Design.html)](img/designhistory.jpg){width="50%"}
:::
::::::::::::::

## Website Design

:::::::::::::: {.columns}
::: {.column width="60%"}
- web development involves multiple technologies
- CSS, HTML, JavaScript, node.js, Python, etc.
- breadcrumb navigation (key interface element): "way finding" to navigate without losing track
- design for smartphone or table interaction modality, for smaller-sized displays and for *infinite scrolling*.
- three core questions proposed by Keith Instone: *"Where am I? What's here? Where can I go?"* [@veen2000art]
:::
::: {.column width="40%"}
![Web Development [tools](https://vocal.media/education/web-development-tools)](img/web-dev-pl.png){width="70%"}

![A breadcrumb trail on the Best Buy website showing [three choices made by the user to get to Smart Lights (source)](https://www.bestbuy.ca)](img/bread-crummb.png){width="100%"}
:::
::::::::::::::

## Mobile Device

:::::::::::::: {.columns}
::: {.column width="60%"}
Smartphones, fitness trackers, smartwatches, large-sized tablets on the flight, educational tablets, etc.

- embedded sensors, such as accelerometer for movement detection, thermometer for temperature measurement, bio/fitness sensors.
- new affordances led to novel and creative apps e.g.,
    - [Ocarina](https://ccrma.stanford.edu/~ge/ocarina/) [@wang2014ocarina]
    - contextual information access: scanning QR codes

:::
::: {.column width="40%"}
![Mobile Devices. Source: StockCake.](img/tech-gadget-array-stockcake.jpg){width="80%"}

![Ocarina, Ge Wang. 2014.](img/o2-hands-480.png){width="80%"}
:::
::::::::::::::

## Research and Design: Mobile Interfaces

- careful design of limited screen and control space, including the selection, placement, and software integration of hardware controls.
- ensuring touch targets like buttons and icons are large enough for accurate use by all finger sizes.
- other guidelines exist providing advice on how to design interfaces for mobile devices, e.g., [@babich2018mobileux].


## Appliances

:::::::::::::: {.columns}
::: {.column width="60%"}
- machines for everyday use in the home
- washing machines, microwaves, refrigerators, toasters, bread makers, blenders
- connections to the internet, control by remote apps
- do such designs help?
- @cooper2014face suggest that appliance interfaces require the designer to view them as transient interfaces, where the interaction is short.
- Two fundamental design principles: simplicity and visibility. 
:::
::: {.column width="40%"}
![The Design of Everyday Things. @Norman:2013](img/design-of-everyday-things.jpg){width="50%"}
:::
::::::::::::::

## Voice Interface

:::::::::::::: {.columns}
::: {.column width="60%"}

- lets users interact with apps (e.g., search engines, chatbots, or travel planners) through spoken language
- commonly used to request information (like flight times or weather) or issue commands (e.g., playing music or selecting a movie)
- Voice interfaces rely on command- or conversation-based interaction.
- early speech systems earned a reputation for *mishearing* all too often what a person said (still true?)
:::
::: {.column width="40%"}
![Apple Siri. Source: CHEEZburger Memebase. ](img/why-so-mean-siri.jpg){width="60%"}
:::
::::::::::::::

## Applications for Voice Interfaces

- Dictation (e.g., Otter.io, Dragon), faster than typing, accessibility.
- Call routing: Automate customer service; saves costs; needs human fallback when needed.
- Barge-in feature: Lets users interrupt system prompts to speed up interactions.
- Directed dialogue: System asks specific questions; user gives limited responses.
- Flexible input risks: Users may give too much info; guided prompts help keep input manageable.
- Mobile speech apps: Used for voice search, translation (e.g., Siri, Google Translate); enables real-time multilingual conversations.
- Voice assistants: Amazon's Alexa and Google Home offer interactive skills; promote shared family use and entertainment.
- Current limits: Struggles with kids' speech, group speaker recognition, and requires name activation.

## Research and Design for Voice Interaction

:::::::::::::: {.columns}
::: {.column width="60%"}
What conversational mechanisms to use to structure the voice interface and how human-like they should be?

- natural conversation
- system navigation efficiency 
- synthesised voice or voice actor: male, female, neutral, dialect, and pronunciation 

Pros and cons of dialogue structures, error handling, and etiquette remain key for modern voice interfaces [@cohen2004voice].
:::
::: {.column width="40%"}
![Tea. Earl grey. Hot. --Captain Picard](img/tea-earlgrey-hot.jpg){width="80%"}
:::
::::::::::::::

## Pen-Based

:::::::::::::: {.columns}
::: {.column width="60%"}
- light pens, styluses, or scanners for drawing and writing
- write, draw, select, and move objects on a page or tablet.
- very early use in [CRT displays with lightpen](https://en.wikipedia.org/wiki/Fairlight_CMI)!
- touchscreen versions most common now
- another option: _digital_ paper that scans what you write (IR sensor, special dot pattern on the paper)

_Pens are great!_ We should do more with them.
:::
::: {.column width="40%"}
![Livescribe Echo 2 Smartpen ([source](https://uk.livescribe.com/collections/smartpens/products/echo-2)).](img/pen-based-example.png){width="80%"}
:::
::::::::::::::

## Touchscreens

:::::::::::::: {.columns}
::: {.column width="60%"}
- common in kiosks, ATMs, checkouts, phones, tablets, computers.
- Now weird to find a _non_ touchscreen.
- **Single-touch** respond to single taps.
- **Multitouch** supports multiple simultaneous touches and gestures like pinching, rotating
- **Multitouch devices** (e.g., smartphones, tablets, tabletops) enable intuitive interactions using one or both hands.
- **Finger gestures** enhance how users interact
- _but_ there are limitations. How do you "undo" on an iPhone?
:::
::: {.column width="40%"}
![A schematic of a multitouch interface. Source: Willtron / CC BY 1.0](img/multitouch-interface.png){width="80%"}
:::
::::::::::::::

<!-- 
## Research and Design for Touchscreens

- Touchscreens are widely used with new ways to interact like swiping, carousels, and virtual keyboards.

- These methods can be less precise or slower than traditional keyboards and mice.

- Multitouch gestures allow more control, like zooming and rotating.

- Gestures can be hard to learn and don’t provide physical feedback.

- Visual and audio cues help make up for the lack of tactile feedback. -->

## Touchless

- gestural interaction: moving arms, hands, position to communicate
- track and understand gestures using cameras, sensors and machine learning
- Watch David Rose's inspirations for gesture at [vimeo.com/224522900](https://vimeo.com/224522900)

### Research and Design for Touchless Interfaces

- **Gesture recognition challenge:** Systems must detect when a gesture starts and ends, and distinguish intentional gestures (e.g., pointing) from unconscious movements (e.g., hand waving).
- **Gestures as output:** Gestures can also be visualised, such as through avatars mirroring user movements in real time.
- **3D sensing:** Devices with depth cameras (e.g., smartphones, laptops, smart speakers) can capture and respond to gestures in 3D space.
- *Design consideration*: How realistic the avatar or mirrored representation must be for users to feel it's believable and connected to their own gestures?

## Haptic Interfaces

:::::::::::::: {.columns}
::: {.column width="60%"}
- vibration and forces (via actuators) to provide tactile feedback
- can be embedded in clothing or mobile devices such as smartphones and watches.
- gaming consoles and driving simulators use haptics to enhance realism.
- vibrotactile feedback can simulate remote physical communication, like hugs or squeezes, using actuators in clothing.
- Haptics can also be used for skill training, such as learning musical instruments.
    - *"novice players responded well to vibrotactile cues, adjusting their actions accordingly."*
:::
::: {.column width="40%"}
![The MusicJacket with embedded actuators that nudge the player to move their arm up to be in the correct position. Source: Yvonne Rogers](img/musicjacket.png){width="50%"}
:::
::::::::::::::

## Haptic Interfaces

:::::::::::::: {.columns}
::: {.column width="60%"}
-  Ultrahaptics uses ultrasound to create 3D shapes and textures in midair that can be felt but not seen.
- It simulates touch-based interfaces (e.g., buttons, sliders) that appear in midair.
- In automotive interfaces to replace physical controls with invisible, tactile controls: adjust volume or change radio stations.
- Haptic Exoskeletons: bedded into wearable exoskeletons, inspired by “Techno Trousers” from *Wallace and Gromit* [@rossiter2018past].
    - Graphene parts are used to stiffen or relax the trousers to assist movement.
    - Application in mobility assistance, fitness.
:::
::: {.column width="40%"}
![Trousers with artificial muscles that use a new kind of bubble haptic feedback. Source: The Right Trousers Project](img/right-trousers.png){width="30%"}
:::
::::::::::::::

<!-- ## Research and Design for Haptic Interfaces

- In gaming, smartphones, and wearables for user experience, stimulating touch, strokes, prods, or buzzes.
- Effective in sensory-motor skill training (e.g. sports, musical instruments).
- Vibrations on snowboarders led to faster reaction times than verbal instructions [@spelmezan2009tactile].
- *Design consideration*: actuator placement, type and timing of touch, intensity and frequency of feedback.
- *Continuous feedback is ineffective due to annoyance and habituation!*
- Intermittent buzzes is more effective for grabbing attention.
- Different buzz patterns can signal different events (e.g. light tap = rain, heavy tap = thunder); e.g., Apple iOS 16 added haptic typing. -->

## Multimodal

:::::::::::::: {.columns}
::: {.column width="60%"}

- multiple input/output modalities (e.g., touch, sight, sound, speech) to enhance user interaction [@bouchet2004icare]; 
- natural, flexible, and expressive interactions, similar the real world interaction experience [@oviatt2017handbook].
- Common combinations: speech and gesture; eye-gaze and gesture; haptic and audio, pen input and speech [@dumas2009multimodal].
- Speech + vision processing is the most common [@deng2004challenges]!

E.g., Kinect for Xbox — combined RGB camera, depth sensor, and microphones for real-time gesture and voice recognition.
:::
::: {.column width="40%"}
![Microsoft's Xbox Kinect. Source: Stephen Brashear / Invision for Microsoft / AP Images](img/xbox.png){width="90%"}
:::
::::::::::::::

## Research and Design for Multimodal Interfaces

:::::::::::::: {.columns}
::: {.column width="60%"}
**must** recognise multiple user aspects: handwriting, speech, gestures, eye movements, and body movements.

- more complex to design than single modality systems.
- most researched interaction modes are: speech, gesture, eye-gaze tracking.
- *What are the actual benefits of combining multiple input/output modalities?*
- Is natural human-like interaction (e.g., talk + gesture) effective when applied to computer interaction?

Design guidelines, see [@oviatt2017handbook].

:::
::: {.column width="40%"}
![Multimodal Mixed Reality Experience. Microsoft HoloLens 2. Source: Charles Martin. 2023.](img/hololens-mate.jpg){width="90%"}
:::
::::::::::::::

## Shareable

:::::::::::::: {.columns}
::: {.column width="60%"}

Designed for multi-user interaction, unlike typical single-user devices (PCs, laptops, phones).

multiple simultaneous inputs by co-located groups. E.g., large wall displays (e.g., SmartBoards); interactive tabletops for users to interact using fingertips on a shared surface.

- A large shared space for group collaboration.
- Allow simultaneous interaction, unlike working on a single PC.
- Users can point, touch, and see the same content.
- This creates a shared point of reference, enhancing group coordination and participation (Rogers et al., 2009).
:::
::: {.column width="40%"}
![Collaborative Musical Instrument Reactable [@jorda2010reactable]. (source)[https://www.ycam.jp/en/archive/works/reactable/].](img/reactable.jpg){width="80%"}
:::
::::::::::::::

## Shareable Research Considerations

:::::::::::::: {.columns}
::: {.column width="60%"}

- tabletop systems used in museums and galleries.
- support interactive, group-based learning [@clegg2020community].
- some shareable interfaces are software platforms for remote collaboration.
- Early example: [ShRedit](https://cacm.acm.org/practice/now-that-we-can-write-simultaneously-how-do-we-use-that-to-our-advantage/) (1990s) – supported shared document editing.
- Google Docs, Microsoft Excel, Miro, Canva, etc.

### Research and Design Consideration

from single-device interactions (e.g.,handwriting) to cross-device collaboration; key design issues around display layout, participation, and balancing personal and shared spaces.
:::
::: {.column width="40%"}
![Pompeii Exhibition at National Museum of Australia. Source: <https://www.australiangeographic.com.au/nature-wildlife/natural-disasters/2025/02/pompeii-awakens-in-canberra/>](img/pompeii-nma.jpg){width="80%"}
:::
::::::::::::::


## Tangible

:::::::::::::: {.columns}
::: {.column width="60%"}
Link physical objects (bricks, cubes, clay) with digital representations through embedded sensors [@ishii1997tangible; @fishkin2004taxonomy] 

Manipulating objects triggers digital effects like sounds, animations, or lights, either on the object or in surrounding media (e.g., Tangible Bits [@ishii1997tangible]).

Some use physical models on digital surfaces (tabletops), where moving objects influences digital events (e.g., Urp for urban planning).

Physical artifacts can be lifted, rearranged, and manipulated directly, distinguishing from purely screen-based or mobile interfaces.


:::
::: {.column width="40%"}
![Tangible Bits. [@ishii1997tangible] ](img/tangible-bits.jpg){width="100%"}
:::
::::::::::::::

<!-- ## Tangible

- Common technologies: RFID tags, embedded sensors, digital tabletops that detect object movement.
- Applications include learning, design, play, collaboration (e.g., urban planning tools, Tinkersheets for warehouse logistics).
- Allow multiple users to work together by physically moving and arranging objects in different ways.
- Educational toolkits like SAM Labs, MicroBit, and MagicCubes help children learn STEM by linking physical actions to digital outcomes.
- Tools like Code Jumper make programming accessible for children with visual impairments using tactile, physical code blocks [@morrison2020torino]. -->

## Research and Design for Tangible Interfaces

- Conceptual frameworks e.g., [@shaer2010tangible; @ullmer2005token; @fishkin2004taxonomy] identify what makes tangible interfaces unique.
- A main design challenge is deciding how to link physical actions to digital effects - the notion of *coupling*.
- Designers must choose the types and where digital feedback appears (e.g., on the object, beside it, or elsewhere), based on the interface’s purpose. E.g., learning? entertainment?
- Choosing the right physical artifacts (e.g., cubes, tokens)to support natural and hands-on interaction.
- Simple materials like sticky notes or cardboard tokens can be used to link physical actions to digital responses.
- history and goals of tangible interfaces, see: @ullmer2022weaving

## Wearables

:::::::::::::: {.columns}
::: {.column width="60%"}

- Digital devices worn on the body -- e.g., smartwatches, fitness trackers, smart glasses, and fashion tech.
- Early wearable computing enabled mobile recording and access to digital info.
- Advances in flexible displays, e-textiles, and physical computing (e.g., Arduino) have made wearables more practical and appealing.
- Items like jackets, jewelry, hats, and shoes have been designed to interact with digital info on the go.
- From convenience design focus to expressive and communicative functions.

:::
::: {.column width="40%"}
![LivingLoom [@zhu2025livingloom].](img/living-loom.jpg){width="80%"}
:::
::::::::::::::

<!-- ## Research and Design for Wearables

- Comfort: Must be light, small, hidden, and wearable without discomfort.
- Hygiene: Should be washable; electronics must be removable and batteries easy to manage.
- Control: Touch, voice, or physical controls need to be intuitive.
- Tech Integration: Combines LEDs, sensors, AR, and more for interactive experiences.
- Stigma Reduction: Fashionable designs help normalize assistive wearables.
- Feedback: Data (e.g., heart rate) must be presented in meaningful, actionable ways—visually, haptically, or multimodally. -->

## Robots and Drones

:::::::::::::: {.columns}
::: {.column width="60%"}
Robots assist in manufacturing, hazardous environments, rescue, and remote exploration with remote controls using cameras and sensors.

Domestic robots help with chores and support elderly or disabled people.

Pet robots like Paro provide companionship and reduce loneliness, especially for dementia patients.

Drones, once military and hobbyist tools, now serve in delivery, entertainment, agriculture, construction, and wildlife monitoring, offering real-time data and automated operations.
:::
::: {.column width="40%"}
![(a) Mel, the penguin robot, designed to host activities; (b) Japan's Paro, an interactive seal, designed as a companion, primarily for the elderly and sick children. Source: (a) Mitsubishi Electric Research Labs (b) Parorobots.com.](img/robot-pet.png){width="100%"}
:::
::::::::::::::

<!-- ## Research and Design with Robots and Drones

- Robots: Ethical questions arise around designing robots with human- or animal-like traits. 
- Should they mimic humans emotionally and physically, or clearly appear as machines with functional roles? 
- Many prefer “cute pet” robots for their comforting and less unsettling nature. Interaction design also varies between human-like engagement (talking, gesturing) and traditional controls (buttons, dials).
- Drones: Ethical concerns include privacy violations (spying on people or property without consent) and the use of drones as autonomous lethal weapons. There is ongoing debate about banning killer drones to maintain meaningful human control. -->

## Brain-Computer Interfaces

:::::::::::::: {.columns}
::: {.column width="60%"}

Create a link between brain activity and external devices (e.g., cursor, robot, game controller).

Detect neural signals via electrodes in headsets placed on the scalp.

Assist or augment cognitive and motor functions—especially for people with disabilities (e.g., BrainGate lets paralyzed users type via thought).

...and *entertainment* -- e.g., Brainball, where relaxation controls a ball’s movement.

Aim to transfer mental states (e.g., “focused,” “relaxed”) between people via stimulation.

**Ethical concerns** arise around mind reading and mental state manipulation, especially with companies like Neuralink pursuing direct brain implants.

:::
::: {.column width="40%"}
![Source: Tim Cordell / Cartoon Stock](img/brian-computer-interface.png){width="80%"}
:::
::::::::::::::

<!-- ## Research and Design Brain-Computer Interfaces

- NextMind developed a noninvasive BCI for real-time device control using thoughts.
- Raises ethical concerns about mental privacy: thoughts could become machine-readable and possibly shared without consent.
- Accuracy concern: systems might misinterpret thoughts or intentions.
- Gaming use is playful, but deep mind reading may feel invasive or socially unacceptable.
- For assistive use, a key design challenge is how to arrange on-screen elements (e.g., letters) to ensure easy and accurate selection.
- AI and predictive text can improve communication efficiency for users with severe motor impairments. -->

## Smart Interfaces

- Smart devices (phones, homes, appliances) are context-aware, often AI-powered, and network-connected, learning from user behaviour (e.g., Nest thermostat).
- Aim is to automate tasks, improve efficiency, and reduce human error—often by removing humans from the loop (e.g., smart buildings managing lighting/heating).
- over-automation can frustrate users, limiting control (e.g., sealed windows, restricted manual overrides).

<!-- ### Research & Design Considerations

- Human–Building Interaction (*new idea*) focuses on user experience in smart environments, prioritising human needs, values, and goals [@alavi2019introduction].
- Designers must decide whether smart tech should amplify human actions or act autonomously [@landay2019smartinterfaces]. -->

## Shape Changing Interfaces

:::::::::::::: {.columns}
::: {.column width="60%"}
- Use physical form changes as input/output (e.g., 3D bar charts moving rods to show data) [@alexander2018grand].
- Enable tactile interaction beyond screens
- Make data more relatable by embedding it in everyday contexts

### Research and Design Consideration

- Do they improve data understanding and engagement?
- Are they better than 2D/3D digital charts for health monitoring?
- Size of rod grids; number of cubes for easy learning and recognition.
:::
::: {.column width="40%"}
![inFORM: A shape-changing interface that uses a series of motor-controlled pins to render digital content in the form of 3D rods; developed by MIT Media Group. Source: <http://trackr-media.tangiblemedia.org/publishedmedia/Projects/2013-inFORM/inFORM%20Collection/4676>](img/inform-mit.png){width="80%"}
:::
::::::::::::::

## Holographic Interfaces

:::::::::::::: {.columns}
::: {.column width="60%"}

- Create the illusion of a 3D person being present through taking advantage of the human perceptual system. 
- The projection and display technology have achieved some convincing results (e.g., ABBA Voyage in London). 

### Research and Design Consideration

-  A lot research conducted in the tech industry exploringhow to represent people in virtual spaces in ways that feel natural, comfortable, engaging, and not creepy.
- Design considerations include hologram size and how users can interact and communicate with projections in their space.

:::
::: {.column width="40%"}
![ABBA Voyage holographic show. 2022. Source: The Guardian.](img/abba-voyage.jpg){width="100%"}
:::
::::::::::::::

## Activity: Choosing an Interface

:::::::::::::: {.columns}
::: {.column width="60%"}
🙋🏽‍♀️🤷💁🏻🧠🗣️

Imagine you are developing a new interface for the classic game "connect four" 

1. what interface what would you choose?
2. how do you think it would evaluate in terms of usability and user experience?

_Chat for 3 minutes with someone next to you then let's hear some ideas._
:::
::: {.column width="40%"}
![The classic game, COnnect Four. [By Jonathan Kellenberg, Flickr, CC BY 2.0](https://commons.wikimedia.org/w/index.php?curid=521287)](img/connect-four.jpg)
:::
::::::::::::::

# Coda

What makes these interfaces good or bad?

How would you choose what interface to use?

## Natural User Interfaces and Beyond

:::::::::::::: {.columns}
::: {.column width="60%"}
A natural user interface (NUI) is designed to allow people to interact with a computer in the same way that they interact with the physical world—using their voice, hands, and bodies.

- but how natural are NUIs?

Don Norman [@Norman:2013] argues "natural" depends on a number of factors:

 - how much learning is required, 
 - the complexity of the app or device's interface, 
 - and whether accuracy and speed are needed. 

A gesture may worth a thousand words; other times a word is worth a thousand gestures. It depends on how many functions the system supports.
:::
::: {.column width="40%"}
![PhD student Sandy Ma drawing-based musical performance in AR environment. 2024.](img/07_sandy_ai_friends.jpg){width="100%"}
:::
::::::::::::::

## Which Interface?

- is multimedia better than tangible interfaces for learning? 
- Is voice effective as a command-based interface? 
- Is a multimodal interface more effective than a single media interface? 
- Are wearable interfaces better than mobile interfaces for helping people find information in foreign cities?
-  How does VR differ from AR, and which is the ultimate interface for playing games?  etc.

It depends! 

...the interplay of a number of factors, including type of task, the people using the system, context, reliability, social acceptability, privacy, ethical, and location concerns.


<!-- boilerplate ending -->


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
