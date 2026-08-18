-- SQLite / DuckDB compatible schema

DROP TABLE IF EXISTS telecom_customers;

CREATE TABLE telecom_customers (
    customer_id BIGINT PRIMARY KEY,
    plan_type TEXT,
    region TEXT,
    acquisition_channel TEXT,
    tenure_months INTEGER,
    monthly_fee DOUBLE,
    monthly_usage_gb DOUBLE,
    support_tickets_90d INTEGER,
    payment_delay_days INTEGER,
    monthly_revenue DOUBLE,
    churned INTEGER,
    usage_segment TEXT,
    value_segment TEXT,
    risk_band TEXT
);
