# Sesión 1 — Fundamentos y Regresión Lineal

Materiales entregados por el instructor **Ricardo Navarro** para la primera sesión del Módulo 04 (Modelos predictivos simples), dictada el **5 de mayo de 2026**. Corresponde a la **Sesión 7** del programa.

## Contenido

| Archivo | Descripción |
|---|---|
| [`modelos_predictivos_simples.pptx`](modelos_predictivos_simples.pptx) | Diapositivas de la sesión: estructura del curso, CRISP-DM, estadística descriptiva e inferencial, EDA, correlación vs. causalidad, ecuación de la recta y regresión lineal simple |
| [`regresion_lineal_basico.ipynb`](regresion_lineal_basico.ipynb) | Notebook guiado para principiantes: regresión lineal simple paso a paso con datos reales de Venezuela (gasto en educación vs. matrícula universitaria), incluye ejercicios propuestos |

## Agenda de la sesión

1. **Presentación e instructor** — trayectoria multisectorial en BI, analítica y gobierno de datos.
2. **Estructura del curso** — 4 sesiones, 8 horas: Fundamentos + Regresión Lineal → Regresión Múltiple → Interpretación Prudente → Proyecto Integrador.
3. **¿Por qué modelos predictivos?** — aplicaciones en Ciencias Sociales, Economía y Administración: ir más allá del análisis descriptivo.
4. **¿Por qué Python?** — `pandas` (manipulación), `statsmodels` (salida estadística: p-valores, IC, R²), `scikit-learn` (ML), `matplotlib`/`seaborn` (visualización).
5. **Metodología CRISP-DM** — las 6 fases: comprensión del negocio → comprensión de los datos → preparación → modelado → evaluación → despliegue.
6. **Estadística descriptiva vs. inferencial** — resumir lo observado vs. inferir sobre una población.
7. **Análisis exploratorio de datos (EDA)** — tendencia central, cuantiles y forma, dispersión, visualización.
8. **Correlación y regresión** — qué mide cada una; correlación detecta asociación, **no causalidad**.
9. **Diagramas de correlación** — scatter plot, heatmap, pairplot.
10. **Coeficientes de correlación** — Pearson, Spearman, Kendall: cuándo usar cada uno.
11. **Correlación ≠ causalidad** — correlaciones espurias y variables confusoras.
12. **Ecuación de la recta** — pendiente (m), intercepto (b), interpretación.
13. **Regresión lineal** — fórmula Ŷ = β₀ + β₁X + ε, interpretación de coeficientes, bondad de ajuste (R²).
14. **Ejemplo aplicado** — ingreso vs. gasto en educación con `sm.OLS(...).fit()` y `model.summary()`.

## Relación con los notebooks del módulo

| Concepto de la sesión | Notebook del repo |
|---|---|
| EDA, correlación, regresión lineal simple | [`notebooks/04_01_regresion_lineal.ipynb`](../../notebooks/04_01_regresion_lineal.ipynb) |
| Bondad de ajuste, R², MSE/RMSE, validación train/test | [`notebooks/04_02_evaluacion_modelos.ipynb`](../../notebooks/04_02_evaluacion_modelos.ipynb) |
| Práctica guiada de regresión | [`laboratorios/lab_07_regresion_ejercicios.ipynb`](../../laboratorios/lab_07_regresion_ejercicios.ipynb) |

## Referencias citadas en las diapositivas

- CRISP-DM — *Cross-Industry Standard Process for Data Mining*.
- George E. P. Box — *"Todos los modelos son incorrectos, pero algunos son útiles."*
- Fuentes de datos del notebook: UNESCO, CEPAL, Banco Mundial, INE Venezuela.
