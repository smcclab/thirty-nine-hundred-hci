# Course Lectures and Assessment for HCI Thirty-Nine-Hundred

Lecture sides and course activities for a course in human computer interaction. The idea is to develop course materials in markdown and build these files into HTML, PDF, or other file formats necessary for displaying to students or pasting into an LMS (learning management system) such as Canvas or Moodle.

The content is in markdown format in the following directories:

- `assessments`
- `lectures`
- `resources`
- `workshops`

References in bibtex format can be placed in the file:

- `references.bib`

## Building

The build process is automated via the `Makefile`. `make`, `pandoc` and a TeX environment (e.g., MacTeX or TeX Live) is required.

All course materials can be built with:

    make all

This takes some time (unfortunately) because pandoc is quite slow at building PDF slides. A quicker build just creates the HTML files:

    make html

The build is automated via a Github Action which runs `make public` rather than `make all` (the idea is that the "public" version of the material may not include draft content).

## Deploying

This repository is configured to build a "public" version of the site and deploy to a Github Pages website automatically. The output website is: <https://smcclab.au/thirty-nine-hundred-hci/> (the older `smcclab.github.io` address redirects here).

## Contributing

Content developers (e.g., course convenors, lecturers, tutors, learning designers) can contribute by directly editing markdown files within the `assessments`, `lectures`, `resources`, and `workshops` directories.

Images can be placed with in an `img` directory associated with each of the above. You can't reference an image across directories. So for example an image in `lectures/img` can't be used in a workshop, you'll have to duplicate the file annoyingly.

A lecture slide can take a full-bleed background image, and it shows up in both the HTML slides and the PDF:

    ## Slide Title {background-image="img/hero.jpg"}

This works on `#` section headings too, and the title slide gets one from `title-slide-attributes` in the frontmatter. Add `background-size="contain"` to fit the whole image in rather than cropping it, and `background-opacity="0.4"` to fade it back when the heading is hard to read over the photo.

All course content should be include references to textbooks, online resources and scholarly publications. The references should go in the common `references.bib` file in bibtex format. You can cite using [pandoc's citation format (see link)](https://pandoc.org/MANUAL.html#extension-citations), e.g., `[@bibtex-key, p26]` etc. The referencing format is APA using `apa.csl`.

(NB: I know we ask the students to use ACM style, but the ACM csl uses numerical citations while author/date is more convenient for these kind fo documents where we want to know what the reference is without looking it up continually).

Editing online in Github is fine for simple changes or adding content. The default `public` build only builds the lecture so nothing added to workshops, assessments, or resources will necessarily block the build.

## Licence

Unless otherwise noted, Copyright © Charles Martin, The Australian National University.

- **Content** (lectures, assessments, workshops, resources) is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), except where otherwise noted — you may reuse and adapt it with attribution.
- **Code** (the Makefile, scripts, filters, SCSS, and templates) is licensed under the [MIT Licence](LICENSE).
- **Third-party images and figures** in the materials remain under their own rights and are not covered by the CC BY licence.

See the [LICENSE](LICENSE) file for the full text.

## Course information

This information is specific for thirty-nine-hundred.

### Learning Outcomes

Upon successful completion, students will have the knowledge and skills to:

1. Explain and illustrate key aspects of human-computer interaction.
2. Apply multiple perspectives, theories, and ethical and inclusive considerations in critiquing technologies and prototyping and developing new design ideas.
3. Investigate activities, practices, and contexts of technology use through contextual research methods.
4. Critically evaluate novel technology design ideas based on Human-Computer Interaction approaches.
5. (PG): Critically reflect on a designer's own presence and influence within a technology design process.

### Course Schedule

Lectures and workshops as built from this repository. Workshop *N* runs in the
tutorials of week *N+1* (there is no workshop in week 1), and the mid-semester
teaching break falls between weeks 6 and 7.

| Week | Week beginning | Lecture | Workshop | Assessment |
|------|----------------|---------|----------|------------|
| 1  | 2026-07-27 | 1. Intro to Human Computer Interaction        |                                   |                                                        |
| 2  | 2026-08-03 | 2. Design                                      | 1. Making                         |                                                        |
| 3  | 2026-08-10 | 3. Sketch and Prototype                        | 2. Personas and Scenarios         |                                                        |
| 4  | 2026-08-17 | 4. Data Gathering                              | 3. Prototyping                    |                                                        |
| 5  | 2026-08-24 | 5. Data Analysis                               | 4. Interviews                     | Assignment 1: Prototyping due Mon 2026-08-24           |
| 6  | 2026-08-31 | 6. Reflexivity and Thematic Analysis           | 5. Surveys                        |                                                        |
| 7  | 2026-09-21 | 7. Interfaces                                  | 6. Thematic Analysis              |                                                        |
| 8  | 2026-09-28 | 8. Evaluation                                  | 7. Planning Evaluations           |                                                        |
| 9  | 2026-10-05 | 9. Cognitive, Social, and Emotional Interaction | 8. Research Design               | Assignment 2: AI Needs Finding due Tue 2026-10-06      |
| 10 | 2026-10-12 | 10. Statistical Analysis                       | 9. Prototyping for Evaluation     |                                                        |
| 11 | 2026-10-19 | 11. Expressive Interfaces                      | 10. From Theme to Implication     |                                                        |
| 12 | 2026-10-26 | 12. Human-Centred AI                           | 11. Positionality                 |                                                        |
| 13 | 2026-11-02 |                                                |                                   | Final Project: Prototype Design and Research Project due Thu 2026-11-05 |

Pre- and in-class tasks are due at the start of each tutorial from week 2 onwards.

### Assessments

1. Pre-class and in-class tasks (10%, 1% per class, best 10 of 11) LO: 1,2
2. Assignment 1: Prototyping (20%) LO: 1,2
3. Assignment 2: AI Needs Finding (30%) LO: 3,4 (PG: 5)
4. Final Project: Prototype Design and Research Project
  (40%) LO: 2,3,4 (PG: 5)




