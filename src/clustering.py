"""Clustering K-Means y exportación por categoría."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

from src.config import N_CLUSTERS, RANDOM_STATE


def fit_kmeans(
    X: pd.DataFrame,
    n_clusters: int = N_CLUSTERS,
    random_state: int = RANDOM_STATE,
) -> tuple[KMeans, StandardScaler, pd.Series]:
    """Escala features y ajusta K-Means."""
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)
    labels = model.fit_predict(X_scaled)
    return model, scaler, pd.Series(labels, index=X.index, name="cluster")


def churn_rate_by_cluster(
    df: pd.DataFrame, cluster_col: str = "cluster", target_col: str = "is_churn"
) -> pd.DataFrame:
    """Tasa de churn observada por cluster (validación de perfiles)."""
    return (
        df.groupby(cluster_col)[target_col]
        .agg(["mean", "count"])
        .rename(columns={"mean": "churn_rate", "count": "n_users"})
        .sort_values("churn_rate")
    )


def order_clusters_by_risk(
    df: pd.DataFrame, cluster_col: str = "cluster", target_col: str = "is_churn"
) -> dict[int, int]:
    """
    Mapea cluster K-Means → etiqueta de riesgo 0 (bajo) … 4 (alto)
    según tasa de churn.
    """
    rates = df.groupby(cluster_col)[target_col].mean().sort_values()
    return {old: new for new, old in enumerate(rates.index)}


def export_clusters_to_excel(
    df: pd.DataFrame,
    output_dir: Path,
    cluster_col: str = "risk_category",
    filename: str = "usuarios_por_riesgo.xlsx",
) -> Path:
    """Un libro Excel con una hoja por categoría de riesgo."""
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / filename
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        for cat in sorted(df[cluster_col].dropna().unique()):
            sheet = f"riesgo_{int(cat)}"
            subset = df[df[cluster_col] == cat]
            subset.to_excel(writer, sheet_name=sheet[:31], index=False)
    return path
