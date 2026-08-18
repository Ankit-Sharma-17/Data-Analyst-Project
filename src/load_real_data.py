"""
Real Telecom Dataset Loader
Supports loading from Kaggle, UCI, and other public sources
"""

from __future__ import annotations

from pathlib import Path
from typing import Literal

import pandas as pd
import requests


def load_kaggle_churn_dataset() -> pd.DataFrame:
    """
    Load IBM Telecom Customer Churn dataset from Kaggle.
    
    Dataset source: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
    
    Instructions:
    1. Install kaggle: pip install kaggle
    2. Download API key from https://www.kaggle.com/settings/account
    3. Place kaggle.json in ~/.kaggle/
    4. Run: kaggle datasets download -d blastchar/telco-customer-churn
    
    Returns:
        pd.DataFrame: Telecom churn dataset with columns:
            - customerID, gender, SeniorCitizen, Partner, Dependents
            - tenure, PhoneService, InternetService, OnlineSecurity
            - MonthlyCharges, TotalCharges, Churn
    """
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
        
        api = KaggleApi()
        api.authenticate()
        
        # Create temp directory
        temp_dir = Path("data/raw/kaggle_temp")
        temp_dir.mkdir(parents=True, exist_ok=True)
        
        # Download dataset
        api.dataset_download_files("blastchar/telco-customer-churn", path=temp_dir, unzip=True)
        
        # Load CSV
        csv_path = temp_dir / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
        df = pd.read_csv(csv_path)
        
        # Clean and standardize
        df = _standardize_kaggle_churn(df)
        
        return df
    
    except ImportError:
        raise ImportError(
            "Kaggle library not installed. Install with: pip install kaggle\n"
            "Then set up authentication at https://www.kaggle.com/settings/account"
        )
    except Exception as e:
        raise RuntimeError(f"Failed to load Kaggle dataset: {e}")


def load_uci_telecom_dataset() -> pd.DataFrame:
    """
    Load Telecom Customer Dataset from UCI Machine Learning Repository.
    
    Dataset source: https://archive.ics.uci.edu/ml/datasets/Telecom+Customer+Churn
    
    Returns:
        pd.DataFrame: Standardized telecom dataset
    """
    url = (
        "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/"
        "master/data/Telecom-Customer-Churn.csv"
    )
    
    try:
        df = pd.read_csv(url)
        df = _standardize_kaggle_churn(df)
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to load UCI dataset: {e}")


def load_custom_csv(file_path: str | Path) -> pd.DataFrame:
    """
    Load a custom telecom dataset from a local CSV file.
    
    Expected columns (minimum):
        - customerID or ID: unique customer identifier
        - tenure or Tenure: months as customer
        - MonthlyCharges or monthly_charges: monthly fee
        - TotalCharges or total_charges: lifetime revenue
        - Churn or churn: boolean churn indicator
    
    Args:
        file_path: Path to CSV file
        
    Returns:
        pd.DataFrame: Loaded and standardized dataset
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    df = pd.read_csv(file_path)
    
    # Auto-detect and standardize column names
    df = _standardize_custom_dataset(df)
    
    return df


def _standardize_kaggle_churn(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize Kaggle Telecom Customer Churn dataset to internal schema.
    
    Maps:
        customerID -> customer_id
        tenure -> tenure_months
        MonthlyCharges -> monthly_fee
        TotalCharges -> total_charges
        Churn -> churned (Yes/No -> 0/1)
    """
    rename_map = {
        "customerID": "customer_id",
        "tenure": "tenure_months",
        "MonthlyCharges": "monthly_fee",
        "TotalCharges": "total_revenue",
        "Churn": "churned",
        "InternetService": "internet_service",
        "OnlineSecurity": "online_security",
        "OnlineBackup": "online_backup",
        "DeviceProtection": "device_protection",
        "TechSupport": "tech_support",
        "StreamingTV": "streaming_tv",
        "StreamingMovies": "streaming_movies",
    }
    
    df = df.rename(columns=rename_map)
    
    # Convert churn to binary
    if "churned" in df.columns:
        df["churned"] = (df["churned"] == "Yes").astype(int)
    
    # Handle TotalCharges (may be string with spaces)
    if "total_revenue" in df.columns:
        df["total_revenue"] = pd.to_numeric(df["total_revenue"], errors="coerce")
        df["total_revenue"] = df["total_revenue"].fillna(0)
    
    return df


def _standardize_custom_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Auto-standardize column names from various common naming conventions.
    """
    # Normalize column names: lowercase, strip spaces
    df.columns = df.columns.str.lower().str.strip()
    
    # Map common column names to standard names
    column_mapping = {
        "id": "customer_id",
        "cust_id": "customer_id",
        "customerid": "customer_id",
        "customer_id": "customer_id",
        "months": "tenure_months",
        "tenure": "tenure_months",
        "tenure_months": "tenure_months",
        "monthly_charge": "monthly_fee",
        "monthly_charges": "monthly_fee",
        "monthly_fee": "monthly_fee",
        "total_charge": "total_revenue",
        "total_charges": "total_revenue",
        "total_revenue": "total_revenue",
        "churn": "churned",
        "churned": "churned",
    }
    
    # Apply mapping for columns that exist
    df = df.rename(columns={k: v for k, v in column_mapping.items() if k in df.columns})
    
    return df


def prepare_for_analysis(df: pd.DataFrame, source_type: Literal["kaggle", "uci", "custom"]) -> pd.DataFrame:
    """
    Prepare raw dataset for analysis pipeline.
    
    Performs:
    - Deduplication
    - Missing value handling
    - Type conversion
    - Outlier handling
    
    Args:
        df: Raw dataset
        source_type: Origin of dataset
        
    Returns:
        pd.DataFrame: Cleaned dataset ready for analysis
    """
    # Deduplication
    df = df.drop_duplicates(subset=["customer_id"] if "customer_id" in df.columns else None)
    
    # Handle missing values in key columns
    required_cols = ["customer_id", "tenure_months", "monthly_fee"]
    for col in required_cols:
        if col in df.columns and df[col].isna().any():
            if col == "tenure_months":
                df[col] = df[col].fillna(df[col].median())
            elif col == "monthly_fee":
                df[col] = df[col].fillna(df[col].mean())
    
    # Type conversion
    numeric_cols = ["tenure_months", "monthly_fee", "total_revenue"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    
    # Handle outliers in tenure and charges
    if "tenure_months" in df.columns:
        df["tenure_months"] = df["tenure_months"].clip(0, 120)
    
    if "monthly_fee" in df.columns:
        # Clip extreme outliers but keep realistic range
        q1 = df["monthly_fee"].quantile(0.01)
        q99 = df["monthly_fee"].quantile(0.99)
        df["monthly_fee"] = df["monthly_fee"].clip(q1, q99)
    
    return df


if __name__ == "__main__":
    print("Real Dataset Loading Module")
    print("\nUsage examples:")
    print("  from load_real_data import load_kaggle_churn_dataset, load_uci_telecom_dataset, load_custom_csv")
    print("  df = load_kaggle_churn_dataset()  # Requires kaggle API key")
    print("  df = load_uci_telecom_dataset()   # GitHub mirror")
    print("  df = load_custom_csv('my_data.csv')  # Your own data")
