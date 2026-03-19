# Glosario Técnico Unificado

Términos técnicos utilizados en el programa de formación docente en BI-FACES, organizados alfabéticamente con definiciones en español.

---

## A

### Accuracy (Exactitud)
Métrica de clasificación que mide la proporción de predicciones correctas sobre el total. Se calcula como (VP + VN) / Total. **Limitación:** Puede ser engañosa en clases desbalanceadas.

### Agregación
Proceso de resumir múltiples valores en uno solo mediante funciones como suma, promedio, conteo, máximo o mínimo. En SQL: `SUM()`, `AVG()`, `COUNT()`. En Pandas: `.groupby().agg()`.

### Algoritmo
Secuencia de pasos o reglas definidas para resolver un problema o realizar un cálculo. En ML, los algoritmos aprenden patrones de los datos para hacer predicciones.

### API (Application Programming Interface)
Interfaz que permite a diferentes programas comunicarse entre sí. Ejemplo: usar la API del Banco Mundial para obtener datos económicos.

### Atributos Pre-atentivos
Propiedades visuales que el cerebro procesa automáticamente sin esfuerzo consciente: color, tamaño, posición, orientación. Fundamentales en diseño de visualizaciones.

### AUC-ROC (Area Under the ROC Curve)
Métrica que mide la capacidad de un clasificador para distinguir entre clases. Valores: 0.5 (aleatorio) a 1.0 (perfecto). Ver también: *Curva ROC*.

---

## B

### Baseline
Modelo simple de referencia contra el cual se comparan modelos más complejos. Ejemplo: predecir siempre la clase mayoritaria, o usar el promedio.

### Big Data
Conjuntos de datos tan grandes o complejos que las herramientas tradicionales no pueden procesarlos eficientemente. Caracterizado por las "3 Vs": Volumen, Velocidad, Variedad.

### Binning
Técnica de discretización que agrupa valores continuos en intervalos o "bins". Ejemplo: convertir edades en rangos (18-25, 26-35, etc.).

### Booleano
Tipo de dato con solo dos valores posibles: Verdadero (True) o Falso (False). En Python: `True`, `False`. Útil para filtros y condiciones.

---

## C

### Cardinalidad
Número de valores únicos en una columna. Alta cardinalidad = muchos valores únicos (ej: nombres). Baja cardinalidad = pocos valores (ej: género).

### Causalidad
Relación donde un cambio en una variable produce directamente un cambio en otra. Diferente de correlación, que solo indica asociación. "Correlación no implica causalidad."

### Chartjunk
Término de Edward Tufte para elementos visuales que no aportan información: decoraciones, 3D innecesario, fondos de colores, bordes excesivos.

### Clasificación
Tipo de problema de ML supervisado donde se predice una categoría (clase). Ejemplos: spam/no spam, aprobado/reprobado. Ver también: *Regresión*.

### Clave Foránea (Foreign Key)
Columna en una tabla que referencia la clave primaria de otra tabla. Establece relaciones entre tablas en bases de datos relacionales.

### Clave Primaria (Primary Key)
Columna (o combinación) que identifica únicamente cada fila en una tabla. Debe ser única y no nula.

### Clustering
Técnica de aprendizaje no supervisado que agrupa datos similares sin etiquetas predefinidas. Algoritmos: K-Means, DBSCAN, Hierarchical.

### Coeficiente de Correlación
Medida de la fuerza y dirección de la relación lineal entre dos variables. Rango: -1 (inversa perfecta) a +1 (directa perfecta). 0 = sin correlación lineal.

### Columna Calculada
En Power BI/DAX, columna creada mediante una fórmula que se evalúa fila por fila y se almacena en el modelo.

### Concatenación
Unir datos verticalmente (agregar filas). En Pandas: `pd.concat()`. Diferente de *merge* que une horizontalmente.

### Correlación
Medida estadística de la relación entre dos variables. No implica causalidad. Ver: *Coeficiente de Correlación*.

### Cross-Filtering
Característica de dashboards interactivos donde seleccionar un elemento en un gráfico filtra automáticamente los demás.

### Cross-Validation
Técnica para evaluar modelos dividiendo los datos en múltiples subconjuntos (folds), entrenando y validando en diferentes combinaciones. Reduce sesgo de una sola división train/test.

### CSV (Comma-Separated Values)
Formato de archivo de texto donde los valores se separan por comas (u otro delimitador). Estándar para intercambio de datos tabulares.

### Curva ROC
Gráfico que muestra la relación entre Tasa de Verdaderos Positivos (Recall) y Tasa de Falsos Positivos para diferentes umbrales de clasificación.

---

## D

### Dashboard
Visualización interactiva que presenta KPIs y métricas clave en una sola pantalla. Permite monitoreo y toma de decisiones.

### Data Frame
Estructura de datos tabular (filas y columnas) en Pandas/R. Similar a una tabla de base de datos o hoja de Excel.

### Data Leakage (Filtración de Datos)
Error donde información del conjunto de test se usa inadvertidamente durante el entrenamiento, produciendo métricas artificialmente altas.

### Data Wrangling
Proceso de transformar datos crudos en formato utilizable: limpieza, transformación, integración. También llamado "data munging".

### DAX (Data Analysis Expressions)
Lenguaje de fórmulas de Microsoft para Power BI, Power Pivot y Analysis Services. Permite crear medidas y columnas calculadas.

### Desbalance de Clases
Situación donde una clase tiene muchos más ejemplos que otra. Ejemplo: 99% transacciones normales, 1% fraude. Requiere técnicas especiales.

### Desviación Estándar
Medida de dispersión que indica cuánto se alejan los valores del promedio. Mayor desviación = mayor variabilidad.

### Dimensionalidad
Número de features (columnas) en un dataset. Alta dimensionalidad puede causar "maldición de la dimensionalidad" en ML.

### Distribución
Patrón de frecuencias de los valores de una variable. Tipos comunes: normal, uniforme, sesgada, bimodal.

### Drill-Down
Funcionalidad de BI que permite explorar datos en niveles de detalle creciente. Ejemplo: de país → región → ciudad.

### Dummy Variable
Variable binaria (0/1) creada a partir de una categórica. Ver: *One-Hot Encoding*.

---

## E

### EDA (Exploratory Data Analysis)
Análisis exploratorio para entender los datos antes de modelar: distribuciones, correlaciones, valores faltantes, outliers.

### Encoding
Proceso de convertir variables categóricas a formato numérico para algoritmos de ML. Tipos: One-Hot, Label, Target Encoding.

### Ensemble
Método que combina múltiples modelos para mejorar predicciones. Tipos: Bagging (Random Forest), Boosting (XGBoost, Gradient Boosting).

### ETL (Extract, Transform, Load)
Proceso de integración de datos: Extraer de fuentes, Transformar (limpiar, formatear), Cargar en destino.

### Evaluación
Fase de ML donde se mide el rendimiento del modelo en datos no vistos durante entrenamiento.

---

## F

### F1-Score
Media armónica de Precision y Recall. Útil cuando hay desbalance de clases. Rango: 0 a 1.

### Falso Negativo (FN)
Error donde el modelo predice negativo pero el valor real es positivo. Ejemplo: no detectar un fraude que sí existía.

### Falso Positivo (FP)
Error donde el modelo predice positivo pero el valor real es negativo. Ejemplo: falsa alarma de fraude.

### Feature
Variable o atributo usado como entrada para un modelo de ML. Sinónimos: característica, variable independiente.

### Feature Engineering
Proceso de crear nuevas features a partir de las existentes para mejorar el rendimiento del modelo.

### Feature Importance
Medida de cuánto contribuye cada feature a las predicciones del modelo. Ver también: *SHAP*.

### Filtro
Operación que selecciona un subconjunto de datos según una condición. En SQL: `WHERE`. En Pandas: `df[condicion]`.

### Fold
Subconjunto de datos usado en cross-validation. K-Fold divide los datos en K partes iguales.

---

## G

### Gestalt (Principios de)
Leyes de percepción visual: proximidad, similitud, cierre, continuidad. Fundamentales para diseño de visualizaciones.

### Gradiente
En ML, dirección de máximo cambio de una función. Usado en optimización (Gradient Descent) para ajustar parámetros.

### Gradient Boosting
Técnica de ensemble que construye modelos secuencialmente, cada uno corrigiendo los errores del anterior. Implementaciones: XGBoost, LightGBM, CatBoost.

### GROUP BY
Cláusula SQL que agrupa filas con valores iguales para aplicar funciones de agregación.

---

## H

### HAVING
Cláusula SQL que filtra grupos (después de GROUP BY). Similar a WHERE pero para agregados.

### Hiperparámetro
Parámetro del algoritmo que se define antes del entrenamiento (no se aprende de los datos). Ejemplo: número de árboles en Random Forest.

### Histograma
Gráfico que muestra la distribución de una variable continua mediante barras que representan frecuencias en intervalos.

### Hoja de Cálculo
Aplicación como Excel o Google Sheets para manipular datos tabulares. Punto de partida común antes de Pandas/SQL.

---

## I

### Imputación
Proceso de reemplazar valores faltantes con estimaciones. Métodos: media, mediana, moda, predicción.

### Índice
En Pandas, etiqueta de las filas del DataFrame. En bases de datos, estructura que acelera búsquedas.

### INNER JOIN
Tipo de unión que devuelve solo las filas con coincidencias en ambas tablas.

### Insight
Hallazgo o comprensión significativa derivada del análisis de datos que puede informar decisiones.

---

## J

### JOIN
Operación que combina filas de dos o más tablas basándose en columnas relacionadas. Tipos: INNER, LEFT, RIGHT, FULL OUTER.

### JSON (JavaScript Object Notation)
Formato de texto para estructurar datos. Común en APIs y configuraciones. Más flexible que CSV.

### Jupyter Notebook
Entorno interactivo que combina código, texto y visualizaciones. Estándar para análisis de datos en Python.

---

## K

### K-Fold Cross-Validation
Técnica que divide datos en K partes, entrena en K-1 y valida en 1, rotando K veces.

### K-Means
Algoritmo de clustering que agrupa datos en K clusters minimizando la distancia intra-cluster.

### KPI (Key Performance Indicator)
Métrica clave que mide el rendimiento hacia un objetivo. Debe ser específico, medible y relevante.

---

## L

### Label (Etiqueta)
Valor objetivo en aprendizaje supervisado. Lo que el modelo intenta predecir.

### Label Encoding
Técnica que convierte categorías en números enteros (0, 1, 2...). Cuidado: implica orden que puede no existir.

### LEFT JOIN
Unión que devuelve todas las filas de la tabla izquierda y las coincidencias de la derecha (NULL si no hay).

### Linealidad
Supuesto de que la relación entre variables es lineal (proporcional). Requerido por regresión lineal.

### Logaritmo
Transformación matemática que comprime valores grandes. Útil para variables con distribución muy sesgada.

---

## M

### Machine Learning (ML)
Campo de la IA donde los sistemas aprenden patrones de datos para hacer predicciones sin ser programados explícitamente.

### MAR (Missing At Random)
Tipo de valor faltante donde la probabilidad de faltar depende de otras variables observadas, no del valor faltante mismo.

### MCAR (Missing Completely At Random)
Tipo de valor faltante donde la probabilidad de faltar es completamente aleatoria, independiente de cualquier variable.

### Media (Promedio)
Suma de valores dividida entre la cantidad. Sensible a outliers.

### Mediana
Valor central cuando los datos están ordenados. Resistente a outliers. Preferible para distribuciones sesgadas.

### Medida
En Power BI/DAX, cálculo dinámico que se evalúa según el contexto de filtros. Diferente de columna calculada.

### Merge
Unir datos horizontalmente (agregar columnas) basándose en una clave común. En Pandas: `pd.merge()`. En SQL: `JOIN`.

### Métrica
Medida cuantitativa del rendimiento. En ML: accuracy, precision, recall. En negocio: KPIs.

### MNAR (Missing Not At Random)
Tipo de valor faltante donde la probabilidad de faltar depende del valor faltante mismo. Más problemático de manejar.

### Moda
Valor más frecuente en un conjunto de datos. Útil para variables categóricas.

### Modelo
En ML, representación matemática aprendida de los datos que puede hacer predicciones sobre nuevos datos.

### Multicolinealidad
Situación donde dos o más features están altamente correlacionadas. Puede afectar interpretación de modelos lineales.

---

## N

### NaN (Not a Number)
Valor especial que representa dato faltante en Python/Pandas. Diferente de 0 o cadena vacía.

### Normalización
1. En datos: escalar valores a un rango (ej: 0-1). 2. En bases de datos: dividir tablas para eliminar redundancia.

### Nulo (NULL)
Valor que representa ausencia de dato. En SQL: `NULL`. En Pandas: `NaN` o `None`.

---

## O

### One-Hot Encoding
Técnica que crea columnas binarias (0/1) para cada categoría. Evita orden implícito de Label Encoding.

### Outlier (Valor Atípico)
Valor que se desvía significativamente del resto. Puede ser error o información valiosa. Requiere investigación.

### Overfitting (Sobreajuste)
Cuando el modelo memoriza los datos de entrenamiento pero no generaliza a datos nuevos. Error de test >> Error de train.

---

## P

### Pandas
Librería de Python para manipulación y análisis de datos tabulares. Estructuras principales: DataFrame y Series.

### Parámetro
Valor aprendido por el modelo durante entrenamiento (ej: coeficientes de regresión). Diferente de *hiperparámetro*.

### Percentil
Valor por debajo del cual cae cierto porcentaje de datos. El percentil 50 es la mediana.

### Pipeline
Secuencia de pasos de procesamiento encadenados. En scikit-learn: combina preprocesamiento y modelado.

### Pivot Table
Tabla que reorganiza y resume datos agrupando por filas/columnas y aplicando agregaciones.

### Power BI
Herramienta de Microsoft para visualización y análisis de datos (Business Intelligence).

### Precision
Métrica: de los casos predichos como positivos, qué proporción realmente lo era. TP / (TP + FP).

### Preprocesamiento
Pasos de preparación de datos antes del modelado: limpieza, encoding, scaling, feature engineering.

---

## Q

### Query (Consulta)
Instrucción para recuperar o manipular datos. En SQL: `SELECT`, `UPDATE`, etc. En Pandas: métodos de filtrado.

### Quintil
Cada uno de los 5 grupos de igual tamaño al dividir datos ordenados. Similar a cuartil (4 grupos).

---

## R

### Random Forest
Algoritmo de ensemble que combina múltiples árboles de decisión entrenados con muestras aleatorias.

### Rango
Diferencia entre valor máximo y mínimo. Medida simple de dispersión.

### Recall (Sensibilidad)
Métrica: de los casos realmente positivos, qué proporción fue identificada. TP / (TP + FN). Importante cuando los falsos negativos son costosos.

### Regresión
Tipo de problema de ML supervisado donde se predice un valor continuo. Ejemplos: precio, temperatura, nota.

### Regularización
Técnica para prevenir overfitting penalizando la complejidad del modelo. Tipos: L1 (Lasso), L2 (Ridge).

### Relación
Conexión entre tablas definida por claves. Permite combinar información mediante JOINs.

---

## S

### Scaling (Escalado)
Transformar variables a rangos comparables. Tipos: StandardScaler (media 0, std 1), MinMaxScaler (0-1).

### Scatter Plot (Diagrama de Dispersión)
Gráfico que muestra la relación entre dos variables continuas mediante puntos.

### Segmentador (Slicer)
Elemento visual en dashboards que permite filtrar datos interactivamente.

### Series
Estructura de datos unidimensional en Pandas (una columna de DataFrame).

### Sesgo
1. En estadística: diferencia sistemática entre estimación y valor real. 2. En ML: error por supuestos simplificadores.

### SHAP (SHapley Additive exPlanations)
Método para explicar predicciones de modelos ML basado en teoría de juegos. Muestra contribución de cada feature.

### SQL (Structured Query Language)
Lenguaje estándar para gestionar bases de datos relacionales. Comandos: SELECT, INSERT, UPDATE, DELETE.

### Stratified
Técnica de muestreo/división que mantiene las proporciones de clases. Importante en clasificación desbalanceada.

### Supervisado (Aprendizaje)
Tipo de ML donde el modelo aprende de datos etiquetados (con variable objetivo conocida).

---

## T

### Tableau
Herramienta de visualización de datos y Business Intelligence (competencia de Power BI).

### Target (Objetivo)
Variable que el modelo intenta predecir. También llamada "variable dependiente" o "label".

### Test Set (Conjunto de Prueba)
Porción de datos reservada para evaluar el rendimiento final del modelo. No se usa durante entrenamiento.

### Tidy Data
Principio de organización: cada variable en una columna, cada observación en una fila. Facilita análisis.

### Train Set (Conjunto de Entrenamiento)
Porción de datos usada para entrenar el modelo.

### Transformación
Operación que modifica los datos: logaritmo, normalización, encoding, agregación.

### Tufte, Edward
Estadístico y experto en visualización. Autor de "The Visual Display of Quantitative Information". Principios: maximizar ratio tinta-datos, evitar chartjunk.

---

## U

### Underfitting (Subajuste)
Cuando el modelo es demasiado simple para capturar los patrones. Error alto tanto en train como en test.

### Unión (UNION)
En SQL, combinar resultados de dos consultas verticalmente (agregar filas).

---

## V

### Validación
Proceso de evaluar el rendimiento del modelo durante el entrenamiento, típicamente en un conjunto separado del entrenamiento.

### Variable
Característica medible que puede tomar diferentes valores. Tipos: cuantitativa (numérica), cualitativa (categórica).

### Variable Confusora
Variable que afecta tanto a la variable independiente como a la dependiente, creando una correlación espuria.

### Varianza
Medida de dispersión: promedio de las desviaciones al cuadrado respecto a la media.

### Verdadero Negativo (VN)
Predicción correcta de clase negativa. El modelo predijo negativo y era negativo.

### Verdadero Positivo (VP)
Predicción correcta de clase positiva. El modelo predijo positivo y era positivo.

---

## W

### WHERE
Cláusula SQL para filtrar filas según condiciones.

### Wide Format
Formato de datos donde categorías son columnas. Opuesto a *long format*. Útil para visualización.

---

## X

### XGBoost
Implementación optimizada de Gradient Boosting. Popular en competencias de ML por su rendimiento.

---

## Z

### Z-Score
Número de desviaciones estándar que un valor está por encima o debajo de la media. Usado en normalización.

---

## Abreviaturas Comunes

| Abreviatura | Significado |
|-------------|-------------|
| API | Application Programming Interface |
| BI | Business Intelligence |
| CSV | Comma-Separated Values |
| DAX | Data Analysis Expressions |
| EDA | Exploratory Data Analysis |
| ETL | Extract, Transform, Load |
| FN | False Negative (Falso Negativo) |
| FP | False Positive (Falso Positivo) |
| JSON | JavaScript Object Notation |
| KPI | Key Performance Indicator |
| ML | Machine Learning |
| SQL | Structured Query Language |
| TN | True Negative (Verdadero Negativo) |
| TP | True Positive (Verdadero Positivo) |

---

*Última actualización: Enero 2025*
