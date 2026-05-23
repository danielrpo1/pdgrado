# Notas para mi reunión con el asesor

**Daniel Restrepo Ospina** — próxima semana

## Lo que acordamos (8 abr 2026)

1. Empezar por **5 clusters de riesgo**, no por red neuronal.
2. Piloto con **~1.000 usuarios**.
3. Priorizar **`transactions`** y variables **numéricas**; categóricas para perfil.
4. Exportar usuarios en **5 hojas Excel**.
5. Hablar de **riesgo / prospectiva**, no solo churn sí/no.
6. Trabajar primero en muestra pequeña (Colab me sirvió para eso).

## Lo que le llevo en esta reunión

| Entregable | Dónde |
|------------|-------|
| Repositorio GitHub | https://github.com/danielrpo1/pdgrado |
| Notebook Colab **ya ejecutado** (gráficos + interpretación) | `notebooks/Colab_Piloto_5_Categorias_Riesgo_KKBox.ipynb` |
| Borrador contexto y vacíos | `docs/01`, `docs/02` |
| Pregunta de investigación (5 categorías) | `docs/03` |
| Excel cinco hojas | `outputs/clusters/usuarios_por_riesgo.xlsx` (local) |

## Resultados de mi piloto (semilla 42)

| Riesgo | Usuarios | % churn |
|--------|----------|---------|
| 0 (bajo) | 712 | ~31% |
| 1 | 20 | ~95% |
| 2 | 177 | ~97% |
| 3 | 83 | 100% |
| 4 (alto) | 8 | 100% |

La forma me convence: a mayor categoría, mayor churn observado.

## Preguntas que quiero validar con usted

1. ¿Le parece bien ordenar los clusters por **% churn** para etiquetar 0–4?
2. ¿Seguimos sin `user_logs` hasta validar transacciones?
3. ¿La pregunta principal del seminario queda la de **variables comportamentales vs. riesgo en 5 categorías**?
4. ¿Próximo hito académico: marco teórico + clasificación multidimensional?

## Después de la reunión (mi plan)

- Completar referencias APA en vacíos de literatura.
- Escribir narrativa de perfil por categoría en el informe.
- Escalar muestra si usted lo ve estable.
- Diseñar Fase 2: red neuronal 5 clases con probabilidades.
