# Telecom Customer Value Analytics

A portfolio-ready telecom analytics project focused on customer value, churn risk, retention strategy, and stakeholder reporting.

## Executive Summary

This project builds a realistic end-to-end analytics workflow for a telecom business scenario:

- Understand which customer segments are most at risk of churn
- Measure customer value through ARPU, revenue contribution, and tenure
- Quantify the strongest churn drivers using behavioral and subscription signals
- Build presentation-ready outputs for business and leadership stakeholders

The project combines Python-based data engineering, SQL analytics, and dashboard-ready metrics into a single, reusable portfolio asset.

## Business Problem

Telecom businesses often lose revenue through preventable churn. Customers with weak engagement, support burden, delayed payments, or low tenure are more likely to churn and create downstream cost and retention issues.

This analysis targets the core business questions:

- Which customer groups are most vulnerable to churn?
- What revenue and retention trade-offs exist by plan type and region?
- Which signals best predict churn before it happens?
- What actions should a retention team prioritize first?

## Key Results

| Metric | Value |
|---|---:|
| Total Customers | 12,000 |
| Churn Rate | 31.6% |
| ARPU | $31.07 |
| Average Tenure | 36.77 months |
| Highest-Risk Segment | At-Risk group |
| Revenue Leverage | Strongest in high-value cohorts |

## Where the Project Adds Value

This project demonstrates a practical, business-facing analytics workflow:

- Customer segmentation and value profiling
- Churn-risk detection using practical operational metrics
- SQL-driven KPI and business logic
- Visual storytelling for leadership and retention teams
- Reproducible code and testing for portfolio credibility

## Analytics Workflow

```text
Generate data -> Clean & transform -> Engineer features -> Segment customers -> Analyze KPIs -> Visualize -> SQL reporting
```

## Project Structure

```text
Telecom-Customer-Value-Analytics/
├── data/
│   ├── raw/
│   └── processed/
├── dashboard/
│   ├── dashboard_spec.md
│   └── POWERBI_BLUEPRINT.md
├── docs/
│   ├── case_study.md
│   └── data_dictionary.md
├── notebooks/
│   └── 01_exploratory_notes.md
├── results/
│   ├── churn_drivers.csv
│   ├── kpi_summary.csv
│   ├── segment_performance.csv
│   └── figures/
├── sql/
│   ├── 01_schema.sql
│   ├── 02_load_and_views.sql
│   └── 03_analytics_queries.sql
├── src/
│   ├── analysis.py
│   ├── etl.py
│   ├── generate_data.py
│   ├── run_pipeline.py
│   ├── visualize.py
│   └── __init__.py
├── tests/
│   └── test_metrics.py
├── LICENSE
├── README.md
├── requirements.txt
├── .gitignore
└── telecom_customers_processed.csv
```

## Tech Stack

- Python: pandas, numpy, matplotlib, seaborn
- SQL: SQLite / DuckDB-compatible analytical queries
- Testing: pytest
- Dashboarding: Power BI-ready business model and visuals

## Quick Start

### 1. Create a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the pipeline

```bash
python src/run_pipeline.py
```

### 4. Run tests

```bash
pytest -q
```

## Visual Storytelling

### Churn by Plan Type

![Churn by plan type](results/figures/01_churn_by_plan.png)

### ARPU by Region

![ARPU by region](results/figures/02_arpu_by_region.png)

### Risk Segmentation

![Risk segmentation](results/figures/03_risk_band_churn.png)

## Key Business Findings

- Payment delays and support burden are strongly associated with churn risk
- Newer and lower-tenure customers appear more exposed to churn
- Prepaid and lower-value segments show elevated churn intensity
- High-value cohorts remain a major retention opportunity if targeted correctly
- Revenue pressure is concentrated in specific plan-region combinations

## Churn Drivers Snapshot

| Driver | Interpretation |
|---|---|
| Support tickets | Higher service burden correlates with churn likelihood |
| Payment delay days | Strong signal of financial stress and risk |
| Tenure | Lower tenure customers churn more often |
| Plan type | Lower-value plans exhibit a higher churn profile |
| Region | Segment performance varies meaningfully by geography |

## Deliverables

This repository includes:

- Reproducible customer data generation pipeline
- ETL and transformation logic
- KPI and segment analysis
- SQL schema, views, and analytics queries
- Chart exports for stakeholder reporting
- Power BI dashboard blueprint for business presentation
- Test suite for core logic validation

## Portfolio Value

This project is useful for data analyst and business analyst interviews because it demonstrates:

- Realistic problem framing
- Structured analytical thinking
- Data cleaning and transformation skills
- Business interpretation of technical findings
- Communication with visual outputs
- End-to-end project ownership from data to decision support

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
