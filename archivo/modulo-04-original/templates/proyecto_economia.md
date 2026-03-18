# Template de Proyecto: Economia

**Modulo 04** | Formacion Docente BI — FACES UC

---

## Contexto

Los docentes de Economia tienen acceso a una rica variedad de datos macroeconomicos, series temporales financieras y estadisticas de desarrollo. Este proyecto busca aplicar las tecnicas aprendidas en el programa para analizar fenomenos economicos relevantes para Venezuela y America Latina.

---

## Preguntas de Investigacion Sugeridas

Elija una o formule la suya propia:

1. **Analisis de la crisis economica venezolana (2015-2025):** ¿Como se relacionan la inflacion, el tipo de cambio y las reservas internacionales? ¿Se pueden identificar puntos de quiebre estructural?
2. **Comparacion de desempeno economico en LATAM:** ¿Que paises han tenido mejor desempeno en inflacion/PIB per capita/desempleo en las ultimas dos decadas? ¿Que factores los diferencian?
3. **Proyeccion de indicadores economicos:** ¿Es posible proyectar la inflacion o el tipo de cambio a corto plazo usando modelos de series temporales? ¿Que tan confiables son estas proyecciones?
4. **Comercio exterior venezolano:** ¿Como ha cambiado la estructura de exportaciones? ¿Se ha diversificado o se mantiene la dependencia petrolera?

---

## Datasets Recomendados

| Dataset | Ubicacion | Variables Clave |
|---------|-----------|-----------------|
| `indicadores_bcv.csv` | `datasets/economia/` | inflacion_mensual, tipo_cambio_indice, reservas_internacionales, pib_trimestral |
| `inflacion_latam.csv` | `datasets/economia/` | pais, inflacion_anual, pib_per_capita, desempleo |
| `comercio_exterior.csv` | `datasets/economia/` | producto, pais_destino, valor_fob, volumen |

Puede complementar con datos del Banco Mundial, CEPAL o FMI (ver [fuentes de datos publicos](../fuentes_datos_publicos.md)).

---

## Tecnicas Aplicables

| Tecnica | Aplicacion en el Proyecto |
|---------|--------------------------|
| EDA | Explorar distribucion y tendencias de indicadores |
| Visualizacion | Graficos de linea temporal, comparaciones entre paises |
| Series temporales | Descomposicion, ARIMA para proyeccion de indicadores |
| Correlacion/Regresion | Relacion entre variables macroeconomicas |
| Storytelling | Narrativa visual de la evolucion economica |
| Power BI | Dashboard de indicadores con filtros por periodo |

---

## Estructura Sugerida del Proyecto

1. **Introduccion** (1 pagina): Contexto, pregunta de investigacion, justificacion
2. **Datos** (1/2 pagina): Fuentes, periodo, variables seleccionadas, limitaciones
3. **Analisis** (2-3 paginas): EDA, visualizaciones, modelado (si aplica)
4. **Resultados** (1 pagina): Hallazgos principales, respuesta a la pregunta
5. **Aplicacion pedagogica** (1/2 pagina): Como usar este analisis o enfoque en una catedra de Economia
6. **Conclusiones** (1/2 pagina): Resumen, limitaciones, proximos pasos

---

## Entregable

- Notebook de Jupyter (.ipynb) o dashboard de Power BI (.pbix)
- Presentacion de 5-7 minutos

---

## Ejemplo de Proyecto Exitoso

**Titulo:** "Anatomia de una crisis: Indicadores macroeconomicos venezolanos 2015-2025"

**Enfoque:** Carga los datos del BCV, descompone las series temporales de inflacion y tipo de cambio, identifica el punto de quiebre con visualizaciones anotadas, realiza proyeccion ARIMA a 6 meses, y presenta un dashboard que un estudiante de Macroeconomia II podria usar como caso de estudio.

---

[Volver al Modulo 04](../README.md)
