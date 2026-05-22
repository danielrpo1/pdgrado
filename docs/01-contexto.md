# 1. Contexto

## 1.1 Situación

Las plataformas de suscripción (streaming, SaaS, membresías) enfrentan **pérdida de ingresos recurrentes** cuando los usuarios no renuevan tras vencer su membresía. En la industria, la gestión de retención suele basarse en modelos **binarios** (¿se va o se queda?), lo cual limita la **acción operativa**: no distingue entre un usuario de riesgo leve y uno crítico, ni permite priorizar recursos (comercial, promociones, o la estrategia *do not poke the bear*: no contactar para no activar la cancelación).

En sectores regulados —**aseguradoras**, **entidades financieras**, **bureaus de crédito** (p. ej. DataCrédito)— la norma es clasificar exposiciones en **cinco categorías de riesgo**, no en sí/no. Esa segmentación permite:

- Políticas de cobertura y reclamación por segmento
- Cortes transversales (ingresos × antigüedad, engagement × tenencia)
- Medidas de gestión diferenciadas por nivel (mantener, ofertar, no contactar, escalamiento comercial)

## 1.2 Problema

El dataset público **KKBox Churn Prediction** (WSDM Cup 2018) modela el retiro como variable binaria `is_churn`. La competencia y la mayoría de notebooks en Kaggle optimizan **AUC-ROC / log-loss** para predicción sí/no, sin entregar **perfiles multidimensionales de riesgo** ni probabilidades por categoría para gestión operativa.

**Problema de investigación (operativo):**  
¿Cómo segmentar usuarios de streaming en **cinco niveles de riesgo de retiro** a partir de comportamiento de transacciones, perfil y engagement, de modo que cada segmento sea **caracterizable** y **accionable** en estrategias de retención?

## 1.3 Caso de datos

| Fuente | Descripción |
|--------|-------------|
| Plataforma | KKBox (streaming musical, Asia) |
| Usuarios | ~970.000 en conjunto completo |
| Archivos | `train`, `members`, `transactions`, `user_logs` |
| Etiqueta original | `is_churn` (renovación en 30 días post-expiración) |
| Uso en el proyecto | La etiqueta binaria se usa para **validar** perfiles de cluster, no como único objetivo del modelo |

**Definición de churn (competencia):** no hay nueva suscripción válida dentro de 30 días después de que expira la membresía actual. `is_cancel` indica cancelación activa del plan (no equivale automáticamente a churn).

## 1.4 Relevancia

- **Académica:** aporte en **clasificación multidimensional** y prospectiva de riesgo vs. predicción binaria.
- **Profesional:** alineación con prácticas de riesgo en HBO/entornos de suscripción (segmentación, *do not poke*, eficiencia de campañas).
- **Estratégica:** cinco categorías permiten definir qué hacer con cada una (promo, silencio, llamada comercial, Champions, etc.).

## 1.5 Alcance (Fase actual — acordado con asesor)

1. **Análisis exploratorio:** inventario de variables numéricas vs. categóricas.
2. **Clustering piloto:** K-Means con **k = 5** sobre muestra de **1.000 usuarios**, priorizando `transactions` + agregados de `members`.
3. **Caracterización:** distribución de variables por cluster; exportación a **5 hojas Excel**.
4. **Siguiente entrega:** marco teórico, estado del arte, clasificadores multidimensionales en redes neuronales.

**Fuera de alcance inicial:** `user_logs` completo (~30 GB); modelos LLM sobre texto; despliegue en producción.

## 1.6 Objetivo general

Desarrollar un marco de **prospectiva de riesgo de retiro** en plataformas de streaming que combine clusterización multidimensional (5 niveles) y, en fase posterior, clasificación neuronal con **probabilidades por categoría**, evaluando balance entre capacidad predictiva e interpretabilidad.

## 1.7 Objetivos específicos

1. Identificar y documentar variables numéricas predictivas de riesgo de retiro (transacciones, tenencia, pagos, cancelaciones).
2. Agrupar usuarios en **5 clusters de riesgo** mediante métodos de clusterización (K-Means, con exploración opcional de DBSCAN / aglomerativo).
3. Caracterizar cada cluster (variables categóricas y tasa de `is_churn` observada).
4. *(Fase 2)* Entrenar clasificador multidimensional (5 clases) y comparar con enfoques tradicionales.
5. *(Fase 2)* Analizar viabilidad de estrategias de retención accionables por categoría.
