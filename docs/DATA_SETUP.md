# Configuración de datos (KKBox)

Fuente de referencia: [apostaremczak/churn-prediction](https://github.com/apostaremczak/churn-prediction)  
Competencia Kaggle: [kkbox-churn-prediction-challenge](https://www.kaggle.com/competitions/kkbox-churn-prediction-challenge/data)

## Archivos requeridos

Coloca estos CSV en `data/raw/` (no se suben a Git):

| Archivo | Contenido |
|---------|-----------|
| `train_v2.csv` | `msno`, `is_churn` (etiqueta para validar clusters) |
| `members_v3.csv` | Perfil: ciudad, género, registro, etc. |
| `transactions_v2.csv` | Pagos, auto-renew, cancelaciones, precios |

**No necesitas** `user_logs` (~30 GB) para la Fase 1.

## Opción A — Kaggle CLI (recomendada)

1. Cuenta Kaggle → Settings → **Create New API Token** → `kaggle.json`
2. `mkdir -p ~/.kaggle && mv ~/Downloads/kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json`
3. `pip install kaggle`
4. Desde la raíz del proyecto:

```bash
bash scripts/download_data.sh
```

Si los nombres tras descomprimir difieren (`train.csv` vs `train_v2.csv`), renómbralos o crea enlaces simbólicos.

## Opción B — Copiar desde el repo de referencia

Si ya trabajaste con [apostaremczak/churn-prediction](https://github.com/apostaremczak/churn-prediction):

```bash
bash scripts/setup_reference.sh
# Copia tus CSV a pdgrado:
cp /ruta/a/churn-prediction/data/train_v2.csv data/raw/
cp /ruta/a/churn-prediction/data/members_v3.csv data/raw/
cp /ruta/a/churn-prediction/data/transactions_v2.csv data/raw/
```

## Verificar y correr piloto

```bash
python scripts/run_pilot.py
```

Salida:

- `data/processed/pilot_clustered.parquet`
- `outputs/clusters/usuarios_por_riesgo.xlsx` (5 hojas)

## Colab

1. Sube los 3 CSV a Google Drive en `MyDrive/pdgrado/data/raw/`
2. Abre `notebooks/01_eda_clustering_piloto.ipynb`
3. Ajusta `DATA_DIR` al montaje de Drive

## Qué no puedo hacer yo por ti

Sin tu `kaggle.json` o los CSV en disco, el pipeline no puede ejecutarse en esta máquina. En cuanto estén los archivos, `run_pilot.py` corre en un solo comando.
