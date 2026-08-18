from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_theme(style="whitegrid", context="talk")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def churn_by_plan(df: pd.DataFrame, out_dir: Path) -> None:
    chart = (
        df.groupby("plan_type", as_index=False)["churned"]
        .mean()
        .sort_values("churned", ascending=False)
    )

    plt.figure(figsize=(10, 6))
    sns.barplot(data=chart, x="plan_type", y="churned", hue="plan_type", palette="crest", legend=False)
    plt.title("Churn Rate by Plan Type")
    plt.xlabel("Plan Type")
    plt.ylabel("Churn Rate")
    plt.tight_layout()
    plt.savefig(out_dir / "01_churn_by_plan.png", dpi=140)
    plt.close()


def arpu_by_region(df: pd.DataFrame, out_dir: Path) -> None:
    chart = (
        df.groupby("region", as_index=False)["monthly_revenue"]
        .mean()
        .sort_values("monthly_revenue", ascending=False)
    )

    plt.figure(figsize=(10, 6))
    sns.barplot(data=chart, x="region", y="monthly_revenue", hue="region", palette="mako", legend=False)
    plt.title("Average Revenue Per User by Region")
    plt.xlabel("Region")
    plt.ylabel("ARPU")
    plt.tight_layout()
    plt.savefig(out_dir / "02_arpu_by_region.png", dpi=140)
    plt.close()


def risk_vs_churn(df: pd.DataFrame, out_dir: Path) -> None:
    chart = (
        df.groupby("risk_band", as_index=False)["churned"]
        .mean()
        .sort_values("churned", ascending=False)
    )

    plt.figure(figsize=(10, 6))
    sns.barplot(data=chart, x="risk_band", y="churned", hue="risk_band", palette="flare", legend=False)
    plt.title("Observed Churn by Risk Band")
    plt.xlabel("Risk Band")
    plt.ylabel("Churn Rate")
    plt.tight_layout()
    plt.savefig(out_dir / "03_risk_band_churn.png", dpi=140)
    plt.close()


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    source = root / "data" / "processed" / "telecom_customers_processed.csv"
    out_dir = root / "results" / "figures"
    ensure_dir(out_dir)

    df = pd.read_csv(source)
    churn_by_plan(df, out_dir)
    arpu_by_region(df, out_dir)
    risk_vs_churn(df, out_dir)

    print(f"Saved charts in: {out_dir}")


if __name__ == "__main__":
    main()
