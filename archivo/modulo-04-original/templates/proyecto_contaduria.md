# Template de Proyecto: Contaduria

**Modulo 04** | Formacion Docente BI — FACES UC

---

## Contexto

Los docentes de Contaduria trabajan con estados financieros, auditoria, costos y control interno. Este proyecto busca aplicar tecnicas de analisis de datos para detectar patrones, anomalias y tendencias en datos financieros, complementando el analisis contable tradicional con herramientas de Business Intelligence.

---

## Preguntas de Investigacion Sugeridas

Elija una o formule la suya propia:

1. **Analisis de estados financieros:** ¿Que patrones emergen al analizar ratios financieros (liquidez, endeudamiento, rentabilidad) de 20 empresas en 11 anos? ¿Se pueden clasificar las empresas por salud financiera?
2. **Deteccion de anomalias contables:** ¿Se pueden identificar empresas con estados financieros atipicos usando clustering? ¿Que variables distinguen a las empresas anomalas?
3. **Analisis de estructura de costos:** ¿Como se distribuyen los costos en el sector retail? ¿Que categorias tienen margenes mas estrechos? ¿Hay tendencias temporales en los margenes?
4. **Prediccion de rentabilidad:** ¿Es posible predecir la utilidad neta a partir de variables como activos, pasivos e ingresos? ¿Que factores tienen mayor influencia?

---

## Datasets Recomendados

| Dataset | Ubicacion | Variables Clave |
|---------|-----------|-----------------|
| `estados_financieros.csv` | `datasets/empresarial/` | activos, pasivos, patrimonio, ingresos, costos, utilidad_neta, sector |
| `ventas_retail.csv` | `datasets/empresarial/` | ingreso, costo, categoria (para analisis de margenes) |
| `presupuesto_facultad.csv` | `datasets/universidad/` | presupuestado, ejecutado, partida (control presupuestario) |

---

## Tecnicas Aplicables

| Tecnica | Aplicacion en el Proyecto |
|---------|--------------------------|
| EDA | Calcular ratios financieros, explorar distribuciones por sector |
| Visualizacion | Heatmaps de correlacion entre ratios, evolucion temporal |
| Clustering | Agrupar empresas por perfil financiero, detectar anomalias |
| Regresion | Predecir utilidad neta o ratios de rentabilidad |
| SHAP | Explicar que variables influyen mas en la rentabilidad |
| Power BI | Dashboard de indicadores financieros con drill-down por empresa y ano |

### Ratios Financieros Sugeridos

Puede calcular estos ratios a partir del dataset `estados_financieros.csv`:

```
Liquidez = activos / pasivos
Endeudamiento = pasivos / activos
Margen_neto = utilidad_neta / ingresos
ROA = utilidad_neta / activos
ROE = utilidad_neta / patrimonio
Eficiencia_costos = costos / ingresos
```

---

## Estructura Sugerida del Proyecto

1. **Introduccion**: Contexto del analisis financiero, pregunta, justificacion
2. **Datos**: Descripcion del dataset, ratios calculados, periodo
3. **Analisis**: EDA, ratios financieros, visualizaciones, modelado
4. **Resultados**: Clasificacion de empresas, anomalias detectadas, predicciones
5. **Aplicacion pedagogica**: Como usar este analisis en catedras de Contabilidad, Auditoria o Analisis de Estados Financieros
6. **Conclusiones**: Resumen, limitaciones, proximos pasos

---

## Entregable

- Notebook de Jupyter (.ipynb) y/o dashboard de Power BI (.pbix)
- Presentacion de 5-7 minutos

---

## Ejemplo de Proyecto Exitoso

**Titulo:** "Radiografia financiera: Clasificacion de empresas por salud financiera usando clustering y SHAP"

**Enfoque:** Calcula 6 ratios financieros para las 20 empresas del dataset, aplica K-Means para identificar 3 clusters (saludables, en riesgo, criticas), visualiza los perfiles con radar charts, y usa SHAP sobre un modelo de regresion de utilidad neta para explicar que impulsa la rentabilidad. Propone usar el notebook como practica en la catedra de Analisis de Estados Financieros.

---

[Volver al Modulo 04](../README.md)
