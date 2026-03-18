# Programa de Formacion Docente en Ciencia de Datos y Business Intelligence

**Ciencia de Datos y Business Intelligence para Ciencias Sociales, Economia y Administracion**

**Facultad de Ciencias Economicas y Sociales (FACES) — Universidad Catolica Andres Bello (UCAB)**

![Status](https://img.shields.io/badge/estado-activo-brightgreen)
![Modulos](https://img.shields.io/badge/modulos-4-blue)
![Horas](https://img.shields.io/badge/duracion-32_horas-green)
![Python](https://img.shields.io/badge/python-3.10+-3776AB?logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?logo=powerbi&logoColor=black)
![License](https://img.shields.io/badge/licencia-MIT-brightgreen)

---

## Descripcion del Programa

Programa de formacion dirigido a **docentes universitarios** de las carreras de Economia, Administracion, Contaduria y Relaciones Industriales de FACES-UCAB. Su objetivo es desarrollar competencias practicas en ciencia de datos y Business Intelligence que puedan aplicarse directamente en la docencia, la investigacion academica y la gestion universitaria.

**Fecha:** 17 de marzo al 14 de mayo de 2026
**Horario:** 6:00 p.m. a 8:00 p.m. (Venezuela)
**Modalidad:** Virtual — clases en vivo + trabajo autonomo guiado
**Duracion:** 32 horas (4 modulos)
**Plataforma:** [gonzalezulises.github.io/formacion-docente-bi-faces](https://gonzalezulises.github.io/formacion-docente-bi-faces/)

---

## Especialistas

| Modulo | Especialista | Horas | Fechas |
|--------|-------------|-------|--------|
| 1. Pensar con datos | Ulises Gonzalez | 6h | 24, 26 mar & 6 abr |
| 2. Data Wrangling | Gabriel Gomez | 8h | 7, 9, 13, 14 abr |
| 3. Business Intelligence | Ilda Rojas | 10h | 16, 21, 23, 28, 30 abr |
| 4. Modelos predictivos | Ricardo Navarro | 8h | 5, 7, 12, 14 may |

**Experiencia estudiantil:** Fabiola De Benedectis (acompanamiento transversal)

---

## Estructura del Programa

| Modulo | Titulo | Horas | Contenido Clave | Detalle |
|--------|--------|-------|------------------|---------|
| 01 | [Pensar con datos en ciencias sociales](modulo-01-fundamentos/) | 6h | Ciclo de valor, sesgos, tipos de analisis, casos reales | [README](modulo-01-fundamentos/README.md) |
| 02 | [Data Wrangling accesible (Python + SQL)](modulo-02-data-wrangling/) | 8h | Python, Pandas, NumPy, SQL, limpieza de datos | [README](modulo-02-data-wrangling/README.md) |
| 03 | [Business Intelligence aplicado a decisiones](modulo-03-business-intelligence/) | 10h | Visualizacion, Power BI, Tableau, KPIs, narrativa | [README](modulo-03-business-intelligence/README.md) |
| 04 | [Modelos predictivos simples y proyecto integrador](modulo-04-predictivo-proyecto/) | 8h | Regresion, clasificacion, flujo completo, proyecto final | [README](modulo-04-predictivo-proyecto/README.md) |

---

## Participantes

Docentes de pregrado y posgrado que:

- Disenan e imparten asignaturas con contenido cuantitativo
- Poseen manejo basico de hoja de calculo (Excel u otros)
- Tienen nociones de estadistica descriptiva e inferencia basica
- Requieren integrar analisis de datos, dashboards y modelos en sus cursos
- Estan dispuestos a aprender herramientas digitales nuevas

---

## Prerequisitos

### Conocimientos previos
- Manejo basico de hojas de calculo (Excel/Google Sheets)
- Nociones de estadistica descriptiva (promedios, varianzas, correlaciones)
- No se requiere experiencia previa en programacion

### Software necesario
- [Google Colab](https://colab.research.google.com/) (opcion recomendada — sin instalacion)
- [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (Windows) o [Tableau Public](https://public.tableau.com/) (multiplataforma)
- Navegador web actualizado

---

## Evaluacion

| Componente | Peso | Descripcion |
|-----------|------|-------------|
| Portafolio de analisis de datos | 40% | Dataset limpio y documentado + notebook con proceso de limpieza y analisis |
| Dashboard de BI | 30% | Dashboard funcional con al menos 3 visualizaciones + explicacion de uso |
| Proyecto de curso con modelo | 30% | Descripcion del proyecto, modelo aplicado y rubrica de evaluacion |

---

## Datasets

El programa incluye 10 datasets sinteticos contextualizados a FACES:

| Categoria | Datasets |
|-----------|----------|
| Universidad | `matricula_faces.csv`, `rendimiento_academico.csv`, `presupuesto_facultad.csv`, `encuesta_docente.csv` |
| Economia | `indicadores_bcv.csv`, `inflacion_latam.csv`, `comercio_exterior.csv` |
| Empresarial | `ventas_retail.csv`, `rrhh_nomina.csv`, `estados_financieros.csv` |

Ver [datasets/README.md](datasets/README.md) para descripcion detallada de cada dataset.

---

## Estructura del Repositorio

```
formacion-docente-bi-faces/
├── modulo-01-fundamentos/          # Pensar con datos (Ulises, 6h)
│   ├── notebooks/                  # 5 notebooks conceptuales
│   └── laboratorios/               # Lab: Traduce tu asignatura a datos
├── modulo-02-data-wrangling/       # Data Wrangling (Gabriel, 8h)
│   ├── notebooks/                  # Python, Pandas, SQL, wrangling avanzado
│   └── laboratorios/               # EDA, SQL, entregable dataset limpio
├── modulo-03-business-intelligence/ # BI aplicado (Ilda, 10h)
│   ├── notebooks/                  # Visualizacion, Power BI, KPIs, Tableau
│   ├── laboratorios/               # Dashboard paso a paso, rediseno, entregable
│   └── recursos/                   # Material complementario
├── modulo-04-predictivo-proyecto/  # Predictivo + Proyecto (Ricardo, 8h)
│   ├── notebooks/                  # Regresion, clasificacion, flujo completo
│   ├── laboratorios/               # Regresion y clasificacion aplicada
│   └── proyecto-integrador/        # Templates por carrera, rubrica, guias
├── datasets/                       # 10 CSVs contextualizados a FACES
├── scripts/                        # Generador de datasets
├── archivo/                        # Contenido original pre-reestructuracion
├── other/                          # Setup checklist, recursos profesionales
├── index.html                      # Landing page (GitHub Pages)
└── requirements.txt                # Dependencias Python
```

---

## Recursos Adicionales

- [Setup Checklist](other/setup_checklist.md) — Guia de configuracion del entorno
- [Recursos de Desarrollo Profesional](other/recursos_desarrollo_profesional.md) — Certificaciones y materiales post-curso
- [Fuentes de Datos Publicos](modulo-04-predictivo-proyecto/proyecto-integrador/fuentes_datos_publicos.md) — Catalogo de datos abiertos

---

## Licencia

MIT License — ver [LICENSE](LICENSE) para detalles.

---

*Programa disenado y desarrollado por [Rizoma](https://rizo.ma) para la Facultad de Ciencias Economicas y Sociales (FACES) de la UCAB.*
