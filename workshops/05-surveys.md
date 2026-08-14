---
title: Surveys
author: Dr Charles Martin and Karla Kelly
---

# Surveys

In this class, we will practice administering one of the classic questionnaires in usability, the SUS (System Usability Scale) [@brooke-sus:1995].

Questionnaires like the SUS and TLX are widely used in assessing how users perceive a user interface. Questionnaires are useful in gaining numerical information from a medium to large group of users quickly. They can be particularly useful in comparing different interactive systems, situations or user types as you can use statistical techniques to assess differences between samples.

In today's tutorial, you will do a mock survey with a user interface and the SUS. You will score a questionnaire by hand, pool your data with the rest of the class, and then use Python to calculate descriptive statistics, generate plots, and perform significance testing. Along the way you'll make predictions and check them against the data — the goal is to understand what each step tells you, not just to run the code.

**NOTE:** Bring your computer to class!

## Pre-Class Tasks

1. Read the following article from NNgroup on the SUS and TLX: <https://www.nngroup.com/articles/measuring-perceived-usability/>
2. Find a quantitative or rating-scale style survey somewhere in the world, take a photo or screenshot.
3. Post on the forum with your image and explain: 1) what the survey is and where you found it, 2) what type of data is captured, 3) how it is similar or different to the SUS and NASA TLX discussed in the article.
4. In this tutorial, we will be using **Python**.
   You will need either:
   1) An active **Google account** to use [Google Colab](https://colab.google/) (runs in your browser, no installation required), **OR**
   2) **Python installed on your laptop** along with a notebook environment of your choice (we recommend [Jupyter Notebook](https://jupyter.org/)).

## Plan for the Class

In this class, you will:

1. Practice administering the SUS
2. Score a SUS response by hand
3. Analyse the whole class's data in Python
4. Discuss what the results do (and don't) tell you and what this means for your assignment.

## In-Class Tasks

### 0. Discuss pre-class responses (10 minutes)

The tutor will bring up the pre-class responses on the big screen and lead you in a discussion. Some questions might be:

- What kind of survey or rating scale did you choose?
- When might you use this survey or rating scale?
- How long might it take for a user to complete this scale?
- What kinds of issues or difficulties might a user encounter when completing this scale? (Consider either as the researcher administering the survey, or the user completing the scale.)

### 1. Administer the SUS (20 minutes)

Your tutor will allocate a **technology** for you to evaluate, along with a **task** to complete using that technology. For example:

- **Technology:** Qantas (Group 1) or Virgin Australia (Group 2) — or another comparable technology
- **User Task:** Book a domestic flight from Canberra to Hobart (*Do not proceed to payment!*)

Your tutor will also give you:

- A **participant identifier (participant ID)**
- A **paper copy of the SUS questionnaire**

**In pairs:**

1. Take turns acting as the **user** and the **researcher**.
2. As the **researcher**:
   - Welcome the user to the study.
   - Ask for their consent to participate.
   - Give the task instructions (e.g., *"Please complete the task, then fill in the SUS questionnaire to rate your experience"*).
   - **Observe** while your participant fills in the questionnaire: do they hesitate on any items? Do they ask you what a question means? Jot these observations down. They are data too, and we will come back to them in the final discussion.
3. Make sure the user:
   - Completes the task.
   - Records their answers on the SUS questionnaire.
4. Ensure the **participant ID** is written on the completed questionnaire — you will need this for the data entry step.

### 2. Score your SUS by hand (10 minutes)

Before touching any code, score the questionnaire you just administered **on paper**. The SUS comes with its own scoring recipe [@brooke-sus:1995]:

1. **Odd-numbered items** (1, 3, 5, 7, 9 — the positively worded ones): score = response − 1.
2. **Even-numbered items** (2, 4, 6, 8, 10 — the negatively worded ones): score = 5 − response. This **reverse-codes** them, so that a higher score always means better usability.
3. Each item is now on a 0–4 scale. **Sum the ten items** (0–40), then **multiply by 2.5** to get a SUS score from 0 to 100.

Write the final score on the questionnaire next to the participant ID — you will use it to check your Python analysis later.

To interpret a SUS score, compare it against results from thousands of published studies. The average across studies is about 68, and mean scores map onto adjective ratings roughly as follows [@bangor-sus-adjective:2009]:

| Mean SUS score | Adjective rating   |
| -------------: | ------------------ |
| 85 and above | Excellent          |
| 71-85        | Good               |
| 50-71        | OK                 |
| below 50     | Poor               |

**Discuss in your pair:**

- Why do you think the SUS alternates positively and negatively worded items, rather than asking ten questions the same way around?
- Where does your participant's score sit on the table above? Does that match how the task *felt*?
- **Commit to a prediction:** when we pool the whole class's data, which technology will score higher, and by roughly how much? Write your prediction down — you will check it against the data shortly.

### 3. Collate your data (5 minutes)

Your tutor will provide a **shared spreadsheet** for the whole class to enter results. This will allow us to compare SUS scores across groups to see which technology had better or worse usability. The spreadsheet has one row per participant with these columns:

| Column | Contents |
|---|---|
| `participant_id` | The participant ID from the paper questionnaire |
| `group` | Which technology was evaluated (e.g., `Group 1` or `Group 2`) |
| `SUS1` … `SUS10` | The **raw responses** from the questionnaire, each 1–5 |

- Enter the **raw responses** (1–5) exactly as written on the paper — *not* your hand-scored values. The recoding will happen in Python, so everyone's data must start from the same place.
- Only enter data in the row corresponding to **your participant's ID**.
- Double-check all 10 values are entered and each is between 1 and 5.
- Ensure no identifying information other than the participant ID is included.

Your tutor will then export the spreadsheet as a **CSV file** (e.g., `sus_class_data.csv`) and share it with the class.

### 4. Analyse the class's data (30 minutes)

Work through this individually, but **sit with your pair**, several steps ask you to stop and compare notes before moving on.

1. Go to Google Colaboratory and start a **New Notebook**: <https://colab.google/>
2. In Colab, drag the class data CSV file into the **Files** pane.
3. In a new code cell, load your data into a DataFrame:

   ```python
   import pandas as pd, numpy as np
   from scipy import stats
   import matplotlib.pyplot as plt

   # --- Load ---
   df = pd.read_csv("sus_class_data.csv")  # replace with your file name

   SUS = [f"SUS{i}" for i in range(1, 11)]
   df  # show the DataFrame
   ```

   **If the class data isn't ready yet** (or something has gone wrong with it), run this cell instead to generate a stand-in dataset with the same structure, then continue with the steps below:

   ```python
   # --- Fallback: generate stand-in data (skip if the class CSV loaded fine) ---
   rng = np.random.default_rng(3900)
   rows = []
   for group, usability in [("Group 1", 3.9), ("Group 2", 3.75)]:
       for i in range(14):
           pos = np.clip(np.round(rng.normal(usability, 1.2, 5)), 1, 5)      # odd items
           neg = np.clip(np.round(rng.normal(6 - usability, 1.2, 5)), 1, 5)  # even items
           rows.append([f"{group[-1]}{i+1:02d}", group,
                        pos[0], neg[0], pos[1], neg[1], pos[2],
                        neg[2], pos[3], neg[3], pos[4], neg[4]])
   SUS = [f"SUS{i}" for i in range(1, 11)]
   df = pd.DataFrame(rows, columns=["participant_id", "group"] + SUS)
   df
   ```

4. **Sanity-check the raw data** before recoding anything. Real class data usually has at least one typo, and it's much easier to find now than after recoding:

   ```python
   # Every response should be between 1 and 5
   raw = df[SUS]
   print("Out-of-range values:", ((raw < 1) | (raw > 5)).sum().sum())
   print("Missing values:", raw.isna().sum().sum())
   ```

   If either count isn't zero, tell your tutor and the class will fix the shared spreadsheet together before going on.

5. Now replicate your hand-scoring in code. First, recode the positively worded SUS items (items 1, 3, 5, 7, and 9) by subtracting 1 from each response, so that their values range from 0 ("Strongly Disagree") to 4 ("Strongly Agree"):

   ```python
   POS = ["SUS1","SUS3","SUS5","SUS7","SUS9"]
   df[POS] = df[POS] - 1
   ```

6. **Reverse code** the negatively worded items (for the SUS, these are the even-numbered items: 2, 4, 6, 8, 10), just as you did on paper:

   ```python
   NEG = ["SUS2","SUS4","SUS6","SUS8","SUS10"]
   df[NEG] = 5 - df[NEG]
   ```

7. **Calculate the SUS score for each participant.**
   We'll remove any rows with missing items, then sum the items (0-40) and scale to 0-100.

   ```python
   # Remove rows with missing SUS items
   df = df.dropna(subset=SUS)

   # Sum (0-40) and scale to 0-100
   df["SUS_score"] = df[SUS].sum(axis=1) * 2.5
   ```

   **Checkpoint — check the code against your hand score.** Look up the participant you scored on paper:

   ```python
   df[df["participant_id"] == "101"]  # replace with your participant's ID
   ```

   Does `SUS_score` match the number you wrote on the questionnaire? If not, one of you (you or the computer) has made a mistake — work out which, with your pair, before continuing.

8. **Predict, then describe.** Before running the next cell, say out loud to your pair what you expect the mean for each group to be — you wrote a prediction down in step 2. Then find the minimum, maximum, mean, and standard deviation of the SUS scores for each group:

   ```python
   # --- Descriptive statistics ---
   print("\nDescriptive stats by group:")
   print(df.groupby("group")["SUS_score"].describe().round(2))
   ```

   How close was your prediction? Where do the group means sit on the adjective table from step 2?

9. **Plot a histogram of your data.** Again, predict first: do you expect the scores to be evenly spread, skewed, or clustered? Then look at the actual shape of the distribution for each group:

   ```python
   # --- Histogram ---
   df["SUS_score"].hist(by=df["group"], bins=10, edgecolor="black", layout=(1, 2))
   plt.suptitle("Distribution of SUS Scores by Group")
   plt.show()
   ```

10. **Create a boxplot.** Compare the median, quartiles, and range of SUS scores for each group. Look for any outliers (points that sit far from the rest of the data).

    ```python
    # --- Boxplot ---
    df.boxplot(column="SUS_score", by="group")
    plt.title("SUS Scores by Group")
    plt.suptitle("")
    plt.ylabel("SUS (0-100)")
    plt.show()
    ```

    **Stop and discuss with your pair before running any test:** looking only at the boxplot, would you say the two technologies are different? How confident are you? Agree on an answer — then see whether the statistics back you up.

11. **Compare the groups.**
    Use Welch's t-test to check whether there is a statistically significant difference in SUS scores between the two groups, and calculate **Cohen's d**, an *effect size* — a measure of how *large* the difference is, separate from whether it's statistically detectable.
    **Interpretation guide:**
    - If `p < 0.05`: the difference is considered statistically significant (unlikely due to chance).
    - If `p >= 0.05`: the difference is *not* statistically significant (could be due to random variation).
    - Cohen's d: roughly, 0.2 is a small effect, 0.5 medium, 0.8 large.

    ```python
    # --- Between-groups comparison (Welch's t-test) ---
    groups = [g["SUS_score"].dropna().values for _, g in df.groupby("group")]

    if len(groups) == 2:
        g1, g2 = groups
        group_names = list(df["group"].unique())

        # Welch's t-test
        t = stats.ttest_ind(g1, g2, equal_var=False)

        # Means for each group
        mean_g1, mean_g2 = np.mean(g1), np.mean(g2)

        # Cohen's d (pooled standard deviation)
        n1, n2 = len(g1), len(g2)
        pooled_sd = np.sqrt(((n1 - 1) * np.var(g1, ddof=1) +
                             (n2 - 1) * np.var(g2, ddof=1)) / (n1 + n2 - 2))
        d = (mean_g1 - mean_g2) / pooled_sd

        print(f"Welch's t-test: t({t.df:.1f}) = {t.statistic:.2f}, p = {t.pvalue:.3f}")
        print(f"Cohen's d = {d:.2f}")
        print(f"Mean SUS for {group_names[0]}: {mean_g1:.2f}")
        print(f"Mean SUS for {group_names[1]}: {mean_g2:.2f}")

        # Interpret significance
        if t.pvalue < 0.05:
            print("Result: Statistically significant difference (p < 0.05).")
        else:
            print("Result: No statistically significant difference (p >= 0.05).")

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

    The `t(24.3)` part of the output is the *degrees of freedom*. You'll learn what it means in the statistical analysis lecture later in the course; for now, just include it when you report the test, as in the template below.

    **A note on test choice:** in the data gathering lecture we said rating-scale data isn't really continuous and suggested non-parametric tests [@kaptein-likert-analysis:2010]. That advice applies to *individual* Likert items. A SUS score is the *sum of ten items* on a 0-100 scale, which behaves much more like continuous data, so parametric tests like the t-test are commonly used and defensible here although statisticians still argue about this [@norman-likert-parametric:2010]. The important thing is to know *why* you chose your test (and the answer is not "my teacher/Claude/chatGPT told me to"). We'll meet the non-parametric alternative (the Mann-Whitney U test) in the statistical analysis lecture.

12. **Summarise your findings in plain language.**
    After running the t-test and checking your descriptive statistics, write a short summary that anyone could understand.
    Post your summary in the class thread!

    **Example reporting template:**

    ```text
    The mean SUS score for Group 1 (Technology A) was 82.3, which falls in the "Good" range, close to "Excellent".
    The mean SUS score for Group 2 (Technology B) was 71.5, at the bottom of the "Good" range.
    A Welch's t-test found that the difference was statistically significant (t(24.3) = 2.30, p = .030), with a large effect size (d = 0.88), indicating that Technology A was rated as more usable for the given task.
    This suggests that, for this context and task, Technology A may offer a better user experience than Technology B.
    ```

### 5. Discuss: from class data to your assignment (15 minutes)

Your tutor will lead a discussion about what you learned — and about what carries over to your own studies. Some questions:

- What did you find? Did the data match the prediction you wrote down in step 2?
- What did you observe while administering the questionnaire? Did participants hesitate or ask questions? What would that mean for data quality in a real study?
- Was the difference between the groups *practically* meaningful, or only *statistically* detectable (or neither)? What do the effect size and the adjective ratings add that the p-value doesn't?
- **Assignment 2 will be different from today.** In your needs-finding study you'll have **3–5 participants and no comparison groups** — so a significance test like today's t-test isn't appropriate there. Discuss: which parts of today's process *do* transfer? (Using a validated instrument, careful scoring, descriptive statistics, plots, and honest plain-language reporting all do.) With 3–5 participants, report **individual scores and ranges** rather than hiding them behind a mean — recall the "use and misuse of data" warning from the data analysis lecture about statements like *"50% of users"* when n = 4.
- What would you do differently next time?

## Important Notes

This activity is a **quick introduction** to using the System Usability Scale (SUS) and basic statistical comparison in Python.
In real usability studies, **statistical tests have specific conditions and assumptions** that must be checked before deciding which analysis is appropriate.

For example:

- **Welch's t-test** assumes the data are approximately normally distributed and the two groups are independent.
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

- Data Analysis lecture: <https://smcclab.au/thirty-nine-hundred-hci/lectures/05-data-analysis.html>
- Textbook: Chapter 9 Data Analysis, Interpretation, and Presentation [@rogers-beyond-hci:2023]
- Python Tutorial <https://www.w3schools.com/python/default.asp>
- t-Test <https://datatab.net/tutorial/t-test>
- How to use Jupyter Notebook (if not using Google Colab): <https://www.youtube.com/watch?v=H9Iu49E6Mxs>

## References
