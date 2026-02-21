# Submission Sheet

Fill this out during the event and include it as submission\_sheet.pdf (or .md) in your PR.

## Section 1 — Team Information

*   **Team Name: MODEL MAVERICKS**
*   **Problem Chosen:** B
*   **Member 1:** Ram Mohan Hota, 23BCEH14, CEN
*   **Member 2:** Ashutosh Rout, 23BCEE72, CEN
*   **Member 3:** Satyabrata Mohapatra, 23BCED53, CEN
*   **Contact (any one member):** 8260625456

## Section 2 — Data Strategy

Did you use any external data beyond the provided train.csv?

*   **No**

If yes, fill the table below for each source:

| Source Name | URL | Rows Used | Why It Was Relevant |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |

How did you verify the external data was clean and trustworthy?

**Answer:**

## Section 3 — Data Cleaning and Preprocessing

How did you handle missing values? Which columns had them and what did you do?

**Answer:** We handled missing values by replacing values with mean of that numerical type features of dataset.

1\. avg\_session\_duration\_min

2\. sessions\_per\_week

3\. features\_used\_pct

4\. avg\_ticket\_resolution\_hrs

5\. rating\_given

6\. os\_version\_age\_months

7\. days\_since\_last\_feature\_use

We replaced each of above columns null values with their mean .

Did you find any noisy or suspicious labels in the training data? What did you do about them?

**Answer:** Yes, we found ouliers in some features of training through help of box plots.

Was the data imbalanced? How did you handle it (if at all)?

**Answer:** Yes, the data was imbalanced and we handled it by training model with XGBOOST,CATBOOST and got performance metric based on F1 score.

Any other transformations you applied (scaling, encoding, outlier removal)?

**Answer:** Yes, we had done scaling on Numerical type features, applied Label encoding on Categorical type features.

## Section 4 — Feature Engineering

What were your top 3 most important features and why?

| Rank | Feature | Why It Matters |
| --- | --- | --- |
| 1 | Price_increase_experienced | Showed highest data correlation value in heatmap |
| 2 | Num_increased_failures_90d | Same as above |
| 3 | Monthly_price_inr | Same as above |

Did you create any new features that were not in the original dataset?

**Answer: No**

Did you drop any features? Which ones and why?

**Answer: No**

Did you check for correlations or feature interactions? What did you find?

**Answer: No**

## Section 5 — Model Selection and Training

What is your final model?

**Answer: XGBOOST**

What other models did you try before this? Why did you pick the final one over them?

| Model Tried | Validation Score | Why You Rejected / Kept It |
| --- | --- | --- |
| XGBBOST | 58.3795 | Keep it |
| CATBOOST | 58.1598 | Rejected |
|  |  |  |

What hyperparameters did you tune? What values did you settle on?

**Answer: Objective, num\_classes, n\_estimator, learning\_rate, max\_depth, sub\_sample, col\_sample**

How did you validate your model? (train/test split, cross-validation, etc.)

**Answer: we did cross validation .**

What was your best validation score before submitting?

**Answer: 58.3795**

## Section 6 — Honest Reflection

What did you try that did NOT work?

**Answer: We tried to implement LightGBM but it shows poor result.**

What are the known limitations of your model?

**Answer:**

What was the hardest part of this challenge for your team?

**Answer: We were unable to remove unessential features from dataset.**

If you had 6 more hours, what would you do differently?

**Answer: We would do outlier removal, more data visualization(boxplot, scatterplot,pairplot).**

## Section 7 — Team Collaboration

| Member | What They Worked On |
| --- | --- |
| Ram Mohan Hota | Trained and test model on given dataset |
| Ashutosh Rout | Data preprocessing and cleaning(EDA) |
| Satyabrata Mohapatra | Github related work |
|  |  |

## Section 8 — External Data Declaration

I confirm that all external data sources used are listed in Section 2 and are publicly available.

*   **Yes**

## May submi this here in markdown only here!!

_SPEC2MODEL Challenge — GDGOC Silicon University — Zygon x Neosis Annual Fest_