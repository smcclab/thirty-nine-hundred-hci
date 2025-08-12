---
title: Surveys
author: Dr Charles Martin
---

In this class we will practice administering some of the classic questionnaire instruments in usability, the SUS (System Usability Scale) and NASA TLX (Task Load Index). 

These questionnaires are widely used in assessing how users perceive a user interface. Questionnaires like these are useful in gaining numerical information from a medium to large group of users quickly. They can be particularly useful in comparing different interactive systems, situations or user types as you can use statistical techniques to assess differences between samples. 

In today's tutorial, you will do a mock survey with a user interface and the SUS instrument. You will collect data together with others in the class and calculate descriptive statistics, generate plots, and perform significance testing using Python.


## Pre-Class Tasks

1. Read the following article from NNgroup on the SUS and TLX: <https://www.nngroup.com/articles/measuring-perceived-usability/>
2. Find a quantitative or rating-scale style survey somewhere in the world, take a photo or screenshot.
3. Post on the forum with your image and explain: 1) what the survey is and where you found it, 2) what type of data is captured, 3) how it is similar or different to the SUS and NASA TLX discussed in the article.
4. Make sure you have Python installed on your laptop and can access a Python notebook of your choice. Bring your computer to class!

## Plan for the Class

In this class, you will:

1. Practice administering the SUS or TLX (25 minutes)
2. Analyse your quantitative data (40 minutes)
3. Discuss what you learned (15 minutes)

## In-Class Tasks

### 0. Discuss pre-class responses (5 minutes)

The tutor will bring up the pre-class responses on the big screen and lead you in a discussion. Some questions might be:

- What kind of survey or rating scale did you choose?
- When might you use this survey or rating scale?
- How long might it take for a user to complete this scale?
- What kinds of issues or difficulties might a user encounter when completing this scale?

### 1. User Evaluation Planning (10 minutes)

In your group, decide on a technology to evaluate. You should also decide on what task you will ask the user to complete using the chosen technology. Some suggestions (but feel free to choose your own!):

- Murray's Bus Website: book a trip to Sydney
- ANU library: Find a specific book or journal article
- Coles: Order groceries delivered to your apartment. Buy eggs, leeks, and shampoo

### 2. Administer the SUS (10 minutes)

In pairs:

- Take turns acting as the user and the researcher.
- As the researcher, welcome the user to the experiment, and give them instructions (i.e. ask the user to do the task and then complete the provided SUS to evaluate the user experience)
- Make sure they record their answers in the survey; you will need these for the next task!

### 3. Analyse your quantitative data

In your group: 

1. Collate your data in a **shared** spreadsheet (e.g. MS Excel, etc.). Note: If we share a joint spreadsheet for the class, we can compare the findings across groups as everyone will have access to the class data. (ie whose was better/worse?)

Individually:

2. Import your data into a Python notebook (e.g. Jupyter Notebook, JupyterLab, etc.)
3. Reverse code the negatively worded items (for the SUS, these are the even-numbered items)
4. Calculate the SUS score for each participant
5. Get the descriptive statistics. What are the min, max, and mean SUS scores? What is the standard deviation?
6. Plot a histogram of your data. How is the data shaped? Does it look evenly spread?
7. Create a boxplot. Are there any outliers?
8. Post your findings in the class thread.

### 4. Discuss your key learnings

Your tutor will lead you in a discussion about what you learned from using the SUS and the analysis process. 

- What did you find?
- How easy or difficult was it to use the scale?
- What would you do differently next time?

## Resources
Reverse scoring: <https://agolix.com/blog/tutorials/reverse-scoring-scale-questions/>
Using the SUS: <https://usabilitygeek.com/how-to-use-the-system-usability-scale-sus-to-evaluate-the-usability-of-your-website/>

## References
