# Submission Sheet

Fill this out during the event and include it as `submission_sheet.pdf` (or `.md`) in your PR.

---

## Section 1 — Team Information

- **Team Name:** Kojak
- **Problem Chosen:** B
- **Member 1:** Saheb Satya Prakash Sha, 23BCSF67, CSE
- **Member 2:** Asish Sarangi, 23BCSD78, CSE
- **Member 3:** Biswajeet Srichandan, 23BCSD65, CSE
- **Contact (any one member):** 

---

## Section 2 — Data Strategy

Did you use any external data beyond the provided train.csv?

- No

If yes, fill the table below for each source:

| Source Name | URL | Rows Used | Why It Was Relevant |
|-------------|-----|-----------|---------------------|
| | | | |
| | | | |

How did you verify the external data was clean and trustworthy?

**Answer:**

---

## Section 3 — Data Cleaning and Preprocessing

**How did you handle missing values? Which columns had them and what did you do?**  
**Answer:** Missing values were handled using median imputation for numerical features and most-frequent imputation for categorical features, along with missing-indicator flags for affected columns.

**Did you find any noisy or suspicious labels in the training data? What did you do about them?**  
**Answer:** No clearly noisy or inconsistent labels were detected, so all training labels were retained as provided.

**Was the data imbalanced? How did you handle it (if at all)?**  
**Answer:** Yes, the data was moderately imbalanced, and this was addressed using macro F1 scoring during tuning and stratified cross-validation.

**Any other transformations you applied (scaling, encoding, outlier removal)?**  
**Answer:** Applied standard scaling to numerical features, one-hot encoding to categorical features, and log transformation to highly skewed numerical features.

---

## Section 4 — Feature Engineering

**What were your top 3 most important features and why?**

| Rank | Feature | Why It Matters |
|------|---------|---------------|
| 1 | engagement_score | Captures overall user activity intensity and feature usage behavior. |
| 2 | recency | Reflects how recently the user interacted with the app, a strong churn indicator. |
| 3 | support_pain | Measures user frustration through support tickets and resolution time. |

**Did you create any new features that were not in the original dataset?**  
**Answer:** Yes, several engineered features were created including engagement_score, recency, support_pain, stability, value_ratio, and interaction-based features.

**Did you drop any features? Which ones and why?**  
**Answer:** The `id` column was dropped as it is a unique identifier and not predictive.

**Did you check for correlations or feature interactions? What did you find?**  
**Answer:** Feature interactions were implicitly captured through engineered interaction features and the gradient boosting model’s tree-based structure.

---

## Section 5 — Model Selection and Training

**What is your final model?**  
**Answer:** HistGradientBoostingClassifier with hyperparameter tuning via GridSearchCV.

**What other models did you try before this? Why did you pick the final one over them?**

| Model Tried | Validation Score | Why You Rejected / Kept It |
|-------------|-----------------|---------------------------|
| Logistic Regression | Lower macro F1 | Underfit complex feature interactions. |
| Random Forest | Moderate macro F1 | Performed well but slightly weaker than gradient boosting. |
| HistGradientBoosting | Best macro F1 | Captured nonlinear interactions and gave highest CV score. |

**What hyperparameters did you tune? What values did you settle on?**  
**Answer:** Tuned max_iter, learning_rate, max_depth, min_samples_leaf, and l2_regularization; best values were max_iter=300, learning_rate=0.02, max_depth=5, min_samples_leaf=5, l2_regularization=1.0.

**How did you validate your model? (train/test split, cross-validation, etc.)**  
**Answer:** Used 5-fold stratified cross-validation with macro F1 scoring during hyperparameter tuning.

**What was your best validation score before submitting?**  
**Answer:** Best cross-validation macro F1 score was 0.5596.

---

## Section 6 — Honest Reflection

**What did you try that did NOT work?**  
**Answer:** Increasing model complexity beyond optimal depth and reducing regularization led to overfitting without improving validation performance.

**What are the known limitations of your model?**  
**Answer:** The model relies only on structured tabular data and may not generalize well if user behavior patterns shift significantly.

**What was the hardest part of this challenge for your team?**  
**Answer:** Handling feature alignment between training and test datasets after feature engineering.

**If you had 6 more hours, what would you do differently?**  
**Answer:** Perform deeper feature importance analysis, experiment with advanced boosting techniques, and apply more refined feature selection.

---

## Section 7 — Team Collaboration

| Member | What They Worked On |
|--------|-------------------|
| Member 1 | Feature engineering and preprocessing |
| Member 2 | Model training and hyperparameter tuning |
| Member 3 | Validation strategy and performance evaluation |
| Member 4 | Submission formatting and pipeline debugging |

---

## Section 8 — External Data Declaration

I confirm that all external data sources used are listed in Section 2 and are publicly available.

- **Yes**
---

## May submit this here in markdown only here!!

*SPEC2MODEL Challenge — GDGOC Silicon University — Zygon x Neosis Annual Fest*
