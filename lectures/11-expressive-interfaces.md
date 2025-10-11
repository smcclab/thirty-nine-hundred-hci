---
title: Expressive Interfaces
author: Dr Charles Martin
title-slide-attributes:
    data-background-image: img/2024-intelligent-microfreak.jpg
    data-background-size: cover
---

## Announcements

- Gitlab Template now available for final project
- Finalised the marking rubric for final project

## Plan for the class

## Lecture Ideation

- Go through ["Composing Interactions" by Marije Baalman](https://composinginteractions.art/#contents)?
- Relate to ANU/UiO Research on Expressive Interaction
- CHI resources on expression and creative interaction
- Creativity and Cognition
- NIME etc.

# Conceptualising Expressive Interactions

> on art, sound and technology that innovates scientific research.

<!-- A historic example: Charles yaps on creative/expressive interaction at the heart of technology advancement.  -->

:::::::::::::: {.columns}
::: {.column width="50%"}
![First head-mounted AR display system[@surtherland1967ar].](img/wk11-ivan-sutherland-headset.jpg){width="70%"}
:::
::: {.column width="50%"}
![Virtual Reality in 1987 - The Sound of One Hand performance by Jaron Lanier[@lanier1993sound]](img/wk11-jaron-lanier-virtual-hand.jpg){width="100%"}

:::
::::::::::::::

## Conceptualising Expressive Interactions

:::::::::::::: {.columns}
::: {.column width="60%"}
- Much of questions concern with the mapping of performed gesture and resulting feedback. 

- Gestures:
    - The use of motions by the limbs or body as a means of expression.
    - Can be unintentional; ancillary gestures.
    - From non-human actors(e.g.,the movement of a leave on a branch of a tree.)
    - *"any sort of motion, that may be understood as an expression of something"* 
:::
::: {.column width="40%"}
![Composing Interactions by Marije Baalman[@baalman2022composing].](img/wk11-composing-interactions.jpg){width="80%"}
:::
::::::::::::::

## Conceptualising Expressive Interactions

:::::::::::::: {.columns}
::: {.column width="60%"}
The mapping from gestures to output media.

> Considering a performer performing making gestures on a stage, which gestures effect changes in the output medium of sound, which can be heard by the performer and audience in the real, physical environment.
:::
::: {.column width="40%"}
![The connection between a gesture in the environment to output media[@baalman2022composing].](img/mapping.jpg){width="80%"}
:::
::::::::::::::

## Conceptualising Expressive Interactions

:::::::::::::: {.columns}
::: {.column width="60%"}

Steps in mapping:

- A gesture is performed in the environment;
- This is captured by a sensor that translates the gesture is processed by an electronic circuit, often to digitalise it;
- Next, the signal enters some sort of computational model that translates the data to parameters;
- These parameters control an output medium such as sound, light, video, or mechatronics.

> how is output from one connected to input, what happens in each step?

Charles discusses how this process relates to expressive interaction.
:::
::: {.column width="40%"}
![Steps in the mapping process[@baalman2022composing]](img/step-in-mapping.jpg){width="90%"}
:::
::::::::::::::

# Drawing Interaction

Surface Drawing system[@schkolne2001organicshape]

- Drawing (hands), moving, scaling, erasing (a pair of kitchen tongs).

:::::::::::::: {.columns}
::: {.column width="40%"}
![Hands define a stroke.](img/organicshapes-hands-interaction.jpg){width="40%"}

![Kitchen tongs move a drawing.](img/organicsahpes-tong.jpg){width="40%"}
:::
::: {.column width="60%"}
![A variety of shapes created with Surface Drawing[@schkolne2001organicshape].](img/3d-organicshapes.jpg){width="40%"}
:::
::::::::::::::

# Drawing Interaction

- [AirPens: Musical Doodling](
 https://nime2025.org/proceedings/166.html) [To Charles: this is installation, not bibtex. I know you may not like this example.]
    - Make music with mark-making.
    - Use IMU sensors to convert movement into sound; explore different mappings between movement and sound.

# Music Interaction

The [New Interface for Musical Expression (NIME)](https://nime.org) research community.

<!-- references -->
- Research into musical instrument design that explores how technological innovation can enable new musical expression, enhance performer control and intimacy, and shape the musician–instrument relationship
- Digital instruments: digital piano, drum pad.
- Augmented instruments: magnetic resonator piano (grand piano -> string instruments).
- Novel instrument: lady's glove, magnetic AI instrument *thales*, percussive instrument [PhaseRings](https://charlesmartin.au/projects/phaserings/), AR instrument *cube*.

# Music Interaction

Guitar Gestures (sound is defined).

# Music Interaction

cube (none mapping).

# Music Interaction

the mapping framework - expressivity and design constraints.

# Dance Interaction

From gestures to body (embodied) movements.

CO/DA System[@coda2022chi]:

![](img/coda-system.jpg){width="80%"}

- Support real-time manipulation of continuous streams of the dancers’ motion data for interactive sound synthesis.
- Enable novel dance improvisations through live coding.
- Live coding: interactively programming musical or visual processes as performance.


# Dance Interaction

<!-- Novelty in terms of expressivity. -->
![](img/coda-process.jpg){width="60%"}

- Movements are measured using motion sensors, and the live coder processes motion signals to generate feedback in real-time.
- Enables a multitude of feedback loops: sound feedback -> movement improvisation -> the coder alters the relationships between movement and sound.
- Dynamic improvisation that stimulates novel movements' exploration.


# Installed Interactions

:::::::::::::: {.columns}
::: {.column width="60%"}

[Dinosaur Choir: Adult Corythosaurus](https://nime2025.org/assets/preprints/nime2025_music_preprint_270.pdf)

- Singing dinosaur skull musical instruments.
- Aim to realise dinosaur vocalisation:  inspired by recent research to base dinosaur vocal anatomy on the bird syrinx, despite dinosaur vocal organs are still an actively debated question in paleontology.
- Use microphone to capture the voice by users, feeding into a computational vocal model and resonating the sound through a 3D printed replica of the dinosaur’s nasal cavities and skull.
- Change the pitch and timbre of the vocalisation by changing the shape of the mouths, like trumpet player. 
:::
::: {.column width="40%"}
![Dinosaur Choir in action.](img/dinosaur-choir.jpg){width="100%"}
:::
::::::::::::::

# Playful Interaction

:::::::::::::: {.columns}
::: {.column width="60%"}
> Have you imagined a breath-controlled amusement rides?

- Inspired by robotic technologies for control of individual seats on rollercoasters and other thrill rides.

- How about using breath instead?

- Enhanced bucking bronco ride that balances realism for breadth control and practicability in cost, tourability and safety.

:::
::: {.column width="40%"}
![Falling off the Broncomatic[@marshall2011chi]](img/breath-controlled-rides.jpg){width="60%"}
:::
::::::::::::::

# Playful Interaction

:::::::::::::: {.columns}
::: {.column width="60%"}

- A straightforward mapping: the rider’s breathing to the horizontal rotation of the ride.
    - Inhale: spins clockwise; exhale: spins anti-clockwise.
    - Breathing speed controls rotation speed: fast breathing faster spin; holding breath stops spinning.
    - Difficulty levels.
- The program is a game in which the player scores more points the more that they breathe: a physical challenge vs reward dynamic.
    - More breathing for faster ride but harder to stay on. To score high, you must breathe more, but this makes the ride tougher.
- *Blast theory if Charles you want to talk about it.*

:::
::: {.column width="40%"}
![Falling off the Broncomatic[@marshall2011chi]](img/broncomatic-system-design.jpg){width="70%"}
:::
::::::::::::::

# Human-AI Creative Interaction

- co-creative drawing.
- holographic / socially
- 

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
