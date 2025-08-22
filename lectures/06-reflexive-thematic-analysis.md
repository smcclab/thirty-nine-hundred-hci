---
title: Reflexivity and Thematic Analysis
author: Dr Charles Martin
---

## Announcements

assignment 2 published [on Canvas](https://canvas.anu.edu.au/courses/2781/assignments/11550):

> Your challenge is choose **one existing AI-integrated interactive computer system or interface** and run a user research study with 3--5 participants. 
> You will formulate a research question, collect and analyse data, and present research findings. Your study should involve at least one form of quantitative and one form of qualitative data and analysis.

You need to:

- apply quantitative and qualitative data analysis
- research **other students** in this class (do not research folks outside the class please)
- participant matching part of labs

## Plan for the class

- Analytical frameworks (qualitative analysis)
- Interpreting and presenting findings
- Deep dive on _Reflexive Thematic Analysis_ (needed for the assignment)
- Reflexivity

# Analytical Frameworks

:::::::::::::: {.columns}
::: {.column width="60%"}
- different approaches can guide qualitative analysis 
- **granularity:** from fine-grained detailed analysis to broader scope examinations
- conversation analysis: fine granularity, examines detailed interactions in short conversation fragments
- systems-based frameworks: coarse granularity, broad group or organisation level analysis
- useful depending on the research goals
:::
::: {.column width="40%"}
![A framework. May not be analytical. (Photo by Maël GRAMAIN on Unsplash)](img/mael-gramain-TyRcLajqJJ4-unsplash.jpg)
:::
::::::::::::::

## Conversation Analysis (CA)

:::::::::::::: {.columns}
::: {.column width="60%"}
- **CA:** examines the semantics of conversations, e.g., turn-taking and interaction
- e.g., compare conversations in different settings
- markup with syntax to capture detailed interactions and speech patterns
- **Square brackets [ ]** indicate overlapping talk between speakers
- **Round brackets ( )** show pauses in conversation with timing details (e.g., (1.1) = 1.1 second pause)
- **Physical spacing** represents temporal sequencing to show exactly when things are said in relation to each other
- aims to reveal subtle cues and conversational mechanisms that might otherwise be missed
:::
::: {.column width="40%"}
```
01  SUS i'd like to play beat the intro in a minute
02  LIA   [ oh no: ]
03  SUS [ alexa ][ (1.1)  ] beat the in[tro
04  CAR      [ °yeah°; ]
05  LIA                 [°no:::…°
06  CAR (0.6) it' mother's day? (0.4)
07  SUS it's (   ) yep (.) listen (.) you need to keep
08    on eating your orange stuff (.) liam
09    (0.7)
10  CAR and your green stuff
11  SUS alexa (1.3) alexa (0.5)=
12  CAR             =°and your brown stuff
13  SUS play beat the intro
```

Conversation with family members and Amazon Alexa with markup from [@porcheron-voice-interfaces:2018]
:::
::::::::::::::

## Discourse Analysis

- Analysing dialogue: what is said, how words convey meaning
- Interpreting context, psychological and social aspects of words.
- Language as social reality, open to interpretation
- [**Constructivist approach:**](https://www.open.edu/openlearn/health-sports-psychology/critically-exploring-psychology/content-section-3.1) Language as a constructive tool: analyse the process of world construction
- Identify subtle and implicit meaning between sources

## Content Analysis

:::::::::::::: {.columns}
::: {.column width="60%"}
- Classifies data into categories and studying frequency of occurrences
- Applicable to diverse media formats including text, video, images, etc
- can involve predefined frameworks or classification systems to systematically examine content across specified dimensions
- can be combined with other analytical techniques such as sentiment analysis
:::
::: {.column width="40%"}
![Analysing some content (Photo by Kaleidico on Unsplash)](img/kaleidico-3V8xo5Gbusk-unsplash.jpg)
:::
::::::::::::::


## Interaction Analysis [@jordan-interaction-analysis:1995]

- investigate human interactions with each other, artifacts, and technologies using video recordings of naturally occurring activities 
- can be teamwork: researchers watch videos together, discuss in real-time 
- coding and annotation through repeated video playing
- hypotheses based on observable participant actions and behaviors
- find patterns inductively by assembling instances of salient events

## Grounded Theory

Grounded Theory (GT) is an _old and important_ qualitative analysis technique [@glaser-strauss-grounded-theory:1967; @corbin-strauss-grounded-theory:2014]

- main idea: identify _categories_ (a kind of theme) through iterative data collection and analysis.
- any kind of data but often ethnographic and interview data
- analysis procedure:
    - _open coding_: categories, properties and dimensions discovered inn data
    - _axial coding_: systematically establishing categories/sub-categories
    - _selective coding_: refine and integrating categories

- _heavier and less flexible in comparison to Reflexive Thematic Analysis_ (not suggested for first-timers)
- @rogers-beyond-hci:2023 claim that GT "uses reflexive thematic analysis", which I guess is accurate.

## Grounded Theory Example: Idle Games

:::::::::::::: {.columns}
::: {.column width="50%"}
![Figure 9.9 @rogers-beyond-hci:2023](img/grounded-theory-example-1.png)

GT process for @alharthi-idle-games:2018
:::
::: {.column width="50%"}
![Figure 9.11 @rogers-beyond-hci:2023](img/grounded-theory-example-2.png)

Codes and categories.
:::
::::::::::::::

## Systems-Based Frameworks

:::::::::::::: {.columns}
::: {.column width="60%"}
- large projects involve many sources of data and stakeholders
- e.g., hospital, corporation, local council, airport, (or university...)
- need ways to understand how the system works together
- manage complex interdependencies
- common theme of management speak: "systems thinking"
:::
::: {.column width="40%"}
![Some kind of system... to be analysed. (Photo by GuerrillaBuzz on Unsplash)](img/guerrillabuzz-7hA2wqBcSF8-unsplash.jpg)
:::
::::::::::::::

## Socio-technical Systems Theory (STS)

- **STS:** technology and people in a work system are interdependent [@klein-sociotechnical:2014]
- treat the whole system as a whole, applied in complex work places.
- More of a philosophy than a methodology, a holistic perspective to address challenges.

### Notable aspects:

1. Task interdependence
2. Socio-technical systems are "open systems": influenced by environmental factors
3. Heterogeneity of system components: subsystems have different technical components
4. Practical contributions: analysing systems, evaluating changes, designing co-optimised systems
5. Fragmentation of design processes


## Distributed Cognition of Teamwork (DiCoT)

- Distributed cognition unpacks how multiple people and technologies interact complete tasks and solve problems.
- DiCoT framework supports this concept with models:
    - **information flow model**
    - **physical model**
    - **artifact model**
    - **social structure model**
    - **system evolution model**
- models have underlying principles, e.g., for physical model:
    - **horizon of observation:** What an individual can see or hear.
    - **perceptual:** How spatial representations aid computation.
    - **arrangement of equipment:** How the physical arrangement of the environment affects access to information.
- may be particularly useful in collaboration contexts, e.g., software development, medicine

## Which Analytical Framework to Use? 

| framework | data | focus | outcomes | granularity |
|---|---|---|---|---|
| conversation analysis | spoken conversation recordings | process of conversations  | how conversations are processed and progress | words or smaller |
| discourse analysis | speech or writing | how words convey meaning | implicit or hidden meanings in text | word, phrase |
| content analysis | written text, video, audio, images | how often something is featured or is spoken about | frequency of items in text | words to artefacts or people |
| interaction analysis | video of activities | interactions between people and artefacts | how knowledge and action are used in an activity | artifact, dialogue, gesture |
| grounded theory | empirical data of any kind | building theory from a phenomenon | theory grounded in data | varying levels |
| systems-based frameworks | large-scale and heterogeneous data | large scale systems of people and technology | organisational insights | macro, organisational level |

adapted from @rogers-beyond-hci:2023 table 9.6

# Interpreting and Presenting Findings

![Here's all the data, enjoy! (Photo by Sear Greyson on Unsplash)](img/sear-greyson-K-ZsC7YdJ6Y-unsplash.jpg){width=50%}

## Biggest Research Writing Tip: Cite your methods

- Applies to research projects at Honours, master, PhD and workplace
- Work with supervisors/mentors/managers to choose methodology and analytical frameworks
- Read and understand the framework from (recent) scholarly sources (not just `nngroup.com`)
- Change and evolution is allowed, but understand that there is a wealth of example and established approaches
- Paraphrase from academic reviewer comments: _"this work cites Braun and Clarke (2006) for reflexive thematic analysis but does not consider newer understandings of this methodology, e.g., Braun and Clarke (2019)..."_

## Structured Notations

- presenting information through formal notations related to particular domains
- e.g., music applications might involve musical notation or symbolic data formats
- could be related to an analytical framework (e.g., conversation analysis)
- tradeoff between precision and flexibility; structured notation can be precise but potentially less accessible to a reader or limited in scope

## Using Stories

Context of use and examples of user experience can be seen as stories or narratives.

- Participants tell stories during data gathering which can illustrate research findings.
- Observations can be framed as stories
- Stories can be written or in the form of storyboards or videos.
- Can be used to support research findings and provide authenticity.

## Summarising Findings

Overall advice about findings...

- Multi-modal is often good: combine styles such as stories, plots, data excerpts, numerical tables
- Developing plots and visualisations is critical and hard work, just like crafting text. We spend hours getting it right in Python/R!
- Important to balance the weight of a **claimed finding** against supporting evidence; however, doesn't mean that small studies are not useful.
- Reviewers hate over-generalisation: careful with terms like "most," "all," "majority," and "none" without justification
- Statistical claims require care to avoid misleading the reader



# Thematic analysis

> “Thematic analysis is a method for identifying, analysing and reporting patterns (themes) within data. It minimally organizes and describes your data set in (rich) detail” (Braun and Clarke 2006, p.79)

- Family of qualitative data analysis techniques
- “Can be applied across a range of theoretical and epistemological approaches” (Braun and Clarke 2006, p.78)
- Not an objective process

## Stages of thematic analysis

![(Braun and Clarke, 2006, p.87)](img/05_02_thematic_analysis_0.jpg)


## Step 1: Familiarise yourself with your data

- Analysis starts as soon as data collection starts
- After each interview, allow time for reflection on data and method
  - What were the key findings of this interview?
  - What was similar/different to previous interviews?
  - What issues were unexpected or surprising?
  - What would you do differently for the next interview? How would you adjust your interview script?
- Note down and mind map any key quotes, examples, or stories from your data

## (Step 1) Transcribing audio/video recordings

- Start of data collection
- Introductory note/context
- Formatting to help distinguish speakers

![[Source](http://www.u.arizona.edu/~kimmehea/purdue/421/exampleinterview.htm)
](img/05_02_thematic_analysis_1.jpg)

## (Step 1) Initial reading

- Immerse yourself in the data: read and re-read transcripts
- Read data in an active way: search for meaning, patterns etc., take notes about ideas for coding.
- But don’t try to code the data yet.

## Step 2: Generate initial codes

“interacting with data, making comparisons between data, and so on, and in doing so, deriving concepts to stand for those data, then developing those concepts in terms of their properties and dimensions” (Corbin & Strauss 2014)

“emergent coding” (your projects) vs “a priori coding” (Lazar et al. 2017, p.304)

## Step 2: What is a code?

![](img/05_02_thematic_analysis_2.jpg)

- A code: Short phrase to describe piece of data
- Identify important features to your research aims
- Subject or nature of comment
- Each item can have multiple codes

(Piggott & Lee-Poy, 2015)

## (Step 2) What to look for when coding?

- Look for specific items
- Ask questions about the data
- Make comparisons at different levels

![](img/05_02_thematic_analysis_3.jpg)

(Lazar et al. 2017, p.312)

## (Step 2) Coding your data: Word/Excel

![](img/05_02_thematic_analysis_4.jpg)
![](img/05_02_thematic_analysis_5.jpg)

(Sharp et. 2019)

## (Step 2) Developing codes

- “In-vivo codes” vs “researcher-denoted concepts”
- __In-vivo: __ e.g., “hot-rodder,” “old-fashioned guy” (Given 2008)
- __Researcher-denoted: __ “My son just sits there and sobs when the computer does not do what he wants. He becomes irritated and keeps pushing the Enter button when the web page loads slowly” e.g. Frustration (Lazar et al. 2017, p.306)

## (Step 2) Coding your data: NVivo

![](img/05_02_thematic_analysis_6.png)

__Image source: https://www.qsrinternational.com/nvivo-qualitative-data-analysis-software/upgrade-nvivo__

## (Step 2) Code book

![](img/05_02_thematic_analysis_7.jpg)

(DeCuir-Gunby 2011, p.147)

## Step 3: Search for themes

> A theme: “A theme captures something important about the data in relation to the research question, and represents some level of patterned response or meaning within the data set” (Braun and Clarke 2006, p.82)

Semantic vs latent themes: 
Can relate to “a behaviour, a user group, events, places, situations” (Sharp et al. 2019, p.322)
Use affinity diagrams to sort codes into group

![](img/05_02_thematic_analysis_8.jpg)

(Sharp et al 2019, p.322)

## (Step 3) Example code structure

![](img/05_02_thematic_analysis_9.jpg)

(Lazar et al. 2017, p.310)

## Step 4: Review themes

- Are themes supported all by the data?
- Can some themes be grouped together?
- Does all the data within the theme describe it?
- Do the themes reflect the overall meaning of the data set?

(Braun and Clarke, 2006)

## Step 5: Refine and name themes

- Does your theme name reflect its ‘essence’?
- Does the theme contain subthemes?
- Are your theme names descriptive but concise?
- Can you summarise your theme in a couple of sentences?

(Braun and Clarke, 2006)

## Step 6: Produce the report

![](img/05_02_thematic_analysis_10.jpg)

- Determine the narrative for your themes
- Include quotes and examples from your data
- Include analysis- “make an argument in relation to your research question”
- In your projects: Present design implications arising from the themes

(Braun and Clarke, 2006)
(Ljungblad et al. 2021, p.6)

## References

- Braun, V & Clarke, V 2006, ‘Using thematic analysis in psychology’,  _Qualitative Research in Psychology_ , vol. 3, no. May 2015, pp. 77–101.
- Corbin, J & Strauss, A 2008,  _Basics of Qualitative Research_  3rd edn, Sage Publications Inc, Thousand Oaks, CA.
- DeCuir-Gunby, JT, Marshall, PL & McCulloch, AW 2011, ‘Developing and Using a Codebook for the Analysis of Interview Data: An Example from a Professional Development Research Project’,  _Field Methods_ , vol. 23, no. 2, pp. 136–155, accessed from <https://doi.org/10.1177/1525822X10388468>.
- Given, L. M. (2008). In vivo coding. In  _The SAGE encyclopedia of qualitative research methods_  (Vol. 1, pp. 473-474). SAGE Publications, Inc., [https://www-doi-org.virtual.anu.edu.au/10.4135/9781412963909.n240](https://www-doi-org.virtual.anu.edu.au/10.4135/9781412963909.n240)
- Lazar, J, Feng, JH & Hochheiser, H 2017,  _Research Methods in Human-Computer Interaction_ , Elsevier Science & Technology, San Francisco, accessed from <http://ebookcentral.proquest.com/lib/anu/detail.action?docID=4851896>.
- Ljungblad, S, Man, Y, Baytacs, MA, Gamboa, M, Obaid, M & Fjeld, M 2021, ‘What Matters in Professional Drone Pilots’ Practice? An Interview Study to Understand the Complexity of Their Work and Inform Human-Drone Interaction Research’, in  _Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems_ , Association for Computing Machinery, New York, NY, USA, accessed from <https://doi.org/10.1145/3411764.3445737>.
- Piggott, T, Morris, C & Lee-Poy, M 2015, ‘Preceptor engagement in distributed medical school campuses’,  _Canadian medical education journal_ , vol. 6, no. 2, pp. e20–e28, accessed from <https://pubmed.ncbi.nlm.nih.gov/27004073>.
- Sharp, H, Preece, J & Rogers, Y 2019,  _Interaction Design: Beyond Human-Computer Interaction_  ProQuest E., Wiley & Sons, West Sussex, accessed from <https://ebookcentral-proquest-com.virtual.anu.edu.au/lib/anu/detail.action?docID=5746446.>.

## Thematic Analysis Bingo [@braun-thematic-analysis:2022]

A bingo card of researcher problems with **reflexive** thematic analysis... which make sense to you so far?

| Mentions inter-coder reliability | Implicitly (post-)positivist TA (not acknowledged) | More than 3 levels of themes | Mention of a lack of (statistical) generalisability | Messy mix of realism and constructionism |
| Unacknowledged social cognitions (e.g., attitude or body image) | Themes are thin - just single idea (a code) | Themes do not have a central organising concept | “Themes emerged” | Data collection stopped at “saturation” |
| Use of passive voice | No reflexivity | **Thematic Analysis** | Only Braun and Clarke 2006 cited | Mention of “bias” |
| Clarke spelled as Clark (no e) | More than 6 themes | No theory of language-treated as a window to truth | Themes are topic summaries | Very few participants quoted / over-quoting of one or more |
| Implicitly realist TA (not acknowledged) | Braun pronounced BRAWN (not Brown) | Mismatch between extracts and analytic claims | Use of a codebook | Data are just paraphrased without interpretation |


# Reflexivity


## Back to defining HCI

> “the design, evaluation, and implementation of interactive computer systems for human use” 

_and_

> “the study of major phenomena surrounding them”

(ACM SIGCHI, 1992)

![Image source: Biplab Chakraborty, Debajit Sarma, Manas Bhuyan, Karl MacDorman. 2017. A Review of Constraints on Vision-based Gesture Recognition for Human-Computer Interaction. IET Computer Vision. 12. 10.1049/iet-cvi.2017.0052.](img/05_01_reflexivity_0.jpg)


## What kinds of interfaces are HCI researchers and practitioners working on?

![(Bardot et al., 2021)](img/05_01_reflexivity_4.jpg)

![(Reinschluessel et al., 2021)](img/05_01_reflexivity_5.jpg)

![(Osone et al., 2021)](img/05_01_reflexivity_6.jpg)

![(Shalawadi et al. 2021)](img/05_01_reflexivity_7.jpg)

## How are HCI paper usually structured?

- Introduction
- Related work/literature review
- Methodology and methods
- Study design
- Findings (e.g., themes, design implications)
- Discussion
- Conclusions
- Limitations and future work


## What makes HCI different from other fields of computing?

- Addresses a broad range of technology users, interfaces, and methods
- Publications often focus on interaction and experience design rather than specifics of implementation (unless the device is novel)
- Qualitative and quantitative research methods
- Often involves human research through evaluating technologies with people
- Different kinds of contributions that HCI research can make: (1)  _empirical_ , (2)  _artifact_ , (3)  _methodological_ , (4)  _theoretical_ , (5)  _benchmark / dataset_ , (6)  _survey_ , and (7)  _opinion_ .  (Wobbrock 2012)


## What is reflexivity?

- Olmos-Vega et al. 2022
- Francisco M. Olmos-Vega, Renée E. Stalmeijer, Lara Varpio & Renate Kahlke (2022) A practical guide to reflexivity in qualitative research: AMEE Guide No. 149, Medical Teacher, DOI:  _[10.1080/0142159X.2022.2057287](https://doi.org/10.1080/0142159X.2022.2057287)_

![(Olmos Vega et al. 2022)](img/05_01_reflexivity_9.png)


## What is reflexivity in HCI?

- Liang et al. 2021
- Calvin A. Liang, Sean A. Munson, and Julie A. Kientz. 2021. Embracing Four Tensions in Human-Computer Interaction Research with Marginalized People. ACM Trans. Comput.-Hum. Interact. 28, 2, Article 14 (April 2021), 47 pages. https://doi-org.virtual.anu.edu.au/10.1145/3443686
- Research is not objective – researcher as instrument
- __Western Feminism is Standpoint Theory__ – “an individual’s experiences and background make up a unique perspective on the world [63, 78]. Because of this, a researcher’s identity influences how they interact with participants …” (Liang et al. 2021, p. 14:6)
- “Reflexivity calls upon researchers to self-reflect and understand their own possible biases, their role in power relations, and how these factors might manifest in their work” (Liang et al. 2021, p. 14:7)
- __Positionality__  - “how a researcher’s perspective compares to others’ perspectives” (Liang et al. 2021, p. 14:7)
- __Positionality is not necessarily about disclosing your identity__
- “[it] doesn’t necessarily mean they have to include an identity disclosure (unless you really really think it’s important). You can talk about privilege, ethics, power, values, all of the above.” - [link](https://medium.com/@caliang/reflexivity-positionality-and-disclosure-in-hci-3d95007e9916)


## What is reflexivity in HCI?

- Rode 2011
- Jennifer A. Rode. 2011. Reflexivity in digital anthropology. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI '11). Association for Computing Machinery, New York, NY, USA, 123–132. https://doi-org.virtual.anu.edu.au/10.1145/1978942.1978961

**Burroway’s definition (in Rode 2011):**

“First, reflexivity, unlike positivism, embraces intervention as a data gathering opportunity.

Second, reflective texts aim to understand how data gathering impacts the quality of the data itself. This approach “commands the observer to unpack those situational experiences by moving with the participants through their time and space” [9. , p14].

Third, reflexive practitioners attempt to find structural patterns in what they have observed, and fourth, in doing so they extend theory [9. ].” (p. 124)

## Types of reflexivity

- Olmos-Vega et al. 2022
- Francisco M. Olmos-Vega, Renée E. Stalmeijer, Lara Varpio & Renate Kahlke (2022) A practical guide to reflexivity in qualitative research: AMEE Guide No. 149, Medical Teacher, DOI:  _[10.1080/0142159X.2022.2057287](https://doi.org/10.1080/0142159X.2022.2057287)_
  - “ __Personal Reflexivity -__   __Ask yourself__ : how are our unique perspectives influencing the research?”
  - __“Interpersonal Reflexivity: Power - Ask yourself__ : what relationships exist and how are they influencing the research and the people involved? What power dynamics are at play?”
  - __“Methodological Reflexivity - Ask yourself__ :  How are we making methodological decisions and what are their implications?”
  - __“Contextual Reflexivity - Ask yourself: __ How are aspects of context influencing the research and people involved?” (Olmos-Vega et al. 2022)

![](img/05_01_reflexivity_10.png)


## Statement of Positionality – Example 1

![](img/05_01_reflexivity_11.png)

- Liang et al. 2021
- Calvin A. Liang, Sean A. Munson, and Julie A. Kientz. 2021. Embracing Four Tensions in Human-Computer Interaction Research with Marginalized People. ACM Trans. Comput.-Hum. Interact. 28, 2, Article 14 (April 2021), 47 pages. https://doi-org.virtual.anu.edu.au/10.1145/3443686


## Statement of Positionality – Example 1 (cont)

- Liang et al. 2021
- Calvin A. Liang, Sean A. Munson, and Julie A. Kientz. 2021. Embracing Four Tensions in Human-Computer Interaction Research with Marginalized People. ACM Trans. Comput.-Hum. Interact. 28, 2, Article 14 (April 2021), 47 pages. https://doi-org.virtual.anu.edu.au/10.1145/3443686

![](img/05_01_reflexivity_12.png)

## Conceptualising Interaction

- Articulating the proposed solution as a conceptual model
- Orientation
- Open-Mindedness
- Common Ground
- What are the underlying assumptions and claims?
- Write them down
- Try to defend/support them

## Further Readings

- Jack Carroll. 2004. Beyond Fun, Interactions 11 (5), 38–40.
- John M. Carroll. 2014. Chapter 2: Human Computer Interaction - brief intro. The Encyclopedia of Human-Computer Interaction, 2nd Ed. https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed
- Kate Finn and Jeff Johnson. 2016. Designing for an Aging Population: Toward Universal Design. In Proceedings of the 2016 CHI Conference Extended Abstracts on Human Factors in Computing Systems (CHI EA '16), 1011–1012. DOI: [https://doi.org/10.1145/2851581.2856669](https://doi.org/10.1145/2851581.2856669)
- Harrison, S., Tatar, D., & Sengers, P. (2007, April). The three paradigms of HCI. In  _Alt CHI. Session at the SIGCHI Conference on Human Factors in Computing Systems San Jose, California, USA_  (pp. 1-18)
- Marc Hassenzahl. 2014. Chapter 3: User Experience and Experience Design. The Encyclopedia of Human-Computer Interaction, 2nd Ed. https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed
- John McCarthy and Peter Wright. 2004. Technology as Experience. Interactions 11, 5. https://interactions.acm.org/archive/view/september-october-2004/technology-as-experience1
- Don Norman. 2013. The design of everyday things: Revised and expanded edition. Basic books.
- Lillian Xiao. 2017. [A Brief History of Human-Computer Interaction (HCI)](https://blog.prototypr.io/the-rise-of-human-computer-interaction-hci-823dd6286e1d).


## Readings / References

- Sandra Bardot, Surya Rawat, Duy Thai Nguyen, Sawyer Rempel, Huizhe Zheng, Bradley Rey, Jun Li, Kevin Fan, Da-Yuan Huang, Wei Li, and Pourang Irani. 2021. ARO: Exploring the Design of Smart-Ring Interactions for Encumbered Hands. In Proceedings of the 23rd International Conference on Mobile Human-Computer Interaction (MobileHCI '21). Association for Computing Machinery, New York, NY, USA, Article 12, 1–11. [https://doi.org/10.1145/3447526.3472037](https://doi.org/10.1145/3447526.3472037)
- Hiroyuki Osone, Jun-Li Lu, and Yoichi Ochiai. 2021. BunCho: AI Supported Story Co-Creation via Unsupervised Multitask Learning to Increase Writers’ Creativity in Japanese. In Extended Abstracts of the 2021 CHI Conference on Human Factors in Computing Systems (CHI EA '21). Association for Computing Machinery, New York, NY, USA, Article 19, 1–10. https://doi.org/10.1145/3411763.3450391
- Anke Verena Reinschluessel, Thomas Muender, Tanja Döring, Verena Nicole Uslar, Thomas Lück, Dirk Weyhe, Andrea Schenk, and Rainer Malaka. 2021. A Study on the Size of Tangible Organ-shaped Controllers for Exploring Medical Data in VR. In Extended Abstracts of the 2021 CHI Conference on Human Factors in Computing Systems (CHI EA '21). Association for Computing Machinery, New York, NY, USA, Article 261, 1–7. [https://doi.org/10.1145/3411763.3451594](https://doi.org/10.1145/3411763.3451594)
- Sujay Shalawadi, Anas Alnayef, Niels van Berkel, Jesper Kjeldskov, and Florian Echtler. 2021. Rainmaker: A Tangible Work-Companion for the Personal Office Space. In Proceedings of the 23rd International Conference on Mobile Human-Computer Interaction (MobileHCI '21). Association for Computing Machinery, New York, NY, USA, Article 39, 1–13. https://doi.org/10.1145/3447526.3472032
- Wobbrock, J.O. and Kientz, J.A., 2016. Research contributions in human-computer interaction. interactions, 23(3), pp.38-44.

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
