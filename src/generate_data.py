from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd


@dataclass
class DataConfig:
    n_customers: int = 12000
    random_seed: int = 42


def _choice(rng: np.random.Generator, values: list[str], p: list[float], size: int) -> np.ndarray:
    return rng.choice(values, p=p, size=size)


def build_customer_table(cfg: DataConfig) -> pd.DataFrame:
    rng = np.random.default_rng(cfg.random_seed)
    customer_ids = np.arange(100000, 100000 + cfg.n_customers)

    plan = _choice(rng, ["Prepaid", "Postpaid", "Family", "Business"], [0.34, 0.38, 0.2, 0.08], cfg.n_customers)
    region = _choice(rng, ["North", "South", "East", "West", "Central"], [0.2, 0.21, 0.18, 0.25, 0.16], cfg.n_customers)
    channel = _choice(rng, ["App", "Store", "Web", "Partner"], [0.44, 0.2, 0.24, 0.12], cfg.n_customers)
    tenure = rng.integers(1, 73, size=cfg.n_customers)

    monthly_fee = np.where(
        plan == "Business", rng.normal(54, 8, cfg.n_customers),
        np.where(plan == "Family", rng.normal(38, 7, cfg.n_customers),
                 np.where(plan == "Postpaid", rng.normal(30, 6, cfg.n_customers), rng.normal(18, 5, cfg.n_customers)))
    ).clip(8, 120)

    monthly_usage_gb = np.where(
        plan == "Business", rng.normal(26, 9, cfg.n_customers),
        np.where(plan == "Family", rng.normal(19, 8, cfg.n_customers),
                 np.where(plan == "Postpaid", rng.normal(14, 7, cfg.n_customers), rng.normal(8, 4, cfg.n_customers)))
    ).clip(0.2, 120)

    support_tickets_90d = rng.poisson(lam=1.2, size=cfg.n_customers)
    payment_delay_days = rng.poisson(lam=2.7, size=cfg.n_customers)

    risk_score = (
        0.012 * payment_delay_days
        + 0.11 * support_tickets_90d
        - 0.004 * tenure
        + np.where(plan == "Prepaid", 0.19, 0)
        + np.where(channel == "Partner", 0.08, 0)
        + rng.normal(0, 0.06, cfg.n_customers)
    )
    churn_probability = 1 / (1 + np.exp(-(risk_score - 0.35) * 3.3))
    churned = rng.binomial(1, churn_probability)

    monthly_revenue = (monthly_fee + np.maximum(monthly_usage_gb - 12, 0) * 0.42).round(2)

    df = pd.DataFrame(
        {
            "customer_id": customer_ids,
            "plan_type": plan,
            "region": region,
            "acquisition_channel": channel,
            "tenure_months": tenure,
            "monthly_fee": monthly_fee.round(2),
            "monthly_usage_gb": monthly_usage_gb.round(2),
            "support_tickets_90d": support_tickets_90d,
            "payment_delay_days": payment_delay_days,
            "monthly_revenue": monthly_revenue,
            "churned": churned,
        }
    )
    return df


def save_raw(df: pd.DataFrame, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    out = output_dir / "telecom_customers_raw.csv"
    df.to_csv(out, index=False)
    return out


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    raw_path = root / "data" / "raw"

    df = build_customer_table(DataConfig())
    file_path = save_raw(df, raw_path)
    print(f"Generated raw dataset: {file_path}")
    print(f"Rows: {len(df):,} | Columns: {df.shape[1]}")


if __name__ == "__main__":
    main()
