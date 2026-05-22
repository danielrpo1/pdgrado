#!/usr/bin/env bash
# Descarga CSV de Kaggle (requiere ~/.kaggle/kaggle.json)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DATA="$ROOT/data/raw"
mkdir -p "$DATA"

if [[ ! -f "$HOME/.kaggle/kaggle.json" ]]; then
  echo "ERROR: Crea API token en https://www.kaggle.com/settings"
  echo "       y guarda kaggle.json en ~/.kaggle/ (chmod 600)"
  exit 1
fi

command -v kaggle >/dev/null || { echo "pip install kaggle"; exit 1; }

kaggle competitions download -c kkbox-churn-prediction-challenge -p "$DATA"
cd "$DATA"
for f in *.zip *.7z; do
  [[ -f "$f" ]] || continue
  echo "Extrayendo $f ..."
  unzip -o "$f" 2>/dev/null || 7z x "$f" 2>/dev/null || true
done

echo ""
echo "Archivos esperados en data/raw/:"
ls -lh "$DATA" | head -20
echo ""
echo "Renombra si Kaggle entrega otros nombres; el proyecto espera:"
echo "  train_v2.csv members_v3.csv transactions_v2.csv"
