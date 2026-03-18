# Guia de Integracion de Business Intelligence en el Aula Universitaria

**Modulo 04** | Formacion Docente BI — FACES UC

---

## Objetivo

Esta guia proporciona estrategias practicas para que los docentes de FACES integren herramientas y conceptos de Business Intelligence en sus catedras, independientemente de la disciplina que ensenan.

---

## 1. Principios de la Docencia Basada en Datos

### 1.1 ¿Por que integrar datos en la ensenanza?

| Beneficio | Descripcion | Ejemplo en FACES |
|-----------|-------------|------------------|
| Relevancia | Los estudiantes trabajan con datos reales de su disciplina | Analizar estados financieros reales en Contaduria |
| Pensamiento critico | Evaluar evidencia antes de formar opiniones | Cuestionar estadisticas de empleo con datos del INE |
| Competencias laborales | El mercado demanda profesionales data-literate | 67% de empleos en administracion requieren manejo de datos (LinkedIn, 2024) |
| Investigacion | Fortalece las lineas de investigacion del docente | Publicaciones con soporte cuantitativo |

### 1.2 Niveles de integracion

No todos los docentes necesitan ensennar Python. La integracion puede ser gradual:

| Nivel | Descripcion | Herramientas | Esfuerzo |
|-------|-------------|--------------|----------|
| **1. Consumidor** | Usar dashboards y visualizaciones existentes como material de clase | Power BI Web, Datawrapper, infografias | Bajo |
| **2. Curador** | Seleccionar y preparar datasets para actividades en clase | Excel, Google Sheets, CSV | Medio |
| **3. Creador** | Disenar actividades donde los estudiantes analizan datos | Jupyter, Google Colab, Power BI | Medio-Alto |
| **4. Investigador** | Integrar analisis de datos en su linea de investigacion | Python, R, SPSS, herramientas de ML | Alto |

**Recomendacion:** Comenzar en el Nivel 1 e ir avanzando progresivamente durante el semestre.

---

## 2. Estrategias por Tipo de Clase

### 2.1 Clase magistral

**Antes:** El docente presenta teoria con diapositivas estaticas.
**Con BI:** El docente muestra un dashboard interactivo en vivo.

**Como implementarlo:**
1. Preparar un dashboard en Power BI Web o Google Looker Studio con datos del tema
2. Proyectar en clase y navegar los filtros en tiempo real
3. Formular preguntas a los estudiantes: "¿Que pasa si filtramos por este ano?" "¿Que patron ven?"
4. Usar la interactividad para generar discusion

**Ejemplo — Macroeconomia:**
- Dashboard con `indicadores_bcv.csv`: inflacion, tipo de cambio, reservas
- Filtrar por periodo pre/post 2017 y discutir los cambios estructurales
- Los estudiantes formulan hipotesis sobre las causas

### 2.2 Seminario o taller

**Actividad:** Los estudiantes reciben un dataset y deben responder preguntas analiticas.

**Formato sugerido (2 horas):**

| Tiempo | Actividad |
|--------|-----------|
| 0-15 min | Presentar el contexto y las preguntas a responder |
| 15-60 min | Trabajo en equipos: explorar datos, crear visualizaciones |
| 60-90 min | Presentacion de hallazgos por equipo (5 min cada uno) |
| 90-120 min | Discusion grupal, conclusiones, conexion con la teoria |

**Ejemplo — Administracion de Empresas:**
- Dataset: `ventas_retail.csv`
- Preguntas: ¿Cual es la categoria mas rentable? ¿Hay estacionalidad? ¿Que tienda tiene peor desempeno?
- Herramienta: Google Sheets o Google Colab (sin instalacion)

### 2.3 Evaluacion continua

**Reemplazar examenes tradicionales por proyectos de datos:**

| Evaluacion tradicional | Evaluacion basada en datos |
|------------------------|---------------------------|
| Examen escrito sobre teoria de costos | Analisis de `estados_financieros.csv` con calculo de ratios |
| Ensayo sobre mercado laboral | Dashboard con datos de `rrhh_nomina.csv` y recomendaciones |
| Presentacion oral sobre inflacion | Visualizacion narrativa de `inflacion_latam.csv` con storytelling |

---

## 3. Actividades Modelo por Carrera

### 3.1 Economia

| Actividad | Dataset | Duracion | Nivel |
|-----------|---------|----------|-------|
| Analizar tendencias de inflacion en LATAM | `inflacion_latam.csv` | 2h | Consumidor |
| Construir indicadores compuestos con Pandas | `indicadores_bcv.csv` | 3h | Creador |
| Pronosticar tipo de cambio con series temporales | `indicadores_bcv.csv` | 4h | Creador |

### 3.2 Administracion

| Actividad | Dataset | Duracion | Nivel |
|-----------|---------|----------|-------|
| Dashboard de ventas en Power BI | `ventas_retail.csv` | 3h | Curador |
| Segmentar clientes con clustering | `ventas_retail.csv` | 3h | Creador |
| Simular escenarios presupuestarios | `presupuesto_facultad.csv` | 2h | Curador |

### 3.3 Contaduria

| Actividad | Dataset | Duracion | Nivel |
|-----------|---------|----------|-------|
| Calcular ratios financieros y detectar anomalias | `estados_financieros.csv` | 3h | Curador |
| Analizar estructura de costos con EDA | `ventas_retail.csv` | 2h | Consumidor |
| Clasificar empresas por riesgo con arboles de decision | `estados_financieros.csv` | 3h | Creador |

### 3.4 Relaciones Industriales

| Actividad | Dataset | Duracion | Nivel |
|-----------|---------|----------|-------|
| Analisis de clima laboral con EDA | `encuesta_docente.csv` | 2h | Consumidor |
| Predecir rotacion con regresion logistica | `rrhh_nomina.csv` | 3h | Creador |
| Segmentar perfiles con clustering | `rrhh_nomina.csv` | 3h | Creador |

---

## 4. Recursos Listos para Usar

### 4.1 Datasets del programa

Todos los datasets estan disponibles en la carpeta `datasets/` del repositorio y pueden cargarse directamente en:
- **Google Colab:** Subir CSV o montar desde GitHub
- **Power BI:** Get Data → CSV
- **Google Sheets:** Importar CSV
- **Excel:** Abrir directamente

### 4.2 Notebooks adaptables

Los notebooks de los Modulos 1-3 pueden reutilizarse como base para actividades de clase:
- Cambiar el dataset por uno especifico de la catedra
- Simplificar el codigo si los estudiantes no conocen Python
- Extraer solo las visualizaciones como imagenes para diapositivas

### 4.3 Plantillas de actividades

**Plantilla basica para actividad de datos en clase:**

```
ACTIVIDAD: [Nombre]
CATEDRA: [Asignatura]
DURACION: [Tiempo]
NIVEL: [Consumidor / Curador / Creador]

CONTEXTO:
[Breve descripcion del problema o situacion a analizar]

DATOS:
[Nombre del dataset, fuente, variables principales]

PREGUNTAS A RESPONDER:
1. [Pregunta descriptiva]
2. [Pregunta diagnostica]
3. [Pregunta predictiva o prescriptiva - opcional]

ENTREGABLE:
[Que deben entregar los estudiantes: informe, dashboard, presentacion]

CRITERIOS DE EVALUACION:
- Correcta manipulacion de datos (30%)
- Calidad de visualizaciones (25%)
- Interpretacion y conclusiones (30%)
- Presentacion (15%)
```

---

## 5. Errores Comunes a Evitar

| Error | Por que es problema | Que hacer en su lugar |
|-------|--------------------|-----------------------|
| Usar datos ficticios obvios | Los estudiantes no se enganchan | Usar datos reales o simulados realistas |
| Pedir solo graficos sin interpretacion | Se pierde el pensamiento critico | Siempre pedir "¿Que significa esto?" |
| Asumir que todos saben Excel | Algunos estudiantes no manejan hojas de calculo | Hacer una nivelacion rapida (15 min) |
| Dar datasets demasiado limpios | No refleja la realidad | Incluir valores faltantes, outliers, inconsistencias |
| Evaluar solo el resultado final | No se valora el proceso analitico | Incluir rubrica que valore el proceso |

---

## 6. Plan de Implementacion Sugerido

### Semestre 1: Piloto

1. Elegir **una** catedra para implementar
2. Disenar **2-3 actividades** de nivel Consumidor o Curador
3. Usar datasets del programa tal como estan
4. Recoger retroalimentacion de los estudiantes
5. Documentar la experiencia

### Semestre 2: Expansion

1. Ampliar a **2-3 catedras**
2. Incluir actividades de nivel Creador
3. Crear datasets propios de la disciplina
4. Colaborar con colegas del programa para compartir materiales

### Semestre 3+: Consolidacion

1. Integrar formalmente en los planes de estudio
2. Publicar experiencias como articulos o ponencias
3. Formar una comunidad de practica entre docentes
4. Proponer actualizacion curricular basada en evidencia

---

## Referencias

- Mandinach, E. & Gummer, E. (2016). *Data Literacy for Educators*. Teachers College Press.
- D'Ignazio, C. & Klein, L. (2020). *Data Feminism*. MIT Press.
- Knaflic, C. N. (2015). *Storytelling with Data*. Wiley.
- Wolff, A. et al. (2016). "Data literacy for learning analytics." *Journal of Learning Analytics*, 3(1).

---

[Volver al Modulo 04](README.md) | [Volver al programa principal](../README.md)
