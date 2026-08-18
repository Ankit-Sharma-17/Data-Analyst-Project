from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_theme(style="whitegrid", context="talk")


BG_COLOR = "#0b1220"
PANEL_COLOR = "#121a2b"
GRID_COLOR = "#334155"
TEXT_COLOR = "#e2e8f0"


def setup_plot_style() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": BG_COLOR,
            "axes.facecolor": PANEL_COLOR,
            "axes.edgecolor": GRID_COLOR,
            "axes.labelcolor": TEXT_COLOR,
            "xtick.color": TEXT_COLOR,
            "ytick.color": TEXT_COLOR,
            "text.color": TEXT_COLOR,
            "axes.titleweight": "bold",
            "axes.titlepad": 14,
            "grid.color": GRID_COLOR,
            "grid.alpha": 0.4,
            "savefig.facecolor": BG_COLOR,
            "savefig.edgecolor": BG_COLOR,
        }
    )


def style_axis(ax: plt.Axes, y_as_percent: bool = False) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(GRID_COLOR)
    ax.spines["bottom"].set_color(GRID_COLOR)
    ax.grid(axis="y", linestyle="--", linewidth=0.8)
    ax.set_axisbelow(True)

    if y_as_percent:
        ymin, ymax = ax.get_ylim()
        ax.set_ylim(ymin, min(max(ymax, 0.35), 1.0))
        ax.yaxis.set_major_formatter(lambda x, _: f"{x * 100:.0f}%")


def add_bar_labels(ax: plt.Axes, suffix: str = "") -> None:
    for container in ax.containers:
        labels = []
        for bar in container:
            value = bar.get_height()
            labels.append(f"{value:.1%}" if suffix == "%" else f"${value:,.2f}")
        ax.bar_label(container, labels=labels, padding=4, color=TEXT_COLOR, fontsize=10)


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def churn_by_plan(df: pd.DataFrame, out_dir: Path) -> None:
    chart = (
        df.groupby("plan_type", as_index=False)["churned"]
        .mean()
        .sort_values("churned", ascending=False)
    )

    fig, ax = plt.subplots(figsize=(11, 6.5))
    sns.barplot(data=chart, x="plan_type", y="churned", hue="plan_type", palette="crest", legend=False, ax=ax)
    ax.set_title("Churn Rate by Plan Type")
    ax.set_xlabel("Plan Type")
    ax.set_ylabel("Churn Rate")
    style_axis(ax, y_as_percent=True)
    add_bar_labels(ax, suffix="%")
    plt.tight_layout()
    plt.savefig(out_dir / "01_churn_by_plan.png", dpi=180)
    plt.close()


def arpu_by_region(df: pd.DataFrame, out_dir: Path) -> None:
    chart = (
        df.groupby("region", as_index=False)["monthly_revenue"]
        .mean()
        .sort_values("monthly_revenue", ascending=False)
    )

    fig, ax = plt.subplots(figsize=(11, 6.5))
    sns.barplot(data=chart, x="region", y="monthly_revenue", hue="region", palette="mako", legend=False, ax=ax)
    ax.set_title("Average Revenue Per User by Region")
    ax.set_xlabel("Region")
    ax.set_ylabel("ARPU (USD)")
    style_axis(ax)
    add_bar_labels(ax)
    plt.tight_layout()
    plt.savefig(out_dir / "02_arpu_by_region.png", dpi=180)
    plt.close()


def risk_vs_churn(df: pd.DataFrame, out_dir: Path) -> None:
    risk_order = ["Low", "Medium", "High"]
    ordered_df = df.copy()
    ordered_df["risk_band"] = pd.Categorical(ordered_df["risk_band"], categories=risk_order, ordered=True)

    chart = (
        ordered_df.groupby("risk_band", as_index=False, observed=False)["churned"]
        .mean()
        .dropna(subset=["churned"])
        .sort_values("risk_band")
    )
    chart["risk_band"] = chart["risk_band"].astype(str)
    present_risk_order = chart["risk_band"].tolist()

    fig, ax = plt.subplots(figsize=(11, 6.5))
    sns.barplot(
        data=chart,
        x="risk_band",
        y="churned",
        hue="risk_band",
        order=present_risk_order,
        palette="rocket",
        legend=False,
        ax=ax,
    )
    ax.set_title("Observed Churn by Risk Band")
    ax.set_xlabel("Risk Band")
    ax.set_ylabel("Churn Rate")
    style_axis(ax, y_as_percent=True)
    add_bar_labels(ax, suffix="%")
    plt.tight_layout()
    plt.savefig(out_dir / "03_risk_band_churn.png", dpi=180)
    plt.close()


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    source = root / "data" / "processed" / "telecom_customers_processed.csv"
    out_dir = root / "results" / "figures"
    ensure_dir(out_dir)
    setup_plot_style()

    df = pd.read_csv(source)
    churn_by_plan(df, out_dir)
    arpu_by_region(df, out_dir)
    risk_vs_churn(df, out_dir)

    print(f"Saved charts in: {out_dir}")


if __name__ == "__main__":
    main()
