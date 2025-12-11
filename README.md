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

This repository is configured to build a "public" version of the site and deploy to a Github Pages website automatically. The output website is: <https://smcclab.github.io/thirty-nine-hundred-hci/>

## Contributing

Content developers (e.g., course convenors, lecturers, tutors, learning designers) can contribute by directly editing markdown files within the `assessments`, `lectures`, `resources`, and `workshops` directories.

Images can be placed with in an `img` directory associated with each of the above. You can't reference an image across directories. So for example an image in `lectures/img` can't be used in a workshop, you'll have to duplicate the file annoyingly.

All course content should be include references to textbooks, online resources and scholarly publications. The references should go in the common `references.bib` file in bibtex format. You can cite using [pandoc's citation format (see link)](https://pandoc.org/MANUAL.html#extension-citations), e.g., `[@bibtex-key, p26]` etc. The referencing format is APA using `apa.csl`.

(NB: I know we ask the students to use ACM style, but the ACM csl uses numerical citations while author/date is more convenient for these kind fo documents where we want to know what the reference is without looking it up continually).

Editing online in Github is fine for simple changes or adding content. The default `public` build only builds the lecture so nothing added to workshops, assessments, or resources will necessarily block the build.

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

|   Week  |   Topic Title                                            |   Schneiderman (6th ed)                              |   CHI Subcommittee                                                |   Tutorial  |   Assessment                                            |
|---------|----------------------------------------------------------|------------------------------------------------------|-------------------------------------------------------------------|-------------|---------------------------------------------------------|
|   1     |   Introduction to HCI, Usability of Interactive Systems  |   1. Usability of Interactive Systems                |   User Experience and Usability                                   |             |                                                         |
|   2     |   Design                                                 |   4. Design                                          |   Design                                                          |   1         |                                                         |
|   3     |   Guidelines, Principles and Theories                    |   3. Guidelines, Principles and Theories             |   Computational Interaction                                       |   2         |                                                         |
|   4     |   Universal Usability                                    |   2. Universal Usability                             |   Accessibility and Aging                                         |   3         |                                                         |
|   5     |   Evaluation and the User Experience                     |   5. Evaluation and the User Experience              |   Understanding People                                            |   4         |   Assignment 1: Prototyping                             |
|   6     |   Direct Manipulation and Immersive Environments         |   7. Direct Manipulation and Immersive Environments  |   Blending Interaction: Engineering Interactive Systems & Tools   |   5         |                                                         |
|   7     |   Fluid Navigation                                       |   8. Fluid Navigation                                |   Games and Play                                                  |   6         |                                                         |
|   8     |   Expressive Interfaces                                  |   9. Expressive Human and Design Languages           |   Developing Novel Devices: Hardware, Materials, and Fabrication  |   7         |                                                         |
|   9     |   Devices                                                |   10. Devices                                        |   Interacting with Devices: Interaction Techniques & Modalities   |   8         |   Assignment 2: User Research                           |
|   10    |   Information Search                                     |   15. Information Search                             |   Interaction Beyond the Individual                               |   9         |                                                         |
|   11    |   Data Visualisation                                     |   16. Data Visualisation                             |   Visualization                                                   |   10        |                                                         |
|   12    |   Human-Centred AI                                       |   “Human-Centred AI”                                 |   Critical Computing, Sustainability, and Social Justice          |             |                                                         |
|   13    |                                                          |                                                      |                                                                   |             |   Final Project: Prototype Design and Research Project  |
### Assessments

1. Pre-class and in-class tasks (10%, 1% per class) LO: 1,2
2. Assignment 1: Prototyping (20%) LO: 1,2
3. Assignment 2: User Research (30%) LO: 3,4 (PG: 5)
4. Final Project: Prototype Design and Research Project
  (40%) LO: 2,3,4 (PG: 5)




