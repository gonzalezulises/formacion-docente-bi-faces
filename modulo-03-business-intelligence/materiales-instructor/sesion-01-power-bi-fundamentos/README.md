# Sesión 01 — Fundamentos de Power BI

Materiales entregados por la instructora **Ilda Rojas** para la primera sesión del Módulo 03 (Business Intelligence aplicado a decisiones), dictada el **16 de abril de 2026**.

## Contenido

La sesión se organiza en dos bloques de diapositivas:

| Archivo | Descripción |
|---|---|
| [`sesion_01_parte_1.pdf`](sesion_01_parte_1.pdf) | Introducción al curso, instalación de Power BI Desktop, historia y evolución del Business Intelligence, visualización y arquitecturas de almacenamiento |
| [`sesion_01_parte_2.pdf`](sesion_01_parte_2.pdf) | Modelado relacional, fuentes de datos en Power BI, esquema estrella, normalización vs. desnormalización, cardinalidad y administración de relaciones |

## Agenda de la sesión

### Parte 1 — Introducción y contexto

1. **Reglas del curso** — interrupciones, ritmo, cultura de preguntas.
2. **Instalación de la herramienta** — dos opciones para Power BI Desktop:
   - Opción 1: Microsoft Store.
   - Opción 2: descarga directa desde [powerbi.microsoft.com/es-es/downloads](https://powerbi.microsoft.com/es-es/downloads/).
3. **Historia y evolución del análisis de datos**:
   - Pre-BI (1865–1970): Richard Devins acuña el término (1865), IBM inventa el disco duro (1956), Hans Peter Luhn escribe sobre *Business Intelligence* (1958), nacen los DSS (1970).
   - BI 1.0 (década del 90): grupo de Roma (1988), cubo OLAP de Edgar F. Codd (1993).
   - BI 2.0 (década del 2000): PC + Internet (1995), SaaS (2001), nube y Mobile BI (2006).
   - Próxima generación (2010s–hoy): democratización de datos (2016), BI vertical (2018), IA generativa con ChatGPT (2022).
4. **Gartner Analytic Continuum** — descriptivo → diagnóstico → predictivo → prescriptivo.
5. **Evolución del almacenamiento** — Data Warehouse, Data Lake y Data Lakehouse.
6. **¿Qué es Business Intelligence?** — definición de TDWI: combinación de **tecnología, herramientas y procesos** que transforman datos → información → conocimiento → estrategia.
7. **Visualización** — herramientas e historia de la visualización.
8. **¿Qué es Power BI?** — panorama del producto.

### Parte 2 — Modelado de datos en Power BI

1. **Modelado relacional** — definición de modelo de datos, representación visual de la información.
2. **Fuentes de datos en Power BI Desktop** — trabajaremos con TXT, Excel y bases de datos.
3. **Conceptos clave del modelado**:
   1. **Consolidación de fuentes y tecnologías** — información en diferentes sistemas, niveles de normalización y completitud.
   2. **Perfil del dato** — *arqueología de datos*: proceso de revisión y limpieza para mantener calidad.
   3. **Esquema estrella** (Ralph Kimball) — tablas de **dimensiones** (las *cosas* que se modelan) y tablas de **hechos** (observaciones o eventos: ventas, existencias, temperaturas).
   4. **Vinculación por un solo campo** — importancia del concatenado.
4. **Normalizado vs. desnormalizado**:
   - Normalizado: muchas tablas compactas, eficiente, para persistencia (OLTP).
   - Desnormalizado: pocas tablas grandes, para análisis y consultas de alto rendimiento (OLAP).
   - *Power BI toma lo bueno de los dos mundos*: consume datos normalizados tabla a tabla y desnormaliza caso a caso al calcular indicadores.
5. **Administración de relaciones**:
   - Vista Relaciones y tres formas de crearlas (arrastrar, *Manage Relationships*, detección automática).
   - **Cardinalidad**: 1 a *, 1 a 1, * a 1.
   - **Dirección del filtro cruzado** y **relación activa**.

## Relación con los notebooks del módulo

| Concepto de la sesión | Notebook del repo |
|---|---|
| Visualización como parte de BI | [`notebooks/03_01_principios_visualizacion.ipynb`](../../notebooks/03_01_principios_visualizacion.ipynb) |
| Power BI: Power Query, modelo de datos, DAX | [`notebooks/03_02_power_bi_fundamentos.ipynb`](../../notebooks/03_02_power_bi_fundamentos.ipynb) |

## Referencias citadas en las diapositivas

- TDWI — *Transforming Data with Intelligence*: <https://tdwi.org/Home.aspx>
- Historia del BI (Agilence): <https://blog.agilenceinc.com/the-history-of-business-intelligence-infographic>
- Data Warehouse vs. Lake vs. Lakehouse (Serokell): <https://serokell.io/blog/data-warehouse-vs-lake-vs-lakehouse>
- Base de datos vs. Data Warehouse vs. Data Lake (Mistral): <https://www.mistralbs.com/blog/base-de-datos-vs-data-warehouse-vs-data-lake/>
