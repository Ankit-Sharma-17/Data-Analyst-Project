from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_processed(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def kpi_summary(df: pd.DataFrame) -> pd.DataFrame:
    total_customers = int(df["customer_id"].nunique())
    churn_rate = float(df["churned"].mean())
    arpu = float(df["monthly_revenue"].mean())
    avg_tenure = float(df["tenure_months"].mean())

    return pd.DataFrame(
        {
            "metric": ["total_customers", "churn_rate", "arpu", "avg_tenure_months"],
            "value": [total_customers, round(churn_rate, 4), round(arpu, 2), round(avg_tenure, 2)],
        }
    )


def segment_performance(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby(["plan_type", "region", "value_segment"], as_index=False)
        .agg(
            customers=("customer_id", "nunique"),
            avg_revenue=("monthly_revenue", "mean"),
            churn_rate=("churned", "mean"),
            avg_usage_gb=("monthly_usage_gb", "mean"),
        )
        .sort_values(["churn_rate", "avg_revenue"], ascending=[False, False])
    )
    summary["avg_revenue"] = summary["avg_revenue"].round(2)
    summary["churn_rate"] = summary["churn_rate"].round(4)
    summary["avg_usage_gb"] = summary["avg_usage_gb"].round(2)
    return summary


def churn_driver_table(df: pd.DataFrame) -> pd.DataFrame:
    features = [
        "tenure_months",
        "monthly_fee",
        "monthly_usage_gb",
        "support_tickets_90d",
        "payment_delay_days",
    ]
    grouped = df.groupby("churned")[features].mean().T.reset_index()
    grouped.columns = ["feature", "non_churn_avg", "churn_avg"]
    grouped["delta_churn_minus_non_churn"] = (grouped["churn_avg"] - grouped["non_churn_avg"]).round(2)
    return grouped.sort_values("delta_churn_minus_non_churn", ascending=False)


def save_outputs(df: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    kpi_summary(df).to_csv(output_dir / "kpi_summary.csv", index=False)
    segment_performance(df).to_csv(output_dir / "segment_performance.csv", index=False)
    churn_driver_table(df).to_csv(output_dir / "churn_drivers.csv", index=False)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    data_path = root / "data" / "processed" / "telecom_customers_processed.csv"
    output_dir = root / "results"

    df = load_processed(data_path)
    save_outputs(df, output_dir)
    print("Saved KPI and analytics tables to results/.")


if __name__ == "__main__":
    main()
