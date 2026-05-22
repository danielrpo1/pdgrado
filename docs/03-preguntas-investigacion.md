# 3. Preguntas de investigación e hipótesis

## Enfoque terminológico

- Evitar marco exclusivo de “predicción sí/no de retiro”.
- Hablar de **riesgo de retiro** y **prospectiva** en **5 categorías**.
- La etiqueta `is_churn` del dataset valida perfiles; el objetivo del modelo es **asignación a categoría de riesgo** con probabilidades.

## Pregunta principal (recomendada por asesoría)

**¿Qué características del comportamiento del usuario (frecuencia de uso, tiempo de escucha, historial de transacciones y perfil) tienen mayor poder explicativo frente al riesgo de dejar la plataforma de streaming, cuando el riesgo se expresa en cinco categorías multidimensionales?**

## Preguntas alternativas (elegir una como principal si el seminario exige una sola)

1. ¿Cuál es el nivel de gestión de riesgos aplicable a un usuario que presenta potencial de retiro, en función de sus variables de comportamiento y transacción?
2. ¿Cuál es la relación entre las variables que describen el comportamiento de suscripción y las medidas de gestión de riesgo de retención por categoría?

## Preguntas secundarias (máximo 1–2 activas en paralelo)

| # | Pregunta | Fase |
|---|----------|------|
| Q2 | ¿Cuál es el balance entre capacidad predictiva e interpretabilidad cuando los clusters de riesgo preceden al modelo neuronal? | Fase 2 |
| Q3 | ¿En qué medida un clasificador neuronal 5-way supera modelos tradicionales (métricas multiclass: macro-F1, log-loss)? | Fase 2 |

*Nota asesoría:* no activar las tres a la vez en el mismo cronograma; **priorizar Q principal + clustering**.

## Hipótesis de trabajo (borrador)

- **H1:** Variables numéricas de `transactions` (días activos, monto pagado, número de pagos, cancelaciones, `plan_list_price`, días hasta expiración en escala tipo juliana) permiten separar usuarios en 5 grupos con tasas de `is_churn` significativamente diferentes.
- **H2:** El cluster de mayor riesgo (a ordenar tras análisis) presenta mayor proporción de `is_cancel` activo y menor tenencia que el cluster de menor riesgo.
- **H3:** *(Fase 2)* Un clasificador entrenado sobre etiquetas de cluster alcanza mejor interpretabilidad operativa que un modelo binario con AUC comparable.

## Variable dependiente (redefinición)

| Enfoque tradicional | Este proyecto |
|---------------------|---------------|
| `is_churn` ∈ {0,1} | **Categoría de riesgo** ∈ {0,1,2,3,4} derivada de clustering, luego predicha por NN |
| Probabilidad de churn | Vector de probabilidades **P(categoría k \| X)** |

## Métricas

**Fase 1 (clustering):**
- Silhouette score, inercia (K-Means)
- % `is_churn` por cluster
- Tablas de caracterización (medias, modas categóricas)

**Fase 2 (clasificación):**
- Macro-F1, log-loss multiclass
- Matriz de confusión 5×5
- Calibración de probabilidades por categoría

## Viabilidad / retención accionable

Por cada categoría, documentar:
- Perfil típico
- Acción sugerida (mantener, promo, silencio, escalamiento)
- Evidencia en tasa de churn del cluster
