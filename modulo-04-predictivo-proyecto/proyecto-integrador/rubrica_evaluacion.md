# Rubrica de Evaluacion — Proyecto Integrador

**Modulo 04 — Modelos predictivos simples y proyecto integrador** | Formacion Docente BI — FACES UC

---

## Estructura de Evaluacion del Programa

| Componente | Peso | Evaluador |
|------------|------|-----------|
| **Portafolio de analisis de datos** | **40%** | Instructor |
| **Dashboard de BI** | **30%** | Instructor |
| **Proyecto de curso con modelo** | **30%** | Instructor + Pares |

---

## Componente 1: Portafolio de Analisis de Datos (40%)

El docente entrega un dataset limpio y un notebook que documenta todo el proceso de analisis.

### Criterios de evaluacion

| Nivel | Puntos | Descriptor |
|-------|--------|------------|
| **Excelente** | 9-10 | Dataset completamente limpio, documentado y reproducible. El notebook muestra el proceso paso a paso: importacion, limpieza (tratamiento de nulos, tipos, outliers), EDA con al menos 3 visualizaciones informativas, y conclusiones parciales. El codigo ejecuta sin errores de principio a fin. |
| **Bueno** | 7-8 | Dataset limpio y notebook funcional, pero falta documentacion en algunos pasos o las visualizaciones son basicas. El proceso es reproducible con ajustes menores. |
| **Aceptable** | 5-6 | El dataset tiene limpieza parcial. El notebook omite pasos importantes (no hay EDA o no hay tratamiento de nulos). Algunas celdas no ejecutan. |
| **Insuficiente** | 0-4 | Dataset sin limpiar o notebook incompleto. Errores graves que impiden la reproducibilidad. |

#### Checklist del portafolio:

- [ ] Dataset cargado y explorado (shape, dtypes, head, describe)
- [ ] Valores faltantes identificados y tratados con justificacion
- [ ] Al menos 3 visualizaciones relevantes con titulos y etiquetas
- [ ] Texto narrativo entre celdas que explica cada decision
- [ ] Codigo ejecutable de principio a fin sin errores

---

## Componente 2: Dashboard de BI (30%)

El docente presenta un dashboard funcional (puede ser en notebook con graficos interactivos, Google Sheets, o herramienta equivalente) que permita explorar los datos de forma visual.

### Criterios de evaluacion

| Nivel | Puntos | Descriptor |
|-------|--------|------------|
| **Excelente** | 9-10 | Dashboard funcional con al menos 3 vistas/graficos. Incluye explicacion de como usarlo para tomar decisiones en contexto educativo. Los graficos son claros, con titulos descriptivos y colores con proposito. Se aplican principios de storytelling. |
| **Bueno** | 7-8 | Dashboard funcional pero con menos vistas o sin explicacion detallada de uso. Graficos correctos pero sin narrativa fuerte. |
| **Aceptable** | 5-6 | Dashboard basico con graficos por defecto sin personalizar. No hay explicacion de uso ni conexion con la toma de decisiones. |
| **Insuficiente** | 0-4 | Dashboard no funcional, incompleto o ausente. |

#### Checklist del dashboard:

- [ ] Al menos 3 graficos/vistas relevantes
- [ ] Titulos descriptivos (no genericos como "Grafico 1")
- [ ] Ejes con etiquetas legibles
- [ ] Explicacion escrita de como usar el dashboard
- [ ] Conexion explicita con una decision educativa o institucional

---

## Componente 3: Proyecto de Curso con Modelo (30%)

El docente aplica un modelo predictivo simple (regresion lineal o clasificacion binaria) a un problema relevante para su catedra, siguiendo el flujo completo: datos → limpieza → EDA → modelo → evaluacion → comunicacion.

### Criterios de evaluacion

| Nivel | Puntos | Descriptor |
|-------|--------|------------|
| **Excelente** | 9-10 | Pregunta de investigacion clara y relevante. Modelo aplicado correctamente con division train/test. Metricas reportadas (R², RMSE o accuracy segun corresponda). Interpretacion de coeficientes en lenguaje no tecnico. Al menos 3 hallazgos clave. Propuesta de aplicacion pedagogica concreta. |
| **Bueno** | 7-8 | Modelo aplicado correctamente pero la interpretacion es parcial o la propuesta pedagogica es vaga. Metricas presentes pero sin contexto. |
| **Aceptable** | 5-6 | Modelo basico sin evaluacion adecuada (no hay train/test o no se reportan metricas). Interpretacion superficial. Sin propuesta pedagogica. |
| **Insuficiente** | 0-4 | Modelo incorrecto, no ejecuta, o no hay intento de modelado. |

#### Checklist del modelo:

- [ ] Pregunta de investigacion formulada explicitamente
- [ ] Variables predictoras y objetivo identificadas
- [ ] Division train/test (80/20)
- [ ] Metricas de evaluacion reportadas e interpretadas
- [ ] Coeficientes interpretados en lenguaje no tecnico
- [ ] 3 hallazgos clave redactados
- [ ] Propuesta de aplicacion en la catedra del docente

---

## Tabla Resumen de Puntuacion

| Componente | Peso | Puntuacion (0-10) | Ponderado |
|------------|------|-------------------|-----------|
| 1. Portafolio de analisis de datos | 40% | ___ | ___ |
| 2. Dashboard de BI | 30% | ___ | ___ |
| 3. Proyecto de curso con modelo | 30% | ___ | ___ |
| **TOTAL** | **100%** | | **___** |

**Escala de calificacion:**

| Rango | Calificacion | Descripcion |
|-------|-------------|-------------|
| 9.0 - 10.0 | Sobresaliente | Excede las expectativas en todos los componentes |
| 7.0 - 8.9 | Bueno | Cumple satisfactoriamente la mayoria de componentes |
| 5.0 - 6.9 | Aceptable | Cumple los requisitos minimos |
| 0.0 - 4.9 | Insuficiente | No cumple los requisitos minimos |

---

## Notas para el Evaluador

1. **Flexibilidad tecnica:** El modelo predictivo puede ser regresion lineal simple, regresion multiple o clasificacion binaria (regresion logistica). No se exigen modelos complejos.
2. **Contexto disciplinario:** Evaluar la pertinencia del analisis desde la disciplina del docente, no solo desde lo tecnico.
3. **Reproducibilidad:** El notebook debe poder ejecutarse sin instrucciones adicionales.
4. **Comunicacion:** Valorar especialmente la capacidad de traducir resultados tecnicos a lenguaje comprensible para audiencias no tecnicas.

---

[Volver al Modulo 04](../README.md) | [Volver al programa principal](../../README.md)
