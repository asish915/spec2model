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

**Problem A:**
```csv
id,prediction
1,late
2,on_time
3,late
```
Values: `late` or `on_time`

**Problem B:**
```csv
id,prediction
1,price_sensitive
2,lost_interest
3,bad_experience
```
Values: `price_sensitive`, `bad_experience`, `found_alternative`, or `lost_interest`

- Exactly two columns: `id` and `prediction`
- Cover every row in the final test dataset
- No missing values, no extra columns
- Lowercase, exact spelling

### Step 5 — Submit via Pull Request
- PR title: `[Submission] Team Name — Problem A` or `[Submission] Team Name — Problem B`
- PR into `main` branch
- **Deadline: T+5:00 sharp.** PR timestamp is final.

### Checklist
- [ ] `predictions.csv` has `id` and `prediction` columns
- [ ] Predictions cover all test rows, no nulls
- [ ] Class labels are spelled exactly right (lowercase)
- [ ] `submission_sheet.pdf` is filled completely
- [ ] All code is included and runnable
- [ ] PR title follows the format

### Late submissions?
No. The PR timestamp is the cutoff.

---
*SPEC2MODEL Challenge — GDGOC Silicon University*
