# Dashboard Specification

## Recommended Tool

Power BI or Tableau

## Data Sources

- `data/processed/telecom_customers_processed.csv`
- `results/kpi_summary.csv`
- `results/segment_performance.csv`
- `results/churn_drivers.csv`

## Dashboard Pages

### 1) Executive Overview

- KPI cards: Total Customers, Churn Rate, ARPU, Avg Tenure
- Bar: Churn Rate by Plan Type
- Bar: ARPU by Region
- Slicer: Plan Type, Region, Risk Band

### 2) Segment Diagnostics

- Matrix: Plan Type x Region with churn and ARPU
- Scatter: Avg Revenue vs Churn Rate by Segment
- Top table: Highest-risk segments (customer count threshold)

### 3) Driver Analysis

- Comparison bars: churned vs non-churned averages
- Risk band waterfall: customer count and churn contribution
- Action table: recommended intervention by segment

## Suggested DAX / Metrics

- Churn Rate % = DIVIDE(SUM(churned), COUNT(customer_id), 0)
- ARPU = AVERAGE(monthly_revenue)
- High Risk Customers = CALCULATE(COUNT(customer_id), risk_band IN {"Elevated","Critical"})

## Design Notes

- Primary color: #0F766E
- Accent color: #F59E0B
- Risk color: #DC2626
- Background: #F8FAFC
