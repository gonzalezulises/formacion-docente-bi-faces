# Programa de Formacion Docente en Ciencia de Datos Aplicada y Business Intelligence

**Facultad de Ciencias Economicas y Sociales (FACES) — Universidad Catolica Andres Bello (UCAB)**

![Status](https://img.shields.io/badge/estado-en_desarrollo-yellow)
![Modulos](https://img.shields.io/badge/modulos-4-blue)
![Horas](https://img.shields.io/badge/duracion-32_horas-green)
![Python](https://img.shields.io/badge/python-3.10+-3776AB?logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?logo=powerbi&logoColor=black)
![License](https://img.shields.io/badge/licencia-MIT-brightgreen)

---

## Descripcion del Programa

Programa de formacion dirigido a **docentes universitarios** de las carreras de Economia, Administracion, Contaduria y Relaciones Industriales de FACES-UC. Su objetivo es desarrollar competencias en ciencia de datos y Business Intelligence aplicadas a la docencia, investigacion y gestion universitaria.

**Modalidad:** Presencial con componente virtual (GitHub + Google Classroom)
**Duracion:** 32 horas (4 modulos de 8 horas cada uno)
**Instructor:** Ulises Gonzalez — [Rizoma](https://rizo.ma) | [LinkedIn](https://linkedin.com/in/gonzalezulises)

---

## Tabla de Contenidos

- [Estructura del Programa](#estructura-del-programa)
- [Prerequisitos](#prerequisitos)
- [Configuracion del Entorno](#configuracion-del-entorno)
- [Evaluacion](#evaluacion)
- [Cronograma](#cronograma)
- [Datasets](#datasets)
- [Recursos Adicionales](#recursos-adicionales)

---

## Estructura del Programa

| Modulo | Titulo | Horas | Contenido Clave | Detalle |
|--------|--------|-------|------------------|---------|
| 01 | [Fundamentos de Ciencia de Datos y BI](modulo-01-fundamentos/) | 8h | Python, Pandas, Jupyter, etica de datos, pensamiento analitico | [README](modulo-01-fundamentos/README.md) |
| 02 | [Analisis y Visualizacion de Datos](modulo-02-analisis-visualizacion/) | 8h | EDA, visualizacion, SQL, Power BI, storytelling | [README](modulo-02-analisis-visualizacion/README.md) |
| 03 | [Modelado Predictivo y Machine Learning](modulo-03-modelado-predictivo/) | 8h | Regresion, clasificacion, clustering, series temporales, SHAP | [README](modulo-03-modelado-predictivo/README.md) |
| 04 | [Proyectos Integradores y Aplicaciones](modulo-04-proyectos-integradores/) | 8h | Proyecto aplicado por carrera, integracion BI en el aula | [README](modulo-04-proyectos-integradores/README.md) |

---

## Prerequisitos

### Conocimientos previos
- Manejo basico de computadora y hojas de calculo (Excel/Google Sheets)
- No se requiere experiencia previa en programacion

### Software necesario
- [Python 3.10+](https://www.python.org/downloads/) (recomendado: [Anaconda](https://www.anaconda.com/download))
- [Jupyter Notebook](https://jupyter.org/install) o [Google Colab](https://colab.research.google.com/) (sin instalacion)
- [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (solo Windows; en Mac usar [Power BI Web](https://app.powerbi.com/))
- [Visual Studio Code](https://code.visualstudio.com/) (opcional, recomendado)
- [Git](https://git-scm.com/downloads) (opcional, para clonar el repositorio)

### Configuracion rapida

```bash
# Clonar el repositorio
git clone https://github.com/gonzalezulises/formacion-docente-bi-faces.git
cd formacion-docente-bi-faces

# Crear entorno virtual e instalar dependencias
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Consulta la [guia de configuracion completa](other/setup_checklist.md) para instrucciones detalladas.

---

## Evaluacion

| Componente | Peso | Descripcion |
|------------|------|-------------|
| Participacion y ejercicios en clase | 20% | Laboratorios completados durante cada modulo |
| Evaluaciones por modulo | 30% | Ejercicios entregables al final de cada modulo (1-3) |
| Proyecto integrador (Modulo 4) | 40% | Proyecto aplicado a la carrera del docente |
| Revision por pares | 10% | Evaluacion cruzada del proyecto de un colega |

Consulta la [rubrica de evaluacion](modulo-04-proyectos-integradores/rubrica_evaluacion.md) para los criterios detallados.

---

## Cronograma

| Sesion | Modulo | Contenido | Entregable |
|--------|--------|-----------|------------|
| 1 | 01 | Python fundamentos, Jupyter, tipos de datos | Lab: ejercicios Python |
| 2 | 01 | Pandas basico, fuentes de datos, etica, pensamiento analitico | Lab: exploracion con Pandas |
| 3 | 02 | EDA, combinacion de datos, limpieza | Lab: EDA sobre dataset FACES |
| 4 | 02 | Visualizacion, SQL, Power BI, storytelling | Lab: dashboard en Power BI |
| 5 | 03 | Regresion lineal y logistica, evaluacion de modelos | Lab: modelo predictivo |
| 6 | 03 | Arboles de decision, clustering, series temporales, SHAP | Lab: analisis temporal + interpretabilidad |
| 7 | 04 | Definicion de proyecto, fuentes de datos, metodologia | Propuesta de proyecto |
| 8 | 04 | Desarrollo, presentacion y revision por pares | Proyecto final + presentacion |

---

## Datasets

El programa utiliza datasets contextualizados al dominio de FACES:

| Categoria | Datasets | Uso |
|-----------|----------|-----|
| **Universidad** | matricula, rendimiento academico, presupuesto, encuesta docente | EDA, visualizacion, prediccion |
| **Economia** | indicadores BCV, inflacion LATAM, comercio exterior | Series temporales, comparaciones |
| **Empresarial** | ventas retail, nomina RRHH, estados financieros | Regresion, clustering, Power BI |
| **Generales** | titanic, bikeshare, bank | Ejemplos introductorios, practica |

Consulta el [catalogo completo de datasets](datasets/README.md) para descripciones detalladas y diccionarios de datos.

---

## Recursos Adicionales

- [Fuentes de datos publicos](modulo-04-proyectos-integradores/fuentes_datos_publicos.md) — BCV, INE, CEPAL, Banco Mundial y mas
- [Guia de desarrollo profesional](other/recursos_desarrollo_profesional.md) — Pasos siguientes despues del programa
- [Configuracion del entorno](other/setup_checklist.md) — Instrucciones detalladas de instalacion

### Herramientas low-code recomendadas
- [Google Colab](https://colab.research.google.com/) — Notebooks en la nube, sin instalacion
- [Datawrapper](https://www.datawrapper.de/) — Visualizaciones interactivas sin codigo
- [RAWGraphs](https://rawgraphs.io/) — Visualizaciones avanzadas desde CSV
- [Flourish](https://flourish.studio/) — Narrativas visuales interactivas

---

## Estructura del Repositorio

```
formacion-docente-bi-faces/
├── README.md                              # Este archivo
├── requirements.txt                       # Dependencias Python
├── modulo-01-fundamentos/                 # Modulo 1: Fundamentos
│   ├── notebooks/                         # 5 notebooks
│   ├── laboratorios/                      # 4 labs (ejercicios + soluciones)
│   ├── guias/                             # Cheat sheets
│   └── bibliografia/                      # Material de referencia
├── modulo-02-analisis-visualizacion/      # Modulo 2: Analisis y Visualizacion
│   ├── notebooks/                         # 6 notebooks
│   ├── laboratorios/                      # 5 labs
│   └── guias/                             # Cheat sheets (Power BI, SQL)
├── modulo-03-modelado-predictivo/         # Modulo 3: ML y Modelado
│   ├── notebooks/                         # 7 notebooks
│   ├── laboratorios/                      # 4 labs
│   └── guias/                             # ML workflow cheat sheet
├── modulo-04-proyectos-integradores/      # Modulo 4: Proyectos
│   ├── templates/                         # 4 templates por carrera
│   ├── rubrica_evaluacion.md
│   └── guia_integracion_bi_aula.md
├── datasets/                              # Todos los datasets del programa
│   ├── universidad/
│   ├── economia/
│   ├── empresarial/
│   └── generales/
├── images/
└── other/                                 # Setup, recursos, comparaciones
```

---

## Licencia

Este material esta licenciado bajo [MIT License](LICENSE).

## Autor

**Ulises Gonzalez** — [Rizoma](https://rizo.ma)

Programa desarrollado para la Facultad de Ciencias Economicas y Sociales (FACES) de la Universidad Catolica Andres Bello (UCAB).
