from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


def load_raw(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()

    cleaned = cleaned.drop_duplicates(subset=["customer_id"])
    cleaned = cleaned[cleaned["monthly_fee"] > 0]
    cleaned = cleaned[cleaned["monthly_revenue"] > 0]
    cleaned = cleaned[cleaned["monthly_usage_gb"] >= 0]
    cleaned = cleaned[cleaned["tenure_months"] >= 1]

    cleaned["usage_segment"] = pd.cut(
        cleaned["monthly_usage_gb"],
        bins=[-np.inf, 5, 15, 35, np.inf],
        labels=["Light", "Moderate", "Heavy", "Power"],
    ).astype(str)

    cleaned["value_segment"] = pd.cut(
        cleaned["monthly_revenue"],
        bins=[-np.inf, 20, 35, 60, np.inf],
        labels=["Low", "Mid", "High", "VIP"],
    ).astype(str)

    cleaned["risk_band"] = pd.cut(
        cleaned["payment_delay_days"] + cleaned["support_tickets_90d"],
        bins=[-np.inf, 2, 5, 9, np.inf],
        labels=["Low", "Medium", "Elevated", "Critical"],
    ).astype(str)

    return cleaned


def save_processed(df: pd.DataFrame, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    output_path = out_dir / "telecom_customers_processed.csv"
    df.to_csv(output_path, index=False)
    return output_path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    raw_path = root / "data" / "raw" / "telecom_customers_raw.csv"
    out_dir = root / "data" / "processed"

    df = load_raw(raw_path)
    cleaned = transform(df)
    output = save_processed(cleaned, out_dir)

    print(f"Processed dataset saved: {output}")
    print(f"Rows: {len(cleaned):,} | Columns: {cleaned.shape[1]}")


if __name__ == "__main__":
    main()
