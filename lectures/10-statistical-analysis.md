---
title: Statistical Analysis
author: Dr Charles Martin
title-slide-attributes:
    data-background-image: img/10_statistical_analysis.jpg
    data-background-size: cover
---
<!-- I like this one but I don't have subscription for downloads: https://unsplash.com/photos/female-programmer-writing-programming-code-on-laptops-and-desktop-computer-at-cozy-home-workplace-close-up-on-hands-and-keyboard-YXC9PuBblTA. -->
## Lecture Ideation

What can this lecture be about?

- Lazar Chapter 4 Statistical Analysis (get up to _p_ and ANOVA properly)
- Python examples
- Put together a colab.google notebook to demo with fake data
- Put activities to collect some live in lectures (if enough people show up)

### Maybe not these things.

- conceptualising interaction (Interaction Design chapter 3 was missed?)
- data at scale ethical concerns (interaction design chapter 10)

## Announcements

## Plan for the class

1. Performing data analysis in details.
2. Understand the *contexts* of use and *assumptions* of each method.
3. Interpret results *appropriately*.
4. Justify the validity of findings in academic contexts.

## Preparing Data for Analysis

> Week 5 content recap: Why are the needs for data pre-processing?

- Manually entered, errors, inconsistent formats.
- Primitive which need higher level coding.
- Specific statistical analysis method or software require layout or format
[@delwiche2019little].

## Preparing Data for Analysis

1. Cleaning up data
    - basic check for manual errors, all data are correctly grouped, remove problematic ones.
2. Coding data
3. Organising data 

Charles does live coding demo -- colab link.


## Descriptive Stats (Recap)
- Charles has discussed this in week 5.

It's covered in collab.

## Comparing Means
- Charles also seemed to have discussed it.

It's covered in collab.

## Statistics: t-tests

See collab.

- Widely used in HCI to compare means between two conditions (e.g., menu selection times) and test if differences are statistically significant.
- Include the t-value, degrees of freedom (df), and p-value, where df depends on participant numbers, and p indicates the probability the result is due to chance.
- `p < 0.05` typically means the difference is significant, allowing rejection of the null hypothesis, with smaller p-values (e.g., <0.01) indicating stronger evidence.


## Analysis of Variance

See collab.

## Assumption of *t* tests and *F* tests

- Homogeneity of variance: when multiple groups are compared, tests are more accurate if variances of the sample population are nearly equal.
    - Use transformation techniques when not.
- Errors should be normally distributed, otherwise highly skewed data result in false results!

## Identifying relationships

## Regression

## Nonparametric statistical tests

See collab.

### Chi-square test

See collab.

### Others

- Data collected from two independent samples (e.g., between group).
    - Consider Mann-Whitney U test/Wald-Wolfowitz run test.
- Two datasets from the same user group - paired-samples t test; otherwise Wilcoxon signed ramks test.
- Three or more datasets: Kruskal-Wallis one-way ANOVA.
    - dependent: Friedman's two-way ANOVA.


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
