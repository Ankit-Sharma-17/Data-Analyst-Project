# Power BI Dashboard Blueprint - Telecom Customer Value Analytics

## Overview
This document specifies a professional Power BI dashboard for stakeholder reporting on telecom customer churn, value, and segmentation insights.

---

## Dashboard Architecture

### Pages
1. **Executive Summary** - KPI overview & key metrics
2. **Churn Analysis** - Churn drivers, risk segments, trends
3. **Customer Segments** - Value, risk, and lifecycle profiles
4. **Operational Metrics** - Support, payment, usage trends

---

## Page 1: Executive Summary

### Layout: 2x3 Grid (Top Section)

#### Card Visuals (Top Row)

| Visual | Measure | Format | Target/Benchmark |
|--------|---------|--------|------------------|
| **Total Customers** | COUNT(customer_id) | 12,000 | Baseline |
| **Churn Rate %** | DIVIDE([Churned Count], [Total Customers]) * 100 | 31.6% | <25% Target |
| **ARPU** | AVERAGE(monthly_fee) | $31.07 | >$30 |

#### Line Chart (Middle Row - Full Width)
- **Title:** Monthly Churn Rate Trend
- **X-Axis:** Month (time-based grouping)
- **Y-Axis:** % Churn Rate
- **Series:** Churn Rate by Plan Type (color-coded)
- **Target Line:** 25% benchmark (red dashed)

#### Gauge Charts (Bottom Row)

| Visual | Measure | Min | Target | Max | Color |
|--------|---------|-----|--------|-----|-------|
| **ARPU Health** | AVG(monthly_fee) | $15 | $30 | $60 | Green/Red |
| **Avg Tenure (months)** | AVG(tenure_months) | 0 | 36 | 72 | Blue/Orange |
| **Revenue at Risk %** | SUM(monthly_fee * churn_risk) / SUM(monthly_fee) * 100 | 0% | 20% | 50% | Red |

---

## Page 2: Churn Analysis

### Layout: Top + 2x2 Grid

#### Stacked Bar Chart (Top - Full Width)
- **Title:** Churn Count & Rate by Plan Type
- **X-Axis:** Plan (Prepaid, Postpaid, Family, Business)
- **Y-Axis (Left):** Count (stacked bar: Churned / Active)
- **Y-Axis (Right):** Churn Rate % (line)
- **Drill-Down:** Click plan → shows region breakdown

#### Matrix Table (Bottom-Left)
- **Title:** Churn Drivers Summary
- **Rows:** Factor (Payment Delay Days, Support Tickets 90d, Tenure Months, Channel)
- **Columns:** Churn Rate, Avg Value, Count
- **Conditional Formatting:** Heat map (red = high churn impact)
- **Sorting:** By churn impact descending

#### Scatter Plot (Bottom-Right)
- **Title:** Risk vs. Value Segmentation
- **X-Axis:** Tenure (months)
- **Y-Axis:** Monthly Fee ($)
- **Bubble Size:** Churn Risk Score
- **Color:** Segment (Value, At-Risk, Churned)
- **Tooltip:** Customer ID, Tenure, Fee, Churn Probability

---

## Page 3: Customer Segments

### Layout: 3-Column Segment Cards + Comparison

#### Segment Profile Cards (Top - 3 Cards)

**Card 1: HIGH VALUE SEGMENT**
```
Count: 2,400 (20%)
Avg Monthly Fee: $48.50
Churn Rate: 18%
Avg Tenure: 42 months
Top Actions: Loyalty Program, VIP Support
```

**Card 2: GROWTH SEGMENT**
```
Count: 4,200 (35%)
Avg Monthly Fee: $28.00
Churn Rate: 31%
Avg Tenure: 24 months
Top Actions: Upgrade Incentives, Education
```

**Card 3: AT-RISK SEGMENT**
```
Count: 5,400 (45%)
Avg Monthly Fee: $22.00
Churn Rate: 42%
Avg Tenure: 12 months
Top Actions: Win-Back Campaigns, Root Cause Fix
```

#### Segment Performance Comparison Table (Bottom - Full Width)
- **Rows:** Segment
- **Columns:** Count, % of Base, Avg Fee, Churn %, Churned Count, Revenue Impact, Recommended Action
- **Drill-Through:** Click segment → detailed customer list page

---

## Page 4: Operational Metrics

### Layout: 2x2 Grid

#### Line Chart (Top-Left)
- **Title:** Average Support Tickets (90-day rolling)
- **X-Axis:** Month
- **Y-Axis:** Avg Tickets per Customer
- **Series:** By Plan Type
- **Target Line:** 1.2 (baseline)

#### Column Chart (Top-Right)
- **Title:** Payment Delay Distribution
- **X-Axis:** Delay Days (0-3, 4-7, 8-15, 15+)
- **Y-Axis:** Count of Customers
- **Color:** Severity (Green → Red)

#### Line Chart (Bottom-Left)
- **Title:** Average Monthly Usage (GB)
- **X-Axis:** Month
- **Y-Axis:** Avg GB
- **Series:** By Plan Type
- **Benchmark:** Included capacity lines

#### KPI Scorecard (Bottom-Right)
```
OPERATIONAL HEALTH SCORE

Payment Health:           82% ✓
Support Satisfaction:     76% ⚠
Usage Efficiency:         88% ✓
Retention Readiness:      64% ✗

Overall: 77.5% (Good)
Trend: ↑ +2.1% MoM
```

---

## Data Model & Measures

### Source Table: telecom_customers (from processed CSV or real dataset)

```
Columns:
- customer_id (PK)
- plan (Prepaid, Postpaid, Family, Business)
- region (North, South, East, West, Central)
- channel (App, Store, Web, Partner)
- tenure_months (0-120)
- monthly_fee (8-120 USD)
- total_revenue (sum of all charges)
- support_tickets_90d (count)
- payment_delay_days (days)
- usage_gb (monthly average)
- churn_risk_score (0-1)
- churned (0/1 binary)
```

### DAX Measures

#### KPI Measures
```DAX
[Total Customers] = COUNTROWS('telecom_customers')
[Churned Count] = CALCULATE(COUNTROWS('telecom_customers'), 'telecom_customers'[churned] = 1)
[Churn Rate %] = DIVIDE([Churned Count], [Total Customers]) * 100
[ARPU] = AVERAGE('telecom_customers'[monthly_fee])
[Total Monthly Revenue] = SUM('telecom_customers'[monthly_fee])
[At-Risk Revenue] = SUMPRODUCT('telecom_customers'[monthly_fee], 'telecom_customers'[churn_risk_score])
```

#### Segment Measures
```DAX
[High Value Count] = CALCULATE([Total Customers], 'telecom_customers'[segment] = "High Value")
[Growth Count] = CALCULATE([Total Customers], 'telecom_customers'[segment] = "Growth")
[At-Risk Count] = CALCULATE([Total Customers], 'telecom_customers'[segment] = "At-Risk")

[High Value Churn %] = DIVIDE(
    CALCULATE([Churned Count], 'telecom_customers'[segment] = "High Value"),
    [High Value Count]) * 100
```

#### Trend Measures
```DAX
[Churn Rate MoM Change %] = 
    VAR CurrentMonth = [Churn Rate %]
    VAR PreviousMonth = CALCULATE([Churn Rate %], DATEADD('date'[date], -1, MONTH))
    RETURN DIVIDE(CurrentMonth - PreviousMonth, PreviousMonth) * 100

[Revenue at Risk %] = DIVIDE([At-Risk Revenue], [Total Monthly Revenue]) * 100
```

---

## Interactive Elements

### Slicers (Top of each page)
- **Date Range:** Month/Quarter (if time data available)
- **Plan Type:** Multi-select dropdown
- **Region:** Multi-select
- **Segment:** Multi-select

### Drill-Through Pages
- **Customer Detail:** Customer ID → full profile page (contract, usage, support history)
- **Segment Deep-Dive:** Segment → list of customers with export option

### Bookmarks
- **View:** Executive vs. Manager vs. Operations view (filters applied)
- **Drill-Down State:** Save expanded/collapsed states

---

## Color Scheme & Formatting

### Theme
- **Primary (Blue):** #0078D4 (Active, Growth)
- **Alert (Red):** #E81123 (Churn, At-Risk)
- **Success (Green):** #107C10 (Healthy, High Value)
- **Neutral (Gray):** #5E5E5E (Baseline)

### Number Formatting
- **Currency:** $#,##0.00
- **Percentage:** 0.00%
- **Large Numbers:** #,##0 (with K/M suffix)
- **Decimals:** Limit to 2 places

---

## Implementation Steps

### Step 1: Load Data
1. In Power BI Desktop, select **Get Data** → **CSV**
2. Load `results/segment_performance.csv` as main table
3. Load `results/kpi_summary.csv` as KPI reference table
4. Create relationships: customer_id (PK-FK)

### Step 2: Create Calculated Columns
1. Add computed columns from generated data (churn_risk_score, segment)
2. Create time-based columns if date field exists

### Step 3: Build Measures
1. Paste DAX measures from above into Measure table
2. Test each measure with sample values

### Step 4: Create Visuals
1. Follow layout specifications for each page
2. Add slicers and enable drill-through
3. Apply color theme and formatting

### Step 5: Publish & Share
1. Save as .pbix in `dashboard/` folder
2. Publish to Power BI Service
3. Set up row-level security (RLS) if multi-tenant
4. Share dashboard link with stakeholders

---

## Export & Refresh

### Scheduled Refresh (Power BI Service)
- **Frequency:** Daily at 8 AM
- **Source:** `data/processed/telecom_customers_processed.csv`
- **Alert:** Send email if refresh fails

### Export to Stakeholders
- **Format:** PDF (static report) or link (interactive)
- **Frequency:** Weekly
- **Recipients:** VP Sales, Operations Manager, Churn Task Force

---

## Sample Dashboard Output
Once implemented, the dashboard provides:
- Real-time churn rate at a glance
- Segment-level drill-down capability
- Risk scoring for targeted retention
- Trend analysis for quarterly business review
- Export-ready visuals for presentations

This blueprint ensures a professional, stakeholder-ready analytics dashboard aligned with business objectives.
