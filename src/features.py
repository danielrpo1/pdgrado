"""Features numéricas por usuario para clustering (asesoría: transacciones primero)."""

from __future__ import annotations

import pandas as pd


def build_user_features(
    transactions: pd.DataFrame,
    members: pd.DataFrame | None = None,
) -> pd.DataFrame:
    """
    Agrega transactions_v2 por msno.
    Nombres alineados con apostaremczak (price_ntd, amount_paid_ntd, etc.).
    """
    df = transactions.copy()
    if "user_id" in df.columns and "msno" not in df.columns:
        df = df.rename(columns={"user_id": "msno"})

    if members is not None:
        m = members.copy()
        if "user_id" in m.columns:
            m = m.rename(columns={"user_id": "msno"})
        df = df.merge(m[["msno", "registration_init_time"]], on="msno", how="left")
        df["time_since_registration_days"] = (
            df["transaction_date"] - df["registration_init_time"]
        ).dt.days

    rename = {}
    if "payment_plan_days" in df.columns:
        rename["payment_plan_days"] = "purchased_membership_length_days"
    if "plan_list_price" in df.columns:
        rename["plan_list_price"] = "price_ntd"
    if "actual_amount_paid" in df.columns:
        rename["actual_amount_paid"] = "amount_paid_ntd"
    df = df.rename(columns=rename)

    df["discount"] = df["price_ntd"] - df["amount_paid_ntd"]
    df["is_discount"] = (df["discount"] > 0).astype("uint8")

    grouped = df.groupby("msno", as_index=False).agg(
        purchased_membership_length_days_mean=("purchased_membership_length_days", "mean"),
        price_ntd_mean=("price_ntd", "mean"),
        amount_paid_ntd_sum=("amount_paid_ntd", "sum"),
        amount_paid_ntd_mean=("amount_paid_ntd", "mean"),
        payment_num_total_max=("payment_num_total", "max"),
        transaction_count=("msno", "count"),
        cancel_count=("is_cancel", "sum"),
        auto_renew_ratio=("is_auto_renew", "mean"),
        first_tx=("transaction_date", "min"),
        last_tx=("transaction_date", "max"),
        last_expire=("membership_expire_date", "max"),
        time_since_registration_days_mean=("time_since_registration_days", "mean"),
        discount_mean=("discount", "mean"),
        is_discount_ratio=("is_discount", "mean"),
    )

    grouped["days_active_span"] = (grouped["last_tx"] - grouped["first_tx"]).dt.days.clip(
        lower=0
    )
    grouped["days_until_expire"] = (
        grouped["last_expire"] - grouped["last_tx"]
    ).dt.days
    grouped = grouped.drop(columns=["first_tx", "last_tx", "last_expire"])
    return grouped


def attach_profile_for_characterization(
    features: pd.DataFrame,
    members: pd.DataFrame,
    train: pd.DataFrame,
) -> pd.DataFrame:
    """Une is_churn y columnas categóricas (no para k-means)."""
    m = members.copy()
    if "user_id" in m.columns:
        m = m.rename(columns={"user_id": "msno"})
    profile_cols = ["msno", "city", "gender", "registered_via"]
    profile_cols = [c for c in profile_cols if c in m.columns]
    out = features.merge(train[["msno", "is_churn"]], on="msno", how="inner")
    out = out.merge(m[profile_cols], on="msno", how="left")
    return out
