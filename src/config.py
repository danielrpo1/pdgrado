"""Rutas y constantes del proyecto."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = PROJECT_ROOT / "data" / "raw"
OUTPUTS = PROJECT_ROOT / "outputs" / "clusters"

KAGGLE_COMPETITION = "kkbox-churn-prediction-challenge"
N_CLUSTERS = 5
PILOT_SAMPLE_SIZE = 1000
RANDOM_STATE = 42

TRANSACTION_NUMERIC = [
    "payment_plan_days",
    "plan_list_price",
    "actual_amount_paid",
    "payment_num_total",
    "days_since_last_payment",
    "days_until_expire",
    "cancel_count",
    "auto_renew_ratio",
]
