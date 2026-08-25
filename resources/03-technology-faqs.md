---
title: Technology FAQs for HCI
author: Dr Charles Martin
---

We are using Gitlab and Markdown to submit assignments in this course.

These two technologies are not very hard to use, but, if you are new to computing, all the new technology platforms can feel overwhelming.

You may find the resources on this page helpful, and if you have any further issues with Gitlab or Markdown, please ask questions on the course forum so that we can help.

## GitLab {#gitlab}

- ANU Teaching GitLab Server: <https://gitlab.cecs.anu.edu.au>
- Missing Manual for ANU GitLab and Git: <https://comp.anu.edu.au/docs/gitlab/>

### Tips

## Markdown {#markdown}

- The Markdown Guide: <https://www.markdownguide.org>

### Tips

- To see expected formatting, look at Charles' example repo: <https://gitlab.cecs.anu.edu.au/u4110680/comp3900-2025-prototyping>
- Use empty lines around headings, lists, and code blocks
- Use empty lines between images
- Use descriptive alt text/caption for images.
- To view the markdown preview, push your markdown to GitLab, view the `.md` file in the gitlab web interface, make sure "Preview" is selected.
- Please make sure URLs in your portfolio have angle brackets around them:
  `<http://example.com>` so that they work properly as links and in the PDF output.
- **Output PDF**: images may move from where they are declared due to the software used to generate the PDF ([pandoc](https://pandoc.org) and [LaTeX](https://en.wikipedia.org/wiki/LaTeX)). This is typical for PDF files generated using LaTeX.
- **Output PDF**: images may take up a lot of space on the page, you can adjust the width of an image like so:

```
![Image caption here](path/to/image.jpg){width=50%}
```


## Google Colab {#colab}

- Google Colaboratory: <https://colab.google>

### Tips



## What reference format is used in this course? {#reference-format}

We use ACM reference format (<https://www.acm.org/publications/authors/reference-formatting>) with **numerical citations**. In your Markdown documents, follow these four rules:

1. **Write your references as a numbered Markdown list** (`1.`, `2.`, ...) under a `## References` heading. Don't write bracketed numbers by hand at the start of a line: `[1]: ...` is Markdown link-definition syntax and the whole line will silently disappear from the rendered page, and `[1] ...` entries need blank lines between them or they merge into one paragraph. A numbered list avoids both problems.
2. **Cite in your text with the number in square brackets**, e.g. "dogs are dichromats [2]". A bare `[1]` renders as-is in Markdown, so no special syntax is needed. Keep the list order matched to your in-text numbers, and cite every listed reference somewhere in your text.
3. **End every reference with a working link**: published work ends with its DOI written as a URL (e.g. `<https://doi.org/10.1145/1978822.1978836>`); web sources end with `Retrieved Month Day, Year from <URL>`. We check these links — a reference that can't be found is a serious problem (see the academic integrity policy).
4. **The rest of the entry follows ACM style**: full author first names (not initials), year, title, venue, volume/issue and pages. The easiest way to get this exactly right is the ACM Digital Library's "Export Citation → ACM Ref" button; for non-ACM papers, search the DOI at <https://doi.org/> or use Google Scholar's cite button and add the missing DOI/URL yourself.

An example References section in Markdown:

```markdown
## References

1. Clara Mancini. 2011. Animal-computer interaction (ACI): a manifesto. *Interactions* 18, 4 (2011), 69-73. <https://doi.org/10.1145/1978822.1978836>
2. Allan MacLean, Richard M. Young, and Thomas P. Moran. 1989. Design rationale: the argument behind the artifact. *ACM SIGCHI Bulletin* 20, SI (1989), 247-252. <https://doi.org/10.1145/67450.67497>
3. Howzit (StackOverflow user). 2018. p5js-image-array (CC BY-SA 2.5). Retrieved August 25, 2026 from <https://stackoverflow.com/questions/51233447/p5js-image-array>
4. Scott Bauer. 2004. Photo of Potatoes (Public Domain). Retrieved August 25, 2026 from <https://en.wikipedia.org/wiki/Potato#/media/File:Patates.jpg>
```

Entries 3 and 4 show the pattern for web sources, code snippets, and images/assets: credit the author (a username is fine if that's all there is), note the licence, and give the retrieval date and URL.

## General writing style {#writing-style}

It is appropriate to use first-person pronouns in the assignments for this course. We follow this resource to help understand the pronouns to use: <https://apastyle.apa.org/style-grammar-guidelines/grammar/first-person-pronouns>