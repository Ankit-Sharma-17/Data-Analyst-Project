-- 1) Highest churn risk segments
SELECT
    plan_type,
    acquisition_channel,
    region,
    COUNT(*) AS customers,
    ROUND(AVG(churned) * 100, 2) AS churn_rate_pct,
    ROUND(AVG(monthly_revenue), 2) AS arpu
FROM telecom_customers
GROUP BY plan_type, acquisition_channel, region
HAVING COUNT(*) >= 100
ORDER BY churn_rate_pct DESC, arpu DESC
LIMIT 20;

-- 2) Value concentration by segment
WITH segment_rev AS (
    SELECT value_segment, SUM(monthly_revenue) AS rev
    FROM telecom_customers
    GROUP BY value_segment
), totals AS (
    SELECT SUM(rev) AS total_rev FROM segment_rev
)
SELECT
    s.value_segment,
    ROUND(s.rev, 2) AS segment_revenue,
    ROUND((s.rev / t.total_rev) * 100, 2) AS revenue_share_pct
FROM segment_rev s
CROSS JOIN totals t
ORDER BY segment_revenue DESC;

-- 3) Churn driver comparison
SELECT
    churned,
    ROUND(AVG(payment_delay_days), 2) AS avg_delay_days,
    ROUND(AVG(support_tickets_90d), 2) AS avg_tickets,
    ROUND(AVG(tenure_months), 2) AS avg_tenure,
    ROUND(AVG(monthly_usage_gb), 2) AS avg_usage_gb
FROM telecom_customers
GROUP BY churned;

-- 4) Region x risk board for action prioritization
SELECT
    region,
    risk_band,
    COUNT(*) AS customers,
    ROUND(AVG(churned) * 100, 2) AS churn_rate_pct
FROM telecom_customers
GROUP BY region, risk_band
ORDER BY churn_rate_pct DESC, customers DESC;
