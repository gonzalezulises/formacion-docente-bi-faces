# Modulo 03: Modelado Predictivo y Machine Learning Aplicado

![Duracion](https://img.shields.io/badge/duracion-8_horas-blue)
![Nivel](https://img.shields.io/badge/nivel-intermedio--avanzado-red)
![Sesiones](https://img.shields.io/badge/sesiones-5_y_6-orange)

---

## Objetivos de Aprendizaje

Al completar este modulo, el docente sera capaz de:

| Competencia | Descripcion |
|-------------|-------------|
| Regresion lineal | Construir modelos de regresion para proyecciones presupuestarias e indicadores economicos |
| Regresion logistica | Aplicar clasificacion binaria a problemas como prediccion de desercion o riesgo crediticio |
| Arboles de decision | Usar arboles para segmentacion de estudiantes y toma de decisiones explicables |
| Clustering | Segmentar perfiles (docentes, estudiantes, instituciones) con K-Means |
| Series temporales | Analizar tendencias, estacionalidad y hacer proyecciones de indicadores economicos |
| Interpretabilidad | Explicar predicciones de modelos usando SHAP y feature importance |
| Evaluacion | Seleccionar metricas apropiadas y evaluar modelos de forma critica |

---

## Contenido

### Sesion 5: Modelos Supervisados (4h)

| # | Notebook | Descripcion | Duracion |
|---|----------|-------------|----------|
| 1 | [`03_01_regresion_lineal.ipynb`](notebooks/03_01_regresion_lineal.ipynb) | Regresion lineal simple y multiple. Casos: proyeccion presupuestaria, indicadores economicos | 1h 15min |
| 2 | [`03_02_evaluacion_modelos.ipynb`](notebooks/03_02_evaluacion_modelos.ipynb) | MSE, RMSE, R2, matriz de confusion, accuracy, precision, recall, F1 | 45min |
| 3 | [`03_03_regresion_logistica.ipynb`](notebooks/03_03_regresion_logistica.ipynb) | Clasificacion binaria. Casos: prediccion de desercion estudiantil, aprobacion crediticia | 1h |
| 4 | [`03_04_arboles_decision.ipynb`](notebooks/03_04_arboles_decision.ipynb) | Arboles de decision y Random Forest. Caso: segmentacion de estudiantes por riesgo | 1h |

**Laboratorios:**
| # | Lab | Descripcion |
|---|-----|-------------|
| 1 | [`lab_06_regresion_ejercicios.ipynb`](laboratorios/lab_06_regresion_ejercicios.ipynb) | Modelo predictivo sobre rendimiento academico |
| 2 | [`lab_07_clasificacion_ejercicios.ipynb`](laboratorios/lab_07_clasificacion_ejercicios.ipynb) | Clasificacion con datos financieros |

### Sesion 6: Clustering, Series Temporales e Interpretabilidad (4h)

| # | Notebook | Descripcion | Duracion |
|---|----------|-------------|----------|
| 5 | [`03_05_clustering.ipynb`](notebooks/03_05_clustering.ipynb) | K-Means, elbow method, silhouette. Caso: tipologias de gestion, perfiles docentes | 1h |
| 6 | [`03_06_series_temporales.ipynb`](notebooks/03_06_series_temporales.ipynb) | Tendencia, estacionalidad, descomposicion, ARIMA basico. Caso: indicadores BCV, presupuesto | 1h 30min |
| 7 | [`03_07_interpretabilidad_shap.ipynb`](notebooks/03_07_interpretabilidad_shap.ipynb) | Feature importance, SHAP values, graficos de explicabilidad. Como comunicar resultados de modelos | 1h 30min |

**Laboratorios:**
| # | Lab | Descripcion |
|---|-----|-------------|
| 3 | [`lab_08_clustering_ejercicios.ipynb`](laboratorios/lab_08_clustering_ejercicios.ipynb) | Segmentacion de perfiles con datos de encuesta docente |
| 4 | [`lab_09_series_temporales_ejercicios.ipynb`](laboratorios/lab_09_series_temporales_ejercicios.ipynb) | Analisis temporal de indicadores economicos |

---

## Datasets Utilizados

| Dataset | Archivo | Descripcion |
|---------|---------|-------------|
| Rendimiento Academico | [`datasets/universidad/rendimiento_academico.csv`](../datasets/universidad/rendimiento_academico.csv) | Target para regresion y clasificacion |
| Presupuesto Facultad | [`datasets/universidad/presupuesto_facultad.csv`](../datasets/universidad/presupuesto_facultad.csv) | Series temporales de ejecucion presupuestaria |
| Encuesta Docente | [`datasets/universidad/encuesta_docente.csv`](../datasets/universidad/encuesta_docente.csv) | Datos para clustering de perfiles |
| Indicadores BCV | [`datasets/economia/indicadores_bcv.csv`](../datasets/economia/indicadores_bcv.csv) | Series temporales macroeconomicas |
| Ventas Retail | [`datasets/empresarial/ventas_retail.csv`](../datasets/empresarial/ventas_retail.csv) | Regresion y forecasting |
| Estados Financieros | [`datasets/empresarial/estados_financieros.csv`](../datasets/empresarial/estados_financieros.csv) | Ratios financieros para clasificacion |
| Bikeshare | [`datasets/generales/bikeshare.csv`](../datasets/generales/bikeshare.csv) | Dataset introductorio para regresion |

---

## Guias y Recursos

| Recurso | Archivo | Descripcion |
|---------|---------|-------------|
| ML Workflow Cheat Sheet | [`guias/ml_workflow_cheatsheet.pdf`](guias/ml_workflow_cheatsheet.pdf) | Pipeline completo: datos → preprocesamiento → modelo → evaluacion |

---

## Nota Pedagogica

Este modulo prioriza la **interpretacion y aplicacion** sobre la teoria matematica. Los docentes no necesitan derivar gradientes — necesitan entender:
- Cuando usar cada tipo de modelo
- Como evaluar si un modelo es util
- Como explicar los resultados a una audiencia no tecnica
- Como aplicar estos conceptos en su docencia e investigacion

---

## Prerequisitos

- Haber completado los [Modulos 01](../modulo-01-fundamentos/README.md) y [02](../modulo-02-analisis-visualizacion/README.md)
- Python, Pandas y visualizacion basica
- Conceptos estadisticos basicos (media, mediana, desviacion estandar, correlacion)

---

[← Modulo 02](../modulo-02-analisis-visualizacion/README.md) | [Volver al programa principal](../README.md) | [Siguiente: Modulo 04 →](../modulo-04-proyectos-integradores/README.md)
