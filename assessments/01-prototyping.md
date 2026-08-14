---
title: Prototyping Animal-Computer Interaction
author: Dr Charles Martin
---

![Photo by [Alison Pang](https://unsplash.com/@alisonpang) on [Unsplash](https://unsplash.com/photos/brown-poodle-puppy-on-white-bed-linen-YJVD4Ddczjo)](img/alison-pang-YJVD4Ddczjo-unsplash.jpg){width=80%}

## Outline {#outline}

- **Due date**: 2026-08-24 23:59 AEST
- **Mark weighting**: 20%
- **Submission**: submit your assignment according to the [instructions below](#submission-process)
- **Policies**: Late submission is not permitted for this assessment. This is an individual assessment task.
- **Gitlab Template Repository**: [`comp3900-2026-A1-prototyping` repo (link)](https://gitlab.cecs.anu.edu.au/comp3900/2026/comp3900-2026-A1-prototyping)

## Description {#description}

Assignment 1 involves creating a prototype that solves a problem.
Your prototype must engage with an interaction design challenge and consider multiple perspectives.

The interaction design challenge is as follows:

> **Animal-Computer Interaction:**[^aci] On 1st June 2026, a burst of precisely tuned neutrinos struck the earth dramatically increasing the intelligence of all non-human animal life. Mammals, birds, fish, reptiles, amphibians and even insects now have near- or above- human intelligence[^int]. After weeks of diplomatic negotiation (and worldwide adoption of vegan diets) animals now seek to participate in pan-species society on earth. The only problem is that _they can't use any of our computer systems!_ Your challenge is choose an interactive computer system (software and hardware) to accomplish **one everyday task**, and produce a **prototype design** that is accessible to **one kind of non-human animal** as well as a human.

[^aci]: Animal-Computer Interaction is actually a [real field](https://dl.acm.org/conference/aci)! See proceedings from the 2024 conference [@aci-conference:2024].

[^int]: This bit is not real. I made this bit up.

To accomplish this task, you will need to have a strong understanding of _usability_, _user experience_, _design_, and _prototyping_ as discussed in the first four weeks of this course. Your submission must demonstrate sophisticated engagement with these concepts.

Your submission will include documentation of your prototype, sketches, and a written design rationale. Your design rationale presents _the argument behind your design_ [@maclean-argument-behind-artifact:1989]: why it is appropriate, why it is likely to succeed compared with the other options you considered, and what trade-offs you have accepted. It explains the user's needs, their context of use, and their individual capacity and perspective, and it shows how your sketching and ideation led you to this prototype rather than another.

Your written rationale should have the following sections:

- **Task, problem, and users:** explain the everyday task, the users you are targeting (i.e., the animal and the human), and the problems that these users will encounter at present.
- **Sketches and ideation:** present your sketches and annotations, articulate what differs between them and what the options would mean for your users.
- **Prototype:** present and explain your prototype and how it meets the needs of the users (animal and human) in this context of use, explain the criteria used to choose this prototype and its limitations compared to other ideas.
- **Acknowledgements:** acknowledge any external help you received, and any use of generative AI including the scope to which it was applied.
- **References:** include at least two references in ACM format.

## Specification {#specification}

Your submission must:

- be a **single markdown file**, `prototype-documentation.md`, using the headings provided in the template
- include at least three hand-drawn sketches, embedded as images in that file
- include visual documentation (i.e., at least one photograph) of a paper based prototype, also embedded
- include at least two references to external sources in ACM format
- be a maximum of 1500 words + 10% acceptable buffer (i.e., no more than 1650 words), and at least 400 words. Acknowledgements, the reference list, commented text, numbers and other non-alphabet characters, and code blocks do not count towards the total; captions and tables do count.
- image and media files go in the `materials/` folder of your fork.
- must be uploaded to _your fork_ of the [`comp3900-2026-A1-prototyping`](https://gitlab.cecs.anu.edu.au/comp3900/2026/comp3900-2026-A1-prototyping) repository on Gitlab by the due date.

## Submission Process {#submission-process}

1. Fork the template repository.
2. Follow a design process of ideation, sketching, and prototyping to address the design challenge.
3. Photograph your sketches and prototype, and add the image files to the `materials/` folder of _your fork_.
4. Write your design rationale in `prototype-documentation.md`, using the headings provided and embedding your images where they support the argument.
5. Don't forget to include at least two references to external sources in ACM format.
6. Commit and **push** your changes to GitLab, and check that the CI jobs pass (green ticks).

## Notes {#notes}

Here's how to get started with the work in this assignment:

1. **Choose one animal and one everyday task.** Pick a single kind of non-human animal, and a single everyday task that a person currently uses a computer system for; e.g., ordering food, booking an appointment, checking a timetable. Specific is good.

2. **Find out what your users can actually do.** Use your [research skills](https://scholar.google.com) to learn about your animal's senses, physical capabilities, and social behaviour. You can imagine that your animal is at least as intelligent as people and, if they have the physical ability to read, write, understand speech, or speak, they can.

3. **Ideate and sketch at least three different options.** Use ideation techniques from week 2. The different sketches map out a design space for your rationale. Sketches should be hand-drawn either on paper or a tablet screen.

4. **Choose one option, and articulate why.** What criteria did you judge the options against? What did you give up by choosing this one? See [design rationale](https://smcclab.github.io/thirty-nine-hundred-hci/lectures/02-design.html#/design-rationale) from week 2.

5. **Build a paper prototype and photograph it.** Low fidelity is expected. Your prototype needs to show how the _interaction_ works, not how a finished product would look.

6. **Write it up** in `prototype-documentation.md` using the provided headings. Refer to each image from your text (e.g., "my first sketch is shown in Figure 1") so your reader knows what they are looking at and why.

7. **Push early and push often.** Check that the CI jobs pass before the deadline --- they check your word count and markdown formatting.

Here's some general advice:

- Don't forget to ask for help or advice on the course forum: [Edstem discussions](https://edstem.org/au/courses/37143/discussion)
- Your rationale is an argument, not a report. If a reader could not possibly disagree with anything in it, you have written a description instead.
- Generative AI is not banned in this course, but sketches, prototypes and written work is expected to be primarily your own work. Any use of generative AI must be cited including the scope to which it is applied. Use of generative AI without appropriate explanation and referencing comes under the _N_ category in the marking rubric.
- "magical" solutions lack sophistication; sure, a magical brain-computer interface that understands all user intentions perfectly solves the task, but the prototype and rationale will be weak.
- the gitlab template repository gives you feedback about your markdown formatting and word length. We grade your work from the gitlab repo, so make sure your submission looks good in gitlab's "preview" of the markdown text.

## Marking Rubric {#rubric}

| CRITERIA | HD | D | CR | P | N |
|---|---|---|---|---|---|
| Sophistication and clarity of the design rationale in terms of HCI theories, perspectives, and concepts. (50%) | Excellent to outstanding design rationale demonstrating consideration of HCI theories and perspectives that goes beyond learning materials. Level of communication and referencing is excellent. | Very good design rationale demonstrating consideration of HCI theories and perspectives that follows specification, but not beyond learning materials. Level of communication and referencing is excellent. | A design rationale that follows specification with HCI theories and perspectives at the level of learning materials. Level of communication and referencing is good. | Some effort to follow the specification for a design rationale. May touch on some HCI concepts. Level of communication and referencing may have some errors. | A design rationale with little connection to HCI concepts or one that is below acceptable standards. May not follow the specification or contain serious errors in communication and referencing. |
| Sophistication as a prototype addressing identified user needs. (50%) | Excellent to outstanding prototype demonstrating a thorough design and prototyping process with clear consideration of user needs. Excellent adherence to the assessment format. | Very good prototype demonstrating a thorough design and prototyping process with consideration of user needs. Excellent adherence to the assessment format. | A good prototype that demonstrates a design and prototyping process. May not fully address user needs. Good adherence to the assessment format. | A satisfactory prototype with limited engagement with the design process or user needs. Adherence to the submission format may be poor. | Below acceptable standards as a prototype. May have very poor adherence to submission format. |

## References

