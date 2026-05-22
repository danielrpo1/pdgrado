#!/usr/bin/env bash
# Clona repo de referencia (datos + EDA binario KKBox)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REF="$ROOT/reference/churn-prediction"

if [[ -d "$REF/.git" ]] || [[ -f "$REF/README.md" ]]; then
  echo "Referencia ya existe: $REF"
  exit 0
fi

mkdir -p "$ROOT/reference"
git clone --depth 1 https://github.com/apostaremczak/churn-prediction.git "$REF"
echo "Listo: $REF"
