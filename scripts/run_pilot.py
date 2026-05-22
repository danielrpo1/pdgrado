#!/usr/bin/env python3
"""Ejecuta piloto de clustering (1000 usuarios) si los CSV están en data/raw."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data_io import check_data_files, DataNotFoundError
from src.pipeline import run_pilot


def main() -> int:
    status = check_data_files()
    print("Archivos en data/raw/:", status)
    if not all(status.values()):
        print("\nFaltan datos. Pasos:")
        print("  1. bash scripts/download_data.sh   (o copiar CSV manualmente)")
        print("  2. Ver docs/DATA_SETUP.md")
        return 1

    result = run_pilot()
    print(f"\nUsuarios en piloto: {result['n_users']}")
    print(f"Features: {result['feature_cols']}")
    print("\nTasa churn por categoría de riesgo (0=bajo → 4=alto):")
    print(result["summary"].to_string())
    print(f"\nParquet: {result['parquet']}")
    print(f"Excel:   {result['excel']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except DataNotFoundError as e:
        print(e, file=sys.stderr)
        raise SystemExit(1)
