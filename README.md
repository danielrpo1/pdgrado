# Proyecto de Grado — Prospectiva de Riesgo de Retiro en Streaming

**Seminario de Proyecto de Grado | Universidad EAFIT**  
**Asesor:** Juan Alejandro Peña Palacio  
**Estudiante:** Daniel Restrepo Ospina

## De qué trata el proyecto

Segmentación de usuarios de la plataforma **KKBox** (streaming musical) en **cinco categorías de riesgo de retiro**, alineada con prácticas de riesgo en suscripción, banca y aseguramiento. El enfoque evita quedarse en un modelo binario (churn sí/no) y apunta a **perfiles accionables** y, en una segunda fase, a un clasificador con **probabilidades por categoría**.

## Datos

- Estructura de referencia: [apostaremczak/churn-prediction](https://github.com/apostaremczak/churn-prediction)
- Fuente: [KKBox Churn — Kaggle](https://www.kaggle.com/competitions/kkbox-churn-prediction-challenge)
- Archivos: `train_v2.csv`, `members_v3.csv`, `transactions_v2.csv`
- Piloto actual documentado en Colab: **10.000 usuarios** (antes 1.000 para validar el pipeline)

## Fases

| Fase | Objetivo | Método |
|------|----------|--------|
| **1** | Perfiles de riesgo interpretables | K-Means (k=5) + caracterización + Excel por categoría |
| **2** | Asignación automática con probabilidades | Clasificador multidimensional (5 clases) |

Variables **numéricas** de transacciones → clustering. Variables **categóricas** (ciudad, género, etc.) → descripción de cada segmento.

## Notebook Colab (ejecutado, con gráficos)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielrpo1/pdgrado/blob/main/notebooks/Colab_Piloto_5_Categorias_Riesgo_KKBox.ipynb)

`notebooks/Colab_Piloto_5_Categorias_Riesgo_KKBox.ipynb` — paso a paso, figuras y tablas de la corrida con 10k usuarios.

## Estructura del repositorio

```
pdgrado/
├── docs/           # Contexto, vacíos, preguntas de investigación
├── notebooks/      # Colab con resultados del piloto
├── src/            # Pipeline de datos y clustering
├── scripts/        # Descarga, piloto y regeneración del notebook
├── data/           # CSV locales (no versionados)
└── outputs/        # Excel por categoría
```

## Documentación del seminario

- [Contexto](docs/01-contexto.md)
- [Vacíos en la literatura](docs/02-vacios-literatura.md)
- [Preguntas de investigación](docs/03-preguntas-investigacion.md)
- [Roadmap](docs/04-roadmap.md)
- [Notas de avance](docs/05-proximos-pasos-asesor.md)
- [Notebook Colab](docs/COLAB.md)

## Reproducir el piloto

```bash
bash scripts/download_data.sh
.venv/bin/python scripts/run_pilot.py
.venv/bin/python scripts/execute_colab_notebook.py   # regenera notebook con salidas
```

## Licencia

Uso académico — Universidad EAFIT.
