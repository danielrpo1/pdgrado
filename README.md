# Proyecto de Grado — Prospectiva de Riesgo de Retiro en Streaming

**Seminario de Proyecto de Grado | Universidad EAFIT**  
**Asesor:** Juan Alejandro Peña Palacio  
**Estudiante:** Daniel Restrepo Ospina

## De qué trata mi proyecto

Estoy desarrollando un marco para segmentar usuarios de una plataforma de streaming (dataset **KKBox**) en **cinco categorías de riesgo de retiro**, en línea con lo que conversé con mi asesor: no me interesa solo un modelo sí/no de churn, sino **perfiles de riesgo accionables** (como en aseguradoras o DataCrédito) y, más adelante, un clasificador que entregue **probabilidades por categoría**.

## Datos que uso

- Referencia de estructura: [apostaremczak/churn-prediction](https://github.com/apostaremczak/churn-prediction)
- Fuente: [KKBox Churn — Kaggle](https://www.kaggle.com/competitions/kkbox-churn-prediction-challenge)
- Archivos: `train_v2.csv`, `members_v3.csv`, `transactions_v2.csv`
- En esta fase trabajé con un **piloto de 1.000 usuarios**; el escalado viene después.

## Fases del trabajo

| Fase | Qué hice / haré | Método |
|------|-----------------|--------|
| **1** (actual) | Explorar datos y crear 5 perfiles de riesgo | K-Means (k=5) + caracterización + Excel por categoría |
| **2** | Clasificación automática con probabilidades | Red neuronal multidimensional (5 clases) |

Las variables categóricas (ciudad, género, etc.) las uso para **describir** cada grupo; al clustering entran las **numéricas** de transacciones, como acordamos en asesoría.

## Cuaderno para mi profesor (Colab, ya ejecutado)

Este es el entregable principal de la Fase 1: paso a paso, gráficos e interpretación en mi voz.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielrpo1/pdgrado/blob/main/notebooks/Colab_Piloto_5_Categorias_Riesgo_KKBox.ipynb)

`notebooks/Colab_Piloto_5_Categorias_Riesgo_KKBox.ipynb` — **incluye las salidas de mi corrida** (tablas y figuras).

## Estructura del repositorio

```
pdgrado/
├── docs/           # Contexto, vacíos, preguntas de investigación
├── notebooks/      # Colab con resultados del piloto
├── src/            # Código del pipeline
├── scripts/        # Descarga de datos y ejecución del piloto
├── data/           # CSV locales (no van a Git)
└── outputs/        # Excel por categoría de riesgo
```

## Documentación del seminario

- [Contexto](docs/01-contexto.md)
- [Vacíos en la literatura](docs/02-vacios-literatura.md)
- [Preguntas de investigación](docs/03-preguntas-investigacion.md)
- [Roadmap](docs/04-roadmap.md)
- [Notas para la reunión con mi asesor](docs/05-proximos-pasos-asesor.md)
- [Enlace al notebook Colab](docs/COLAB.md)

## Cómo reproduje el piloto en mi máquina

```bash
bash scripts/download_data.sh
.venv/bin/python scripts/run_pilot.py
```

Para regenerar el notebook con salidas:

```bash
.venv/bin/python scripts/execute_colab_notebook.py
```

## Licencia

Uso académico — Universidad EAFIT.
