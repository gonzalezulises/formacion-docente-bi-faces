# Rubrica de Evaluacion — Proyecto Integrador

**Modulo 04** | Formacion Docente BI — FACES UC

---

## Estructura de Evaluacion del Programa

| Componente | Peso | Evaluador |
|------------|------|-----------|
| Participacion y ejercicios en clase (Modulos 1-3) | 20% | Instructor |
| Evaluaciones por modulo (Modulos 1-3) | 30% | Instructor |
| **Proyecto integrador (Modulo 4)** | **40%** | Instructor + Pares |
| Revision por pares | 10% | Pares |

---

## Rubrica del Proyecto Integrador (40%)

### Criterio 1: Formulacion del Problema (20% del proyecto = 8% total)

| Nivel | Puntos | Descriptor |
|-------|--------|------------|
| **Excelente** | 9-10 | Las preguntas de investigacion son claras, especificas, relevantes para la disciplina y respaldadas por contexto. Se distingue entre preguntas descriptivas, diagnosticas y predictivas. Se justifica la relevancia para la catedra del docente. |
| **Bueno** | 7-8 | Las preguntas son claras y relevantes, pero falta profundidad en la justificacion o no se distinguen tipos de preguntas. |
| **Aceptable** | 5-6 | Las preguntas son genericas o poco conectadas con la disciplina. La justificacion es superficial. |
| **Insuficiente** | 0-4 | No hay preguntas claras, o son irrelevantes para el contexto academico. |

### Criterio 2: Analisis Tecnico (30% del proyecto = 12% total)

| Nivel | Puntos | Descriptor |
|-------|--------|------------|
| **Excelente** | 9-10 | Demuestra dominio de las tecnicas aprendidas: EDA completo, visualizaciones informativas, modelado apropiado (si aplica). El codigo es limpio, reproducible y bien comentado. Los datos estan correctamente preparados y documentados. |
| **Bueno** | 7-8 | Aplica las tecnicas correctamente pero con algunos errores menores. El codigo funciona pero podria estar mejor organizado. |
| **Aceptable** | 5-6 | Aplica tecnicas basicas pero omite pasos importantes (por ejemplo: no hace EDA, no evalua el modelo). Errores que afectan los resultados. |
| **Insuficiente** | 0-4 | Errores graves en la aplicacion de tecnicas. Codigo que no ejecuta. Datos mal preparados. |

#### Checklist tecnico (referencia para el evaluador):

- [ ] Dataset cargado y explorado correctamente (shape, dtypes, head, describe)
- [ ] Valores faltantes identificados y tratados
- [ ] Al menos 3 visualizaciones relevantes con titulos y etiquetas
- [ ] Si usa modelado: metricas de evaluacion reportadas
- [ ] Si usa series temporales: componentes identificados
- [ ] Codigo ejecutable de principio a fin sin errores

### Criterio 3: Visualizacion y Comunicacion (25% del proyecto = 10% total)

| Nivel | Puntos | Descriptor |
|-------|--------|------------|
| **Excelente** | 9-10 | Las visualizaciones son claras, esteticas y efectivas. Hay una narrativa coherente que guia al lector. Los graficos tienen titulos descriptivos, ejes etiquetados y colores con proposito. Se aplican principios de storytelling. |
| **Bueno** | 7-8 | Visualizaciones correctas y legibles, pero la narrativa podria ser mas fuerte. Algunos graficos carecen de contexto. |
| **Aceptable** | 5-6 | Visualizaciones basicas (graficos por defecto sin personalizar). No hay narrativa clara entre los graficos. |
| **Insuficiente** | 0-4 | Visualizaciones confusas, incorrectas o ausentes. No hay intento de narrativa. |

#### Checklist de comunicacion:

- [ ] Titulo narrativo en cada grafico (no generico como "Grafico 1")
- [ ] Ejes con etiquetas legibles y unidades
- [ ] Colores con proposito (no aleatorios)
- [ ] Annotations o referencias donde sea necesario
- [ ] Texto entre graficos que conecta la narrativa

### Criterio 4: Aplicacion Pedagogica (15% del proyecto = 6% total)

| Nivel | Puntos | Descriptor |
|-------|--------|------------|
| **Excelente** | 9-10 | El docente explica claramente como el proyecto se conecta con su catedra. Propone al menos una actividad concreta que podria implementar con sus estudiantes. La propuesta es viable y bien fundamentada. |
| **Bueno** | 7-8 | Hay conexion con la catedra pero la propuesta de actividad es vaga o poco desarrollada. |
| **Aceptable** | 5-6 | La conexion con la docencia es superficial. No hay propuesta concreta de actividad. |
| **Insuficiente** | 0-4 | No se menciona la aplicacion pedagogica. |

### Criterio 5: Presentacion (10% del proyecto = 4% total)

| Nivel | Puntos | Descriptor |
|-------|--------|------------|
| **Excelente** | 9-10 | Presentacion clara, estructurada y dentro del tiempo (5-7 min). Demuestra dominio del tema. Responde preguntas con solvencia. Usa apoyo visual efectivo. |
| **Bueno** | 7-8 | Presentacion clara pero se excede en tiempo o le falta profundidad en alguna seccion. |
| **Aceptable** | 5-6 | Presentacion desorganizada o que no cubre todos los aspectos del proyecto. |
| **Insuficiente** | 0-4 | No presenta o la presentacion es incomprensible. |

---

## Tabla Resumen de Puntuacion

| Criterio | Peso | Puntuacion (0-10) | Ponderado |
|----------|------|-------------------|-----------|
| 1. Formulacion del problema | 20% | ___ | ___ |
| 2. Analisis tecnico | 30% | ___ | ___ |
| 3. Visualizacion y comunicacion | 25% | ___ | ___ |
| 4. Aplicacion pedagogica | 15% | ___ | ___ |
| 5. Presentacion | 10% | ___ | ___ |
| **TOTAL** | **100%** | | **___** |

**Escala de calificacion:**

| Rango | Calificacion | Descripcion |
|-------|-------------|-------------|
| 9.0 - 10.0 | Sobresaliente | Excede las expectativas en todos los criterios |
| 7.0 - 8.9 | Bueno | Cumple satisfactoriamente la mayoria de criterios |
| 5.0 - 6.9 | Aceptable | Cumple los requisitos minimos |
| 0.0 - 4.9 | Insuficiente | No cumple los requisitos minimos |

---

## Notas para el Evaluador

1. **Flexibilidad tecnica:** No todos los proyectos requieren modelado predictivo. Un EDA profundo con Power BI puede ser tan valioso como un modelo de ML, dependiendo de las preguntas formuladas.
2. **Contexto disciplinario:** Evaluar la pertinencia del analisis desde la disciplina del docente, no solo desde lo tecnico.
3. **Reproducibilidad:** El notebook o dashboard debe poder ejecutarse/abrirse sin instrucciones adicionales.
4. **Originalidad:** Valorar los proyectos que van mas alla de replicar los ejercicios del curso.

---

[Volver al Modulo 04](README.md) | [Volver al programa principal](../README.md)
