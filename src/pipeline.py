"""Pipeline Fase 1: piloto clustering 5 categorías de riesgo."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.clustering import (
    churn_rate_by_cluster,
    export_clusters_to_excel,
    fit_kmeans,
    order_clusters_by_risk,
)
from src.config import (
    CLUSTER_FEATURE_COLS,
    DATA_PROCESSED,
    OUTPUTS,
    PILOT_SAMPLE_SIZE,
    RANDOM_STATE,
)
from src.data_io import (
    load_members,
    load_train,
    load_transactions,
    require_data_files,
    sample_users,
)
from src.features import attach_profile_for_characterization, build_user_features


def run_pilot(
    sample_size: int = PILOT_SAMPLE_SIZE,
    data_dir: Path | None = None,
    output_dir: Path | None = None,
) -> dict:
    """
    Ejecuta EDA operativo + K-Means k=5 + export Excel.
    Retorna resumen (tasas de churn por categoría).
    """
    require_data_files(data_dir)

    train = load_train(data_dir)
    members = load_members(data_dir)
    transactions = load_transactions(data_dir)

    # Solo usuarios con transacciones (evita perder filas tras el merge)
    train_with_tx = train[train["msno"].isin(transactions["msno"].unique())]
    pilot_msno = sample_users(train_with_tx, sample_size, RANDOM_STATE)
    tx = transactions[transactions["msno"].isin(pilot_msno)]
    mem = members[members["msno"].isin(pilot_msno)]

    features = build_user_features(tx, members=mem)
    df = attach_profile_for_characterization(features, mem, train)

    feature_cols = [c for c in CLUSTER_FEATURE_COLS if c in df.columns]
    X = df[feature_cols].fillna(0)

    _, _, labels = fit_kmeans(X)
    df["cluster_raw"] = labels.values
    risk_map = order_clusters_by_risk(df, cluster_col="cluster_raw")
    df["risk_category"] = df["cluster_raw"].map(risk_map)

    summary = churn_rate_by_cluster(df, cluster_col="risk_category")

    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    out_processed = DATA_PROCESSED / "pilot_clustered.parquet"
    df.to_parquet(out_processed, index=False)

    excel_dir = output_dir or OUTPUTS
    excel_path = export_clusters_to_excel(df, excel_dir)

    return {
        "n_users": len(df),
        "feature_cols": feature_cols,
        "summary": summary,
        "parquet": out_processed,
        "excel": excel_path,
    }
