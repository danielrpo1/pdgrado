# Proyecto de Grado — Prospectiva de Riesgo de Retiro en Streaming

**Seminario de Proyecto de Grado | Universidad EAFIT**  
**Asesor:** Juan Alejandro Peña Palacio  
**Estudiante:** Daniel Restrepo Ospina

## Resumen

Segmentación multidimensional de usuarios de una plataforma de streaming (dataset KKBox) en **5 categorías de riesgo de retiro**, alineado con estándares de gestión de riesgo (aseguradoras, DataCrédito, banca). El proyecto evita la clasificación binaria (sí/no churn) y prioriza **prospectiva de riesgos** con perfiles accionables por categoría.

## Dataset

- **Referencia de datos:** [apostaremczak/churn-prediction](https://github.com/apostaremczak/churn-prediction) → Kaggle [KKBox Churn](https://www.kaggle.com/competitions/kkbox-churn-prediction-challenge)
- **Archivos (en `data/raw/`):** `train_v2.csv`, `members_v3.csv`, `transactions_v2.csv`
- **Setup:** [`docs/DATA_SETUP.md`](docs/DATA_SETUP.md)
- **Estrategia de volumen:** piloto **1.000 usuarios** → escalado incremental

## Enfoque metodológico (2 fases)

| Fase | Objetivo | Método |
|------|----------|--------|
| **1** | Explorar variables y crear 5 clusters de riesgo | EDA + K-Means (k=5) sobre variables numéricas |
| **2** | Clasificación automática con probabilidades | Red neuronal / clasificador multidimensional (5 salidas) |

Variables **categóricas** (ciudad, género, método de pago) → **caracterización de perfiles**, no clustering.

## Estructura del repositorio

```
pdgrado/
├── docs/                    # Entregables del seminario y plan de trabajo
├── notebooks/               # Notebooks Colab (EDA, clustering, modelo)
├── src/                     # Código reutilizable
├── data/                    # Datos locales (gitignored)
└── outputs/                 # Excels por cluster, figuras (gitignored)
```

## Plataforma de ejecución

**Recomendación:** Google Colab para Fase 1 (piloto 1.000 usuarios).  
Kaggle se usa para descargar datos y, si aplica, escalar con GPU. Detalle en [`docs/04-roadmap.md`](docs/04-roadmap.md).

## Documentación del seminario

- [1. Contexto](docs/01-contexto.md)
- [2. Vacíos en la literatura](docs/02-vacios-literatura.md)
- [3. Preguntas de investigación](docs/03-preguntas-investigacion.md)
- [4. Roadmap paso a paso](docs/04-roadmap.md)
- [5. Próximos pasos (reunión con asesor)](docs/05-proximos-pasos-asesor.md)

## Inicio rápido

```bash
# 1. Referencia (opcional, local)
bash scripts/setup_reference.sh

# 2. Descargar CSV (Kaggle API) — ver DATA_SETUP.md
bash scripts/download_data.sh

# 3. Piloto clustering
python scripts/run_pilot.py
```

O en Colab: `notebooks/01_eda_clustering_piloto.ipynb`

## Licencia

Uso académico — Universidad EAFIT.
