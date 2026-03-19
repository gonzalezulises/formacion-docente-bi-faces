# Evaluaciones Diagnósticas Pre/Post

Este documento contiene cuestionarios de autoevaluación para medir el conocimiento antes y después de cada módulo.

**Instrucciones:**
- Responder honestamente sin consultar materiales
- Tiempo sugerido: 10-15 minutos por evaluación
- Comparar resultados Pre vs Post para medir aprendizaje

---

## Módulo 1: Pensar con Datos

### Pre-Test (Antes del módulo)

**Nombre:** _________________ **Fecha:** _________________

#### Sección A: Conceptos (1 punto c/u)

1. **¿Qué es una variable cuantitativa?**
   - [ ] a) Una variable que representa categorías
   - [ ] b) Una variable que se puede medir numéricamente
   - [ ] c) Una variable que solo tiene dos valores
   - [ ] d) Una variable que siempre es entera

2. **¿Cuál es la diferencia entre población y muestra?**
   - [ ] a) No hay diferencia
   - [ ] b) La población es un subconjunto de la muestra
   - [ ] c) La muestra es un subconjunto de la población
   - [ ] d) La población siempre es más pequeña

3. **El sesgo de confirmación ocurre cuando:**
   - [ ] a) Buscamos datos que confirmen nuestras creencias previas
   - [ ] b) Confirmamos que los datos son correctos
   - [ ] c) Los datos confirman la hipótesis nula
   - [ ] d) Usamos muestras muy grandes

4. **¿Qué significa que una correlación no implica causalidad?**
   - [ ] a) Las correlaciones siempre son falsas
   - [ ] b) Dos variables pueden estar relacionadas sin que una cause la otra
   - [ ] c) La causalidad no se puede medir
   - [ ] d) Solo las correlaciones negativas implican causalidad

5. **Un valor faltante tipo MCAR (Missing Completely At Random) significa que:**
   - [ ] a) El dato falta por un error sistemático
   - [ ] b) La probabilidad de faltar es completamente aleatoria
   - [ ] c) El dato falta porque el valor es muy alto
   - [ ] d) Siempre debemos eliminar esos registros

#### Sección B: Aplicación (2 puntos c/u)

6. **Identifique el tipo de variable:** "Estado civil (soltero, casado, divorciado)"
   - [ ] a) Cuantitativa discreta
   - [ ] b) Cuantitativa continua
   - [ ] c) Cualitativa nominal
   - [ ] d) Cualitativa ordinal

7. **Si el promedio de notas es 14 y la mediana es 16, la distribución es:**
   - [ ] a) Simétrica
   - [ ] b) Sesgada a la derecha (positiva)
   - [ ] c) Sesgada a la izquierda (negativa)
   - [ ] d) No se puede determinar

8. **Una encuesta pregunta: "¿Está de acuerdo con la excelente gestión del rector?" Esto es un ejemplo de:**
   - [ ] a) Pregunta bien formulada
   - [ ] b) Pregunta con sesgo de aquiescencia
   - [ ] c) Pregunta con sesgo de selección
   - [ ] d) Pregunta cerrada neutral

#### Sección C: Reflexión (3 puntos)

9. **Describa en 2-3 oraciones por qué es importante el pensamiento crítico al analizar datos.**

_________________________________________________________________________

_________________________________________________________________________

_________________________________________________________________________

**Puntuación Pre-Test:** _____ / 20

---

### Post-Test (Después del módulo)

*Las mismas preguntas 1-9, más las siguientes preguntas adicionales:*

#### Sección D: Integración (2 puntos c/u)

10. **Usted encuentra que estudiantes con beca tienen mejor promedio. Antes de concluir que las becas causan mejor rendimiento, ¿qué debería considerar?**
    - [ ] a) Nada, la correlación es suficiente
    - [ ] b) Variables confusoras como nivel socioeconómico o motivación
    - [ ] c) Solo el tamaño de la muestra
    - [ ] d) El tipo de beca

11. **En una encuesta, el 30% no respondió la pregunta sobre ingresos. Los que no responden tienen educación similar a los que sí responden. El tipo de valor faltante probablemente es:**
    - [ ] a) MCAR
    - [ ] b) MAR
    - [ ] c) MNAR
    - [ ] d) No se puede determinar

**Puntuación Post-Test:** _____ / 24

**Mejora:** Post - Pre = _____ puntos

---

## Módulo 2: Data Wrangling

### Pre-Test

**Nombre:** _________________ **Fecha:** _________________

#### Sección A: Python/Pandas Básico (1 punto c/u)

1. **¿Qué librería de Python se usa principalmente para manipular datos tabulares?**
   - [ ] a) NumPy
   - [ ] b) Matplotlib
   - [ ] c) Pandas
   - [ ] d) Scikit-learn

2. **Para seleccionar una columna 'edad' de un DataFrame df, se usa:**
   - [ ] a) df.edad
   - [ ] b) df['edad']
   - [ ] c) df.loc['edad']
   - [ ] d) a y b son correctas

3. **El método `.isnull()` en Pandas:**
   - [ ] a) Elimina valores nulos
   - [ ] b) Reemplaza valores nulos por cero
   - [ ] c) Identifica valores nulos (devuelve True/False)
   - [ ] d) Cuenta valores nulos

4. **¿Qué hace `df.groupby('carrera')['nota'].mean()`?**
   - [ ] a) Filtra por carrera
   - [ ] b) Calcula el promedio de notas por carrera
   - [ ] c) Agrupa las carreras por nota promedio
   - [ ] d) Ordena por carrera

5. **Un LEFT JOIN entre tabla A y tabla B:**
   - [ ] a) Devuelve solo filas que coinciden en ambas tablas
   - [ ] b) Devuelve todas las filas de A y las coincidencias de B
   - [ ] c) Devuelve todas las filas de B y las coincidencias de A
   - [ ] d) Devuelve todas las filas de ambas tablas

#### Sección B: SQL Básico (1 punto c/u)

6. **La cláusula WHERE en SQL se usa para:**
   - [ ] a) Ordenar resultados
   - [ ] b) Filtrar filas
   - [ ] c) Agrupar datos
   - [ ] d) Seleccionar columnas

7. **¿Cuál es la diferencia entre WHERE y HAVING?**
   - [ ] a) No hay diferencia
   - [ ] b) WHERE filtra antes de agrupar, HAVING después
   - [ ] c) HAVING es más rápido
   - [ ] d) WHERE solo funciona con números

8. **La función COUNT(*) en SQL:**
   - [ ] a) Cuenta valores únicos
   - [ ] b) Cuenta todas las filas
   - [ ] c) Suma todos los valores
   - [ ] d) Cuenta columnas

#### Sección C: Aplicación (2 puntos c/u)

9. **Tiene un DataFrame con columna 'fecha' como string "2024-01-15". ¿Cómo la convertiría a fecha?**
   - [ ] a) df['fecha'].to_date()
   - [ ] b) pd.to_datetime(df['fecha'])
   - [ ] c) df['fecha'].astype(date)
   - [ ] d) date(df['fecha'])

10. **Para unir dos DataFrames df1 y df2 por la columna 'id', manteniendo todos los registros de df1:**
    - [ ] a) pd.merge(df1, df2, on='id', how='inner')
    - [ ] b) pd.merge(df1, df2, on='id', how='left')
    - [ ] c) pd.merge(df1, df2, on='id', how='right')
    - [ ] d) df1.join(df2)

**Puntuación Pre-Test:** _____ / 14

---

### Post-Test

*Las mismas preguntas 1-10, más:*

#### Sección D: Código (3 puntos c/u)

11. **Escriba el código Pandas para: calcular el promedio de 'nota' por 'carrera' y 'semestre', ordenado descendentemente por promedio.**

```python
# Su código aquí:


```

12. **Escriba la consulta SQL para: obtener las 5 carreras con mayor cantidad de estudiantes, mostrando carrera y cantidad.**

```sql
-- Su código aquí:


```

**Puntuación Post-Test:** _____ / 20

---

## Módulo 3: Business Intelligence

### Pre-Test

**Nombre:** _________________ **Fecha:** _________________

#### Sección A: Conceptos de Visualización (1 punto c/u)

1. **Según Edward Tufte, el "ratio tinta-datos" ideal es:**
   - [ ] a) Maximizar la cantidad de elementos decorativos
   - [ ] b) Usar la mínima tinta necesaria para mostrar los datos
   - [ ] c) Usar colores brillantes en todos los gráficos
   - [ ] d) Incluir la mayor cantidad de datos posible

2. **Un gráfico de torta (pie chart) es apropiado cuando:**
   - [ ] a) Siempre es la mejor opción
   - [ ] b) Hay pocas categorías (2-3) y se quiere mostrar proporción del todo
   - [ ] c) Hay muchas categorías para comparar
   - [ ] d) Se quiere mostrar tendencias en el tiempo

3. **El principio de Gestalt de "proximidad" indica que:**
   - [ ] a) Elementos cercanos se perciben como relacionados
   - [ ] b) Elementos similares se perciben como relacionados
   - [ ] c) Los elementos más grandes son más importantes
   - [ ] d) El fondo es tan importante como la figura

4. **Un KPI (Key Performance Indicator) debe ser:**
   - [ ] a) Complejo y detallado
   - [ ] b) Específico, medible y relevante para decisiones
   - [ ] c) Siempre expresado en porcentaje
   - [ ] d) Calculado diariamente

5. **El "chartjunk" se refiere a:**
   - [ ] a) Gráficos con errores de datos
   - [ ] b) Elementos decorativos que no aportan información
   - [ ] c) Gráficos desactualizados
   - [ ] d) Visualizaciones interactivas

#### Sección B: Herramientas BI (1 punto c/u)

6. **En Power BI, las medidas DAX se diferencian de las columnas calculadas en que:**
   - [ ] a) Las medidas se calculan en tiempo de consulta según filtros
   - [ ] b) Las columnas calculadas son más rápidas
   - [ ] c) Las medidas solo funcionan con números
   - [ ] d) No hay diferencia

7. **Un segmentador (slicer) en un dashboard permite:**
   - [ ] a) Exportar datos
   - [ ] b) Filtrar interactivamente los visuales
   - [ ] c) Crear nuevas columnas
   - [ ] d) Conectar a bases de datos

8. **El cross-filtering entre gráficos significa que:**
   - [ ] a) Los gráficos no se afectan entre sí
   - [ ] b) Al hacer clic en un gráfico, otros se filtran automáticamente
   - [ ] c) Los filtros se aplican solo al gráfico seleccionado
   - [ ] d) Se requiere programación adicional

#### Sección C: Storytelling (2 puntos c/u)

9. **La estructura "Contexto-Conflicto-Conclusión" en narrativa de datos sirve para:**
   - [ ] a) Hacer presentaciones más largas
   - [ ] b) Estructurar la información de forma que genere interés y lleve a la acción
   - [ ] c) Incluir más gráficos
   - [ ] d) Evitar mostrar datos negativos

10. **Un título efectivo para un gráfico debería:**
    - [ ] a) Describir el tipo de gráfico ("Gráfico de barras")
    - [ ] b) Comunicar el hallazgo principal ("Las ventas cayeron 15% en Q4")
    - [ ] c) Ser lo más corto posible
    - [ ] d) Incluir la fuente de datos

**Puntuación Pre-Test:** _____ / 14

---

### Post-Test

*Las mismas preguntas 1-10, más:*

#### Sección D: Aplicación (3 puntos c/u)

11. **Identifique 3 errores en esta descripción de dashboard y proponga solución:**

*"Dashboard con fondo degradado azul-morado, 8 tarjetas KPI sin etiquetas mostrando solo números, gráfico de torta 3D con 15 categorías en colores arcoíris, título 'Datos 2024'"*

| Error | Solución |
|-------|----------|
| 1. | |
| 2. | |
| 3. | |

12. **Escriba un hook (apertura) efectivo para una presentación sobre deserción estudiantil, dado que la tasa aumentó de 5% a 12% en 3 años.**

_________________________________________________________________________

_________________________________________________________________________

**Puntuación Post-Test:** _____ / 20

---

## Módulo 4: Modelos Predictivos

### Pre-Test

**Nombre:** _________________ **Fecha:** _________________

#### Sección A: Conceptos ML (1 punto c/u)

1. **La diferencia entre aprendizaje supervisado y no supervisado es:**
   - [ ] a) Supervisado requiere más datos
   - [ ] b) Supervisado tiene variable objetivo conocida, no supervisado no
   - [ ] c) No supervisado es más preciso
   - [ ] d) Supervisado solo funciona con números

2. **El overfitting (sobreajuste) ocurre cuando:**
   - [ ] a) El modelo es muy simple
   - [ ] b) El modelo memoriza los datos de entrenamiento pero no generaliza
   - [ ] c) Hay pocos datos
   - [ ] d) El modelo tiene alta varianza en entrenamiento

3. **La métrica "Recall" mide:**
   - [ ] a) Qué proporción de predicciones positivas son correctas
   - [ ] b) Qué proporción de casos positivos reales fueron identificados
   - [ ] c) El promedio de precision y recall
   - [ ] d) La exactitud general del modelo

4. **Cross-validation se usa para:**
   - [ ] a) Limpiar los datos
   - [ ] b) Evaluar el modelo de forma más robusta que un solo train/test split
   - [ ] c) Seleccionar features
   - [ ] d) Normalizar variables

5. **Un árbol de decisión clasifica datos mediante:**
   - [ ] a) Reglas de división basadas en features
   - [ ] b) Distancia entre puntos
   - [ ] c) Combinación lineal de variables
   - [ ] d) Clustering

#### Sección B: Preparación de Datos para ML (1 punto c/u)

6. **One-Hot Encoding se usa para:**
   - [ ] a) Normalizar variables numéricas
   - [ ] b) Convertir variables categóricas en columnas binarias
   - [ ] c) Eliminar outliers
   - [ ] d) Imputar valores faltantes

7. **¿Por qué se divide en train y test antes de cualquier transformación?**
   - [ ] a) Para ahorrar tiempo de cómputo
   - [ ] b) Para evitar data leakage (filtración de información del test al train)
   - [ ] c) Por convención
   - [ ] d) No es necesario dividir antes

8. **El StandardScaler transforma los datos para que tengan:**
   - [ ] a) Valores entre 0 y 1
   - [ ] b) Media 0 y desviación estándar 1
   - [ ] c) Solo valores positivos
   - [ ] d) Distribución normal

#### Sección C: Interpretación (2 puntos c/u)

9. **En una matriz de confusión para clasificación binaria, un "Falso Negativo" significa:**
   - [ ] a) Predijo positivo, era negativo
   - [ ] b) Predijo negativo, era positivo
   - [ ] c) Predijo positivo, era positivo
   - [ ] d) Predijo negativo, era negativo

10. **Si un modelo tiene Precision=0.90 y Recall=0.60 para detectar fraude, significa:**
    - [ ] a) El modelo detecta casi todos los fraudes
    - [ ] b) El modelo tiene pocas falsas alarmas pero pierde muchos fraudes reales
    - [ ] c) El modelo tiene muchas falsas alarmas
    - [ ] d) El modelo no funciona

**Puntuación Pre-Test:** _____ / 14

---

### Post-Test

*Las mismas preguntas 1-10, más:*

#### Sección D: Aplicación (3 puntos c/u)

11. **Dado el siguiente output de SHAP, interprete los resultados:**

```
Feature Importance (SHAP):
1. asistencia_pct: 0.25
2. materias_reprobadas: 0.18
3. semestre: 0.12
4. trabaja: 0.10
5. beca: 0.08
```

**Interpretación (qué significa cada valor, qué acciones sugiere):**

_________________________________________________________________________

_________________________________________________________________________

_________________________________________________________________________

12. **Un modelo de Random Forest tiene:**
- Accuracy en train: 98%
- Accuracy en test: 72%

**¿Qué problema tiene? ¿Qué soluciones propondría?**

_________________________________________________________________________

_________________________________________________________________________

**Puntuación Post-Test:** _____ / 20

---

## Hoja de Respuestas

### Módulo 1
| Pregunta | Respuesta |
|----------|-----------|
| 1 | b |
| 2 | c |
| 3 | a |
| 4 | b |
| 5 | b |
| 6 | c |
| 7 | c |
| 8 | b |
| 10 | b |
| 11 | b |

### Módulo 2
| Pregunta | Respuesta |
|----------|-----------|
| 1 | c |
| 2 | d |
| 3 | c |
| 4 | b |
| 5 | b |
| 6 | b |
| 7 | b |
| 8 | b |
| 9 | b |
| 10 | b |

### Módulo 3
| Pregunta | Respuesta |
|----------|-----------|
| 1 | b |
| 2 | b |
| 3 | a |
| 4 | b |
| 5 | b |
| 6 | a |
| 7 | b |
| 8 | b |
| 9 | b |
| 10 | b |

### Módulo 4
| Pregunta | Respuesta |
|----------|-----------|
| 1 | b |
| 2 | b |
| 3 | b |
| 4 | b |
| 5 | a |
| 6 | b |
| 7 | b |
| 8 | b |
| 9 | b |
| 10 | b |

---

## Interpretación de Resultados

| Mejora (Post - Pre) | Interpretación |
|---------------------|----------------|
| +6 o más puntos | Aprendizaje significativo |
| +3 a +5 puntos | Aprendizaje moderado |
| +1 a +2 puntos | Aprendizaje leve, revisar conceptos |
| 0 o negativo | Requiere repaso del módulo |

---

*Última actualización: Enero 2025*
