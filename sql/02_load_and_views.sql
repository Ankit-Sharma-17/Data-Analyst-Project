-- DuckDB load command example:
-- COPY telecom_customers FROM 'data/processed/telecom_customers_processed.csv' (HEADER, DELIMITER ',');

DROP VIEW IF EXISTS vw_kpi_snapshot;
CREATE VIEW vw_kpi_snapshot AS
SELECT
    COUNT(DISTINCT customer_id) AS total_customers,
    ROUND(AVG(monthly_revenue), 2) AS arpu,
    ROUND(AVG(tenure_months), 2) AS avg_tenure_months,
    ROUND(AVG(churned) * 100, 2) AS churn_rate_pct
FROM telecom_customers;

DROP VIEW IF EXISTS vw_plan_risk_matrix;
CREATE VIEW vw_plan_risk_matrix AS
SELECT
    plan_type,
    risk_band,
    COUNT(*) AS customers,
    ROUND(AVG(monthly_revenue), 2) AS avg_revenue,
    ROUND(AVG(churned) * 100, 2) AS churn_rate_pct
FROM telecom_customers
GROUP BY plan_type, risk_band;
