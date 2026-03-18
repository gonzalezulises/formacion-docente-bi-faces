# Módulo 2 — Data Wrangling accesible (Python + SQL)

![Duración](https://img.shields.io/badge/duración-8_horas-blue)
![Nivel](https://img.shields.io/badge/nivel-intermedio-yellow)
![Instructor](https://img.shields.io/badge/instructor-Gabriel_Gómez-green)

---

## Descripción

Este módulo enseña las habilidades fundamentales de limpieza y preparación de datos usando Python (Pandas) y SQL. Los participantes aprenderán a transformar datos crudos en datasets listos para análisis, con énfasis en decisiones contextuales y reproducibilidad.

## Fechas

| Sesión | Fecha | Duración |
|--------|-------|----------|
| 1 | 7 de abril 2026 | 2h |
| 2 | 9 de abril 2026 | 2h |
| 3 | 13 de abril 2026 | 2h |
| 4 | 14 de abril 2026 | 2h |

---

## Objetivos de Aprendizaje

Al completar este módulo, el docente será capaz de:

| Competencia | Descripción |
|-------------|-------------|
| Entorno de trabajo | Configurar y usar Google Colab/Jupyter para análisis de datos |
| Python básico | Manejar variables, listas, diccionarios y funciones para manipular datos |
| EDA | Realizar análisis exploratorio de datos: estadísticas descriptivas, distribuciones, correlaciones, valores faltantes |
| Combinación de datos | Unir múltiples fuentes de datos con merge, join y concat |
| SQL | Escribir consultas básicas (SELECT, WHERE, JOIN, GROUP BY) para extraer datos |
| Wrangling avanzado | Limpiar datasets: tratar faltantes, detectar outliers, crear variables derivadas |
| Documentación | Producir un dataset limpio y documentado con diccionario de variables |

---

## Contenido

### Notebooks (en orden)

| # | Notebook | Tema | Duración |
|---|----------|------|----------|
| 0 | [`02_00_entorno_python.ipynb`](notebooks/02_00_entorno_python.ipynb) | Entorno de trabajo: Colab, Jupyter, Python básico, primer contacto con Pandas | 1h |
| 1 | [`02_01_eda_exploratorio.ipynb`](notebooks/02_01_eda_exploratorio.ipynb) | Análisis exploratorio completo: describe(), value_counts(), distribución, outliers, correlación | 1.5h |
| 2 | [`02_02_combinacion_datos.ipynb`](notebooks/02_02_combinacion_datos.ipynb) | merge, join, concat — caso: cruzar datos de inscripción con rendimiento académico | 1.5h |
| 3 | [`02_03_sql_introductorio.ipynb`](notebooks/02_03_sql_introductorio.ipynb) | SQL con SQLite: SELECT, WHERE, JOIN, GROUP BY, subconsultas básicas | 1h |
| 4 | [`02_04_wrangling_avanzado.ipynb`](notebooks/02_04_wrangling_avanzado.ipynb) | read_excel, variables derivadas, tratamiento de faltantes y outliers contextuales | 1.5h |

### Laboratorios

| # | Lab | Descripción |
|---|-----|-------------|
| 1 | [`lab_03_eda_ejercicios.ipynb`](laboratorios/lab_03_eda_ejercicios.ipynb) | EDA completo sobre dataset de rendimiento académico FACES |
| 2 | [`lab_03_eda_soluciones.ipynb`](laboratorios/lab_03_eda_soluciones.ipynb) | Soluciones comentadas |
| 3 | [`lab_03b_combinacion_ejercicios.ipynb`](laboratorios/lab_03b_combinacion_ejercicios.ipynb) | Ejercicios de combinación de datos |
| 4 | [`lab_05_sql_ejercicios.ipynb`](laboratorios/lab_05_sql_ejercicios.ipynb) | Consultas SQL sobre base de datos universitaria |
| 5 | [`lab_05_sql_soluciones.ipynb`](laboratorios/lab_05_sql_soluciones.ipynb) | Soluciones comentadas |

### Entregable

| Archivo | Descripción |
|---------|-------------|
| [`entregable_dataset_limpio.ipynb`](laboratorios/entregable_dataset_limpio.ipynb) | Plantilla del entregable: dataset limpio y documentado |

---

## Datasets Utilizados

| Dataset | Archivo | Descripción |
|---------|---------|-------------|
| Matrícula FACES | [`universidad/matricula_faces.csv`](../datasets/universidad/matricula_faces.csv) | Datos de inscripción por carrera y periodo |
| Rendimiento Académico | [`universidad/rendimiento_academico.csv`](../datasets/universidad/rendimiento_academico.csv) | Notas y factores sociodemográficos |
| Presupuesto Facultad | [`universidad/presupuesto_facultad.csv`](../datasets/universidad/presupuesto_facultad.csv) | Series temporales de ejecución presupuestaria |
| Encuesta Docente | [`universidad/encuesta_docente.csv`](../datasets/universidad/encuesta_docente.csv) | Encuesta de evaluación docente |
| RRHH Nómina | [`empresarial/rrhh_nomina.csv`](../datasets/empresarial/rrhh_nomina.csv) | Nómina de recursos humanos |
| Ventas Retail | [`empresarial/ventas_retail.csv`](../datasets/empresarial/ventas_retail.csv) | Ventas de comercio minorista |

---

## Prerrequisitos

- Haber completado el [Módulo 01](../modulo-01-fundamentos/README.md)

---

[← Módulo 01](../modulo-01-fundamentos/README.md) | [Volver al programa principal](../README.md) | [Siguiente: Módulo 03 →](../modulo-03-modelado-predictivo/README.md)
