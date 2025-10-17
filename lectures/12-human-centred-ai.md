---
title: Human-Centred AI
author: Dr Charles Martin
title-slide-attributes:
    data-background-image: img/turing-machine-1950.jpg
    data-background-size: cover
---

## Announcements

## Plan for the class

## Lecture Ideation

Go through: Shneiderman, Ben. Human-Centered AI, Oxford University Press, Incorporated, 2022. ProQuest Ebook Central, <https://ebookcentral.proquest.com/lib/anu/detail.action?docID=6838500>.

# Course Wrap-up

What was this course about again?

:::::::::::::: {.columns}
::: {.column width="50%"}
![from this...](img/blog-hintz-eric-2018-12-10-chord-keyset-mouse.jpg){width=100%}
:::
::: {.column width="50%"}
![to this...](img/hci-in-2022.jpg)
:::
::::::::::::::

## core concepts, design, and evaluation

![A map of concepts in our HCI course with loose-ish connections.](img/hci-concept-map.png)

## stakeholders and perspectives

|  | designer | programmer | business manager | researcher |
|---|---|---|---|---|
| **concepts and knowledge** | "what concepts are the basis for my decisions?" | "which parts of software are exposed to user?" | "what heuristics will ensure success?" | "can established knowledge be challenged?" |
| **designing interactions** | "what processes should I follow?" | "how will requirements be established?" | "how can I iterate or pivot to success?" | "how can I find solutions to my research problem?" |
| **evaluating interactions** | "how do I know the user's needs?" | "how can I test user success and experience?" | "what signals tell me if users will buy?" | "how to balance detailed and valid knowledge?" |

Researcher has a hard job here... needs to be a designer, programmer, and business manager where the market is intellectual as well as financial.

## HCI history: The "wave" theory

- First wave: Human Factors in Computing (1980-1992) [@chignell-evolution-hci:2023]
  - Optimising/measuring efficiency, cognitive psychology approach, studying individual users. Lab setting.
- Second wave: Cognitive revolution — mind and computer coupled (1992-2006)
  - Optimise interactions, hypothesis testing, affordances, activity theory, user-centred design. Work environments.
- Third wave: Situated perspectives [@boedker-third-wave:2015] (2006-)
  - Consumer tech, participation and sharing, pervasive computing, AR, tangible interaction, home environments,
- Fourth wave: Entanglement HCI [@frauenberger-entanglement-hci:2019] (2019-)
  - Computer and humans entangled in society: focus on values, accessibility, diversity, policy, law, ethics, individuals’ and society’s responsibilities

## Usability Goals (Interaction Design, Beyond HCI)

:::::::::::::: {.columns}
::: {.column width="50%"}
- Effective to use (effectiveness)
- Efficient to use (efficiency)
- Safe to use (safety)
- Having good utility (utility)
- Easy to learn (learnability)
- Easy to remember how to use (memorability)

This version from: [@rogers-beyond-hci:2023]
:::
::: {.column width="40%"}
![@Raffaele:2016, illustrating @rogers-beyond-hci:2023](img/01_01_usability_8.png){width=100%}
:::
::::::::::::::

## Design Stages

:::::::::::::: {.columns}
::: {.column width="40%"}
1. _Discover_: understand the problem and the people affected
2. _Define_: define the problem clearly so that it can be addressed
3. _Develop_: create ideas, prototypes, sketches, etc, that might address the problem
4. _Deliver_: test potential solutions to find promising directions, and iterate
:::
::: {.column width="60%"}
![The double diamond model of design [adapted from @double-diamond-model]](img/hci-design-double-diamond.png){width=100%}
:::
::::::::::::::

## What is a sketch?

:::::::::::::: {.columns}
::: {.column width="60%"}
- quick
- timely
- inexpensive
- disposable
- plentiful
- clear vocabulary
- distinct gesture
- minimal detail
- appropriate degree of refinement
- suggest and explore rather than confirm

(@buxton-sketching:2007, p.111-113)
:::
::: {.column width="40%"}
![Sketching a stage in 2010](img/sketch-2010.jpg){width=80%}
:::
::::::::::::::

## What is a prototype

:::::::::::::: {.columns}
::: {.column width="60%"}
- _"primitive form"_
- the form that comes before... something.
- in this context: 
  - a _testable_ form
  - a form we can _experience_
- enables evaluation and iteration
- _primitive_: should be somehow rough or limited
:::
::: {.column width="40%"}
![A prototype AI musical instrument.](img/impsy-micro.jpg)
:::
::::::::::::::

## Data Gathering: Interviews and Questionnaires

:::::::::::::: {.columns}
::: {.column width="60%"}

- **Interview techniques:** structured, semi-structured, open
- **Questionnaires:** closed, open, rating scale questions
- **Established questionnaires:** Software Usability Survey (SUS), NASA Task Load Index (TLX), Creativity Support Index (CSI)
- **DIY questionnaires** can be tricky to do well!
- All useful, but need to be justified
- Require different types of analysis, both can involve quantitative and qualitative.

:::
::: {.column width="40%"}
![Photo by Nguyen Dang Hoang Nhu on Unsplash](img/nguyen-dang-hoang-nhu-qDgTQOYk6B8-unsplash.jpg)
:::
::::::::::::::

## Basic Quantitative Analysis

:::::::::::::: {.columns}
::: {.column width="60%"}

- **descriptive statistics**
    - minimum, maximum
    - lower and upper quartile
    - median and mean
    - number of data points (count)
- **plot distribution**
    - **scatter plot:** see all the data! good for checking outliers and comparing aspects of data
    - **boxplot:** useful to compare distributions clearly **charles approved plot!**

These approaches may be enough to make clear research findings!
:::
::: {.column width="40%"}
| stat  | interactive activities |
|-------|------------------------|
| min   | 1                      |
| 25%   | 2                      |
| 50%   | 3                      |
| 75%   | 4                      |
| max   | 5                      |

![Box plots of the data](img/fake_data_boxplot.png){width=70%}
:::
::::::::::::::

## Basic Qualitative Analysis: Thematic Analysis

:::::::::::::: {.columns}
::: {.column width="60%"}
Lots of qualitative techniques but our focus is (Reflexive) Thematic Analysis (RTA) [@braun-thematic-analysis:2022], a well-known and accessible methodology.
 
1. familiarise with the data
2. coding (short labels, multiple rounds)
3. generating initial themes (higher level than codes)
4. developing, reviewing, and refining themes

Your themes become the findings of your qualitative analysis.
:::
::: {.column width="40%"}
![A Miro board from [Yichen Wang](https://yichenwangs.github.io)'s thematic analysis (2025)](img/reflexive-thematic-analysis-yichen-wang-miro-2025.png)
:::
::::::::::::::

## Thin vs thick themes

:::::::::::::: {.columns}
::: {.column width="60%"}
There are different types of themes, and a common distinction:

- Themes that categorise groups of codes: bucket themes, semantic themes, _thin_ themes
- Themes that interpret the codes, revealing hidden information: latent themes, _thick_ themes

Charles (2025; i.e., these slides!) suggests that **4** is a key heuristic for assessing theme thickness. (Disclaimer: may be revised in future!)

:::
::: {.column width="40%"}
Number of words heuristic:

> If your theme is <4 words, it _might_ be a bit thin.

Number of themes heuristic:

> If you are proposing >4 themes, they _might_ be a bit thin.

Source: Charles, 2025. 😬
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

## Cognitive, Social, Emotional Interaction

:::::::::::::: {.columns}
::: {.column width="50%"}
Cognitive Processes [@eysenck-brysbaert:2023]:

1. Attention
2. Perception
3. Memory
4. Learning
5. Reading, speaking, listening
6. Problem solving, planning, reasoning, decision making

:::
::: {.column width="50%"}
Social and Emotional aspects

- conversation (face-to-face vs remote)
- co-presence
- Emotions and behaviour relate
- Models of emotional design
- Affective Computing and Emotional AI
- Persuasive Technologies
- Anthropomorphism
:::
::::::::::::::

## Developing an evaluation plan

:::::::::::::: {.columns}
::: {.column width="60%"}
- Evaluation Goal/Aims
- Participants
- Setting
- Data to collect
- Methods
- Ethical Considerations and Consent
- Data capture, recording, storage
- Analysis method
- Output(s) of evaluation process
:::
::: {.column width="40%"}
![How to evaluate this app?](img/2018-microjam.jpg)
:::
::::::::::::::

## Statistical Analysis and Signficance Testing?

:::::::::::::: {.columns}
::: {.column width="50%"}
- going beyond descriptive statistics...
- **significance testing:** quantifying differences in mean
    - $t$-tests: for comparing two means
    - ANOVA: for comparing 3+ means, incl. repeated measures
    - non-parametric alternatives: Mann-Whitney $U$, Wilcoxon signed ranks
    - $\chi^2$ test: comparing categorical data
- correlation analysis
- regression
:::
::: {.column width="50%"}
One-way ANOVA:

```python
from scipy.stats import f_oneway
import statsmodels.api as sm
from statsmodels.formula.api import ols

# group by 'independent' column and compare dependent column
groups = [group['dependent'].values for _, group in df.groupby('independent')]
f_stat, p_value = f_oneway(*groups)

# create a Model from a formula and dataframe and run anova on that
model = ols('dependent ~ C(independent)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
```

Factorial ANOVA:

```python
# factorial anova: example effects of two independent variables and their interaction
# model: tempo ~ key + mode + key:mode
model = ols('dep ~ C(ind_1) + C(ind_2) + C(ind_1):C(ind_2)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
```
:::
::::::::::::::

## What is an expressive interaction?

:::::::::::::: {.columns}
::: {.column width="60%"}

Mapping sensed **gestures** to an expressive output that is fed back to the user.

- **gestures:** the use of motions by the limbs or body as a means of expression
- can be unintentional, control, or ancillary gestures
- from non-human actors (e.g.,the movement of a leaves on a branch of a tree)
- *"any sort of motion, that may be understood as an expression of something"*

The interaction itself is expressive, and the output is an expression as well. We consult Composing Interactions [@baalman2022composing] as a resource.
:::
::: {.column width="40%"}
![Sensing movement and touch to create music, Atau Tanaka performing in 2010 [@tanaka-mapping-out-instruments:2010] ](img/virtuoso-atau2010.jpg)
:::
::::::::::::::


# What is HCAI?

# HCAI frameworks

# Design Metaphor

<!-- INTRO / Overview -->
- Reflect on both science and innovation goals.
- Four pairs of design metaphors.
- Balance between automation and human control for reliability.

<!-- Notes for Charles -->
 <!-- key is to combine designs that take an automated approach for tasks that can be carried out reliably, and a user-controlled approach for tasks that users want to manage.
 <!--  -->

## History on Artificial Intelligence:  
<!-- can machines think? -->
<!--  a picture of turing test -->
- Charles briefly explains turing test.
- Computers to do what humans do, matching or exceeding human perceptual cognitive, and motor abilities. 
- Pattern recognition such as images, speech, MLP; robotics; emotion recognition; and games (e.g., Alpha Go).
- Statistical approach: GANs, CNN, RNN, and IRL. <!-- inverse reinforcement learning  -->
- Criticisms: brute-force computation; less successful knowledge-based expert systems over engineered rule-based systems; DL approaches.
- **AI is in its early days.**
- **Make AI products with more transparency and human control over the algorithms.**

## Science and Innovation Goals

:::::::::::::: {.columns}
::: {.column width="40%"}
- Understand human perceptual, cognitive, and motor abilities so as to build computers that perform tasks as well as or better than humans. 
    - social robots, common-sense reasoning, affective computers, machine consciousness, and artificial general intelligence (AGI).
- Develop widely-used products and services by applying HCAI methods.
    - supertools, telebots, etc.
<!-- Notes for Charles -->
<!-- Maybe you can discuss these two goals' differences.  More see Printed page 11 in green highlights.-->

:::
::: {.column width="60%"}
![Two Grand Goals of AI Research](img/hcai-two-goals.jpg){width="100%"}
:::
::::::::::::::

## Science and Innovation Goals

:::::::::::::: {.columns}
::: {.column width="60%"}
Autonomous social robots

- Science goals: a general purpose robot elders, parcel delivery, etc.
- Innovation goals: tune solution for each context of use.
<!-- Notes for Charles -->
<!-- More see Printed page 11 in yellow highlights; just think it's good to discuss an example.-->

Online meeting services

- Science: devices / software support collaboration.
- Innovation: Microsoft Teams, Zoom, Google meet.
:::
::: {.column width="40%"}
![Pepper: The world's first social humanoid robot able to recognize faces and human emotions. [Source](https://aldebaran.com/en/pepper/).](img/pepper-photo.jpg){width="50%"}
:::
::::::::::::::

## Intelligent Agents and Supertools
Early Perceptions of Computers

- 1940s–1950s: Computers were labeled "awesome thinking machines" and "electronic brains".
- Dianne Martin: Argues that such myths slowed workplace acceptance and created unrealistic expectations[@martin1933myth].
- Alan Turing (1950):
    - Introduced "Can Machines Think?" [@turing1950computing].
    - Proposed the Turing Test (aka the imitation game).
    - Envisioned machines competing with humans in intellectual fields.
- Debate: a deceptive metaphor rather than a meaningful test[@natale2021deceitful].

## Intelligent Agents and Supertools
Human–Computer Symbiosis (1960)[@licklider1960man]

- Computers and humans as collaborative partners.
- Humans make decisions; computers handle routine tasks.

AI Language & Metaphors

- Terms like smart, intelligent, thinking have influenced public perception.
- AI described using neuroscience metaphors (e.g., neural networks).
- IBM Watson: Marketed under "cognitive computing", later shifted to "augmented intelligence" for clarity.
- Google PAIR: Focus on People and AI Research, emphasising human-centered design.

## Intelligent Agents and Supertools
:::::::::::::: {.columns}
::: {.column width="60%"}
Media & Popular Culture Influences

- Journalists & magazines (e.g., Newsweek, Time) popularised ideas of thinking machines and robots replacing jobs.
- Graphic art & Hollywood films (e.g., 2001: A Space Odyssey, The Terminator, Her, Ex Machina) reinforced human-like AI images.

Human-Centered Perspectives

- Portrayed as independent actors or agents that (“who”).
- Warn again terms such as know, read, explain, but to **empower**, not replace humans[@rusdaniela2020].

:::
::: {.column width="40%"}
![HAL 9000 in movie "2001: A Space Odyssey." [Source](https://www.indiewire.com/features/general/douglas-rain-dead-hal-9000-2001-a-space-odyssey-stanley-kubrick-cast-1202019828/)](img/hal-9000.jpg){width="100%"}
:::
::::::::::::::

## Intelligent Agents and Supertools
Human–AI Design Debate: automation vs direct user control [ref]
<!-- - Shneiderman: Emphasised user control via direct manipulation (buttons, sliders, etc.).
- Maes: Advocated for proactive software agents that anticipate user needs. -->

Industry Design Guidelines on user control, flexibility, accessibility.
<!-- Guidelines from Apple, IBM, Microsoft: -->
<!-- User Control: “People—not apps—are in control.”
Flexibility: Users need fine-grained control.
Accessibility success story: A blind woman using a laptop to do professional work on a flight. -->

AI in Conferences & Applications:

- Science Goal (AI researchers): Automated performance (e.g., self-driving cars, reading x-rays).
- Innovation Goal (HCAI researchers): Promote human-supervised tools (e.g., SIGCHI, UXPA, Augmented Humans conferences) such as digital cameras.

> Combine intelligent agents with human-controlled tools to ensure trust, usability, and control


## Teammates and Tele-bots

## Assured Autonomy and Control Centers

## Social Robots and Active Appliances

<!-- KEY TAKEAWAY -->



# Governing Structure

# Hwo do we (NIMEy/Creative Computing) approach HCAI?



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
