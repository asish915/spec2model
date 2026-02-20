# SPEC2MODEL Challenge

**Organized by [GDGOC Silicon University](https://github.com/GDGOC-SiliconUniversity)**

---

### What Is This?

You get a **problem statement**, a **feature schema**, and a **training dataset**. Your job: clean the data, engineer features, build a model, and predict labels on a hidden test set.

### Event Structure

| When | What You Get |
|------|-------------|
| **12 hrs before** | Problem statements, feature schemas, dummy test data, rules |
| **Event start** | Training dataset (2000-5000 rows with labels) |
| **T + 4:30** | Final test dataset (500-700 rows, NO labels) |
| **T + 5:00** | Submission deadline |

### Problems

Two problem statements are available. **Pick one.**

- [`problems/problem_A/`](problems/problem_A/) — Problem A statement, schema, and data
- [`problems/problem_B/`](problems/problem_B/) — Problem B statement, schema, and data

### Evaluation

| Component | Weight |
|-----------|--------|
| Model performance (Macro F1 on hidden test set) | 50% |
| Professor viva (live Q&A on your approach) | 50% |

### How to Submit

See **[SUBMISSIONS.md](SUBMISSIONS.md)** for full instructions.

### Repo Structure

```
spec2model/
├── README.md
├── SUBMISSIONS.md
├── problems/
│   ├── problem_A/
│   │   ├── PROBLEM.md          # Problem statement + schema
│   │   ├── dummy_test.csv      # 50-100 rows, with labels (pre-release)
│   │   └── train.csv           # Training data (released at event start)
│   └── problem_B/
│       ├── PROBLEM.md
│       ├── dummy_test.csv
│       └── train.csv
├── submissions/
│   └── team_name/              # Your team's folder
│       ├── predictions.csv
│       ├── code/
│       └── submission_sheet.pdf
└── evaluation/
    └── final_test.csv          # Released at T+4:30
```

### Rules

- **External data is allowed** — must be relevant to the problem and cited in your submission sheet
- **Any ML library is allowed** — scikit-learn, XGBoost, PyTorch, TensorFlow, etc.
- **No pre-trained models on the exact task** — general libraries and tools are fine
- **All team members must be able to explain the code** during the viva
- **Deadline is final** — PR timestamp is the official submission time

### Links

- [Submission Guide](SUBMISSIONS.md)
- [Problem A](problems/problem_A/PROBLEM.md)
- [Problem B](problems/problem_B/PROBLEM.md)

---

*SPEC2MODEL Challenge — GDGOC Silicon University*
