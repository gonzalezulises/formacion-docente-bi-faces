# Template de Proyecto: Relaciones Industriales

**Modulo 04** | Formacion Docente BI — FACES UC

---

## Contexto

Los docentes de Relaciones Industriales trabajan con datos de recursos humanos, clima organizacional, relaciones laborales y gestion del talento. Este proyecto busca aplicar tecnicas de analisis de datos para comprender patrones en la gestion de personas y proponer intervenciones basadas en evidencia.

---

## Preguntas de Investigacion Sugeridas

Elija una o formule la suya propia:

1. **Segmentacion de perfiles docentes:** ¿Se pueden identificar tipologias de docentes en FACES segun su perfil (formacion, antiguedad, dedicacion, satisfaccion, productividad)? ¿Que caracteriza a cada grupo?
2. **Analisis de satisfaccion laboral:** ¿Que factores tienen mayor influencia en la satisfaccion general de los docentes? ¿Hay diferencias por departamento, genero o antiguedad?
3. **Prediccion de desempeno laboral:** ¿Es posible predecir la evaluacion de desempeno de un empleado a partir de sus caracteristicas demograficas y laborales? ¿Que variables son mas influyentes?
4. **Analisis de rotacion y ausentismo:** ¿Que factores se asocian con mayor ausentismo? ¿Se puede predecir que empleados tienen mayor riesgo de ausentismo excesivo?

---

## Datasets Recomendados

| Dataset | Ubicacion | Variables Clave |
|---------|-----------|-----------------|
| `encuesta_docente.csv` | `datasets/universidad/` | satisfaccion_*, departamento, antiguedad, dedicacion, formacion, publicaciones |
| `rrhh_nomina.csv` | `datasets/empresarial/` | evaluacion_desempeno, ausencias_anuales, departamento, cargo, salario |
| `rendimiento_academico.csv` | `datasets/universidad/` | asistencia_pct, beca, trabaja (factores sociolaborales de estudiantes) |

---

## Tecnicas Aplicables

| Tecnica | Aplicacion en el Proyecto |
|---------|--------------------------|
| EDA | Explorar distribuciones de satisfaccion, desempeno, ausentismo |
| Visualizacion | Heatmaps de satisfaccion por departamento, boxplots comparativos |
| Clustering | Segmentar docentes o empleados en perfiles tipicos |
| Regresion logistica | Predecir riesgo de ausentismo excesivo (binario) |
| Regresion lineal | Predecir evaluacion de desempeno |
| SHAP | Explicar que factores impulsan la satisfaccion o el desempeno |
| Power BI | Dashboard de indicadores de RRHH (ausentismo, desempeno, satisfaccion) |

### Indices Compuestos Sugeridos

A partir de `encuesta_docente.csv` puede calcular:

```
Satisfaccion_promedio = (satisfaccion_general + satisfaccion_salarial +
                         satisfaccion_infraestructura + satisfaccion_desarrollo) / 4

Productividad_relativa = publicaciones / antiguedad

Carga_vs_dedicacion = carga_horaria / horas_esperadas_dedicacion
```

---

## Estructura Sugerida del Proyecto

1. **Introduccion**: Contexto de gestion de RRHH o clima laboral, pregunta, justificacion
2. **Datos**: Descripcion del dataset, variables seleccionadas, indices calculados
3. **Analisis**: EDA, visualizaciones, clustering o modelado predictivo
4. **Resultados**: Perfiles identificados, factores de influencia, recomendaciones
5. **Aplicacion pedagogica**: Como usar este analisis en catedras de RRHH, Comportamiento Organizacional o Relaciones Laborales
6. **Conclusiones**: Resumen, limitaciones, proximos pasos

---

## Entregable

- Notebook de Jupyter (.ipynb) y/o dashboard de Power BI (.pbix)
- Presentacion de 5-7 minutos

---

## Ejemplo de Proyecto Exitoso

**Titulo:** "Perfiles docentes en FACES: Segmentacion por satisfaccion y productividad"

**Enfoque:** Calcula un indice de satisfaccion compuesto y un indice de productividad relativa para los 200 docentes de la encuesta. Aplica K-Means (k=4) y encuentra 4 perfiles: "comprometidos y productivos", "satisfechos pero poco productivos", "insatisfechos pero activos", "en riesgo de burnout". Visualiza los clusters con scatter plots y radar charts. Usa SHAP para identificar que la dedicacion y la satisfaccion con desarrollo profesional son los factores mas influyentes. Propone usar el analisis como caso de estudio en Comportamiento Organizacional.

---

[Volver al Modulo 04](../README.md)
