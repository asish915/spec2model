# How to Submit

### Step 1 — Fork this repo

### Step 2 — Create your team folder
```
submissions/your_team_name/
```
Use lowercase, underscores, no spaces. Example: `submissions/team_phoenix/`

### Step 3 — Add your files
```
submissions/your_team_name/
├── predictions.csv          # Required
├── submission_sheet.pdf     # Required
└── code/                    # Required — all notebooks/scripts
    ├── main.ipynb (or .py)
    └── (any other files)
```

### Step 4 — predictions.csv format
```csv
id,prediction
1,class_a
2,class_b
3,class_a
...
```
- Must have exactly two columns: `id` and `prediction`
- Must cover every row in the final test dataset
- No missing values

### Step 5 — Submit via Pull Request
- PR title: `[Submission] Team Name — Problem A/B`
- PR into the `main` branch of this repo
- **Deadline: T + 5:00 sharp.** PR timestamp is final.

### Checklist before submitting
- [ ] `predictions.csv` has `id` and `prediction` columns
- [ ] `predictions.csv` covers all test rows, no nulls
- [ ] `submission_sheet.pdf` is filled completely
- [ ] All code is included and runnable
- [ ] PR title follows the format above

### Late submissions?
No. The PR timestamp is the cutoff. Plan ahead.

---
*SPEC2MODEL Challenge — GDGOC Silicon University*
