# Problem B — Why Did This User Cancel Their Subscription?

## Overview

You work for a subscription-based app. Users are cancelling. But knowing *that* they cancelled isn't enough — the product team needs to know **why**.

Every churned user left for one of four reasons. **Your task:** Given a user's behavior, account, and device data, predict the **reason** they cancelled.

## Target Variable

| Column | Type | Values |
|--------|------|--------|
| `churn_reason` | string | `price_sensitive`, `bad_experience`, `found_alternative`, `lost_interest` |

- `price_sensitive` — user left primarily due to cost (price increase, couldn't justify the spend, found it too expensive)
- `bad_experience` — user left due to app quality issues (crashes, bugs, poor support, slow performance)
- `found_alternative` — user switched to a competing app that better met their needs
- `lost_interest` — user gradually disengaged; no specific trigger, just stopped caring

**Why this is hard:** These reasons overlap. A user on a budget phone with frequent crashes who also installed a competitor — is that `bad_experience` or `found_alternative`? A user who experienced a price increase and also stopped logging in — is that `price_sensitive` or `lost_interest`? The boundaries are fuzzy by design. This is what makes real-world multiclass problems difficult.

## Evaluation Metric

**Macro F1 Score**

Macro F1 averages the F1 score across all four classes equally. Your model must perform reasonably on every class — not just the most common one. Predicting only the majority class will get a very low score.

## Feature Schema

Your training data, dummy test data, and final test data will all follow this exact schema. Every column name, data type, and allowed value is defined below. There are no other columns.

| # | Column Name | Type | Allowed Values / Range | Description |
|---|-------------|------|----------------------|-------------|
| 1 | `id` | integer | 1+ | Unique row identifier |
| 2 | `user_age_group` | string | `teen`, `young_adult`, `adult`, `middle_aged`, `senior` | User's age bracket |
| 3 | `gender` | string | `male`, `female`, `non_binary`, `undisclosed` | User's gender |
| 4 | `subscription_plan` | string | `free_trial`, `basic`, `standard`, `premium`, `student` | Plan at time of cancellation |
| 5 | `monthly_price_inr` | float | 0.0–999.0 | Monthly subscription cost in INR (0 for free trial) |
| 6 | `subscription_duration_days` | integer | 1–1825 | How long the user was subscribed before cancelling (up to 5 years) |
| 7 | `payment_method` | string | `upi`, `credit_card`, `debit_card`, `net_banking`, `wallet` | Payment method used |
| 8 | `num_payment_failures_90d` | integer | 0–15 | Number of failed payment attempts in last 90 days |
| 9 | `days_since_last_login` | integer | 0–365 | Days between last login and cancellation date |
| 10 | `avg_session_duration_min` | float | 0.0–180.0 | Average session length in minutes |
| 11 | `sessions_per_week` | float | 0.0–50.0 | Average sessions per week over subscription period |
| 12 | `session_trend_30d` | string | `increasing`, `stable`, `declining`, `inactive` | Trend in session activity over last 30 days |
| 13 | `features_used_pct` | float | 0.0–100.0 | Percentage of app features the user has ever used |
| 14 | `num_support_tickets_90d` | integer | 0–20 | Support tickets raised in last 90 days |
| 15 | `avg_ticket_resolution_hrs` | float | 0.0–720.0 | Average time to resolve a support ticket in hours (up to 30 days; 0.0 if no tickets) |
| 16 | `unresolved_tickets` | integer | 0–10 | Number of support tickets still open at cancellation |
| 17 | `app_crash_count_30d` | integer | 0–50 | Number of app crashes in the last 30 days |
| 18 | `rating_given` | float | 0.0–5.0 | Rating user gave the app on the store (0.0 = never rated) |
| 19 | `num_referrals_made` | integer | 0–20 | Number of friends the user referred to the app |
| 20 | `competitor_app_installed` | boolean | `true`, `false` | Whether a competing app was detected on the user's device |
| 21 | `price_increase_experienced` | boolean | `true`, `false` | Whether the user's price was increased during subscription |
| 22 | `used_discount_code` | boolean | `true`, `false` | Whether the user originally signed up using a discount or promo |
| 23 | `device_type` | string | `budget_android`, `mid_android`, `flagship_android`, `iphone`, `ipad`, `desktop`, `multi_device` | User's primary device |
| 24 | `os_version_age_months` | integer | 0–60 | How old the user's OS version is in months |
| 25 | `internet_speed_category` | string | `slow_2g`, `moderate_3g`, `fast_4g`, `ultra_5g`, `broadband` | User's typical internet speed |
| 26 | `onboarding_completed` | boolean | `true`, `false` | Whether the user completed the app's onboarding/tutorial |
| 27 | `content_category_preference` | string | `entertainment`, `education`, `productivity`, `fitness`, `news`, `social`, `mixed` | User's primary content category |
| 28 | `days_since_last_feature_use` | integer | 0–365 | Days since user last used a core app feature |
| 29 | `notification_opt_in` | boolean | `true`, `false` | Whether the user has push notifications enabled |

**Total: 28 features + 1 id + 1 target = 30 columns in training data, 29 columns in test data (no target)**

## Class Descriptions and Signal Patterns

These descriptions are hints, not rules. The real patterns are in the data.

**`price_sensitive`** — These users cared about cost. Look for signals around pricing, payment failures, discount usage, and subscription plan changes. But not every user who experienced a price increase left because of price — some had other reasons too.

**`bad_experience`** — These users had a frustrating time with the app. Look for signals around crashes, support tickets, unresolved issues, and device/connectivity problems. But some users with crashes left for other reasons (found a competitor that works better, or just lost interest entirely).

**`found_alternative`** — These users actively switched. Look for signals around competitor apps, declining engagement despite previously high usage, and abrupt behavior changes. But having a competitor app installed doesn't automatically mean that's why they left.

**`lost_interest`** — These users drifted away. No dramatic trigger — just gradual disengagement. Look for signals around low feature usage, long gaps since last login, no referrals, no ratings, and notification opt-out. But some disengaged users actually left for a specific reason they didn't bother reporting.

## Submission Format

Your `predictions.csv` must have exactly two columns:

```csv
id,prediction
1,price_sensitive
2,lost_interest
3,bad_experience
4,found_alternative
...
```

- Column names must be exactly `id` and `prediction`
- Prediction values must be exactly one of: `price_sensitive`, `bad_experience`, `found_alternative`, `lost_interest` (lowercase, underscores, no spaces)
- Every `id` from the test set must be present
- No missing values allowed
- No extra columns

## What You Get

| File | When | Labels? | Purpose |
|------|------|---------|---------|
| `dummy_test.csv` | 12 hrs before event | Yes | Explore the schema, test your pipeline |
| `train.csv` | Event start (T+0:00) | Yes | Train your model |
| `final_test_B.csv` | T+4:30 | No | Generate predictions, submit |

## Tips

- This is **harder than Problem A**. The four classes overlap by design. Don't expect very high F1 scores — a good score here is genuinely impressive.
- The training data has some missing values, noise in labels (~8-10% of rows have ambiguous labels), and imbalanced classes. Cleaning and handling imbalance matters a lot.
- **No single feature solves any class.** `competitor_app_installed = true` does NOT mean `found_alternative`. Many users across all classes share similar boolean flags. The signal is in feature **combinations**.
- Feature selection may help. Not all 28 features contribute equally. Figuring out which features matter is part of the challenge.
- Split your training data for validation. If your training accuracy is 95% but validation is 45%, you're overfitting.
- External data is allowed but optional. The test set follows the same distribution as the provided training data.

## Why This Problem Matters

In the real world, knowing *why* users leave is more valuable than knowing *that* they left. A company that knows 40% of churn is `bad_experience` can invest in app stability. A company that knows 30% is `price_sensitive` can rethink pricing. This problem mirrors real product analytics challenges where the classes are messy, the signals overlap, and perfect accuracy is impossible.

---

*SPEC2MODEL Challenge — Problem B — GDGOC Silicon University*
