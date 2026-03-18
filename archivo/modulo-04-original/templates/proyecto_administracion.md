# Template de Proyecto: Administracion

**Modulo 04** | Formacion Docente BI — FACES UC

---

## Contexto

Los docentes de Administracion trabajan con datos de gestion organizacional: ventas, presupuestos, operaciones, recursos humanos. Este proyecto busca aplicar Business Intelligence para resolver problemas reales de gestion empresarial o institucional.

---

## Preguntas de Investigacion Sugeridas

Elija una o formule la suya propia:

1. **Dashboard de gestion universitaria:** ¿Como se puede monitorear la salud de FACES (matricula, rendimiento, presupuesto) en un solo dashboard? ¿Que indicadores clave de gestion (KPIs) son los mas relevantes?
2. **Analisis de desempeno comercial:** ¿Cuales son los patrones de venta por categoria, region y temporada? ¿Que categorias tienen mejor margen? ¿Hay estacionalidad predecible?
3. **Optimizacion presupuestaria:** ¿Como ha evolucionado la ejecucion presupuestaria de FACES? ¿Que partidas muestran mayor brecha entre lo presupuestado y lo ejecutado? ¿Se puede proyectar?
4. **Segmentacion de mercado:** ¿Se pueden identificar grupos de clientes o tiendas con patrones distintos usando clustering?

---

## Datasets Recomendados

| Dataset | Ubicacion | Variables Clave |
|---------|-----------|-----------------|
| `ventas_retail.csv` | `datasets/empresarial/` | fecha, tienda, region, categoria, ingreso, costo |
| `presupuesto_facultad.csv` | `datasets/universidad/` | anio, mes, partida, presupuestado, ejecutado |
| `matricula_faces.csv` | `datasets/universidad/` | periodo, carrera, estatus, sede |
| `rendimiento_academico.csv` | `datasets/universidad/` | carrera, promedio, materias_aprobadas |

---

## Tecnicas Aplicables

| Tecnica | Aplicacion en el Proyecto |
|---------|--------------------------|
| EDA | Explorar ventas por segmento, identificar outliers |
| Visualizacion | Graficos de tendencia, composicion, comparacion |
| Power BI | Dashboard de KPIs con drill-down y filtros |
| Clustering | Segmentar tiendas o periodos por desempeno |
| Regresion | Proyectar ventas o ejecucion presupuestaria |
| Storytelling | Presentar hallazgos al "comite directivo" |

---

## Estructura Sugerida del Proyecto

1. **Introduccion**: Contexto organizacional, pregunta de gestion, justificacion
2. **Datos**: Fuentes, variables clave, periodo analizado
3. **Analisis**: EDA, visualizaciones, dashboard, modelado (si aplica)
4. **Resultados**: KPIs calculados, hallazgos, recomendaciones
5. **Aplicacion pedagogica**: Como usar este enfoque en una catedra de Administracion (Gestion, Mercadeo, Operaciones, etc.)
6. **Conclusiones**: Resumen, limitaciones, proximos pasos

---

## Entregable

- Notebook de Jupyter (.ipynb) y/o dashboard de Power BI (.pbix)
- Presentacion de 5-7 minutos

---

## Ejemplo de Proyecto Exitoso

**Titulo:** "Panel de Control FACES: Dashboard de Gestion Universitaria"

**Enfoque:** Combina datos de matricula, rendimiento y presupuesto en un unico dashboard de Power BI. Incluye KPIs (tasa de retencion, indice de rendimiento, tasa de ejecucion presupuestaria), filtros por periodo y carrera, y alertas visuales para indicadores por debajo del umbral. El docente propone usarlo como caso de estudio en la catedra de Control de Gestion.

---

[Volver al Modulo 04](../README.md)
