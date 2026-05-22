# 4. Roadmap paso a paso

## Kaggle vs Google Colab — decisión

| Criterio | Kaggle Notebooks | Google Colab |
|----------|------------------|--------------|
| Datos KKBox | Integración directa con API/dataset | Descarga vía `kaggle` CLI o manual a Drive |
| RAM / tiempo | Límite sesión; dataset grande pesado | Similar en free; Colab Pro más RAM |
| Muestra 1.000 usuarios | ✅ Suficiente en ambos | ✅ **Recomendado por asesor** |
| `user_logs` 30 GB | Incómodo | Incómodo — **evitar en piloto** |
| Revisión con profesor | Link Kaggle | Link Colab + repo GitHub |
| Versionado código | Kernel en Kaggle | **Notebook en GitHub** + Colab |

### Recomendación

1. **Colab** para ejecutar el piloto (EDA + K-Means, 1.000 usuarios), como acordaste con el profesor.
2. **Kaggle** solo como **origen de datos** (descargar `transactions`, `members`, `train`).
3. **GitHub** (este repo) como fuente de verdad: notebooks, `src/`, documentación del seminario.

Flujo sugerido: desarrollar en Colab → “Guardar copia en GitHub” / exportar `.ipynb` a `notebooks/` → commit.

---

## Cronograma

### Semana 1 (ahora → reunión con asesor)

| Paso | Entregable | Estado |
|------|------------|--------|
| 1.1 | Repo GitHub + estructura | ✅ |
| 1.2 | Documento contexto + vacíos (borrador) | ✅ borrador |
| 1.3 | Inventario de variables (`transactions` + `members`) | Notebook 01 |
| 1.4 | Muestra estratificada 1.000 `msno` | Notebook 01 |
| 1.5 | Feature table numérica + estándar scaler | Notebook 01 |
| 1.6 | K-Means k=5 + silhouette | Notebook 01 |
| 1.7 | 5 archivos/hojas Excel por cluster | `outputs/` |
| 1.8 | One-pager para asesor | `docs/05-proximos-pasos-asesor.md` |

### Semana 2–3

| Paso | Entregable |
|------|------------|
| 2.1 | Caracterización perfiles (gráficos por cluster) |
| 2.2 | Ordenar clusters por % churn → etiqueta riesgo 0–4 |
| 2.3 | Marco teórico + estado del arte (entrega seminario) |
| 2.4 | Comparar K-Means vs aglomerativo (opcional) |

### Semana 4–8 (Fase 2)

| Paso | Entregable |
|------|------------|
| 3.1 | Escalar a 10k → 100k usuarios si validación OK |
| 3.2 | Agregados de `user_logs` (muestra o SQL) |
| 3.3 | NN clasificador 5 clases + probabilidades |
| 3.4 | Comparación con baseline binario |
| 3.5 | Borrador metodología tesis |

---

## Pipeline técnico (Fase 1)

```
train.csv (msno, is_churn)
        │
        ├──► members.csv ──► categóricas (perfil)
        │
        └──► transactions.csv ──► agregar por msno:
                 • membership_expire_days (juliano)
                 • plan_list_price, actual_amount
                 • payment_num_total, cancel counts
                 • is_auto_renew, is_cancel (perfil)
                        │
                        ▼
              Matriz numérica (n usuarios × p features)
                        │
                        ▼
              StandardScaler → KMeans(n_clusters=5)
                        │
                        ▼
              Unir cluster_id + exportar 5 Excels
                        │
                        ▼
              Tabla % is_churn por cluster + narrativa perfil
```

## Variables (guía asesoría)

**Entran al clustering (numéricas):**
- Días de membresía / expiración (juliano)
- Precio plan, monto pagado acumulado
- Conteo de transacciones, cancelaciones
- Días activos, duración media entre pagos

**No entran al clustering (caracterización):**
- `city`, `gender`, `registered_via`, `payment_method_id`
- `is_cancel` en transacción puntual → perfil agregado

**Etiqueta de validación (no target del k-means):**
- `is_churn` del `train.csv`

## Métodos de clusterización

1. **K-Means (k=5)** — principal, rápido (recomendación asesor).
2. DBSCAN — exploratorio (ruido).
3. Agglomerative — comparación opcional.

## Enlace dataset

https://www.kaggle.com/competitions/kkbox-churn-prediction-challenge/data
