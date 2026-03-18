# Guía de Estudio: Módulo 4 - Modelos Predictivos Simples y Proyecto Integrador

## De describir el pasado a anticipar el futuro

---

> *"Todos los modelos son incorrectos, pero algunos son útiles."*
> — George E. P. Box, estadístico

---

## Tabla de Contenidos

1. [Propósito y Relevancia del Módulo](#1-propósito-y-relevancia-del-módulo)
2. [Marco Conceptual: ¿Qué es el modelado predictivo?](#2-marco-conceptual-qué-es-el-modelado-predictivo)
3. [Conceptos Fundamentales](#3-conceptos-fundamentales)
4. [Metaaprendizaje: El Docente como Constructor de Modelos](#4-metaaprendizaje-el-docente-como-constructor-de-modelos)
5. [Conexiones con la Práctica Docente](#5-conexiones-con-la-práctica-docente)
6. [El Proyecto Integrador: Síntesis del Programa](#6-el-proyecto-integrador-síntesis-del-programa)
7. [Preguntas de Reflexión Metacognitiva](#7-preguntas-de-reflexión-metacognitiva)
8. [Lecturas Fundamentales](#8-lecturas-fundamentales)
9. [Lecturas Complementarias](#9-lecturas-complementarias)
10. [Recursos Multimedia](#10-recursos-multimedia)
11. [Actividades de Metaaprendizaje](#11-actividades-de-metaaprendizaje)
12. [Glosario de Machine Learning](#12-glosario-de-machine-learning)
13. [Referencias Bibliográficas](#13-referencias-bibliográficas)

---

## 1. Propósito y Relevancia del Módulo

### 1.1 El salto de lo descriptivo a lo predictivo

A lo largo del programa, hemos recorrido un camino:

- **Módulo 1**: Aprendimos a *pensar* con datos
- **Módulo 2**: Aprendimos a *preparar* datos
- **Módulo 3**: Aprendimos a *comunicar* con datos

Este módulo final da el paso siguiente: aprender a usar datos para **predecir el futuro**.

No es magia. No es inteligencia artificial de ciencia ficción. Es matemática aplicada: usar patrones del pasado para hacer conjeturas informadas sobre lo que vendrá.

### 1.2 Desmitificando el Machine Learning

El término "Machine Learning" (aprendizaje automático) puede intimidar. Evoca imágenes de algoritmos impenetrables y matemáticas incomprensibles.

La realidad es más accesible:

- **La regresión lineal**, que muchos de ustedes conocen de estadística, es Machine Learning
- **La regresión logística**, común en epidemiología y economía, es Machine Learning
- Estos modelos "simples" resuelven una gran cantidad de problemas reales

Este módulo se enfoca en modelos que puede **entender, explicar e interpretar**—no cajas negras impenetrables.

### 1.3 Por qué docentes necesitan entender modelos predictivos

| Contexto | Aplicación predictiva |
|----------|----------------------|
| **Investigación** | Predecir variables de interés, probar hipótesis |
| **Docencia** | Identificar estudiantes en riesgo tempranamente |
| **Gestión académica** | Proyectar matrícula, deserción, recursos |
| **Consultoría** | Ofrecer análisis predictivo a organizaciones |
| **Alfabetización** | Evaluar críticamente afirmaciones predictivas de otros |

Más allá de aplicaciones específicas, entender modelos predictivos les permite **participar informadamente** en conversaciones donde estos modelos se discuten, proponen o critican.

### 1.4 Competencias que desarrollará

| Competencia | Descripción | Nivel esperado |
|-------------|-------------|----------------|
| **Regresión lineal** | Construir e interpretar modelos de regresión | Intermedio |
| **Clasificación** | Construir e interpretar modelos de clasificación | Introductorio |
| **Evaluación de modelos** | Usar métricas apropiadas para juzgar calidad | Intermedio |
| **Pensamiento de validación** | Entender train/test, overfitting, generalización | Intermedio |
| **Interpretación** | Traducir coeficientes a lenguaje sustantivo | Avanzado |
| **Comunicación de incertidumbre** | Presentar predicciones con sus limitaciones | Intermedio |

---

## 2. Marco Conceptual: ¿Qué es el modelado predictivo?

### 2.1 Aprendizaje supervisado: El paradigma central

El **aprendizaje supervisado** es el paradigma de Machine Learning más común y relevante para este módulo.

La idea es simple:
1. Tenemos datos históricos con **entradas** (X) y **salidas conocidas** (Y)
2. Encontramos una **función** que relaciona X con Y
3. Usamos esa función para predecir Y cuando solo conocemos X

```
ENTRENAMIENTO:
  Datos históricos     →   Algoritmo    →   Modelo
  (X₁, Y₁), (X₂, Y₂)...                      f(X) ≈ Y

PREDICCIÓN:
  Nuevos datos (X_nuevo) →   Modelo   →   Predicción (Ŷ)
```

### 2.2 Tipos de problemas supervisados

| Tipo | Variable a predecir | Ejemplos | Algoritmos típicos |
|------|---------------------|----------|-------------------|
| **Regresión** | Numérica continua | Precio, nota, salario | Regresión lineal, árboles |
| **Clasificación** | Categórica | Aprobado/Reprobado, Desertor/No desertor | Regresión logística, árboles |

### 2.3 El flujo de un proyecto de Machine Learning

```
┌─────────────────────────────────────────────────────────────────┐
│                     FLUJO DE ML SIMPLIFICADO                     │
└─────────────────────────────────────────────────────────────────┘

┌──────────────────┐
│ 1. PREGUNTA      │  ¿Qué queremos predecir? ¿Por qué importa?
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ 2. DATOS         │  Recolectar, limpiar, explorar (Módulo 2)
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ 3. PREPARACIÓN   │  Selección de variables, transformaciones
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ 4. DIVISIÓN      │  Train / Test split
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ 5. MODELADO      │  Entrenar modelo(s) en datos de train
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ 6. EVALUACIÓN    │  Medir desempeño en datos de test
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ 7. INTERPRETACIÓN│  ¿Qué aprendió el modelo? ¿Tiene sentido?
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ 8. COMUNICACIÓN  │  Presentar hallazgos (Módulo 3)
└──────────────────┘
```

### 2.4 La tensión fundamental: Sesgo vs. Varianza

Todo modelo enfrenta un trade-off fundamental:

**Sesgo (Bias)**: Error por simplificación excesiva
- Modelo muy simple que no captura patrones reales
- Ejemplo: Asumir relación lineal cuando es curva

**Varianza**: Error por ajuste excesivo al ruido
- Modelo muy complejo que memoriza datos de entrenamiento
- Ejemplo: Modelo que predice perfecto en train pero falla en test

```
       Error de predicción
              │
              │    ╲           ╱
              │     ╲ Total   ╱
              │      ╲       ╱
              │       ╲     ╱
              │ Bias   ╲   ╱  Varianza
              │  ────   ╲ ╱   ────────
              │          ╳
              │         ╱ ╲
              │        ╱   ╲
              └────────────────────────▶
                  Simple    Complejo
                  Modelo
```

El **punto óptimo** está donde el error total (sesgo + varianza) es mínimo.

### 2.5 Ética del modelado predictivo

Los modelos predictivos no son neutrales. Pueden:

1. **Perpetuar sesgos históricos**: Si los datos pasados reflejan discriminación, el modelo la aprenderá
2. **Generar profecías autocumplidas**: Predecir que un estudiante desertará puede reducir recursos hacia él, causando la deserción
3. **Dar falsa sensación de certeza**: Una predicción de "75% de probabilidad" sigue siendo incierta
4. **Deshumanizar decisiones**: Reducir personas a scores y probabilidades

**Reflexión ética constante**: ¿Qué decisiones se tomarán con este modelo? ¿Quién puede ser perjudicado? ¿Es este el uso apropiado de predicción?

---

## 3. Conceptos Fundamentales

### 3.1 Regresión Lineal

#### El modelo más interpretable

La regresión lineal es probablemente el modelo predictivo más importante, no porque sea el más preciso, sino porque es el más **interpretable**.

**Modelo simple**:
```
Y = β₀ + β₁X + ε
```

Donde:
- Y = Variable a predecir (dependiente)
- X = Variable predictora (independiente)
- β₀ = Intercepto (valor de Y cuando X = 0)
- β₁ = Pendiente (cambio en Y por cada unidad de cambio en X)
- ε = Error (lo que el modelo no explica)

**Modelo múltiple**:
```
Y = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ + ε
```

#### Interpretación de coeficientes

Esta es la habilidad más importante de este módulo: traducir coeficientes a lenguaje sustantivo.

**Ejemplo**:
```python
# Modelo: Nota final ~ Asistencia + Horas de estudio
# Resultados:
# Intercepto (β₀) = 5.2
# Asistencia (β₁) = 0.08
# Horas_estudio (β₂) = 0.45
```

**Interpretación**:
- "Un estudiante con 0% de asistencia y 0 horas de estudio tendría una nota esperada de 5.2"
- "Por cada punto porcentual adicional de asistencia, la nota esperada aumenta 0.08 puntos, manteniendo horas de estudio constante"
- "Por cada hora adicional de estudio semanal, la nota esperada aumenta 0.45 puntos, manteniendo asistencia constante"

**Nota crítica**: Los coeficientes no implican causalidad. Pueden reflejar correlación, confusión, o causalidad inversa.

#### Supuestos de regresión lineal

Los modelos de regresión asumen:

| Supuesto | Descripción | Consecuencia si se viola |
|----------|-------------|-------------------------|
| **Linealidad** | Relación lineal entre X e Y | Modelo sesgado |
| **Independencia** | Errores no correlacionados | Errores estándar incorrectos |
| **Homocedasticidad** | Varianza de errores constante | Inferencia poco confiable |
| **Normalidad** | Errores normalmente distribuidos | Afecta intervalos de confianza |
| **No multicolinealidad** | Predictores no altamente correlacionados | Coeficientes inestables |

**En la práctica**: La regresión lineal es robusta a violaciones moderadas. Verificar supuestos es importante, pero no obsesionarse con perfección.

#### En Python con Scikit-learn

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# Cargar datos
df = pd.read_csv('rendimiento_academico.csv')

# Definir X (predictores) e y (variable objetivo)
X = df[['asistencia', 'horas_estudio', 'trabaja']]
y = df['nota_final']

# Dividir en train y test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Entrenar modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Ver coeficientes
print("Intercepto:", modelo.intercept_)
print("Coeficientes:", dict(zip(X.columns, modelo.coef_)))

# Predecir
predicciones = modelo.predict(X_test)
```

### 3.2 Métricas de Evaluación para Regresión

#### R² (Coeficiente de determinación)

**Interpretación**: Proporción de varianza en Y explicada por el modelo.

```
R² = 1 - (SS_residual / SS_total)
```

- R² = 1: Modelo explica toda la varianza (perfecto, sospechoso)
- R² = 0: Modelo no explica nada (tan bueno como la media)
- R² negativo: Modelo peor que la media

**Valores típicos**:
- Ciencias físicas: R² > 0.9 común
- Ciencias sociales: R² de 0.2-0.4 puede ser excelente
- **No hay R² "bueno" universal**; depende del fenómeno

#### Error Cuadrático Medio (MSE) y Raíz (RMSE)

```
MSE = (1/n) Σ(y_real - y_pred)²
RMSE = √MSE
```

**Interpretación de RMSE**: Error promedio en las mismas unidades que Y.
- Si predecimos notas (escala 0-20), RMSE de 2 significa error promedio de 2 puntos.

#### Error Absoluto Medio (MAE)

```
MAE = (1/n) Σ|y_real - y_pred|
```

**Diferencia con RMSE**: MAE es menos sensible a outliers. RMSE penaliza más los errores grandes.

#### En Python

```python
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np

# Evaluar
r2 = r2_score(y_test, predicciones)
mse = mean_squared_error(y_test, predicciones)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, predicciones)

print(f"R²: {r2:.3f}")
print(f"RMSE: {rmse:.3f}")
print(f"MAE: {mae:.3f}")
```

### 3.3 Clasificación: Regresión Logística

#### Del continuo al binario

Cuando la variable a predecir es categórica (Sí/No, Aprobado/Reprobado, Desertor/No desertor), usamos modelos de **clasificación**.

La **regresión logística** es el modelo de clasificación más interpretable para respuestas binarias.

#### El modelo logístico

En lugar de predecir Y directamente, predecimos la **probabilidad** de que Y = 1:

```
P(Y=1) = 1 / (1 + e^(-z))

donde z = β₀ + β₁X₁ + β₂X₂ + ...
```

La función logística transforma cualquier valor z en una probabilidad entre 0 y 1:

```
P(Y=1)
   │
 1 │                    ────────
   │                 ╱
   │              ╱
0.5│           ╱
   │        ╱
   │     ╱
 0 │────
   └──────────────────────────▶ z
```

#### Interpretación: Odds Ratios

Los coeficientes de regresión logística se interpretan como **log-odds**. Para facilitar interpretación, usamos **odds ratios** (OR):

```
OR = e^β
```

**Interpretación del OR**:
- OR = 1: Variable no tiene efecto
- OR > 1: Aumenta probabilidad de Y = 1
- OR < 1: Disminuye probabilidad de Y = 1

**Ejemplo**:
```
Modelo: Deserción ~ Trabaja + Promedio_previo + Beca

Coeficientes:
- Trabaja: β = 0.7 → OR = e^0.7 = 2.01
- Promedio_previo: β = -0.3 → OR = e^-0.3 = 0.74
- Beca: β = -0.5 → OR = e^-0.5 = 0.61

Interpretación:
- Estudiantes que trabajan tienen 2x las odds de desertar vs. quienes no trabajan
- Por cada punto adicional de promedio, las odds de desertar se reducen 26%
- Estudiantes con beca tienen 39% menos odds de desertar
```

#### En Python

```python
from sklearn.linear_model import LogisticRegression
import numpy as np

# Definir X e y (y debe ser binaria)
X = df[['trabaja', 'promedio_previo', 'tiene_beca']]
y = df['deserto']  # 0 o 1

# Dividir y entrenar
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
modelo_log = LogisticRegression()
modelo_log.fit(X_train, y_train)

# Coeficientes y Odds Ratios
print("Coeficientes:", modelo_log.coef_)
print("Odds Ratios:", np.exp(modelo_log.coef_))

# Predecir probabilidades
probabilidades = modelo_log.predict_proba(X_test)[:, 1]

# Predecir clases (usando umbral 0.5 por defecto)
predicciones = modelo_log.predict(X_test)
```

### 3.4 Métricas de Evaluación para Clasificación

#### Matriz de Confusión

La matriz de confusión compara predicciones con realidad:

```
                    PREDICCIÓN
                    Negativo    Positivo
              ┌────────────┬────────────┐
    Negativo  │     TN     │     FP     │
REAL          ├────────────┼────────────┤
    Positivo  │     FN     │     TP     │
              └────────────┴────────────┘

TN = True Negative (correcto)
FP = False Positive (error Tipo I)
FN = False Negative (error Tipo II)
TP = True Positive (correcto)
```

#### Métricas derivadas

| Métrica | Fórmula | Interpretación |
|---------|---------|----------------|
| **Accuracy** | (TP+TN) / Total | % de predicciones correctas |
| **Precision** | TP / (TP+FP) | De los predichos positivos, ¿cuántos lo son? |
| **Recall (Sensibilidad)** | TP / (TP+FN) | De los positivos reales, ¿cuántos detectamos? |
| **Specificity** | TN / (TN+FP) | De los negativos reales, ¿cuántos detectamos? |
| **F1 Score** | 2 × (Prec × Rec) / (Prec + Rec) | Media armónica de Precision y Recall |

#### Cuándo importa cada métrica

| Contexto | Métrica prioritaria | Por qué |
|----------|---------------------|---------|
| **Detectar fraude** | Recall | No queremos perder fraudes (FN costoso) |
| **Spam filter** | Precision | No queremos marcar email válido como spam (FP costoso) |
| **Diagnóstico médico** | Recall | No queremos perder enfermos (FN peligroso) |
| **Clases balanceadas** | Accuracy | Todas las métricas similares |
| **Clases desbalanceadas** | F1, AUC-ROC | Accuracy puede engañar |

#### El problema de clases desbalanceadas

Si el 95% de estudiantes no desertan, un modelo que predice "no desertor" para todos tiene 95% accuracy pero es inútil.

**Soluciones**:
- Usar métricas que no dependan del balance (AUC-ROC)
- Re-muestrear (oversampling de minoría, undersampling de mayoría)
- Ajustar umbrales de clasificación
- Usar algoritmos robustos a desbalance

#### En Python

```python
from sklearn.metrics import (
    confusion_matrix, accuracy_score, precision_score,
    recall_score, f1_score, classification_report
)

# Matriz de confusión
cm = confusion_matrix(y_test, predicciones)
print("Matriz de confusión:")
print(cm)

# Métricas individuales
print(f"Accuracy: {accuracy_score(y_test, predicciones):.3f}")
print(f"Precision: {precision_score(y_test, predicciones):.3f}")
print(f"Recall: {recall_score(y_test, predicciones):.3f}")
print(f"F1: {f1_score(y_test, predicciones):.3f}")

# Reporte completo
print(classification_report(y_test, predicciones))
```

### 3.5 Validación: Train/Test Split y Cross-Validation

#### Por qué dividir datos

El error que un modelo comete en los datos que usó para entrenarse es **optimista**. Para estimar cómo funcionará con datos nuevos, necesitamos evaluarlo en datos que **nunca ha visto**.

#### Train/Test Split

```
Datos totales (100%)
├── Train (70-80%): Para entrenar el modelo
└── Test (20-30%): Para evaluar el modelo
```

**Reglas**:
1. Dividir ANTES de cualquier transformación
2. No usar test para ninguna decisión de modelado
3. Evaluar en test solo al final

#### Cross-Validation (Validación Cruzada)

Para usar los datos más eficientemente, especialmente con datasets pequeños:

```
K-Fold Cross-Validation (K=5):

Iteración 1: [TEST][Train][Train][Train][Train]
Iteración 2: [Train][TEST][Train][Train][Train]
Iteración 3: [Train][Train][TEST][Train][Train]
Iteración 4: [Train][Train][Train][TEST][Train]
Iteración 5: [Train][Train][Train][Train][TEST]

→ Promedio de 5 evaluaciones
```

**Ventaja**: Usa todos los datos tanto para train como para test
**Desventaja**: Más computacionalmente costoso

#### En Python

```python
from sklearn.model_selection import cross_val_score, KFold

# Cross-validation simple
scores = cross_val_score(modelo, X, y, cv=5, scoring='r2')
print(f"R² promedio: {scores.mean():.3f} (+/- {scores.std()*2:.3f})")

# Con más control
kf = KFold(n_splits=5, shuffle=True, random_state=42)
for i, (train_idx, test_idx) in enumerate(kf.split(X)):
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
    # ... entrenar y evaluar
```

### 3.6 Overfitting y Underfitting

#### Underfitting

El modelo es **demasiado simple** para capturar los patrones en los datos.

**Síntomas**:
- Error alto en train Y en test
- R² bajo en ambos
- Residuos con patrones sistemáticos

**Soluciones**:
- Agregar variables predictoras
- Usar modelo más flexible
- Agregar términos no lineales

#### Overfitting

El modelo es **demasiado complejo** y "memoriza" el ruido de los datos de entrenamiento.

**Síntomas**:
- Error muy bajo en train, alto en test
- Diferencia grande entre R² en train vs. test
- Modelo funciona perfecto en train pero falla con datos nuevos

**Soluciones**:
- Simplificar modelo
- Agregar más datos
- Usar regularización
- Cross-validation para seleccionar modelo

#### Diagnóstico visual

```python
import matplotlib.pyplot as plt

# Comparar predicciones en train vs test
train_pred = modelo.predict(X_train)
test_pred = modelo.predict(X_test)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].scatter(y_train, train_pred)
axes[0].set_title(f'Train (R²={r2_score(y_train, train_pred):.3f})')

axes[1].scatter(y_test, test_pred)
axes[1].set_title(f'Test (R²={r2_score(y_test, test_pred):.3f})')

plt.show()
```

---

## 4. Metaaprendizaje: El Docente como Constructor de Modelos

### 4.1 De usuario a constructor de modelos mentales

Todos construimos **modelos mentales** del mundo constantemente:
- "Si estudio más, obtendré mejores notas"
- "Los estudiantes que trabajan tienen más dificultades"
- "La asistencia correlaciona con el rendimiento"

El Machine Learning formaliza este proceso. Los modelos explícitos tienen ventajas:
- Son **falsificables**: Podemos probarlos con datos
- Son **comunicables**: Otros pueden evaluarlos y criticarlos
- Son **mejorables**: Podemos refinarlos sistemáticamente

### 4.2 El peligro de la sobreconfianza

Los modelos predictivos pueden generar **falsa sensación de certeza**:

- Un modelo con 85% de accuracy sigue fallando 15% del tiempo
- Las predicciones son probabilísticas, no determinísticas
- El modelo refleja patrones pasados que pueden no continuar

**Práctica recomendada**: Siempre comunicar la incertidumbre junto con la predicción.

### 4.3 Modelos como herramientas de pensamiento

Más allá de las predicciones, el proceso de construir modelos es valioso porque:

1. **Obliga a ser explícito**: ¿Qué variables creo que importan? ¿Qué relaciones espero?
2. **Revela supuestos**: Los supuestos se hacen visibles y cuestionables
3. **Facilita experimentación**: ¿Qué pasa si agrego esta variable? ¿Si la quito?
4. **Genera preguntas**: ¿Por qué este coeficiente tiene este signo? ¿Por qué este predictor no importa?

### 4.4 Interpretabilidad vs. Precisión

Existe un trade-off entre modelos interpretables y modelos precisos:

```
Interpretabilidad ←───────────────────────────────► Precisión
       │                                                  │
Regresión lineal                               Deep Learning
Regresión logística                            Random Forest
Árboles de decisión                            Gradient Boosting
```

Para este programa, priorizamos **interpretabilidad**:
- Coeficientes que podemos explicar
- Relaciones que tienen sentido sustantivo
- Modelos que generan comprensión, no solo predicción

### 4.5 Reflexión sobre la enseñanza de modelos

Enseñar modelado predictivo requiere balance:

**Riesgo 1: Tecnicismo excesivo**
- Enfocarse en código y algoritmos
- Perder de vista el propósito y la interpretación

**Riesgo 2: Caja negra**
- Enseñar a "presionar botones" sin comprensión
- Generar usuarios que no pueden diagnosticar problemas

**Riesgo 3: Falta de crítica**
- Presentar modelos como verdad absoluta
- No discutir limitaciones y sesgos

**Balance recomendado**:
- Empezar con el *por qué* antes del *cómo*
- Enfatizar interpretación sobre predicción
- Discutir limitaciones explícitamente
- Usar ejemplos del dominio de los estudiantes

---

## 5. Conexiones con la Práctica Docente

### 5.1 Para docentes de Economía

#### Aplicaciones de modelado predictivo

| Problema | Tipo | Variables posibles |
|----------|------|-------------------|
| Proyectar inflación | Regresión | Liquidez, tipo de cambio, expectativas |
| Predecir PIB trimestral | Regresión | Indicadores adelantados, comercio |
| Clasificar países por desarrollo | Clasificación | Indicadores socioeconómicos |
| Riesgo crediticio | Clasificación | Historial, ingresos, empleo |

#### Conexión con econometría

Si ha estudiado econometría, reconocerá:
- **Regresión lineal** = OLS (Mínimos Cuadrados Ordinarios)
- **Regresión logística** = Modelos de elección binaria (Probit/Logit)

La diferencia de ML es el énfasis en **predicción** y **validación fuera de muestra**, vs. el énfasis econométrico en **inferencia causal** y **errores estándar**.

**Ambos enfoques son valiosos y complementarios.**

#### Reflexión pedagógica

*¿Cómo distingue actualmente entre asociación y causalidad en su enseñanza de econometría? ¿Podría incorporar la perspectiva predictiva de ML para complementar?*

### 5.2 Para docentes de Administración

#### Aplicaciones de modelado predictivo

| Problema | Tipo | Variables posibles |
|----------|------|-------------------|
| Predecir ventas | Regresión | Histórico, temporada, precio |
| Scoring de clientes | Clasificación | Demografía, comportamiento |
| Rotación de empleados | Clasificación | Satisfacción, antigüedad, salario |
| Customer Lifetime Value | Regresión | Compras, frecuencia, recencia |

#### Analytics aplicado a gestión

El "Analytics" empresarial se categoriza frecuentemente como:

| Nivel | Pregunta | Herramientas |
|-------|----------|--------------|
| **Descriptivo** | ¿Qué pasó? | BI, dashboards |
| **Diagnóstico** | ¿Por qué pasó? | Análisis de causa raíz |
| **Predictivo** | ¿Qué pasará? | ML, regresión |
| **Prescriptivo** | ¿Qué hacer? | Optimización, simulación |

Este módulo les equipa para el nivel **predictivo**.

#### Reflexión pedagógica

*¿Sus estudiantes de administración aprenden a consumir predicciones críticamente, o podrían ser engañados por proveedores de "soluciones de IA"? ¿Cómo desarrollar escepticismo informado?*

### 5.3 Para docentes de Contaduría

#### Aplicaciones de modelado predictivo

| Problema | Tipo | Variables posibles |
|----------|------|-------------------|
| Detectar fraude | Clasificación | Anomalías, patrones |
| Riesgo de quiebra | Clasificación | Ratios financieros (Altman Z) |
| Proyectar ingresos | Regresión | Histórico, indicadores |
| Valoración de empresas | Regresión | Fundamentales, comparables |

#### Auditoría y Analytics

La auditoría moderna incorpora cada vez más analytics:
- **Análisis de toda la población** en lugar de muestreo
- **Detección de anomalías** automatizada
- **Evaluación de riesgo** basada en modelos

#### El modelo Z de Altman

El Z-score de Altman (1968) es un ejemplo clásico de modelo predictivo en contaduría:

```
Z = 1.2×(Working Capital/Total Assets)
  + 1.4×(Retained Earnings/Total Assets)
  + 3.3×(EBIT/Total Assets)
  + 0.6×(Market Value Equity/Total Liabilities)
  + 1.0×(Sales/Total Assets)

Z > 2.99: Zona segura
1.81 < Z < 2.99: Zona gris
Z < 1.81: Zona de peligro
```

Este modelo de los años 60 ilustra cómo la regresión puede crear herramientas de decisión duraderas.

#### Reflexión pedagógica

*¿Sus estudiantes aprenden modelos como el Z-score como "fórmulas a aplicar" o entienden que son modelos empíricos derivados de datos, con supuestos y limitaciones?*

### 5.4 Para docentes de Relaciones Industriales

#### Aplicaciones de modelado predictivo

| Problema | Tipo | Variables posibles |
|----------|------|-------------------|
| Predecir rotación | Clasificación | Satisfacción, salario, antigüedad |
| Proyectar ausentismo | Regresión | Clima, variables personales |
| Identificar talento | Clasificación | Desempeño, potencial, competencias |
| Equidad salarial | Regresión | Nivel, experiencia, educación, género |

#### People Analytics

El campo de **People Analytics** aplica ciencia de datos a RRHH:

- Análisis de redes para identificar empleados clave
- NLP para análisis de encuestas abiertas
- Predicción de desempeño y potencial
- Optimización de equipos

**Nota ética**: Los modelos predictivos en RRHH son particularmente sensibles. Pueden violar privacidad, perpetuar discriminación, y deshumanizar la gestión de personas.

#### Reflexión pedagógica

*¿Cómo equilibrar el potencial de People Analytics con las consideraciones éticas? ¿Qué debería ser off-limits para la predicción algorítmica?*

---

## 6. El Proyecto Integrador: Síntesis del Programa

### 6.1 Propósito del proyecto

El proyecto integrador es la culminación del programa. Demuestra que puede:

1. **Formular** una pregunta relevante para su disciplina
2. **Obtener y preparar** datos apropiados (Módulo 2)
3. **Construir** un modelo predictivo (Módulo 4)
4. **Evaluar** el modelo con métricas apropiadas
5. **Comunicar** hallazgos efectivamente (Módulo 3)
6. **Reflexionar** sobre implicaciones pedagógicas (Módulo 1)

### 6.2 Estructura recomendada

```
┌─────────────────────────────────────────────────────────────────┐
│  1. INTRODUCCIÓN Y MOTIVACIÓN                                    │
│  - ¿Por qué esta pregunta importa?                              │
│  - ¿Quién se beneficiaría de esta predicción?                   │
│  - Conexión con su disciplina/asignatura                        │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│  2. DATOS                                                        │
│  - Fuente y descripción del dataset                             │
│  - EDA: estadísticas descriptivas, visualizaciones              │
│  - Limpieza y transformaciones aplicadas                        │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│  3. MODELADO                                                     │
│  - Selección de variables (justificada)                         │
│  - División train/test                                          │
│  - Entrenamiento del modelo                                     │
│  - Coeficientes e interpretación                                │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│  4. EVALUACIÓN                                                   │
│  - Métricas en train y test                                     │
│  - Diagnóstico de overfitting/underfitting                      │
│  - Visualizaciones de desempeño                                 │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│  5. HALLAZGOS Y DISCUSIÓN                                        │
│  - 3 hallazgos principales (en lenguaje no técnico)             │
│  - Limitaciones del modelo                                      │
│  - Implicaciones prácticas                                      │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│  6. APLICACIÓN PEDAGÓGICA                                        │
│  - ¿Cómo usaría este análisis en su enseñanza?                  │
│  - ¿Qué ejercicio diseñaría para sus estudiantes?               │
│  - Reflexión sobre metaaprendizaje                              │
└─────────────────────────────────────────────────────────────────┘
```

### 6.3 Criterios de evaluación (resumen)

| Componente | Peso | Foco principal |
|------------|------|----------------|
| **Portafolio de análisis** | 40% | Dataset limpio, proceso documentado, reproducibilidad |
| **Dashboard de BI** | 30% | Visualizaciones efectivas, storytelling |
| **Proyecto predictivo** | 30% | Modelo correcto, evaluación, interpretación |

### 6.4 Errores comunes a evitar

1. **Pregunta vaga**: "Analizar rendimiento estudiantil" vs. "Predecir qué estudiantes están en riesgo de reprobar"

2. **Modelo sin propósito**: Entrenar modelo sin claridad sobre qué decisión informaría

3. **Evaluar solo en train**: No reportar métricas en test es error grave

4. **Coeficientes sin interpretación**: Listar números sin explicar qué significan

5. **Ignorar limitaciones**: Todo modelo tiene limitaciones; ocultarlas es deshonesto

6. **Jerga técnica excesiva**: Hallazgos deben ser comprensibles para no expertos

### 6.5 Guías por carrera

El repositorio incluye guías específicas con preguntas de investigación sugeridas para cada carrera:

- `proyecto_administracion.md`: Gestión, eficiencia, recursos
- `proyecto_contaduria.md`: Análisis financiero, auditoría
- `proyecto_economia.md`: Indicadores macro, comercio
- `proyecto_relaciones_industriales.md`: RRHH, clima laboral

**Use estas guías como punto de partida, no como límite.**

---

## 7. Preguntas de Reflexión Metacognitiva

### 7.1 Antes de comenzar el módulo

1. ¿Qué entiende actualmente por "Machine Learning"? ¿De dónde viene esa comprensión?

2. ¿Ha usado alguna vez regresión (lineal o logística)? ¿En qué contexto?

3. ¿Qué predicción sería útil en su contexto profesional? ¿Qué datos necesitaría?

4. ¿Cómo se siente ante la idea de "predecir" comportamiento humano con algoritmos?

### 7.2 Durante el módulo

5. ¿Qué concepto le ha costado más entender? ¿Qué estrategia ha usado?

6. ¿Ha encontrado conexiones entre estos modelos y técnicas que ya conocía de su disciplina?

7. ¿Qué modelo (regresión o clasificación) le parece más relevante para su trabajo?

8. ¿Qué preocupaciones éticas le surgen al trabajar con modelos predictivos?

### 7.3 Al finalizar el módulo

9. ¿Cómo explicaría la diferencia entre regresión y clasificación a un colega no técnico?

10. ¿Qué métrica de evaluación usaría para un modelo que predice deserción estudiantil? ¿Por qué?

11. ¿Cómo ha cambiado su comprensión de qué significa "predecir" algo?

12. ¿Qué aspecto del modelado predictivo quiere seguir explorando después del programa?

### 7.4 Reflexión integradora del programa

13. ¿Cómo se conectan los cuatro módulos en su comprensión?

14. ¿Qué competencia desarrollada considera más valiosa para su práctica profesional?

15. ¿Qué cambios concretos hará en su enseñanza como resultado de este programa?

16. Si tuviera que explicar en 2 minutos qué aprendió en este programa, ¿qué diría?

---

## 8. Lecturas Fundamentales

### 8.1 Lectura obligatoria principal

**James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning with Applications in R* (2da edición). Springer.**

- **ISBN**: 978-1071614174
- **Páginas**: 607
- **Acceso gratuito**: [PDF oficial](https://www.statlearning.com/)
- **Por qué es fundamental**: Conocido como "ISLR", es LA introducción accesible a Machine Learning. Los autores son estadísticos de Stanford que priorizan comprensión sobre complejidad. Los primeros 4 capítulos cubren exactamente lo que necesita para este módulo.
- **Capítulos prioritarios**: 2 (Statistical Learning), 3 (Linear Regression), 4 (Classification)

### 8.2 Lectura obligatoria complementaria

**Bruce, P., Bruce, A., & Gedeck, P. (2020). *Practical Statistics for Data Scientists* (2da edición). O'Reilly Media.**

- **ISBN**: 978-1492072942
- **Páginas**: 368
- **Disponibilidad**: [Amazon](https://www.amazon.com/Practical-Statistics-Data-Scientists-Essential/dp/149207294X)
- **Por qué es fundamental**: Puente entre estadística tradicional y Data Science. Más práctico que ISLR, con ejemplos en Python. Excelente para refrescar conceptos estadísticos en contexto de ML.
- **Capítulos prioritarios**: 4 (Regression), 5 (Classification)

### 8.3 Lectura recomendada

**Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3ra edición). O'Reilly Media.**

- **ISBN**: 978-1098125974
- **Páginas**: 856
- **Por qué es importante**: La guía práctica más completa para ML en Python. Los primeros capítulos son accesibles; el resto es referencia para cuando quiera ir más allá.
- **Capítulos prioritarios**: 1 (The Machine Learning Landscape), 2 (End-to-End ML Project), 4 (Training Models)

---

## 9. Lecturas Complementarias

### 9.1 Para profundizar en regresión

**Montgomery, D. C., Peck, E. A., & Vining, G. G. (2021). *Introduction to Linear Regression Analysis* (6ta edición). Wiley.**

- **ISBN**: 978-1119578727
- **Relevancia**: Tratamiento exhaustivo de regresión lineal. Más técnico, pero excelente para profundizar si tiene formación estadística.

**Fox, J. (2015). *Applied Regression Analysis and Generalized Linear Models* (3ra edición). SAGE.**

- **ISBN**: 978-1452205663
- **Relevancia**: Enfoque aplicado con ejemplos en ciencias sociales. Buen balance entre teoría y aplicación.

### 9.2 Para profundizar en clasificación

**Hosmer, D. W., Lemeshow, S., & Sturdivant, R. X. (2013). *Applied Logistic Regression* (3ra edición). Wiley.**

- **ISBN**: 978-0470582473
- **Relevancia**: LA referencia para regresión logística. Orientado a epidemiología pero aplicable a ciencias sociales.

### 9.3 Para ética y ML

**O'Neil, C. (2016). *Weapons of Math Destruction*. Crown.**

- **ISBN**: 978-0553418811
- **Relevancia**: Casos de cómo modelos predictivos pueden causar daño. Esencial para perspectiva crítica.

**Eubanks, V. (2018). *Automating Inequality: How High-Tech Tools Profile, Police, and Punish the Poor*. St. Martin's Press.**

- **ISBN**: 978-1250074317
- **Relevancia**: Cómo sistemas algorítmicos afectan a poblaciones vulnerables. Importante para considerar impactos de modelos predictivos.

### 9.4 Artículos académicos clave

**Breiman, L. (2001). Statistical modeling: The two cultures. *Statistical Science*, 16(3), 199-231.**

- **DOI**: [10.1214/ss/1009213726](https://doi.org/10.1214/ss/1009213726)
- **Relevancia**: Artículo seminal que contrasta cultura de "modelado de datos" (estadística tradicional) vs. "modelado algorítmico" (ML). Fundamental para entender las tensiones entre enfoques.

**Mullainathan, S., & Spiess, J. (2017). Machine learning: An applied econometric approach. *Journal of Economic Perspectives*, 31(2), 87-106.**

- **DOI**: [10.1257/jep.31.2.87](https://doi.org/10.1257/jep.31.2.87)
- **Relevancia**: Para economistas, este artículo explica qué puede aportar ML a la economía y qué no.

---

## 10. Recursos Multimedia

### 10.1 Videos esenciales

#### Serie: StatQuest - Josh Starmer

- **URL**: [YouTube Channel](https://www.youtube.com/c/joshstarmer)
- **Por qué verla**: Josh Starmer tiene el don de explicar conceptos estadísticos y de ML de manera accesible y entretenida. Sus videos sobre regresión y clasificación son particularmente recomendados.
- **Videos prioritarios**:
  - "Linear Regression, Clearly Explained!!!"
  - "Logistic Regression, Clearly Explained!!!"
  - "Machine Learning Fundamentals: Cross Validation"
  - "ROC and AUC, Clearly Explained!"

#### Serie: 3Blue1Brown - Essence of Linear Algebra

- **URL**: [YouTube Playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- **Por qué verla**: Para entender la matemática detrás de regresión (que es álgebra lineal), Grant Sanderson ofrece la visualización más intuitiva disponible.

#### Curso: Andrew Ng - Machine Learning (Coursera)

- **URL**: [Coursera](https://www.coursera.org/learn/machine-learning)
- **Duración**: ~60 horas
- **Por qué verlo**: El curso que popularizó ML para audiencias no técnicas. Andrew Ng es claro y pedagógico. Se puede auditar gratis.

#### Charla: Cassie Kozyrkov - Making Friends with Machine Learning

- **URL**: [YouTube](https://www.youtube.com/watch?v=1vkb7BCMQd0)
- **Duración**: ~6 horas (serie)
- **Por qué verla**: Cassie, Chief Decision Scientist de Google, desmitifica ML con humor y claridad. Excelente para perspectiva de alto nivel.

### 10.2 Cursos online gratuitos

**Google Machine Learning Crash Course**

- **URL**: [developers.google.com/machine-learning/crash-course](https://developers.google.com/machine-learning/crash-course)
- **Duración**: ~15 horas
- **Descripción**: Curso oficial de Google con ejercicios interactivos. Equilibrio entre conceptos y práctica.

**Kaggle Learn - Intro to Machine Learning**

- **URL**: [kaggle.com/learn/intro-to-machine-learning](https://www.kaggle.com/learn/intro-to-machine-learning)
- **Duración**: ~3 horas
- **Descripción**: Introducción práctica con notebooks interactivos. Excelente para comenzar.

**fast.ai - Practical Deep Learning**

- **URL**: [course.fast.ai](https://course.fast.ai/)
- **Descripción**: Aunque enfocado en deep learning, los primeros capítulos sobre ML son accesibles y prácticos.

### 10.3 Recursos de práctica

**Kaggle Competitions (Beginner)**

- **URL**: [kaggle.com/competitions](https://www.kaggle.com/competitions)
- **Competencias recomendadas**:
  - Titanic (clasificación)
  - House Prices (regresión)
  - Digit Recognizer (clasificación)

**Scikit-learn Examples Gallery**

- **URL**: [scikit-learn.org/stable/auto_examples](https://scikit-learn.org/stable/auto_examples/)
- **Descripción**: Ejemplos ejecutables de todos los algoritmos de scikit-learn. Excelente para entender API y casos de uso.

**UCI Machine Learning Repository**

- **URL**: [archive.ics.uci.edu/ml](https://archive.ics.uci.edu/ml/)
- **Descripción**: Repositorio clásico de datasets para ML. Datasets bien documentados para práctica.

---

## 11. Actividades de Metaaprendizaje

### 11.1 Actividad: Modelo mental explícito

**Objetivo**: Hacer explícito un modelo predictivo que ya tiene en mente.

**Duración**: 30-45 minutos

**Instrucciones**:

1. Piense en una predicción que hace regularmente en su trabajo:
   - ¿Qué estudiantes aprobarán?
   - ¿Qué proyectos tendrán éxito?
   - ¿Qué tendencia seguirá un indicador?

2. Escriba su "modelo" informal:
   - ¿Qué factores considera?
   - ¿Cómo los combina?
   - ¿Qué pesos les da implícitamente?

3. Traduzca a notación de regresión:
   ```
   Y = β₀ + β₁X₁ + β₂X₂ + ...
   ```
   - ¿Qué es Y?
   - ¿Qué son las X?
   - ¿Los β son positivos o negativos?

4. Reflexione:
   - ¿En qué datos se basa su modelo mental?
   - ¿Cuánto confía en sus predicciones?
   - ¿Podría probarlo con datos reales?

### 11.2 Actividad: Interpretación de coeficientes

**Objetivo**: Practicar la traducción de coeficientes a lenguaje sustantivo.

**Duración**: 45-60 minutos

**Instrucciones**:

Dado el siguiente modelo de regresión para predecir **nota final** de estudiantes:

```
Nota = 4.5 + 0.05×Asistencia + 0.8×Horas_estudio - 1.2×Trabaja + 0.6×Beca

Donde:
- Asistencia: % de clases atendidas (0-100)
- Horas_estudio: horas semanales dedicadas (0-30)
- Trabaja: 1 si trabaja, 0 si no
- Beca: 1 si tiene beca, 0 si no

Métricas:
- R² = 0.42
- RMSE = 2.3
```

Responda:

1. Interprete cada coeficiente en lenguaje no técnico.

2. ¿Cuál factor tiene mayor impacto en la nota? ¿Cómo lo determinó?

3. Prediga la nota de un estudiante con:
   - 80% asistencia
   - 10 horas de estudio semanal
   - Trabaja
   - No tiene beca

4. ¿Qué significa R² = 0.42 en este contexto? ¿Es "bueno"?

5. ¿Qué significa RMSE = 2.3? ¿Cómo lo comunicaría a un decano?

6. ¿Qué limitaciones tiene este modelo? ¿Qué no captura?

### 11.3 Actividad: Diseño de evaluación

**Objetivo**: Desarrollar criterio para elegir métricas de evaluación.

**Duración**: 30-45 minutos

**Instrucciones**:

Para cada escenario, seleccione la métrica más apropiada y justifique:

**Escenario 1**: Modelo que predice si un estudiante desertará
- Opciones: Accuracy, Precision, Recall, F1
- Contexto: El programa de retención tiene recursos limitados para intervenir con 20 estudiantes
- Su elección y justificación:

**Escenario 2**: Modelo que proyecta inscripción para el próximo semestre
- Opciones: R², RMSE, MAE
- Contexto: El presupuesto se asigna basado en esta proyección
- Su elección y justificación:

**Escenario 3**: Modelo que clasifica transacciones como fraudulentas
- Opciones: Accuracy, Precision, Recall, F1
- Contexto: Las transacciones marcadas como fraude se bloquean automáticamente
- Su elección y justificación:

### 11.4 Actividad: Crítica de modelo publicado

**Objetivo**: Desarrollar capacidad crítica para evaluar modelos de otros.

**Duración**: 60-90 minutos

**Instrucciones**:

1. Busque un artículo académico o reporte que use regresión o clasificación en su disciplina.

2. Analice críticamente:
   - ¿Cuál es la pregunta de investigación?
   - ¿Qué modelo usaron?
   - ¿Cómo evaluaron el modelo?
   - ¿Cómo reportaron los resultados?
   - ¿Hay división train/test?
   - ¿Se discuten limitaciones?

3. Califique (1-5) y justifique:
   - Claridad de la pregunta
   - Apropiación del modelo
   - Rigor de la evaluación
   - Calidad de la interpretación
   - Discusión de limitaciones

4. ¿Qué haría diferente si fuera usted quien condujera el estudio?

### 11.5 Actividad: Planificación del proyecto integrador

**Objetivo**: Estructurar el proyecto integrador antes de comenzar.

**Duración**: 60-90 minutos

**Instrucciones**:

Complete este template de planificación:

**1. Pregunta de investigación**:
- ¿Qué quiero predecir?
- ¿Por qué importa esta predicción?
- ¿Quién usaría esta predicción?

**2. Datos**:
- ¿Qué dataset usaré? (del programa o propio)
- ¿Cuál es la variable objetivo (Y)?
- ¿Cuáles son los predictores candidatos (X)?
- ¿Cuántas observaciones hay?

**3. Tipo de problema**:
- [ ] Regresión (Y continua)
- [ ] Clasificación (Y categórica)

**4. Evaluación**:
- ¿Qué métrica(s) usaré? ¿Por qué?
- ¿Qué sería un resultado "exitoso"?

**5. Limitaciones anticipadas**:
- ¿Qué puede salir mal?
- ¿Qué no puede capturar este modelo?

**6. Aplicación pedagógica**:
- ¿Cómo conecta con mi asignatura?
- ¿Qué ejercicio derivaría para mis estudiantes?

---

## 12. Glosario de Machine Learning

### Accuracy
**Definición**: Proporción de predicciones correctas sobre el total.
**Fórmula**: (TP + TN) / Total
**Limitación**: Engañosa con clases desbalanceadas.

### Bias (Sesgo del modelo)
**Definición**: Error por simplificación excesiva; diferencia entre predicción promedio y valor real.
**No confundir con**: Sesgo estadístico o sesgo cognitivo.

### Classification (Clasificación)
**Definición**: Problema de ML donde la variable objetivo es categórica.
**Ejemplos**: Spam/No spam, Aprobado/Reprobado, Tipo de cliente.

### Coefficient (Coeficiente)
**Definición**: En regresión lineal, el peso asociado a cada variable predictora.
**Interpretación**: Cambio en Y por unidad de cambio en X, manteniendo otras variables constantes.

### Cross-Validation (Validación Cruzada)
**Definición**: Técnica de evaluación que usa múltiples divisiones train/test para estimar desempeño.
**Variantes**: K-Fold, Leave-One-Out, Stratified.

### Feature (Característica)
**Definición**: Variable predictora, input del modelo. Sinónimo de variable independiente.
**En español**: A veces "atributo" o "predictor".

### F1 Score
**Definición**: Media armónica de Precision y Recall.
**Fórmula**: 2 × (Precision × Recall) / (Precision + Recall)
**Uso**: Cuando se necesita balance entre Precision y Recall.

### Generalization (Generalización)
**Definición**: Capacidad del modelo de hacer buenas predicciones en datos nuevos, no vistos durante entrenamiento.

### Label (Etiqueta)
**Definición**: La variable objetivo en aprendizaje supervisado. Lo que queremos predecir.
**Sinónimos**: Target, variable dependiente, Y.

### Logistic Regression (Regresión Logística)
**Definición**: Modelo de clasificación binaria que estima probabilidades usando función logística.
**A pesar del nombre**: Es un modelo de clasificación, no de regresión.

### MSE / RMSE
**Definición**: Mean Squared Error / Root Mean Squared Error.
**Uso**: Métricas de error para regresión.
**Interpretación RMSE**: Error promedio en las mismas unidades que Y.

### Odds Ratio
**Definición**: En regresión logística, e^β. Razón de odds entre grupos.
**Interpretación**: OR > 1 aumenta odds; OR < 1 disminuye odds.

### Overfitting (Sobreajuste)
**Definición**: Modelo que se ajusta demasiado a los datos de entrenamiento, capturando ruido.
**Síntoma**: Desempeño excelente en train, malo en test.

### Precision
**Definición**: De los predichos como positivos, proporción que realmente lo es.
**Fórmula**: TP / (TP + FP)

### R² (R-cuadrado)
**Definición**: Coeficiente de determinación; proporción de varianza explicada.
**Rango**: 0 a 1 (puede ser negativo si modelo es peor que la media).

### Recall (Sensibilidad)
**Definición**: De los positivos reales, proporción que detectamos.
**Fórmula**: TP / (TP + FN)
**Sinónimo**: Sensitivity, True Positive Rate.

### Regression (Regresión)
**Definición**: Problema de ML donde la variable objetivo es numérica continua.
**Ejemplos**: Precio, nota, salario.

### Regularization (Regularización)
**Definición**: Técnica para prevenir overfitting penalizando complejidad del modelo.
**Tipos**: L1 (Lasso), L2 (Ridge).

### Supervised Learning (Aprendizaje Supervisado)
**Definición**: Paradigma de ML donde entrenamos con datos que tienen etiquetas conocidas.
**Contraste**: Unsupervised learning no tiene etiquetas.

### Target
**Definición**: Variable objetivo a predecir. Sinónimo de label, Y, variable dependiente.

### Test Set
**Definición**: Porción de datos reservada para evaluación final del modelo.
**Regla**: Nunca usar para decisiones de modelado.

### Train Set
**Definición**: Porción de datos usada para entrenar el modelo.

### Underfitting (Subajuste)
**Definición**: Modelo demasiado simple que no captura patrones en los datos.
**Síntoma**: Desempeño malo en train y en test.

### Variance (Varianza del modelo)
**Definición**: Sensibilidad del modelo a fluctuaciones en datos de entrenamiento.
**Trade-off**: Modelos complejos tienen alta varianza, bajo sesgo.

---

## 13. Referencias Bibliográficas

### Referencias citadas en esta guía

Box, G. E. P. (1976). Science and statistics. *Journal of the American Statistical Association*, 71(356), 791-799.

Breiman, L. (2001). Statistical modeling: The two cultures. *Statistical Science*, 16(3), 199-231.

Bruce, P., Bruce, A., & Gedeck, P. (2020). *Practical Statistics for Data Scientists* (2da edición). O'Reilly Media.

Eubanks, V. (2018). *Automating Inequality: How High-Tech Tools Profile, Police, and Punish the Poor*. St. Martin's Press.

Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3ra edición). O'Reilly Media.

Hosmer, D. W., Lemeshow, S., & Sturdivant, R. X. (2013). *Applied Logistic Regression* (3ra edición). Wiley.

James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning with Applications in R* (2da edición). Springer.

Mullainathan, S., & Spiess, J. (2017). Machine learning: An applied econometric approach. *Journal of Economic Perspectives*, 31(2), 87-106.

O'Neil, C. (2016). *Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy*. Crown.

### Referencias adicionales recomendadas

Altman, E. I. (1968). Financial ratios, discriminant analysis and the prediction of corporate bankruptcy. *The Journal of Finance*, 23(4), 589-609.

Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.

Chollet, F. (2021). *Deep Learning with Python* (2da edición). Manning.

Deisenroth, M. P., Faisal, A. A., & Ong, C. S. (2020). *Mathematics for Machine Learning*. Cambridge University Press.

Fox, J. (2015). *Applied Regression Analysis and Generalized Linear Models* (3ra edición). SAGE.

Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2da edición). Springer.

Kuhn, M., & Johnson, K. (2013). *Applied Predictive Modeling*. Springer.

Molnar, C. (2022). *Interpretable Machine Learning* (2da edición). [christophm.github.io/interpretable-ml-book](https://christophm.github.io/interpretable-ml-book/)

Montgomery, D. C., Peck, E. A., & Vining, G. G. (2021). *Introduction to Linear Regression Analysis* (6ta edición). Wiley.

Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.

Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, 12, 2825-2830.

Rudin, C. (2019). Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. *Nature Machine Intelligence*, 1(5), 206-215.

---

## Nota Final

Este módulo cierra el círculo del programa. Comenzamos preguntándonos cómo pensar con datos (Módulo 1), aprendimos a prepararlos (Módulo 2), a comunicarlos (Módulo 3), y ahora a usarlos para anticipar el futuro (Módulo 4).

Pero "predecir el futuro" requiere humildad. Los modelos son simplificaciones de una realidad compleja. Son útiles, pero no omniscientes. Son herramientas, no oráculos.

Como docentes, su rol va más allá de usar estos modelos: es formar la próxima generación de profesionales que los usarán. Eso implica enseñar no solo técnicas, sino también **criterio**: cuándo usar un modelo, cuándo no confiar en él, cómo interpretarlo con matices, y cómo comunicar su incertidumbre.

El proyecto integrador es su oportunidad de demostrar que ha internalizado no solo las técnicas, sino también esta perspectiva crítica.

*Los modelos nos ayudan a ver patrones, pero somos nosotros quienes decidimos qué hacer con ellos.*

---

**Versión**: 1.0
**Fecha**: Marzo 2026
**Programa**: Formación Docente en Ciencia de Datos y BI - FACES UCAB
**Licencia**: CC BY-SA 4.0

