# Problem A — Will This Delivery Arrive Late?

## Overview

You work for a food delivery platform. Every order has an **estimated delivery time**. Sometimes, due to weather, traffic, restaurant delays, or other factors, the order arrives **after** the estimated time.

**Your task:** Given features about an order, predict whether it will arrive **late** or **on time**.

## Target Variable

| Column | Type | Values |
|--------|------|--------|
| `is_late` | string | `late` or `on_time` |

- `late` — the order arrived after the estimated delivery time
- `on_time` — the order arrived at or before the estimated delivery time

## Evaluation Metric

**Macro F1 Score**

Macro F1 averages the F1 score across both classes equally. This means your model must perform well on BOTH `late` and `on_time` predictions — not just the majority class.

## Feature Schema

Your training data, dummy test data, and final test data will all follow this exact schema. Every column name, data type, and allowed value is defined below. There are no other columns.

| # | Column Name | Type | Allowed Values / Range | Description |
|---|-------------|------|----------------------|-------------|
| 1 | `id` | integer | 1+ | Unique row identifier |
| 2 | `order_hour` | integer | 0–23 | Hour of day the order was placed (24hr format) |
| 3 | `day_of_week` | string | `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`, `sunday` | Day the order was placed |
| 4 | `restaurant_type` | string | `fast_food`, `casual_dining`, `cafe`, `cloud_kitchen`, `fine_dining` | Type of restaurant |
| 5 | `cuisine_type` | string | `indian`, `chinese`, `italian`, `south_indian`, `biryani`, `pizza_burger`, `dessert`, `healthy`, `other` | Cuisine category |
| 6 | `distance_km` | float | 0.5–15.0 | Distance from restaurant to delivery address in km |
| 7 | `estimated_delivery_min` | integer | 10–90 | Estimated delivery time shown to customer in minutes |
| 8 | `order_value_inr` | float | 99.0–3000.0 | Total order value in INR |
| 9 | `num_items` | integer | 1–15 | Number of items in the order |
| 10 | `is_peak_hour` | boolean | `true`, `false` | Whether the order was placed during peak hours |
| 11 | `weather_condition` | string | `clear`, `light_rain`, `heavy_rain`, `fog`, `hot`, `humid` | Weather at time of order |
| 12 | `traffic_density` | string | `low`, `moderate`, `heavy`, `gridlock` | Traffic conditions in the delivery area |
| 13 | `delivery_partner_rating` | float | 1.0–5.0 | Delivery partner's historical rating |
| 14 | `delivery_partner_orders` | integer | 1–5000 | Delivery partner's total lifetime completed orders |
| 15 | `restaurant_rating` | float | 1.0–5.0 | Restaurant's average rating |
| 16 | `restaurant_avg_prep_min` | float | 5.0–60.0 | Restaurant's historical average food preparation time in minutes |
| 17 | `is_promo_order` | boolean | `true`, `false` | Whether a promo code / discount was applied |
| 18 | `area_type` | string | `college_area`, `residential`, `commercial`, `market`, `highway` | Type of area the delivery address is in |

**Total: 17 features + 1 id + 1 target = 19 columns in training data, 18 columns in test data (no target)**

## Submission Format

Your `predictions.csv` must have exactly two columns:

```csv
id,prediction
1,late
2,on_time
3,late
4,on_time
...
```

- Column names must be exactly `id` and `prediction`
- Prediction values must be exactly `late` or `on_time` (lowercase, no spaces)
- Every `id` from the test set must be present
- No missing values allowed
- No extra columns

## What You Get

| File | When | Labels? | Purpose |
|------|------|---------|---------|
| `dummy_test.csv` | 12 hrs before event | Yes | Explore the schema, test your pipeline |
| `train.csv` | Event start (T+0:00) | Yes | Train your model |
| `final_test_A.csv` | T+4:30 | No | Generate predictions, submit |

## Tips

- The training data is **not perfect**. Expect some missing values, noise, and class imbalance. Cleaning it well is part of the challenge.
- No single feature will solve this problem. The patterns involve **combinations** of features (e.g., heavy rain + gridlock + long distance = likely late).
- Split your training data into train/validation sets (e.g., 80/20) to check for overfitting before submitting.
- Use the dummy test data as a final sanity check — does your pipeline produce predictions in the right format?
- External data is allowed but optional. The test set follows the same distribution as the provided training data.

---

*SPEC2MODEL Challenge — Problem A — GDGOC Silicon University*
