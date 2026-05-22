"""Carga de CSV KKBox (nombres v2/v3 como en apostaremczak/churn-prediction)."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.config import DATA_FILES, DATA_RAW


class DataNotFoundError(FileNotFoundError):
    """Faltan archivos en data/raw."""


def _path(name: str) -> Path:
    return DATA_RAW / DATA_FILES[name]


def check_data_files(data_dir: Path | None = None) -> dict[str, bool]:
    """Indica qué archivos existen en data/raw."""
    base = data_dir or DATA_RAW
    return {key: (base / fname).exists() for key, fname in DATA_FILES.items()}


def require_data_files(data_dir: Path | None = None) -> None:
    status = check_data_files(data_dir)
    missing = [k for k, ok in status.items() if not ok]
    if missing:
        files = ", ".join(DATA_FILES[k] for k in missing)
        raise DataNotFoundError(
            f"Faltan en {data_dir or DATA_RAW}: {files}. "
            "Ver docs/DATA_SETUP.md"
        )


def load_train(data_dir: Path | None = None) -> pd.DataFrame:
    df = pd.read_csv(_path("train") if data_dir is None else data_dir / DATA_FILES["train"])
    df["is_churn"] = df["is_churn"].astype("uint8")
    return df


def load_members(data_dir: Path | None = None) -> pd.DataFrame:
    df = pd.read_csv(
        _path("members") if data_dir is None else data_dir / DATA_FILES["members"]
    )
    df["registration_init_time"] = pd.to_datetime(
        df["registration_init_time"].astype(str), format="%Y%m%d", errors="coerce"
    )
    if "gender" in df.columns:
        df["gender"] = df["gender"].fillna("unknown")
    return df


def load_transactions(data_dir: Path | None = None) -> pd.DataFrame:
    path = _path("transactions") if data_dir is None else data_dir / DATA_FILES["transactions"]
    df = pd.read_csv(path)
    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"].astype(str), format="%Y%m%d", errors="coerce"
    )
    df["membership_expire_date"] = pd.to_datetime(
        df["membership_expire_date"].astype(str), format="%Y%m%d", errors="coerce"
    )
    for col in ("is_cancel", "is_auto_renew"):
        if col in df.columns:
            df[col] = df[col].astype("uint8")
    return df


def sample_users(
    train: pd.DataFrame,
    n: int,
    random_state: int,
    stratify: bool = True,
) -> pd.Series:
    """Muestra de msno; por defecto estratificada por is_churn."""
    if not stratify or train["is_churn"].nunique() < 2:
        return train["msno"].drop_duplicates().sample(
            min(n, train["msno"].nunique()), random_state=random_state
        )
    half = n // 2
    parts = []
    for _, group in train.groupby("is_churn"):
        k = min(half, group["msno"].nunique())
        parts.append(group["msno"].drop_duplicates().sample(k, random_state=random_state))
    msno = pd.concat(parts).drop_duplicates()
    if len(msno) > n:
        msno = msno.sample(n, random_state=random_state)
    return msno
