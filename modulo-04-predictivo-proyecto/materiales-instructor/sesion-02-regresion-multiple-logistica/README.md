# Sesión 2 — Regresión Múltiple, Logística y Logarítmica

Materiales entregados por el instructor **Ricardo Navarro** para la segunda sesión del Módulo 04 (Modelos predictivos simples), dictada el **7 de mayo de 2026**. Corresponde a la **Sesión 8** del programa.

## Contenido

| Archivo | Descripción |
|---|---|
| [`modelos_predictivos_multiple_logaritmica.pptx`](modelos_predictivos_multiple_logaritmica.pptx) | Diapositivas de la sesión: repaso de fundamentos, evaluación formativa del módulo, regresión múltiple, regresión logística (binaria), regresión logarítmica y guía del proyecto integrador |
| [`regresion_multiple_logaritmica.ipynb`](regresion_multiple_logaritmica.ipynb) | Notebook guiado: regresión lineal múltiple y regresión logarítmica paso a paso con datos de Venezuela, comparación de los tres modelos y ejercicios propuestos |

## Agenda de la sesión

1. **Repaso** — instructor, estructura del curso, CRISP-DM, EDA y correlación (recapitulación de la Sesión 1).
2. **Evaluación formativa del módulo** — Participación 20%, Proyecto 30%, Tareas 50%; sistema de puntos y bonificación por trabajo anticipado.
3. **Regresión múltiple** — de una a varias variables: Ŷ = β₀ + β₁X₁ + β₂X₂ + … + βₖXₖ + ε.
   - **Coeficiente parcial** — efecto de X₁ manteniendo el resto constante (*ceteris paribus*).
   - **R² ajustado** — penaliza variables irrelevantes; útil para comparar modelos.
   - **Multicolinealidad** — VIF > 10 indica coeficientes inestables; solución: Ridge regression.
   - Caso aplicado: determinantes del salario (educación, experiencia, género).
4. **Regresión binaria (logística)** — predecir una probabilidad y clasificar en dos categorías.
   - **Función sigmoide** — P(y=1) = 1 / (1 + e⁻ᶻ); umbral 0.5.
   - Implementación con `sklearn.linear_model.LogisticRegression` y `predict_proba`.
5. **Regresión logarítmica** — modelar crecimiento que se desacelera: y = a + b·ln(x).
   - Cuándo usarla (X siempre positiva, residuos del modelo lineal con patrón curvo) y cuándo **no**.
   - Ajuste con `scipy.optimize.curve_fit`.
   - Guía rápida para elegir entre modelo lineal, logarítmico, exponencial o polinómico.
6. **Guía del proyecto integrador** — formular la pregunta (Y y predictores con justificación teórica), datos y EDA (DANE, Banco Mundial, Kaggle), ajustar el modelo OLS y verificar supuestos.
7. **Rúbrica de evaluación del proyecto integrador.**
8. **Cierre** — síntesis del curso: herramienta cuantitativa, analítica con Python, interpretación crítica y proyecto real.

## Relación con los notebooks del módulo

| Concepto de la sesión | Notebook del repo |
|---|---|
| Regresión logística / clasificación binaria | [`notebooks/04_03_clasificacion_binaria.ipynb`](../../notebooks/04_03_clasificacion_binaria.ipynb) |
| Flujo completo end-to-end (CRISP-DM en código) | [`notebooks/04_04_flujo_completo.ipynb`](../../notebooks/04_04_flujo_completo.ipynb) |
| Práctica guiada de clasificación | [`laboratorios/lab_08_clasificacion_ejercicios.ipynb`](../../laboratorios/lab_08_clasificacion_ejercicios.ipynb) |
| Guía y rúbrica del proyecto integrador | [`proyecto-integrador/`](../../proyecto-integrador/) |

## Referencias citadas en las diapositivas

- CRISP-DM — *Cross-Industry Standard Process for Data Mining*.
- VIF (Variance Inflation Factor) para diagnóstico de multicolinealidad.
- Fuentes de datos del notebook: UNESCO, CEPAL, Banco Mundial, INE Venezuela.
- Fuentes sugeridas para el proyecto: DANE, Banco Mundial, Kaggle.
