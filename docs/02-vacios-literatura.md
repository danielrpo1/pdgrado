# 2. Vacíos en la literatura

> Borrador para el primer entregable del seminario. Completar con referencias APA en la siguiente iteración.

## 2.1 Predicción binaria vs. gestión multidimensional de riesgo

**Vacío:** La literatura de *churn prediction* en streaming y telecomunicaciones se concentra en modelos binarios (logística, XGBoost, redes neuronales) optimizando AUC, F1 o log-loss ([Chen et al., competencia KKBox; enfoques ensemble XGBoost + NN]).

**Brecha:** Pocos trabajos traducen el problema a **cinco categorías de riesgo** alineadas con marcos de aseguramiento y scoring crediticio, donde la granularidad es requisito operativo, no un refinamiento opcional.

**Aporte del proyecto:** Reformular el retiro como **prospectiva de riesgo** en escala ordinal/categórica (5 niveles), con perfiles por segmento.

## 2.2 Clusterización previa a modelos neuronales (interpretabilidad)

**Vacío:** Las redes neuronales para churn suelen consumir features engineered directamente; la **interpretabilidad** del riesgo queda en atributos globales (SHAP, importancia de variables) sin estructura de **patrones de riesgo** previos.

**Brecha:** Falta evidencia sistemática del **balance predictividad–interpretabilidad** cuando se fijan **5 patrones de riesgo** vía clustering antes del entrenamiento supervisado (enfoque tipo *fuzzy* / probabilidad de pertenencia a cluster).

**Aporte:** Pipeline explícito: (1) clusters interpretables → (2) NN clasificador 5-way con probabilidades por categoría.

## 2.3 Clasificadores multidimensionales y redes neuronales

**Vacío:** Búsqueda pendiente de artículos sobre **clasificadores multidimensionales** en redes neuronales aplicados a retención (no solo softmax binario).

**Líneas a revisar (acción):**
- Clasificación ordinal y multiclass en churn
- *PUC* / redes borrosas con salidas probabilísticas por clase
- Segmentación RFM extendida a riesgo dinámico

## 2.4 Variables de engagement a escala masiva

**Vacío:** `user_logs` aporta señales fuertes (p. ej. % de canción completada: 25% vs 75%), pero la literatura que usa logs completos es limitada por costo computacional; predominan agregados mensuales.

**Aporte (fase escalada):** Incorporar engagement agregado sin procesar 30 GB en el piloto.

## 2.5 Prospectiva vs. predicción puntual

**Vacío:** Confusión terminológica entre **predicción** (valor puntual), **pronóstico** y **prospectiva** (escenarios y potenciales de retiro).

**Aporte:** Uso deliberado de **prospectiva de riesgos**: probabilidades y proyecciones por categoría, sin comprometerse a un único desenlace binario.

## 2.6 Eficiencia operativa y “do not poke”

**Vacío:** Poca literatura académica sobre **no intervención** como estrategia óptima para ciertos segmentos de riesgo (contacto que aumenta churn).

**Aporte cualitativo:** Vincular categoría 4–5 con políticas de contacto / silencio desde práctica industria.

---

## Referencias iniciales (completar formato APA)

1. WSDM Cup 2018 — KKBox Churn Prediction Challenge. Kaggle.  
2. Documentación de competencia: criterio `is_churn`, `is_cancel`, ventana 30 días.  
3. *Ensembling XGBoost and Neural Network for Churn Prediction* — WSDM Cup 2018.  
4. Pirani / marcos de riesgo empresarial (5 categorías) — material de asesoría.  
5. Clustering: K-Means, DBSCAN, aglomerativo — textos de maestría (Analítica de negocios / Integración de datos).

**Tarea próxima semana:** 15–20 referencias en Zotero/Mendeley cubriendo los vacíos 2.1, 2.2 y 2.3.
