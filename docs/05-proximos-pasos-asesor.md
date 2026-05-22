# Próximos pasos — reunión con asesor (1 página)

**Fecha objetivo:** próxima semana  
**Estudiante:** Daniel Restrepo Ospina

## Lo acordado en asesoría (8 abr 2026)

1. No empezar por red neuronal; empezar por **5 clusters de riesgo**.
2. Piloto con **~1.000 usuarios** antes de escalar.
3. Priorizar archivo **`transactions`** + variables **numéricas**; categóricas para **perfil**.
4. Exportar usuarios en **5 hojas Excel** y analizar comportamiento por grupo.
5. Lenguaje del proyecto: **riesgo / prospectiva**, no solo “churn sí/no”.
6. Plataforma sugerida: **Google Colab** (muestra pequeña).

## Lo que traigo a la reunión

| # | Entregable | Dónde |
|---|------------|-------|
| 1 | Repo GitHub con estructura y documentación | `github.com/danielrpo1/pdgrado` (o nombre final) |
| 2 | Borrador **Contexto** y **Vacíos en literatura** | `docs/01`, `docs/02` |
| 3 | Pregunta de investigación alineada (5 categorías) | `docs/03` |
| 4 | Notebook Colab: inventario de variables + K-Means piloto | `notebooks/01_eda_clustering_piloto.ipynb` |
| 5 | Resultado preliminar: tabla % `is_churn` por cluster | salida del notebook |
| 6 | 5 Excels (o 1 libro con 5 hojas) por cluster | `outputs/clusters/` |

## Decisiones que pido validar

1. ¿Ordenamos clusters por **% churn ascendente** para etiquetar riesgo 0 (bajo) → 4 (alto)?
2. ¿Confirmamos **solo transactions + members** para el piloto, sin `user_logs`?
3. ¿La pregunta principal del seminario es la de **características comportamentales** (Q en `docs/03`)?
4. ¿Siguiente hito académico es **marco teórico + estado del arte** con foco en clasificación multidimensional?

## Plan inmediato post-reunión

- Completar 15–20 referencias APA (vacíos 2.1–2.3).
- Refinar perfiles narrativos por cluster (qué hacer con categoría 0 vs 4).
- Escalar muestra (5k → 10k) si perfiles son estables.
- Diseñar arquitectura NN 5-way (Fase 2).

## Riesgos / mitigaciones

| Riesgo | Mitigación |
|--------|------------|
| Dataset muy grande | Muestra 1k; agregación por usuario |
| `user_logs` 30 GB | Fase 2; agregados mensuales |
| Clusters sin orden de riesgo | Post-procesar por % churn |
| Colab sin datos | Kaggle API + Drive |

## Enlace Colab (completar tras primera ejecución)

`[Pegar aquí URL del notebook en Colab después de Run All]`
