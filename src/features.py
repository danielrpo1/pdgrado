"""Agregación de transacciones por usuario (msno)."""

from __future__ import annotations

import numpy as np
import pandas as pd


def to_julian_days(series: pd.Series) -> pd.Series:
    """Convierte fechas a días julianos (enteros) para operaciones numéricas."""
    dt = pd.to_datetime(series, errors="coerce")
    origin = pd.Timestamp("1965-01-01")
    return (dt - origin).dt.days


def build_user_features(transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega transactions.csv a nivel msno con variables numéricas
    recomendadas en asesoría.
    """
    df = transactions.copy()
    df["transaction_date_julian"] = to_julian_days(df["transaction_date"])
    df["membership_expire_date_julian"] = to_julian_days(df["membership_expire_date"])

    grouped = df.groupby("msno", as_index=False).agg(
        payment_plan_days_mean=("payment_plan_days", "mean"),
        plan_list_price_mean=("plan_list_price", "mean"),
        actual_amount_paid_sum=("actual_amount_paid", "sum"),
        actual_amount_paid_mean=("actual_amount_paid", "mean"),
        payment_num_total_max=("payment_num_total", "max"),
        transaction_count=("msno", "count"),
        cancel_count=("is_cancel", "sum"),
        auto_renew_ratio=("is_auto_renew", "mean"),
        last_expire_julian=("membership_expire_date_julian", "max"),
        first_tx_julian=("transaction_date_julian", "min"),
        last_tx_julian=("transaction_date_julian", "max"),
    )

    grouped["days_active_span"] = (
        grouped["last_tx_julian"] - grouped["first_tx_julian"]
    ).clip(lower=0)
    grouped["days_until_expire"] = (
        grouped["last_expire_julian"] - grouped["last_tx_julian"]
    )

    return grouped
