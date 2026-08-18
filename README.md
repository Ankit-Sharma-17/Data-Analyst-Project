# Telecom Customer Value Analytics

<p align="center">
  End-to-end telecom churn and customer value analytics project focused on actionable retention strategy.
</p>

<p align="center">
  <strong>Data Analyst Portfolio Project</strong> | <strong>Business Analyst Case Study</strong> | <strong>SQL Analyst Workflow</strong>
</p>

<p align="center">
  <a href="results/kpi_summary.csv"><img alt="KPI Output" src="https://img.shields.io/badge/KPI%20Output-CSV-1f6feb"></a>
  <a href="sql/03_analytics_queries.sql"><img alt="SQL Layer" src="https://img.shields.io/badge/SQL-Analytics%20Queries-0e8a16"></a>
  <a href="tests/test_metrics.py"><img alt="Tests" src="https://img.shields.io/badge/Tested-pytest-6f42c1"></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/License-MIT-f59e0b"></a>
</p>

## Executive Snapshot

Telecom providers often lose margin from preventable churn. This project builds a realistic analytics pipeline that identifies risk drivers, segments customer value, and translates findings into campaign-ready business actions.

| Metric | Value |
|---|---:|
| Total Customers | 12,000 |
| Churn Rate | 31.6% |
| ARPU | $31.07 |
| Average Tenure | 36.77 months |

Top drivers of churn: support tickets, payment delay, tenure, and plan type.

## Visual Storytelling

<table>
  <tr>
    <td align="center"><strong>Churn by Plan Type</strong><br><img src="results/figures/01_churn_by_plan.png" alt="Churn by plan type" width="430" /></td>
    <td align="center"><strong>ARPU by Region</strong><br><img src="results/figures/02_arpu_by_region.png" alt="ARPU by region" width="430" /></td>
  </tr>
  <tr>
    <td align="center" colspan="2"><strong>Observed Churn by Risk Band</strong><br><img src="results/figures/03_risk_band_churn.png" alt="Observed churn by risk band" width="860" /></td>
  </tr>
</table>

## Business Insights

- Customers with delayed payments and higher support burden churn more frequently.
- Lower-tenure cohorts are materially more vulnerable to early churn.
- Prepaid and lower-value plans show higher risk concentration.
- High-value customers are the strongest retention ROI opportunity.
- Region-specific variance supports targeted campaign design.

## Project Pipeline

```text
Generate synthetic telecom data -> Clean and transform -> Engineer risk/value features -> Segment customers -> Compute KPIs -> Build charts -> Run SQL analytics views
```

## Repository Structure

- src: data generation, ETL, analysis, pipeline orchestration, visualization
- sql: schema setup, load scripts, analytical query layer
- results: KPI outputs, segment outputs, churn driver exports, chart assets
- dashboard: Power BI blueprint and specification notes
- docs: case study narrative and data dictionary
- tests: validation for KPI and transformation logic

## Technology Stack

- Python: pandas, numpy, matplotlib, seaborn
- SQL: schema, views, analytics queries
- Testing: pytest
- BI Design: Power BI-ready dashboard specification

## Quick Start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src/run_pipeline.py
python src/visualize.py
pytest -q
```

## Portfolio Relevance

This project demonstrates end-to-end analyst capability across data preparation, KPI design, business framing, SQL reporting, and stakeholder-facing storytelling.

Role keywords: Data Analyst, Business Analyst, SQL Analyst, Product Analytics, Churn Analysis, Customer Segmentation, Retention Analytics.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
