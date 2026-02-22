# Modulo 02: Analisis y Visualizacion de Datos

![Duracion](https://img.shields.io/badge/duracion-8_horas-blue)
![Nivel](https://img.shields.io/badge/nivel-intermedio-yellow)
![Sesiones](https://img.shields.io/badge/sesiones-3_y_4-orange)

---

## Objetivos de Aprendizaje

Al completar este modulo, el docente sera capaz de:

| Competencia | Descripcion |
|-------------|-------------|
| EDA | Realizar analisis exploratorio de datos completo: estadisticas descriptivas, distribuciones, correlaciones, valores faltantes |
| Combinacion de datos | Unir multiples fuentes de datos con merge, join y concat |
| Visualizacion | Crear graficos efectivos con Matplotlib, Seaborn y herramientas low-code |
| SQL | Escribir consultas basicas (SELECT, WHERE, JOIN, GROUP BY) para extraer datos |
| Power BI | Conectar datos, crear modelos, escribir medidas DAX basicas y disenar dashboards interactivos |
| Storytelling | Construir narrativas de datos efectivas para presentaciones academicas |

---

## Contenido

### Sesion 3: EDA y Combinacion de Datos (4h)

| # | Notebook | Descripcion | Duracion |
|---|----------|-------------|----------|
| 1 | [`02_01_eda_exploratorio.ipynb`](notebooks/02_01_eda_exploratorio.ipynb) | Analisis exploratorio completo: describe(), value_counts(), distribucion, outliers, correlacion | 1h 30min |
| 2 | [`02_02_combinacion_datos.ipynb`](notebooks/02_02_combinacion_datos.ipynb) | merge, join, concat — caso: cruzar datos de inscripcion con rendimiento academico | 1h |
| 3 | [`02_03_visualizacion_matplotlib_seaborn.ipynb`](notebooks/02_03_visualizacion_matplotlib_seaborn.ipynb) | Graficos de barras, linea, scatter, box, heatmap con datos economicos | 1h 30min |

**Laboratorios:**
| # | Lab | Descripcion |
|---|-----|-------------|
| 1 | [`lab_03_eda_ejercicios.ipynb`](laboratorios/lab_03_eda_ejercicios.ipynb) | EDA completo sobre dataset de rendimiento academico FACES |
| 2 | [`lab_03_eda_soluciones.ipynb`](laboratorios/lab_03_eda_soluciones.ipynb) | Soluciones comentadas |

### Sesion 4: SQL, Power BI y Storytelling (4h)

| # | Notebook | Descripcion | Duracion |
|---|----------|-------------|----------|
| 4 | [`02_04_sql_introductorio.ipynb`](notebooks/02_04_sql_introductorio.ipynb) | SQL con SQLite: SELECT, WHERE, JOIN, GROUP BY, subconsultas basicas | 1h |
| 5 | [`02_05_power_bi_fundamentos.ipynb`](notebooks/02_05_power_bi_fundamentos.ipynb) | Guia paso a paso: conexion de datos, modelado, DAX basico, visualizaciones, dashboards | 1h 30min |
| 6 | [`02_06_storytelling_datos.ipynb`](notebooks/02_06_storytelling_datos.ipynb) | Narrativa de datos: estructura, contexto, audiencia, diseno para presentaciones academicas | 1h 30min |

**Laboratorios:**
| # | Lab | Descripcion |
|---|-----|-------------|
| 3 | [`lab_04_visualizacion_ejercicios.ipynb`](laboratorios/lab_04_visualizacion_ejercicios.ipynb) | Crear visualizaciones con datos economicos venezolanos |
| 4 | [`lab_04_visualizacion_soluciones.ipynb`](laboratorios/lab_04_visualizacion_soluciones.ipynb) | Soluciones comentadas |
| 5 | [`lab_05_sql_ejercicios.ipynb`](laboratorios/lab_05_sql_ejercicios.ipynb) | Consultas SQL sobre base de datos universitaria |

---

## Datasets Utilizados

| Dataset | Archivo | Descripcion |
|---------|---------|-------------|
| Matricula FACES | [`datasets/universidad/matricula_faces.csv`](../datasets/universidad/matricula_faces.csv) | Datos de inscripcion por carrera y periodo |
| Rendimiento Academico | [`datasets/universidad/rendimiento_academico.csv`](../datasets/universidad/rendimiento_academico.csv) | Notas y factores sociodemograficos |
| Presupuesto Facultad | [`datasets/universidad/presupuesto_facultad.csv`](../datasets/universidad/presupuesto_facultad.csv) | Series temporales de ejecucion presupuestaria |
| Indicadores BCV | [`datasets/economia/indicadores_bcv.csv`](../datasets/economia/indicadores_bcv.csv) | Indicadores macroeconomicos venezolanos |
| Inflacion LATAM | [`datasets/economia/inflacion_latam.csv`](../datasets/economia/inflacion_latam.csv) | Comparacion de inflacion entre paises |

---

## Guias y Recursos

| Recurso | Archivo | Descripcion |
|---------|---------|-------------|
| EDA Paso a Paso | [`guias/eda_paso_a_paso.pdf`](guias/eda_paso_a_paso.pdf) | Guia de referencia para EDA sistematico |
| Power BI Cheat Sheet | [`guias/power_bi_cheatsheet.pdf`](guias/power_bi_cheatsheet.pdf) | Referencia rapida de Power BI y DAX |
| SQL Cheat Sheet | [`guias/sql_cheatsheet.pdf`](guias/sql_cheatsheet.pdf) | Referencia rapida de SQL |

---

## Nota sobre Power BI

Power BI Desktop solo funciona en Windows. Para usuarios de Mac/Linux:
- Usar [Power BI Web](https://app.powerbi.com/) (requiere cuenta Microsoft gratuita)
- El notebook `02_05_power_bi_fundamentos.ipynb` es una guia paso a paso con screenshots, no requiere ejecucion programatica
- Alternativa: Google Looker Studio (gratuito, multiplataforma)

---

## Prerequisitos

- Haber completado el [Modulo 01](../modulo-01-fundamentos/README.md)
- Python y Pandas basico
- Power BI Desktop instalado (ver [guia de setup](../other/setup_checklist.md))

---

[← Modulo 01](../modulo-01-fundamentos/README.md) | [Volver al programa principal](../README.md) | [Siguiente: Modulo 03 →](../modulo-03-modelado-predictivo/README.md)
