# Banco de Ejercicios Adicionales con Soluciones

Este documento contiene ejercicios de práctica adicional para cada módulo, con soluciones detalladas.

---

## Índice

1. [Módulo 1: Pensar con Datos](#módulo-1-pensar-con-datos)
2. [Módulo 2: Data Wrangling](#módulo-2-data-wrangling)
3. [Módulo 3: Business Intelligence](#módulo-3-business-intelligence)
4. [Módulo 4: Modelos Predictivos](#módulo-4-modelos-predictivos)

---

## Módulo 1: Pensar con Datos

### Ejercicio 1.1: Identificación de Variables

**Instrucciones:** Para cada variable, identifique el tipo (cuantitativa discreta, cuantitativa continua, cualitativa nominal, cualitativa ordinal).

| Variable | Su Respuesta |
|----------|--------------|
| 1. Número de hijos | |
| 2. Temperatura corporal | |
| 3. Código postal | |
| 4. Nivel de satisfacción (1-5) | |
| 5. Tipo de sangre | |
| 6. Estatura en cm | |
| 7. Número de cédula | |
| 8. Calificación (Sobresaliente, Notable, Aprobado, Suspenso) | |

<details>
<summary>Ver Solución</summary>

| Variable | Tipo | Explicación |
|----------|------|-------------|
| 1. Número de hijos | Cuantitativa discreta | Conteo, valores enteros |
| 2. Temperatura corporal | Cuantitativa continua | Medición, valores decimales |
| 3. Código postal | Cualitativa nominal | Es identificador, no se opera matemáticamente |
| 4. Nivel de satisfacción | Cualitativa ordinal | Tiene orden pero intervalos no son iguales |
| 5. Tipo de sangre | Cualitativa nominal | Categorías sin orden |
| 6. Estatura en cm | Cuantitativa continua | Medición continua |
| 7. Número de cédula | Cualitativa nominal | Identificador, no es cantidad |
| 8. Calificación | Cualitativa ordinal | Categorías con orden claro |

</details>

---

### Ejercicio 1.2: Sesgos en Estudios

**Instrucciones:** Identifique el sesgo presente en cada escenario.

**Escenario A:** Un estudio sobre efectividad de un programa de tutorías compara las notas de estudiantes que voluntariamente asistieron a tutorías vs los que no asistieron.

**Escenario B:** Una encuesta sobre satisfacción con el transporte público se realiza únicamente en las estaciones de metro.

**Escenario C:** Un investigador que cree que las redes sociales dañan el rendimiento académico encuentra correlación negativa entre horas en redes y notas.

<details>
<summary>Ver Solución</summary>

**Escenario A: Sesgo de selección (autoselección)**
- Los estudiantes que asisten voluntariamente probablemente son más motivados
- La diferencia en notas podría deberse a la motivación, no a las tutorías
- Solución: Asignación aleatoria a grupos

**Escenario B: Sesgo de muestreo**
- Solo captura opinión de usuarios de metro, no de buses, taxis, etc.
- Resultados no son generalizables a todo el transporte público
- Solución: Muestreo estratificado por tipo de transporte

**Escenario C: Sesgo de confirmación**
- El investigador puede haber ignorado evidencia contraria
- Correlación no implica causalidad (¿tal vez estudiantes con problemas usan más redes?)
- Solución: Revisión ciega, considerar hipótesis alternativas

</details>

---

### Ejercicio 1.3: Correlación vs Causalidad

**Instrucciones:** Para cada par de variables, proponga una variable confusora que podría explicar la correlación.

1. **Ventas de helados** y **ahogamientos en piscinas** (correlación positiva)
2. **Número de bomberos en un incendio** y **daños causados** (correlación positiva)
3. **Consumo de vino** y **longevidad** (correlación positiva)

<details>
<summary>Ver Solución</summary>

1. **Helados y ahogamientos**
   - Variable confusora: **Temperatura/estación del año**
   - En verano se consumen más helados Y hay más actividad en piscinas

2. **Bomberos y daños**
   - Variable confusora: **Tamaño del incendio**
   - Incendios más grandes requieren más bomberos Y causan más daños
   - No es que los bomberos causen daños

3. **Vino y longevidad**
   - Variables confusoras: **Nivel socioeconómico, dieta mediterránea**
   - Personas que consumen vino moderadamente suelen tener mejor acceso a salud
   - La dieta general podría ser el factor real

</details>

---

### Ejercicio 1.4: Valores Faltantes

**Instrucciones:** Clasifique cada situación como MCAR, MAR o MNAR.

1. Un servidor falló aleatoriamente y se perdieron datos de 3 horas de un día cualquiera.
2. Los estudiantes que trabajan tienen mayor probabilidad de no completar la encuesta de satisfacción.
3. Los pacientes más enfermos abandonan el estudio clínico antes de completarlo.
4. Un asistente de investigación olvidó algunas encuestas en el bus.

<details>
<summary>Ver Solución</summary>

1. **MCAR (Missing Completely At Random)**
   - La falla del servidor no tiene relación con los datos
   - Los datos perdidos son aleatorios

2. **MAR (Missing At Random)**
   - La probabilidad de faltar depende de una variable observable (trabaja)
   - No depende del valor de la satisfacción misma

3. **MNAR (Missing Not At Random)**
   - La probabilidad de faltar depende del valor faltante mismo (estado de salud)
   - Los más enfermos son precisamente los que faltan

4. **MCAR (Missing Completely At Random)**
   - Fue un accidente sin relación con el contenido de las encuestas

</details>

---

## Módulo 2: Data Wrangling

### Ejercicio 2.1: Pandas Básico

**Instrucciones:** Escriba el código Pandas para cada operación.

```python
import pandas as pd
import numpy as np

# Dataset de ejemplo
df = pd.DataFrame({
    'nombre': ['Ana', 'Juan', 'María', 'Pedro', 'Lucía'],
    'edad': [22, 25, np.nan, 28, 21],
    'carrera': ['Admin', 'Econ', 'Admin', 'Contad', 'Econ'],
    'nota': [15.5, 12.0, 18.0, 14.5, 16.0],
    'semestre': [4, 6, 5, 8, 3]
})
```

1. Seleccionar solo las columnas 'nombre' y 'nota'
2. Filtrar estudiantes con nota mayor a 15
3. Calcular la media de edad (ignorando nulos)
4. Reemplazar el valor faltante de edad por la mediana
5. Agregar una columna 'aprobado' (True si nota >= 10)

<details>
<summary>Ver Solución</summary>

```python
# 1. Seleccionar columnas
df[['nombre', 'nota']]

# 2. Filtrar por nota
df[df['nota'] > 15]

# 3. Media de edad
df['edad'].mean()  # Pandas ignora NaN por defecto

# 4. Reemplazar faltante con mediana
df['edad'].fillna(df['edad'].median(), inplace=True)
# O: df['edad'] = df['edad'].fillna(df['edad'].median())

# 5. Agregar columna aprobado
df['aprobado'] = df['nota'] >= 10
```

</details>

---

### Ejercicio 2.2: GroupBy y Agregaciones

**Instrucciones:** Usando el DataFrame anterior, escriba el código para:

1. Calcular el promedio de nota por carrera
2. Contar estudiantes por carrera
3. Obtener nota máxima y mínima por carrera en una sola operación
4. Calcular la suma de semestres de todos los estudiantes de 'Admin'

<details>
<summary>Ver Solución</summary>

```python
# 1. Promedio por carrera
df.groupby('carrera')['nota'].mean()

# 2. Contar por carrera
df.groupby('carrera').size()
# O: df['carrera'].value_counts()

# 3. Max y min por carrera
df.groupby('carrera')['nota'].agg(['max', 'min'])

# 4. Suma de semestres de Admin
df[df['carrera'] == 'Admin']['semestre'].sum()
# O: df.groupby('carrera')['semestre'].sum()['Admin']
```

</details>

---

### Ejercicio 2.3: Merge/Join

**Instrucciones:** Dados los siguientes DataFrames:

```python
estudiantes = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'nombre': ['Ana', 'Juan', 'María', 'Pedro'],
    'carrera_id': [101, 102, 101, 103]
})

carreras = pd.DataFrame({
    'carrera_id': [101, 102, 104],
    'nombre_carrera': ['Administración', 'Economía', 'Sociología']
})
```

1. Haga un INNER JOIN para obtener estudiantes con su carrera
2. Haga un LEFT JOIN para mantener todos los estudiantes
3. ¿Qué estudiante no tiene carrera después del LEFT JOIN?
4. ¿Qué carrera no tiene estudiantes?

<details>
<summary>Ver Solución</summary>

```python
# 1. INNER JOIN
pd.merge(estudiantes, carreras, on='carrera_id', how='inner')
# Resultado: Ana, Juan, María (Pedro tiene carrera_id=103 que no existe)

# 2. LEFT JOIN
pd.merge(estudiantes, carreras, on='carrera_id', how='left')
# Resultado: Todos los estudiantes, Pedro con NaN en nombre_carrera

# 3. Pedro no tiene carrera (carrera_id=103 no existe en tabla carreras)

# 4. Sociología (carrera_id=104) no tiene estudiantes
# Para verificar:
pd.merge(estudiantes, carreras, on='carrera_id', how='right')
```

</details>

---

### Ejercicio 2.4: SQL

**Instrucciones:** Escriba la consulta SQL para cada pregunta.

Tabla `estudiantes`:
| id | nombre | carrera | semestre | nota |
|----|--------|---------|----------|------|
| 1 | Ana | Admin | 4 | 15.5 |
| 2 | Juan | Econ | 6 | 12.0 |
| 3 | María | Admin | 5 | 18.0 |
| 4 | Pedro | Contad | 8 | 14.5 |

1. Seleccionar nombre y nota de todos los estudiantes
2. Filtrar estudiantes de la carrera 'Admin'
3. Calcular el promedio de nota por carrera
4. Obtener las carreras con más de 1 estudiante
5. Ordenar por nota descendente y mostrar los 3 mejores

<details>
<summary>Ver Solución</summary>

```sql
-- 1. Seleccionar nombre y nota
SELECT nombre, nota FROM estudiantes;

-- 2. Filtrar por carrera
SELECT * FROM estudiantes WHERE carrera = 'Admin';

-- 3. Promedio por carrera
SELECT carrera, AVG(nota) as promedio
FROM estudiantes
GROUP BY carrera;

-- 4. Carreras con más de 1 estudiante
SELECT carrera, COUNT(*) as cantidad
FROM estudiantes
GROUP BY carrera
HAVING COUNT(*) > 1;

-- 5. Top 3 por nota
SELECT nombre, nota
FROM estudiantes
ORDER BY nota DESC
LIMIT 3;
```

</details>

---

## Módulo 3: Business Intelligence

### Ejercicio 3.1: Selección de Gráficos

**Instrucciones:** Para cada objetivo de visualización, seleccione el tipo de gráfico más apropiado.

| Objetivo | Opciones | Su Respuesta |
|----------|----------|--------------|
| 1. Comparar ventas de 5 regiones | Torta / Barras / Línea | |
| 2. Mostrar tendencia de matrícula (10 años) | Torta / Barras / Línea | |
| 3. Mostrar composición de presupuesto (3 categorías) | Torta / Barras / Scatter | |
| 4. Correlación entre inversión y retorno | Línea / Scatter / Barras | |
| 5. Comparar antes/después de intervención | Barras agrupadas / Línea / Torta | |

<details>
<summary>Ver Solución</summary>

| Objetivo | Respuesta | Justificación |
|----------|-----------|---------------|
| 1. Comparar 5 regiones | **Barras** | Fácil comparar longitudes, no ángulos |
| 2. Tendencia 10 años | **Línea** | Muestra continuidad temporal |
| 3. Composición 3 categorías | **Torta** (o barras) | Pocas categorías, muestra parte del todo |
| 4. Correlación | **Scatter** | Muestra relación entre 2 variables continuas |
| 5. Antes/después | **Barras agrupadas** | Comparación directa de dos períodos |

</details>

---

### Ejercicio 3.2: Identificar Errores de Visualización

**Instrucciones:** Identifique todos los errores en esta descripción de gráfico.

*"Gráfico de barras 3D mostrando ventas de enero a diciembre. El eje Y comienza en 50,000 (valores van de 52,000 a 58,000). Cada mes tiene un color diferente del arcoíris. Título: 'Gráfico de Barras'. No hay etiquetas de datos. Fuente no especificada."*

<details>
<summary>Ver Solución</summary>

| Error | Principio Violado | Solución |
|-------|-------------------|----------|
| 1. 3D sin propósito | Tufte: ratio tinta-datos | Usar 2D |
| 2. Eje Y truncado | Honestidad visual | Empezar en 0 |
| 3. 12 colores diferentes | Pre-atentivo | Un solo color o degradado |
| 4. Título genérico | Narrativa | "Ventas se mantuvieron estables en 2024" |
| 5. Sin etiquetas | Claridad | Agregar valores clave |
| 6. Sin fuente | Credibilidad | Citar origen de datos |

Además: para 12 meses de tendencia, un gráfico de línea sería más apropiado que barras.

</details>

---

### Ejercicio 3.3: Escribir Títulos Efectivos

**Instrucciones:** Reescriba cada título genérico como un título que comunique el hallazgo.

| Título Genérico | Dato | Título Mejorado |
|-----------------|------|-----------------|
| "Ventas por Región" | Región Norte lidera con 45% | |
| "Tendencia de Matrícula" | Cayó 20% en 5 años | |
| "Satisfacción de Empleados" | 78% está satisfecho | |
| "Comparación de Gastos" | Marketing gastó 2x más que el presupuesto | |

<details>
<summary>Ver Solución</summary>

| Título Mejorado |
|-----------------|
| "Región Norte lidera ventas con 45% del total" |
| "La matrícula ha caído 20% en los últimos 5 años" |
| "78% de empleados reporta satisfacción con su trabajo" |
| "Marketing excedió su presupuesto en un 100%" |

</details>

---

### Ejercicio 3.4: Diseñar KPIs

**Instrucciones:** Para un dashboard de recursos humanos, diseñe 4 KPIs.

| KPI | Fórmula | Frecuencia | Meta | Alerta |
|-----|---------|------------|------|--------|
| 1. | | | | |
| 2. | | | | |
| 3. | | | | |
| 4. | | | | |

<details>
<summary>Ver Solución</summary>

| KPI | Fórmula | Frecuencia | Meta | Alerta |
|-----|---------|------------|------|--------|
| 1. Tasa de rotación | (Bajas / Promedio empleados) × 100 | Mensual | <5% | >10% |
| 2. Tiempo promedio de contratación | Días desde vacante hasta contrato | Mensual | <30 días | >45 días |
| 3. Índice de ausentismo | (Días ausencia / Días laborables) × 100 | Mensual | <3% | >5% |
| 4. Satisfacción (NPS) | % Promotores - % Detractores | Trimestral | >50 | <30 |

</details>

---

## Módulo 4: Modelos Predictivos

### Ejercicio 4.1: Conceptos de ML

**Instrucciones:** Responda verdadero o falso.

| Afirmación | V/F |
|------------|-----|
| 1. Un modelo con accuracy de 95% siempre es bueno | |
| 2. Random Forest puede manejar variables categóricas sin encoding | |
| 3. El overfitting se detecta cuando el error de test es mucho mayor que el de train | |
| 4. Precision y Recall siempre mejoran juntos | |
| 5. Cross-validation elimina la necesidad de conjunto de test | |
| 6. SHAP values pueden ser negativos | |

<details>
<summary>Ver Solución</summary>

| Afirmación | V/F | Explicación |
|------------|-----|-------------|
| 1 | **Falso** | En clases desbalanceadas (99% clase A), predecir siempre A da 99% accuracy |
| 2 | **Falso** | Sklearn requiere encoding; algunas implementaciones (LightGBM) lo manejan |
| 3 | **Verdadero** | Gap grande train-test indica overfitting |
| 4 | **Falso** | Generalmente hay trade-off entre ambas |
| 5 | **Falso** | CV estima performance, pero test final sigue siendo necesario |
| 6 | **Verdadero** | SHAP negativo indica que esa feature disminuye la predicción |

</details>

---

### Ejercicio 4.2: Interpretar Métricas

**Instrucciones:** Dado el siguiente output de clasificación:

```
              precision    recall  f1-score   support

       Clase0       0.92      0.98      0.95       500
       Clase1       0.85      0.60      0.70       100

    accuracy                           0.92       600
```

1. ¿Qué clase es más fácil de predecir?
2. ¿Por qué el modelo tiene bajo recall para Clase1?
3. Si Clase1 representa fraude, ¿es este modelo aceptable?
4. ¿Qué sugeriría para mejorar el recall de Clase1?

<details>
<summary>Ver Solución</summary>

1. **Clase0 es más fácil de predecir**
   - Mayor precision (0.92 vs 0.85) y recall (0.98 vs 0.60)
   - Tiene más ejemplos (500 vs 100) - desbalance

2. **Bajo recall para Clase1 porque:**
   - Desbalance de clases (5:1)
   - El modelo "favorece" la clase mayoritaria
   - Solo detecta 60% de los casos positivos reales

3. **No es aceptable para detección de fraude**
   - Perder 40% de fraudes (recall=0.60) es crítico
   - Preferible más falsas alarmas que fraudes no detectados

4. **Sugerencias para mejorar recall Clase1:**
   - Balancear clases (oversampling, undersampling, SMOTE)
   - Ajustar umbral de decisión (bajar de 0.5)
   - Usar class_weight='balanced' en el modelo
   - Optimizar por recall o F1 en lugar de accuracy

</details>

---

### Ejercicio 4.3: Feature Importance

**Instrucciones:** Dado el siguiente output de importancia:

```
Feature               Importance
asistencia_pct        0.35
materias_reprobadas   0.25
semestre              0.15
trabaja               0.12
beca                  0.08
genero                0.05
```

1. ¿Cuál es la variable más importante para el modelo?
2. ¿Qué intervención práctica sugeriría basándose en esto?
3. ¿Por qué 'genero' tiene baja importancia? ¿Es bueno o malo?
4. ¿Estas importancias indican dirección del efecto?

<details>
<summary>Ver Solución</summary>

1. **Asistencia es la más importante (0.35)**
   - Representa 35% de la importancia total
   - Es el predictor más fuerte de rendimiento

2. **Intervención sugerida:**
   - Sistema de monitoreo de asistencia temprana
   - Alertas cuando asistencia cae por debajo de umbral
   - Contactar estudiantes con baja asistencia proactivamente

3. **Género con baja importancia:**
   - **Es bueno**: indica que el modelo no discrimina por género
   - El rendimiento no depende del género una vez controladas otras variables
   - Importante para equidad del modelo

4. **No indican dirección:**
   - Solo magnitud de importancia, no si es positivo o negativo
   - Para dirección, necesitamos SHAP o coeficientes de regresión
   - Ej: ¿más asistencia = mejor nota o peor? Importancia no lo dice

</details>

---

### Ejercicio 4.4: Overfitting

**Instrucciones:** Para cada escenario, indique si hay overfitting y qué haría.

| Escenario | Train Accuracy | Test Accuracy | ¿Overfitting? | Solución |
|-----------|----------------|---------------|---------------|----------|
| A | 95% | 93% | | |
| B | 99% | 65% | | |
| C | 70% | 68% | | |
| D | 85% | 84% | | |

<details>
<summary>Ver Solución</summary>

| Escenario | ¿Overfitting? | Explicación | Solución |
|-----------|---------------|-------------|----------|
| A | **No** | Gap pequeño (2%), ambos altos | Modelo OK |
| B | **Sí, severo** | Gap de 34%, train perfecto | Regularizar, simplificar, más datos |
| C | **No, pero underfitting** | Ambos bajos, modelo muy simple | Modelo más complejo, más features |
| D | **No** | Gap pequeño (1%), buen rendimiento | Modelo OK |

</details>

---

## Respuestas Rápidas

### Módulo 1
- 1.1: Discreto, Continuo, Nominal, Ordinal, Nominal, Continuo, Nominal, Ordinal
- 1.2: Selección, Muestreo, Confirmación
- 1.3: Temperatura, Tamaño incendio, Nivel socioeconómico
- 1.4: MCAR, MAR, MNAR, MCAR

### Módulo 2
- 2.1: Ver código en soluciones
- 2.2: Ver código en soluciones
- 2.3: Pedro sin carrera, Sociología sin estudiantes
- 2.4: Ver SQL en soluciones

### Módulo 3
- 3.1: Barras, Línea, Torta, Scatter, Barras agrupadas
- 3.2: 6 errores identificados
- 3.3: Ver títulos mejorados
- 3.4: Ver KPIs propuestos

### Módulo 4
- 4.1: F, F, V, F, F, V
- 4.2: Ver análisis completo
- 4.3: Asistencia, Monitoreo, Es bueno, No indican dirección
- 4.4: No, Sí, No (underfitting), No

---

*Última actualización: Enero 2025*
