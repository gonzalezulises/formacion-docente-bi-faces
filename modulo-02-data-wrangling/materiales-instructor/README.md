# Materiales del instructor — Módulo 02

> **Instructor:** Gabriel Gómez
> **Fuente:** carpeta compartida `Data Wrangling accesible (Python + SQL)` (2026-04-22)
> **Drive:** https://drive.google.com/drive/folders/1HR8-Lz9hh-neLj2IAA_9D5pZltyaO5TN

Esta carpeta reproduce los materiales originales del instructor organizados por clase, y añade un `README.md` por subcarpeta con el **código extraído en markdown legible** (los `.docx` quedan como referencia autoritativa).

---

## Contenido

| Carpeta / archivo | Sesión | Temas |
|-------------------|--------|-------|
| [`presentacion_data_wrangling.pptx`](presentacion_data_wrangling.pptx) | Todas | Diapositivas generales del módulo |
| [`clase-01-limpieza/`](clase-01-limpieza/README.md) | Clase 1 — 7 abr | Limpieza con Pandas (matrícula FACES) + ejercicio con `Hipotecas.xlsx` |
| [`clase-02-graficos/`](clase-02-graficos/README.md) | Clase 2 — 9 abr | EDA y visualización (boxplot, IQR, histograma, stem) sobre `Insurance claims.csv` |
| [`clase-03-outliers/`](clase-03-outliers/README.md) | Clase 3 — 13 abr | Detección de outliers con **KNN** (`tserie.csv`) y **Isolation Forest** (`jewellery.csv`) |
| [`clase-04-sql/`](clase-04-sql/README.md) | Clase 4 — 14 abr | Consultas SQL: `JOIN`, `GROUP BY`, `HAVING`, `CTE`, `INSERT`, `UPDATE` |
| [`actividad-2-pdf/`](actividad-2-pdf/README.md) | Actividad integradora | Lectura/transformación de datos desde PDF (población de Panamá) |

---

## Datasets

| Dataset | Ubicación | Tamaño | Notas |
|---------|-----------|--------|-------|
| `Hipotecas.xlsx` | [`clase-01-limpieza/`](clase-01-limpieza/Hipotecas.xlsx) | 68 KB | ✅ En repo |
| `insurance_claims.csv.gz` | [`clase-02-graficos/`](clase-02-graficos/insurance_claims.csv.gz) | 640 KB (11.7 MB sin comprimir) | ✅ En repo — Pandas lee `.csv.gz` directo |
| `tserie.csv` | [`clase-03-outliers/`](clase-03-outliers/tserie.csv) | 260 KB | ✅ En repo |
| `poblacion_provincias_panama.pdf` | [`actividad-2-pdf/`](actividad-2-pdf/poblacion_provincias_panama.pdf) | 112 KB | ✅ En repo |
| `jewellery.csv` | URL pública PyCaret | — | Descarga en código |

---

## Relación con los notebooks del repositorio

| Material instructor | Notebook del repo |
|---------------------|-------------------|
| Clase 1 — limpieza | [`02_00_entorno_python.ipynb`](../notebooks/02_00_entorno_python.ipynb), [`02_04_wrangling_avanzado.ipynb`](../notebooks/02_04_wrangling_avanzado.ipynb) |
| Clase 2 — gráficos | [`02_01_eda_exploratorio.ipynb`](../notebooks/02_01_eda_exploratorio.ipynb) |
| Clase 3 — outliers | [`02_01_eda_exploratorio.ipynb`](../notebooks/02_01_eda_exploratorio.ipynb), [`02_04_wrangling_avanzado.ipynb`](../notebooks/02_04_wrangling_avanzado.ipynb) |
| Clase 4 — SQL | [`02_03_sql_introductorio.ipynb`](../notebooks/02_03_sql_introductorio.ipynb), [`../laboratorios/lab_05_sql_ejercicios.ipynb`](../laboratorios/lab_05_sql_ejercicios.ipynb) |
| Actividad 2 — PDF | [`02_04_wrangling_avanzado.ipynb`](../notebooks/02_04_wrangling_avanzado.ipynb) |

---

[← Volver al Módulo 02](../README.md)
