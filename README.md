# Telecom Customer Value Analytics

A fully original, end-to-end analytics portfolio project for Data Analyst roles.

This project is inspired by the analytics workflow idea (clean -> analyze -> visualize -> dashboard) but uses a different business domain, different metrics, and different implementation: telecom customer value and churn analytics.

## Why This Project Matters

Telecom operators lose significant recurring revenue through preventable churn. This project builds a practical analytics pipeline to:

- Profile customer value segments
- Quantify churn risk patterns
- Identify action-ready segments for retention campaigns
- Provide SQL assets and dashboard-ready outputs

## Project Scope

- Domain: Telecom subscription analytics
- Grain: Customer-level monthly profile
- Core outcomes:
  - KPI snapshot (ARPU, churn rate, customer base health)
  - Segment performance table
  - Churn driver comparison
  - Visualization pack for stakeholder reporting

## Architecture

```
Telecom-Customer-Value-Analytics/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── generate_data.py
│   ├── etl.py
│   ├── analysis.py
│   ├── visualize.py
│   └── run_pipeline.py
├── sql/
│   ├── 01_schema.sql
│   ├── 02_load_and_views.sql
│   └── 03_analytics_queries.sql
├── dashboard/
│   └── dashboard_spec.md
├── docs/
│   ├── data_dictionary.md
│   └── case_study.md
├── notebooks/
│   └── 01_exploratory_notes.md
├── results/
│   ├── kpi_summary.csv
│   ├── segment_performance.csv
│   ├── churn_drivers.csv
│   └── figures/
├── tests/
│   └── test_metrics.py
├── requirements.txt
└── .gitignore
```

## Tech Stack

- Python: pandas, numpy, matplotlib, seaborn
- SQL: SQLite / DuckDB-compatible scripts
- Testing: pytest
- Dashboard layer: Power BI / Tableau-ready data model guide

## Quick Start

### 1) Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Run Pipeline

```bash
python src/run_pipeline.py
```

Pipeline outputs:
- `data/raw/telecom_customers_raw.csv`
- `data/processed/telecom_customers_processed.csv`
- `results/kpi_summary.csv`
- `results/segment_performance.csv`
- `results/churn_drivers.csv`
- `results/figures/*.png`

### 3) Run Tests

```bash
pytest -q
```

## Analytical Questions Answered

1. Which customer segments have the highest churn exposure?
2. Which plan-region combinations generate high ARPU but weak retention?
3. How strongly do support tickets and payment delays correlate with churn?
4. Which risk bands should retention teams prioritize first?

## Example KPI Definitions

- Churn Rate = churned customers / total customers
- ARPU = average monthly revenue per customer
- Revenue Share by Segment = segment revenue / total revenue

## Professional Portfolio Value

This project demonstrates:

- Production-style data pipeline structure
- Reproducible analytics workflow
- SQL and Python fluency
- Business translation of technical findings
- Hiring-ready documentation and test coverage

## License

MIT (see `LICENSE`)
