# Data Dictionary

## Source

The dataset is synthetically generated for portfolio use and reproducibility.

## Core Columns

| Column | Type | Description |
|---|---|---|
| customer_id | int | Unique customer identifier |
| plan_type | text | Subscription family (Prepaid/Postpaid/Family/Business) |
| region | text | Customer geographic region |
| acquisition_channel | text | Primary onboarding channel |
| tenure_months | int | Customer age in months |
| monthly_fee | float | Base monthly subscription fee |
| monthly_usage_gb | float | Approx monthly data usage |
| support_tickets_90d | int | Customer support contacts in last 90 days |
| payment_delay_days | int | Days delayed in typical payment cycle |
| monthly_revenue | float | Estimated realized monthly revenue |
| churned | int | 1 = churned, 0 = retained |

## Derived Columns

| Column | Type | Description |
|---|---|---|
| usage_segment | text | Usage tier from monthly_usage_gb |
| value_segment | text | Revenue tier from monthly_revenue |
| risk_band | text | Operational risk bucket from delay + ticket behavior |

## Data Quality Rules

- Remove duplicate `customer_id`
- Enforce positive revenue and fee
- Enforce non-negative usage
- Enforce tenure >= 1
