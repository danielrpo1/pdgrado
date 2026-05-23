# Avance del piloto — notas de seguimiento

**Daniel Restrepo Ospina**

## Enfoque de la Fase 1

- Cinco categorías de riesgo vía clustering (no modelo binario primero).
- Variables numéricas de `transactions`; categóricas para perfil.
- Exportación a Excel (cinco hojas).
- Piloto ampliado de **1.000 → 10.000 usuarios** para segmentos más estables.

## Entregables en el repositorio

| Item | Ubicación |
|------|-----------|
| Código y pipeline | https://github.com/danielrpo1/pdgrado |
| Notebook Colab ejecutado | `notebooks/Colab_Piloto_5_Categorias_Riesgo_KKBox.ipynb` |
| Contexto y vacíos (borrador) | `docs/01`, `docs/02` |
| Preguntas de investigación | `docs/03` |
| Excel por categoría | `outputs/clusters/usuarios_por_riesgo.xlsx` |

## Resultados (10k usuarios, semilla 42)

| Riesgo | Usuarios | % churn |
|--------|----------|---------|
| 0 | 7.222 | 32,1% |
| 1 | 170 | 85,9% |
| 2 | 99 | 91,9% |
| 3 | 1.665 | 96,2% |
| 4 | 844 | 100% |

La gradación 0→4 se mantiene. Con 10k hay más usuarios en categorías medias y altas que en el piloto de 1k, lo que facilita leer perfiles con más confianza.

## Preguntas abiertas del diseño

1. ¿Mantener el orden de riesgo por % de churn observado?
2. ¿Postergar `user_logs` hasta cerrar el marco con transacciones?
3. ¿Escalar a 50k–100k o pasar a Fase 2 (red neuronal 5 clases)?

## Siguiente trabajo

- Referencias APA en vacíos de literatura (clasificación multidimensional).
- Narrativa de perfiles por categoría en el informe del seminario.
- Diseño del clasificador con probabilidades por segmento.
