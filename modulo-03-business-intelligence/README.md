# Módulo 03 — Business Intelligence aplicado a decisiones

![Duración](https://img.shields.io/badge/duración-10_horas-blue)
![Nivel](https://img.shields.io/badge/nivel-intermedio-yellow)
![Instructora](https://img.shields.io/badge/instructora-Ilda_Rojas-green)
![Fechas](https://img.shields.io/badge/fechas-16,_21,_23,_28,_30_abr-lightgrey)

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=flat-square&logo=tableau&logoColor=white)
![KPIs](https://img.shields.io/badge/KPIs_&_métricas-2c3e50?style=flat-square)
![Storytelling](https://img.shields.io/badge/storytelling_con_datos-8e44ad?style=flat-square)
![Dashboards](https://img.shields.io/badge/dashboards-3498db?style=flat-square)
![DAX](https://img.shields.io/badge/DAX-F2C811?style=flat-square)

---

## Objetivos de aprendizaje

Al finalizar este módulo, el participante será capaz de:

1. Aplicar principios de visualización eficaz para comunicar datos de forma clara y honesta
2. Utilizar Power BI para importar, transformar y visualizar datos académicos
3. Definir y calcular KPIs relevantes para la gestión universitaria
4. Construir narrativas con datos orientadas a la toma de decisiones
5. Crear dashboards interactivos en Power BI y Tableau

---

## Contenido por sesión

| Sesión | Fecha | Tema | Duración |
|---|---|---|---|
| 03.01 | 16 abril | Principios de visualización eficaz | 2h |
| 03.02 | 21 abril | Introducción a Power BI | 2h |
| 03.03 | 23 abril | KPIs para FACES | 2h |
| 03.04 | 28 abril | Narrativa con datos | 2h |
| 03.05 | 30 abril | Introducción a Tableau | 2h |

---

## Archivos del módulo

### Notebooks (sesiones teórico-prácticas)

| Archivo | Descripción |
|---|---|
| `notebooks/03_01_principios_visualizacion.ipynb` | Elección de gráficos, Gestalt, pre-attentive attributes, distorsiones |
| `notebooks/03_02_power_bi_fundamentos.ipynb` | Power Query, modelo de datos, DAX básico, visualizaciones |
| `notebooks/03_03_kpis_faces.ipynb` | KPIs académicos, organizacionales, socioeconómicos y financieros |
| `notebooks/03_04_narrativa_datos.ipynb` | Framework de storytelling, reportes ejecutivos, audiencias |
| `notebooks/03_05_tableau_fundamentos.ipynb` | Dimensiones y medidas, gráficos, dashboards, comparación con Power BI |

### Laboratorios

| Archivo | Descripción |
|---|---|
| `laboratorios/lab_05_dashboard_paso_a_paso.ipynb` | Construir un dashboard completo en Power BI |
| `laboratorios/lab_06_rediseno_dashboard.ipynb` | Identificar errores y rediseñar un dashboard |
| `laboratorios/entregable_dashboard_prototipo.ipynb` | Template del entregable final del módulo |

### Recursos

Directorio `recursos/` disponible para materiales complementarios.

---

## Materiales del instructor (Ilda Rojas)

Las diapositivas originales compartidas por la instructora están en [`materiales-instructor/`](materiales-instructor/README.md), organizadas por sesión con un `README.md` que resume la agenda y conecta los temas con los notebooks del repo.

| Sesión | Fecha | Carpeta | Enfoque |
|--------|-------|---------|---------|
| 03.01 | 16 abr | [`sesion-01-power-bi-fundamentos/`](materiales-instructor/sesion-01-power-bi-fundamentos/README.md) | Fundamentos de Power BI: instalación, historia del BI, visualización, modelado relacional, esquema estrella, cardinalidad |

---

## Prerequisitos

- **Módulos 1 y 2 completados** (fundamentos de datos y análisis con Python)
- Manejo básico de hojas de cálculo (Excel / Google Sheets)
- Cuenta de correo para registrarse en servicios gratuitos

---

## Software requerido

| Software | Plataforma | Costo | Uso |
|---|---|---|---|
| **Power BI Desktop** | Windows | Gratuito | Herramienta principal del módulo |
| **Tableau Public** | Windows / Mac | Gratuito | Alternativa y complemento |
| **Google Looker Studio** | Web (cualquier SO) | Gratuito | Alternativa si no tiene Windows |

### Instalación de Power BI Desktop

1. Ir a [powerbi.microsoft.com](https://powerbi.microsoft.com/desktop/)
2. Descargar Power BI Desktop (requiere Windows 10/11)
3. Instalar con opciones por defecto
4. No requiere cuenta Microsoft para uso local

### Para usuarios de Mac/Linux

Si no dispone de Windows, puede:
- Usar **Tableau Public** (disponible para Mac)
- Usar **Google Looker Studio** (web, cualquier sistema operativo)
- Instalar Windows en una máquina virtual (VirtualBox, Parallels)

---

## Datasets utilizados

Los datasets se encuentran en `../datasets/universidad/`:

| Archivo | Descripción |
|---|---|
| `rendimiento_academico.csv` | Notas, carreras, estados por estudiante |
| `matricula_faces.csv` | Datos de matrícula por carrera y período |
| `presupuesto_facultad.csv` | Distribución presupuestaria |
| `encuesta_docente.csv` | Resultados de encuesta a docentes |

---

## Evaluación

| Componente | Peso | Descripción |
|---|---|---|
| Participación en laboratorios | 30% | Labs 05 y 06 |
| Entregable: Prototipo de dashboard | 50% | Dashboard funcional + documentación |
| Ejercicios en clase | 20% | Actividades de los notebooks |
