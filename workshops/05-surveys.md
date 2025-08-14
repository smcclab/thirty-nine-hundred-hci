---
title: Surveys
author: Dr Charles Martin and Karla Kelly
---

In this class, we will practice administering one of the classic questionnaires in usability, the SUS (System Usability Scale). 

Questionnaires like the SUS and TLX are widely used in assessing how users perceive a user interface. Questionnaires are useful in gaining numerical information from a medium to large group of users quickly. They can be particularly useful in comparing different interactive systems, situations or user types as you can use statistical techniques to assess differences between samples. 

In today's tutorial, you will do a mock survey with a user interface and the SUS. You will collect data together with others in the class and calculate descriptive statistics, generate plots, and perform significance testing using Python.


## Pre-Class Tasks

1. Read the following article from NNgroup on the SUS and TLX: <https://www.nngroup.com/articles/measuring-perceived-usability/>
2. Find a quantitative or rating-scale style survey somewhere in the world, take a photo or screenshot.
3. Post on the forum with your image and explain: 1) what the survey is and where you found it, 2) what type of data is captured, 3) how it is similar or different to the SUS and NASA TLX discussed in the article.
4. Optional (in case the wifi is slow or no internet): make sure you have Python installed on your laptop and can access a Python notebook of your choice (we recommend Jupyter Notebook). Bring your computer to class!

## Plan for the Class

In this class, you will:

1. Practice administering the SUS
2. Analyse your quantitative data
3. Discuss what you learned.

## In-Class Tasks

### 0. Discuss pre-class responses (10 minutes)

The tutor will bring up the pre-class responses on the big screen and lead you in a discussion. Some questions might be:

- What kind of survey or rating scale did you choose?
- When might you use this survey or rating scale?
- How long might it take for a user to complete this scale?
- What kinds of issues or difficulties might a user encounter when completing this scale? (Consider either as the researcher administering the survey, or the user completing the scale.)

### 1. Administer the SUS (20 minutes)

Your tutor will allocate a technology to be evaluated, with a task for the user to evaluate using the technology, e.g.:

- Technology: Qantas (Group 1) or Virgin Australia (Group 2) - or some other comparable technology
- User Task: Book a domestic flight from Canberra to Hobart (Do not proceed to payment!)

Your tutor will also provide you with a participant identifier (participant ID).

In pairs:

- Take turns acting as the user and the researcher.
- As the researcher, welcome the user to the experiment, and give them instructions (i.e. ask the user to do the task and then complete the provided SUS to evaluate the user experience)
- Make sure the user records their answers in the survey; you will need these for the next task!
- Make sure the user's participant ID is recorded on the user's completed survey!

### 2. Collate your data (5 minutes)

Your tutor will share a spreadsheet for everyone to enter their results into. (So we can compare the findings across groups, i.e. to compare which technologies' usability scores were better/worse.)

- Collate/enter the results from the survey you administered the **shared** spreadsheet (e.g. MS Excel).
- Make sure you only enter the data against the participant ID of your participant

### 3. Analyse your quantitative data (40 minutes)

**Individually:**

1. Go to Google Colaboratory and start a **New Notebook**: <https://colab.google/>
2. In Colab, drag the class data spreadsheet file into the **Files** pane.
3. In a new code cell, load your data into a DataFrame:

   ```python
   import pandas as pd, numpy as np
   from scipy import stats
   import matplotlib.pyplot as plt

   # --- Load ---
   df = pd.read_csv("sus_dummy_two_groups.csv")  # replace with your file name

   SUS = [f"SUS{i}" for i in range(1, 11)]
   df  # show the DataFrame
   
4. Recode the positively worded SUS items (items 1, 3, 5, 7, and 9) by subtracting 1 from each response, so that their values range from 0 (“Strongly Disagree”) to 4 (“Strongly Agree”):

   ```python
   POS = ["SUS1","SUS3","SUS5","SUS7","SUS9"]
   df[POS] = df[POS] - 1
   
5. **Reverse code** the negatively worded items (for the SUS, these are the even-numbered items: 2, 4, 6, 8, 10).  
   This makes the scale consistent so that higher numbers always indicate better usability.

   ```python
   NEG = ["SUS2","SUS4","SUS6","SUS8","SUS10"]
   df[NEG] = 5 - df[NEG]
   
6. **Calculate the SUS score for each participant**  
   Make sure all 10 items have been recoded to the 0–4 scale before this step.
   We’ll remove any rows with missing items, then sum the items (0–40) and scale to 0–100.

   ```python
   # Remove rows with missing SUS items
   df = df.dropna(subset=SUS)
   
   # Sum (0–40) and scale to 0–100
   df["SUS_score"] = df[SUS].sum(axis=1) * 2.5
   
   # (Optional) quick check of the results
   print(df["SUS_score"].describe())
   
7. **Get the descriptive statistics**  
   Find the minimum, maximum, mean, and standard deviation of the SUS scores for each group.

   ```python
   # --- Descriptive statistics ---
   print("\nDescriptive stats by group:")
   print(df.groupby("group")["SUS_score"].describe().round(2))

8. **Plot a histogram of your data**  
   Look at the shape of the distribution for each group.  
   Is the data evenly spread, skewed, or clustered?

   ```python
   # --- Histogram ---
   df["SUS_score"].hist(by=df["group"], bins=10, edgecolor="black", layout=(1, 2))
   plt.suptitle("Distribution of SUS Scores by Group")
   plt.show()

9. **Create a boxplot**  
   Compare the median, quartiles, and range of SUS scores for each group.  
   Look for any outliers (points that sit far from the rest of the data).

   ```python
   # --- Boxplot ---
   df.boxplot(column="SUS_score", by="group")
   plt.title("SUS Scores by Group")
   plt.suptitle("")
   plt.ylabel("SUS (0–100)")
   plt.show()

10. **Compare the findings**  
    Use Welch’s t-test to check whether there is a statistically significant difference in SUS scores between the two groups.  
    The output will also show which group had the higher average score.  
    **Interpretation guide:**  
    - If `p < 0.05`: The difference is considered statistically significant (unlikely due to chance).  
    - If `p ≥ 0.05`: The difference is *not* statistically significant (could be due to random variation).

    ```python
    # --- Between-groups comparison (Welch’s t-test) ---
    groups = [g["SUS_score"].dropna().values for _, g in df.groupby("group")]

    if len(groups) == 2:
        g1, g2 = groups
        group_names = list(df["group"].unique())

        # Welch’s t-test
        t = stats.ttest_ind(g1, g2, equal_var=False)

        # Means for each group
        mean_g1, mean_g2 = np.mean(g1), np.mean(g2)

        print(f"Welch’s t-test: t = {t.statistic:.2f}, p = {t.pvalue:.3f}")
        print(f"Mean SUS for {group_names[0]}: {mean_g1:.2f}")
        print(f"Mean SUS for {group_names[1]}: {mean_g2:.2f}")

        # Interpret significance
        if t.pvalue < 0.05:
            print("Result: Statistically significant difference (p < 0.05).")
        else:
            print("Result: No statistically significant difference (p ≥ 0.05).")

        # Which group scored higher
        if mean_g1 > mean_g2:
            print(f"{group_names[0]} had higher usability scores.")
        elif mean_g2 > mean_g1:
            print(f"{group_names[1]} had higher usability scores.")
        else:
            print("Both groups had the same average score.")
    else:
        print("Need exactly two groups for comparison.")
    ```
       
11. Post your findings and plots in the class thread!

### 3. Discuss your key learnings (10 minutes)

Your tutor will lead you in a discussion about what you learned from using the SUS and the analysis process. 

- What did you find?
- How easy or difficult was it to use the scale?
- What would you do differently next time?

## Important Notes

This activity is a **quick introduction** to using the System Usability Scale (SUS) and basic statistical comparison in Python.  
In real usability studies, **statistical tests have specific conditions and assumptions** that must be checked before deciding which analysis is appropriate.  

For example:
- **Welch’s t-test** assumes the data are approximately normally distributed and the two groups are independent.
- **Sample size** affects the reliability of your results; small samples may fail to detect real differences or may exaggerate differences due to chance.
- **Experimental design** (within- vs between-subjects) changes which test you should use and how you interpret results.

We have **skipped these detailed checks** in this exercise to focus on learning the mechanics of:
1. Scoring the SUS
2. Performing basic descriptive statistics
3. Running a simple between-groups comparison

**In practice**, you should:
- Plan your study with a **power analysis** to determine the needed sample size.
- Choose an analysis method that matches your design and data type.
- Check the assumptions of the test you run.
- Interpret statistical significance alongside **practical significance** (effect size, context, and stakeholder needs).

## Resources

- Python Tutorial <https://www.w3schools.com/python/default.asp>
- t-Test <https://datatab.net/tutorial/t-test>
- How to use Jupyter Notebook (if not using Google Colab): <https://www.youtube.com/watch?v=H9Iu49E6Mxs>

## References

- Reverse scoring: <https://agolix.com/blog/tutorials/reverse-scoring-scale-questions/>
- Using the SUS: <https://usabilitygeek.com/how-to-use-the-system-usability-scale-sus-to-evaluate-the-usability-of-your-website/>
- Chapter 9 Data Analysis, Interpretation, and Presentation (Rogers et al)
