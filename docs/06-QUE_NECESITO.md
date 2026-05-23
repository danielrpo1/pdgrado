# Qué necesito de ti para seguir

## Datos

Los CSV ya se descargan con `bash scripts/download_data.sh` (dataset `qmdo97/kkboxdataset`).

En tu máquina deben quedar en `data/raw/` (~560 MB descomprimido).

## Ya está hecho en el repo

- [x] Clon de referencia local: `reference/churn-prediction/` (en tu máquina; no va a Git)
- [x] Pipeline Fase 1: `python scripts/run_pilot.py`
- [x] Código alineado a nombres v2/v3 del repo de referencia
- [x] Salida: Excel 5 hojas + `pilot_clustered.parquet`

## Por dónde empezamos (orden)

| Paso | Quién | Acción |
|------|-------|--------|
| **1** | Tú | Poner los 3 CSV en `data/raw/` |
| **2** | Tú o yo | `python scripts/run_pilot.py` |
| **3** | Tú | Revisar Excel y tabla de % churn por categoría |
| **4** | Nosotros | Ajustar features si algún cluster no separa riesgo |
| **5** | Tú | Llevar resultados al profesor + link Colab |
| **6** | Después | Fase 2: red neuronal 5 clases |

## Si usas Colab

- Sube los CSV a Drive **o** descarga en el notebook con Kaggle secrets.
- Abre `notebooks/01_eda_clustering_piloto.ipynb` desde GitHub.

## Avísame cuando

Tengas los CSV listos (puedes decir “ya están en data/raw”) y ejecutamos el piloto juntos o revisamos los resultados.
