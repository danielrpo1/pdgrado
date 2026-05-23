# Cómo abrir el notebook en Google Colab

## Enlace directo

https://colab.research.google.com/github/danielrpo1/pdgrado/blob/main/notebooks/Colab_Piloto_5_Categorias_Riesgo_KKBox.ipynb

## Antes de ejecutar

1. En Kaggle → [Settings](https://www.kaggle.com/settings) → **Create New Token**
2. En Colab → panel **Secrets** (🔑) → nombre `KAGGLE_API_TOKEN` → pegar el token
3. **Runtime → Run all**

## Si no quieres usar Kaggle en Colab

Sube los 3 CSV a Google Drive en `MyDrive/pdgrado/data/raw/` y en el notebook activa la **Opción B** (comentada en el Paso 1).

## Qué contiene el notebook

- Contexto del proyecto de grado (5 categorías de riesgo)
- Descarga de datos
- EDA con gráficos
- K-Means y validación con % churn
- Interpretación en lenguaje sencillo
- Exportación del Excel con 5 hojas
