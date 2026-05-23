#!/usr/bin/env bash
# Descarga train_v2, members_v3, transactions_v2 (KKBox churn)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DATA="$ROOT/data/raw"
mkdir -p "$DATA"

if [[ -f "$HOME/.kaggle/access_token" ]]; then
  export KAGGLE_API_TOKEN="$(tr -d '\n' < "$HOME/.kaggle/access_token")"
elif [[ -f "$HOME/.kaggle/kaggle.json" ]]; then
  export KAGGLE_USERNAME="$(python3 -c "import json;print(json.load(open('$HOME/.kaggle/kaggle.json'))['username'])")"
  export KAGGLE_KEY="$(python3 -c "import json;print(json.load(open('$HOME/.kaggle/kaggle.json'))['key'])")"
else
  echo "ERROR: Configura ~/.kaggle/access_token o kaggle.json"
  exit 1
fi

KAGGLE="${ROOT}/.venv/bin/kaggle"
if [[ ! -x "$KAGGLE" ]]; then
  echo "Creando venv e instalando kaggle..."
  python3.12 -m venv "$ROOT/.venv" 2>/dev/null || python3 -m venv "$ROOT/.venv"
  "$ROOT/.venv/bin/pip" install -q kaggle
  KAGGLE="$ROOT/.venv/bin/kaggle"
fi

cd "$DATA"
DATASET="qmdo97/kkboxdataset"

for f in train_v2.csv members_v3.csv transactions_v2.csv; do
  if [[ -f "$f" ]]; then
    echo "Ya existe $f"
    continue
  fi
  echo "Descargando $f desde $DATASET ..."
  "$KAGGLE" datasets download -d "$DATASET" -f "$f" -p . --force
  unzip -o -q "${f}.zip" && rm -f "${f}.zip"
done

echo ""
ls -lh "$DATA"/*.csv
