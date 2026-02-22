# Guia de Presentacion de Resultados

**Modulo 04** | Formacion Docente BI — FACES UC

---

## Objetivo

Esta guia establece el formato y las mejores practicas para presentar los resultados del proyecto integrador de forma clara, estructurada y persuasiva ante una audiencia academica.

---

## 1. Formato de la Presentacion

| Elemento | Especificacion |
|----------|---------------|
| Duracion | 5-7 minutos por docente |
| Formato | Presentacion oral con apoyo visual (diapositivas, dashboard en vivo, o notebook) |
| Audiencia | Colegas docentes + instructor |
| Preguntas | 2-3 minutos de preguntas despues de cada presentacion |

---

## 2. Estructura Recomendada (5-7 diapositivas)

### Diapositiva 1: Portada
- Titulo del proyecto
- Nombre del docente
- Carrera / Catedra
- Fecha

### Diapositiva 2: Contexto y Pregunta
- ¿Cual es el problema o la pregunta que aborda?
- ¿Por que es relevante para su disciplina?
- ¿Que datos utilizo?

**Tip:** Una buena pregunta de investigacion es la base de una buena presentacion. Si la pregunta no es clara, el resto no importa.

### Diapositiva 3: Datos y Metodologia
- Fuente y tamano del dataset
- Variables clave utilizadas
- Tecnicas aplicadas (EDA, visualizacion, modelado, dashboard)
- Herramientas utilizadas (Python, Power BI, etc.)

**Tip:** No mostrar codigo en la presentacion (a menos que sea un punto clave). Mostrar resultados, no proceso.

### Diapositiva 4-5: Resultados Principales
- 2-3 visualizaciones clave con interpretacion
- Hallazgos mas importantes
- Numeros destacados (KPIs, metricas)

**Tip:** Cada grafico debe responder una pregunta especifica. Si no puede decir "este grafico muestra que...", el grafico sobra.

### Diapositiva 6: Aplicacion Pedagogica
- ¿Como se conecta este proyecto con su catedra?
- ¿Que actividad concreta podria disenar para sus estudiantes?
- ¿Que competencias desarrollarian los estudiantes?

### Diapositiva 7: Conclusiones y Proximos Pasos
- 2-3 conclusiones principales
- Limitaciones del analisis
- ¿Que haria con mas tiempo o datos?

---

## 3. Principios de Diseno Visual

### Lo que SI hacer

| Principio | Ejemplo |
|-----------|---------|
| Un mensaje por diapositiva | "La matricula en Economia cayo 45% entre 2017 y 2023" |
| Titulos como conclusiones | "La desercion afecta mas a estudiantes que trabajan" (no "Grafico de desercion") |
| Colores con proposito | Rojo para lo negativo, verde para lo positivo, gris para contexto |
| Numeros grandes y visibles | KPIs en fuente grande, graficos de soporte detras |
| Espacio en blanco | No llenar cada centimetro de la diapositiva |

### Lo que NO hacer

| Error | Alternativa |
|-------|-------------|
| Parrafos completos en la diapositiva | Usar bullet points de maximo 7 palabras |
| Tablas con 20+ filas | Resumir en un grafico o mostrar solo el top 5 |
| Graficos 3D | Siempre usar 2D |
| Leer las diapositivas textualmente | Las diapositivas son apoyo visual, no guion |
| Mas de 5 colores en un grafico | Usar 2-3 colores + gris |
| Fuentes menores a 18pt | Minimo 18pt para texto, 24pt para titulos |

---

## 4. Como Presentar Resultados Tecnicos a No-Tecnicos

### Regla general: Traducir de tecnico a impacto

| En lugar de decir... | Decir... |
|---------------------|----------|
| "El R2 del modelo es 0.73" | "El modelo explica el 73% de la variacion en las notas" |
| "El p-value es 0.003" | "La diferencia es estadisticamente significativa — no es casualidad" |
| "El SHAP value de asistencia es 2.1" | "La asistencia es el factor que mas influye en el rendimiento" |
| "Use un Random Forest con 200 arboles" | "Use un modelo de machine learning que combina multiples reglas de decision" |
| "El RMSE es 1.8 puntos" | "El modelo se equivoca en promedio por 1.8 puntos sobre 20" |

### La prueba del cafe

Antes de presentar un resultado, preguntese: ¿Podria explicar esto a un colega tomando cafe en la sala de profesores? Si la respuesta es no, simplifique.

---

## 5. Manejo de Preguntas

### Tipos de preguntas frecuentes y como responderlas

| Tipo | Ejemplo | Estrategia |
|------|---------|------------|
| Metodologica | "¿Por que uso regresion y no otra tecnica?" | Explicar brevemente la razon (tipo de variable, tamano de datos) |
| De validez | "¿Son confiables estos datos?" | Reconocer limitaciones, explicar las medidas tomadas |
| De aplicacion | "¿Esto se podria usar para...?" | Conectar con posibilidades reales, ser honesto sobre alcances |
| Critica | "¿No estara sesgado el analisis?" | Agradecer la observacion, explicar como se considero el sesgo |

### Si no sabe la respuesta

"Es una excelente pregunta. No tengo la respuesta en este momento, pero seria interesante explorarla como siguiente paso."

---

## 6. Checklist Pre-Presentacion

- [ ] ¿Mi presentacion dura entre 5 y 7 minutos? (ensayar con cronometro)
- [ ] ¿Cada diapositiva tiene un solo mensaje claro?
- [ ] ¿Los graficos tienen titulos descriptivos y ejes etiquetados?
- [ ] ¿Puedo explicar cada grafico en una oracion?
- [ ] ¿Menciono la aplicacion pedagogica?
- [ ] ¿Mi notebook/dashboard ejecuta sin errores?
- [ ] ¿Tengo backup del archivo en la nube (por si falla la laptop)?
- [ ] ¿Conozco las limitaciones de mi analisis?

---

[Volver al Modulo 04](README.md) | [Volver al programa principal](../README.md)
