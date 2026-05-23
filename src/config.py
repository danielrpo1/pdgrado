"""Rutas y constantes del proyecto."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
OUTPUTS = PROJECT_ROOT / "outputs" / "clusters"

# Fuente: https://github.com/apostaremczak/churn-prediction + Kaggle competition
KAGGLE_COMPETITION = "kkbox-churn-prediction-challenge"
DATA_FILES = {
    "train": "train_v2.csv",
    "members": "members_v3.csv",
    "transactions": "transactions_v2.csv",
}

REFERENCE_REPO = "https://github.com/apostaremczak/churn-prediction"
N_CLUSTERS = 5
PILOT_SAMPLE_SIZE = 10_000
RANDOM_STATE = 42

# Columnas numéricas agregadas por usuario (clustering)
CLUSTER_FEATURE_COLS = [
    "purchased_membership_length_days_mean",
    "price_ntd_mean",
    "amount_paid_ntd_sum",
    "amount_paid_ntd_mean",
    "transaction_count",
    "cancel_count",
    "auto_renew_ratio",
    "days_active_span",
    "days_until_expire",
    "time_since_registration_days_mean",
    "discount_mean",
    "is_discount_ratio",
]
