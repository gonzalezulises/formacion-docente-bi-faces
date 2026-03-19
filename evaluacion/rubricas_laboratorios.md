# Rúbricas de Evaluación - Laboratorios

Este documento contiene las rúbricas de evaluación detalladas para todos los laboratorios del programa de formación docente en BI-FACES.

---

## Índice

1. [Módulo 2: Data Wrangling](#módulo-2-data-wrangling)
2. [Módulo 3: Business Intelligence](#módulo-3-business-intelligence)
3. [Módulo 4: Modelos Predictivos](#módulo-4-modelos-predictivos)
4. [Proyecto Integrador](#proyecto-integrador)

---

## Escala General

| Nivel | Puntuación | Descripción |
|-------|------------|-------------|
| **Excelente** | 90-100% | Supera las expectativas, demuestra dominio completo |
| **Competente** | 75-89% | Cumple todos los requisitos satisfactoriamente |
| **En desarrollo** | 60-74% | Cumple requisitos mínimos, necesita mejoras |
| **Insuficiente** | <60% | No cumple requisitos mínimos |

---

## Módulo 2: Data Wrangling

### Lab 01: Limpieza de Datos con Pandas

**Peso total: 100 puntos**

| Criterio | Excelente (25) | Competente (20) | En desarrollo (15) | Insuficiente (10) |
|----------|----------------|-----------------|--------------------|--------------------|
| **Identificación de problemas** | Identifica >90% de problemas de calidad (nulos, duplicados, tipos incorrectos, outliers) | Identifica 75-90% de problemas | Identifica 50-74% de problemas | Identifica <50% de problemas |
| **Tratamiento de valores faltantes** | Justifica estrategia (eliminar/imputar) según tipo de faltante, documenta decisión | Aplica estrategia correcta sin justificación completa | Aplica estrategia pero con errores menores | Estrategia incorrecta o no aplicada |
| **Transformación de tipos** | Todos los tipos correctos, fechas parseadas, categorías optimizadas | Tipos correctos con 1-2 omisiones menores | Varios tipos incorrectos que no afectan análisis | Tipos incorrectos que generan errores |
| **Código y documentación** | Código limpio, comentado, funciones reutilizables, markdown explicativo | Código funcional con comentarios básicos | Código funcional sin documentación | Código con errores o ilegible |

**Entregable:** Notebook ejecutable con datos limpios y documentación del proceso.

---

### Lab 02: Transformación y Agregación

**Peso total: 100 puntos**

| Criterio | Excelente (25) | Competente (20) | En desarrollo (15) | Insuficiente (10) |
|----------|----------------|-----------------|--------------------|--------------------|
| **Uso de groupby** | Agregaciones complejas (múltiples columnas, múltiples funciones), uso de agg() | Agregaciones correctas con groupby básico | Agregaciones simples, errores menores | No logra agregaciones correctas |
| **Creación de columnas derivadas** | Variables calculadas correctas, uso de apply/lambda, vectorización | Variables correctas con métodos básicos | Algunas variables con errores de cálculo | Variables incorrectas o ausentes |
| **Merge/Join de tablas** | Joins correctos, manejo de claves duplicadas, validación post-join | Joins correctos sin validación | Joins con pérdida de datos no intencional | Joins incorrectos |
| **Pivot y reshape** | Uso correcto de pivot_table, melt, stack/unstack según necesidad | Reshape básico correcto | Reshape con errores menores | No logra reshape requerido |

---

### Lab 03: SQL Básico

**Peso total: 100 puntos**

| Criterio | Excelente (25) | Competente (20) | En desarrollo (15) | Insuficiente (10) |
|----------|----------------|-----------------|--------------------|--------------------|
| **SELECT y filtros** | Consultas complejas con WHERE, AND/OR, LIKE, BETWEEN, IN | Consultas correctas con filtros básicos | Filtros simples, errores de sintaxis menores | Consultas incorrectas |
| **Agregaciones SQL** | GROUP BY con HAVING, múltiples agregaciones, subconsultas | Agregaciones correctas sin HAVING | Agregaciones básicas con errores | No logra agregaciones |
| **JOINs** | Múltiples JOINs correctos, entiende diferencia entre tipos | JOINs simples correctos | JOINs con resultados incorrectos parciales | No logra JOINs |
| **Orden y límites** | ORDER BY múltiple, LIMIT/OFFSET, combinación eficiente | Ordenamiento básico correcto | Errores menores en ordenamiento | Ordenamiento incorrecto |

---

### Lab 04: Integración Pandas + SQL

**Peso total: 100 puntos**

| Criterio | Excelente (25) | Competente (20) | En desarrollo (15) | Insuficiente (10) |
|----------|----------------|-----------------|--------------------|--------------------|
| **Conexión a base de datos** | Conexión correcta, manejo de credenciales seguro, cierre de conexiones | Conexión funcional | Conexión con warnings no manejados | No logra conexión |
| **Lectura con pd.read_sql** | Queries optimizados, parámetros correctos, chunking si necesario | Lectura correcta básica | Lectura con ineficiencias | Lectura fallida |
| **Escritura con to_sql** | Escritura correcta, if_exists apropiado, tipos mapeados | Escritura funcional | Escritura con pérdida de tipos | Escritura fallida |
| **Pipeline completo** | ETL funcional: extracción SQL → transformación Pandas → carga | Pipeline parcial funcional | Pipeline con errores recuperables | Pipeline no funcional |

---

## Módulo 3: Business Intelligence

### Lab 05: Dashboard Paso a Paso

**Peso total: 100 puntos**

| Criterio | Excelente (20) | Competente (16) | En desarrollo (12) | Insuficiente (8) |
|----------|----------------|-----------------|--------------------|--------------------|
| **Importación y transformación** | Datos importados correctamente, tipos verificados, transformaciones en Power Query documentadas | Importación correcta con transformaciones básicas | Importación con errores menores de tipos | Importación fallida o datos incorrectos |
| **Medidas DAX** | ≥4 medidas correctas incluyendo CALCULATE, formato apropiado, nombres descriptivos | 3 medidas correctas con formato | 2 medidas correctas | <2 medidas o incorrectas |
| **Visualizaciones** | ≥5 visualizaciones apropiadas, sin chartjunk, colores consistentes, títulos descriptivos | 4 visualizaciones correctas | 3 visualizaciones con errores menores | <3 visualizaciones o inapropiadas |
| **Interactividad** | Segmentadores funcionales, cross-filtering configurado, drill-down implementado | Segmentadores básicos funcionales | Interactividad limitada | Sin interactividad |
| **Diseño y narrativa** | Layout profesional, jerarquía visual clara, título con hallazgo, fuente citada | Diseño aceptable con título | Diseño básico sin narrativa | Diseño desorganizado |

**Entregable:** Archivo .pbix funcional

---

### Lab 06: Rediseño de Dashboard

**Peso total: 100 puntos**

| Criterio | Excelente (25) | Competente (20) | En desarrollo (15) | Insuficiente (10) |
|----------|----------------|-----------------|--------------------|--------------------|
| **Identificación de errores** | ≥8 errores identificados correctamente con descripción precisa | 5-7 errores identificados | 3-4 errores identificados | <3 errores identificados |
| **Justificación teórica** | Cada error vinculado a principio específico (Tufte, Gestalt, Few, etc.) con explicación | Principios citados pero explicación básica | Algunos principios mencionados vagamente | Sin justificación teórica |
| **Soluciones propuestas** | Soluciones concretas, aplicables, con ejemplo visual o descripción detallada | Soluciones correctas pero genéricas | Soluciones parciales | Soluciones incorrectas o ausentes |
| **Boceto mejorado** | Diseño completo con todos los elementos corregidos, paleta definida, justificación | Boceto con mejoras principales | Boceto incompleto | Sin boceto |

---

### Lab 07: Storytelling con Datos

**Peso total: 100 puntos**

| Criterio | Excelente (20) | Competente (16) | En desarrollo (12) | Insuficiente (8) |
|----------|----------------|-----------------|--------------------|--------------------|
| **Hook/Apertura** | Dato sorprendente, específico, que captura atención inmediatamente | Hook presente pero menos impactante | Hook genérico | Sin hook |
| **Estructura 3C** | Contexto-Conflicto-Conclusión claramente identificables y bien desarrollados | Estructura presente pero transiciones débiles | Estructura parcial | Sin estructura narrativa |
| **Hallazgos** | ≥3 hallazgos con Afirmación + Evidencia + Implicación, ordenados por importancia | 2-3 hallazgos con estructura parcial | 1-2 hallazgos básicos | Hallazgos confusos o ausentes |
| **Visualizaciones** | Títulos con mensaje, anotaciones, colores con propósito, sin chartjunk | Visualizaciones mejoradas parcialmente | Visualizaciones básicas | Visualizaciones tipo "default" |
| **Recomendaciones** | ≥2 recomendaciones SMART (específicas, medibles, alcanzables, relevantes, temporales) | Recomendaciones específicas pero incompletas | Recomendaciones genéricas | Sin recomendaciones |

---

## Módulo 4: Modelos Predictivos

### Lab 08: Exploración para ML

**Peso total: 100 puntos**

| Criterio | Excelente (25) | Competente (20) | En desarrollo (15) | Insuficiente (10) |
|----------|----------------|-----------------|--------------------|--------------------|
| **Análisis univariado** | Distribuciones de todas las variables, identificación de outliers, estadísticas descriptivas completas | Análisis de variables principales | Análisis superficial | Análisis ausente o incorrecto |
| **Análisis bivariado** | Correlaciones, relación con target, visualizaciones apropiadas (scatter, box, heatmap) | Correlaciones básicas calculadas | Análisis limitado | Sin análisis bivariado |
| **Identificación de problemas** | Documenta: desbalance, multicolinealidad, valores faltantes, outliers con propuesta de manejo | Identifica problemas principales | Identificación parcial | No identifica problemas |
| **Hipótesis para modelado** | Formula ≥3 hipótesis sobre qué variables serán predictivas y por qué | Hipótesis básicas formuladas | Hipótesis vagas | Sin hipótesis |

---

### Lab 09: Interpretabilidad con SHAP

**Peso total: 100 puntos**

| Criterio | Excelente (25) | Competente (20) | En desarrollo (15) | Insuficiente (10) |
|----------|----------------|-----------------|--------------------|--------------------|
| **Implementación SHAP** | TreeExplainer correcto, shap_values calculados, sin errores | Implementación funcional con warnings menores | Implementación con errores recuperados | Implementación fallida |
| **Visualizaciones SHAP** | Summary plot, bar plot, waterfall para casos individuales, dependence plot | 3 tipos de visualizaciones | 2 tipos de visualizaciones | 1 o ninguna visualización |
| **Interpretación global** | Explica top 5 features, dirección del efecto, magnitud relativa, comparación con feature_importances | Interpretación correcta pero básica | Interpretación parcial | Interpretación incorrecta |
| **Interpretación local** | Analiza ≥2 casos individuales contrastantes, explica predicción específica | Análisis de 1 caso correcto | Análisis superficial | Sin análisis local |

---

### Lab 10: Cross-Validation

**Peso total: 100 puntos**

| Criterio | Excelente (25) | Competente (20) | En desarrollo (15) | Insuficiente (10) |
|----------|----------------|-----------------|--------------------|--------------------|
| **Implementación CV** | K-Fold y Stratified correctos, justifica elección de k, múltiples métricas | CV implementado correctamente | CV con errores menores | CV incorrecto |
| **Comparación de modelos** | ≥3 modelos comparados, intervalos de confianza, visualización de resultados | 2-3 modelos comparados | Comparación básica | Sin comparación |
| **Detección de overfitting** | Compara train vs validation, identifica gap, propone soluciones | Detecta overfitting si existe | Detección parcial | No considera overfitting |
| **Selección justificada** | Elige modelo final con justificación basada en métricas, varianza, interpretabilidad | Selección correcta con justificación básica | Selección sin justificación completa | Selección arbitraria |

---

## Proyecto Integrador

**Peso total: 100 puntos**

### Rúbrica Detallada

| Criterio | Peso | Excelente | Competente | En desarrollo | Insuficiente |
|----------|------|-----------|------------|---------------|--------------|
| **Definición del problema** | 10% | Problema de negocio claro, pregunta de investigación específica, métricas de éxito definidas | Problema definido, métricas básicas | Problema vago | Sin definición clara |
| **Exploración de datos** | 15% | EDA completo, visualizaciones informativas, insights documentados | EDA básico correcto | EDA superficial | EDA ausente |
| **Preparación de datos** | 15% | Pipeline reproducible, encoding correcto, scaling justificado, split estratificado | Preparación correcta | Preparación con errores menores | Preparación incorrecta |
| **Modelado** | 20% | ≥3 modelos comparados con CV, hiperparámetros tuneados, baseline definido | 2 modelos comparados | 1 modelo sin comparación | Modelado incorrecto |
| **Evaluación** | 15% | Múltiples métricas, matriz de confusión, curvas ROC/PR, análisis de errores | Métricas principales reportadas | Evaluación básica | Evaluación incorrecta |
| **Interpretación** | 10% | SHAP o feature importance, explicación de predicciones, limitaciones reconocidas | Interpretación básica | Interpretación superficial | Sin interpretación |
| **Conclusiones** | 10% | Recomendaciones accionables, conexión con problema de negocio, próximos pasos | Conclusiones correctas | Conclusiones genéricas | Sin conclusiones |
| **Presentación** | 5% | Notebook organizado, código limpio, narrativa fluida, reproducible | Presentación aceptable | Presentación desorganizada | Ilegible |

---

## Criterios de Integridad Académica

Todos los trabajos deben cumplir:

1. **Originalidad**: Código propio o correctamente atribuido
2. **Reproducibilidad**: Notebook ejecutable de principio a fin
3. **Documentación**: Explicaciones claras de decisiones
4. **Colaboración permitida**: Discusión de conceptos, NO compartir código

**Penalizaciones:**
- Código copiado sin atribución: -50% del lab
- Notebook no ejecutable: -20% hasta corrección
- Entrega tardía: -10% por día (máximo 3 días)

---

## Retroalimentación

Cada lab recibirá retroalimentación en tres áreas:

1. **Fortalezas**: Qué se hizo bien
2. **Áreas de mejora**: Qué puede mejorar
3. **Recursos sugeridos**: Lecturas o práctica adicional

---

*Última actualización: Enero 2025*
