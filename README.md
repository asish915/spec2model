# SPEC2MODEL Challenge

**Organized by [GDGOC Silicon University](https://github.com/GDGOC-SiliconUniversity) | Zygon x Neosis Annual Fest**

---

### What Is This?

A machine learning competition where you get a **problem statement**, a **feature schema**, and a **training dataset**. Your job: clean the data, engineer features, build a model, and predict labels on a hidden test set.

No hand-holding. No perfect data. Real ML engineering.

### Timeline

| When | What You Get |
|------|-------------|
| **12 hrs before event** | Problem statements, feature schemas, dummy test data (50-100 rows with labels), submission sheet, rules |
| **Event start (T+0:00)** | Training dataset (2000-5000 rows with labels) — this is when building begins |
| **T+4:30** | Final test dataset (500-700 rows, NO labels) |
| **T+5:00** | Submission deadline |

### Problems

Two problems. **Pick one.**

| | Problem A | Problem B |
|---|---|---|
| **Name** | [Late Delivery Prediction](problems/PROBLEM_A/PROBLEM_A.md) | [App Churn Reason Classification](problems/PROBLEM_B/PROBLEM_B.md) |
| **Type** | Binary classification | Multiclass classification (4 classes) |
| **Features** | 17 | 28 |
| **Difficulty** | Accessible — clear patterns, fewer features | Harder — overlapping classes, fuzzy boundaries |
| **Good for** | All skill levels | Teams wanting a challenge |

### Evaluation

| Component | Weight | Method |
|-----------|--------|--------|
| Model performance | **50%** | Automated — Macro F1 on hidden test set |
| Professor viva | **50%** | Live Q&A — explain your approach, decisions, code |

**Cross-problem scoring:** Raw F1 scores are NOT compared across problems. Your model score is calculated relative to the best F1 within your chosen problem:

```
Model Score = (Your F1 / Best F1 in your problem) × 50
```

This ensures teams picking the harder Problem B are not disadvantaged.

### External Data Policy

- **Allowed.** You may use any publicly available data to supplement the provided training set.
- **Must be relevant** to the problem statement.
- **Must be cited** in your submission sheet — source name, URL, and why you used it.
- **Not required.** You can score well using only the provided data if you clean and engineer it properly.
- **Caution:** The final test set follows the same distribution as the provided training data. External data that doesn't match this distribution may hurt rather than help.

### How to Submit

See **[SUBMISSIONS.md](SUBMISSIONS.md)**.

### Repo Structure

```
spec2model/
├── README.md
├── SUBMISSIONS.md
├── problems/
│   ├── problem_A/
│   │   ├── PROBLEM.md            # Problem statement + full schema
│   │   ├── dummy_test.csv        # 50-100 rows, with labels (pre-release)
│   │   └── train.csv             # Training data (released at event start)
│   └── problem_B/
│       ├── PROBLEM.md
│       ├── dummy_test.csv
│       └── train.csv
├── submissions/
│   └── team_name/                # Your team's folder
│       ├── predictions.csv
│       ├── submission_sheet.pdf
│       └── code/
└── evaluation/
    ├── final_test_A.csv          # Released at T+4:30
    └── final_test_B.csv
```

### Rules

- **External data allowed** — must be relevant and cited
- **Any ML library allowed** — scikit-learn, XGBoost, PyTorch, TensorFlow, LightGBM, CatBoost, etc.
- **No pre-trained models on the exact task** — general-purpose libraries and tools are fine
- **All team members must explain the code** individually during viva
- **Deadline is final** — PR timestamp is the official submission time
- **predictions.csv format must match exactly** — see your problem's PROBLEM.md for exact class labels

---

*SPEC2MODEL Challenge — GDGOC Silicon University — Zygon x Neosis Annual Fest*
