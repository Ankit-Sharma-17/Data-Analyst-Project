from pathlib import Path

from src.analysis import load_processed, kpi_summary
from src.etl import transform
from src.generate_data import DataConfig, build_customer_table


def test_kpi_summary_rows() -> None:
    raw = build_customer_table(DataConfig(n_customers=200, random_seed=7))
    cleaned = transform(raw)
    summary = kpi_summary(cleaned)
    assert set(summary["metric"]) == {"total_customers", "churn_rate", "arpu", "avg_tenure_months"}


def test_transform_adds_segments() -> None:
    raw = build_customer_table(DataConfig(n_customers=50, random_seed=11))
    cleaned = transform(raw)
    assert "usage_segment" in cleaned.columns
    assert "value_segment" in cleaned.columns
    assert "risk_band" in cleaned.columns


def test_processed_file_exists_after_pipeline_shape() -> None:
    root = Path(__file__).resolve().parents[1]
    sample = build_customer_table(DataConfig(n_customers=80, random_seed=2))
    cleaned = transform(sample)
    tmp = root / "data" / "processed" / "_test_temp_processed.csv"
    cleaned.to_csv(tmp, index=False)
    loaded = load_processed(tmp)
    assert loaded.shape[0] == cleaned.shape[0]
    tmp.unlink(missing_ok=True)
