# Guía de Estudio: Módulo 2 - Data Wrangling Accesible

## El arte de preparar datos para el análisis

---

> *"Los datos son como el petróleo crudo. Valiosos, pero sin refinar no sirven para nada."*
> — Clive Humby, matemático británico

---

## Tabla de Contenidos

1. [Propósito y Relevancia del Módulo](#1-propósito-y-relevancia-del-módulo)
2. [Marco Conceptual: ¿Qué es Data Wrangling?](#2-marco-conceptual-qué-es-data-wrangling)
3. [Conceptos Fundamentales](#3-conceptos-fundamentales)
4. [Metaaprendizaje: El Docente como Aprendiz de Código](#4-metaaprendizaje-el-docente-como-aprendiz-de-código)
5. [Conexiones con la Práctica Docente](#5-conexiones-con-la-práctica-docente)
6. [Preguntas de Reflexión Metacognitiva](#6-preguntas-de-reflexión-metacognitiva)
7. [Lecturas Fundamentales](#7-lecturas-fundamentales)
8. [Lecturas Complementarias](#8-lecturas-complementarias)
9. [Recursos Multimedia](#9-recursos-multimedia)
10. [Actividades de Metaaprendizaje](#10-actividades-de-metaaprendizaje)
11. [Glosario Técnico-Crítico](#11-glosario-técnico-crítico)
12. [Referencias Bibliográficas](#12-referencias-bibliográficas)

---

## 1. Propósito y Relevancia del Módulo

### 1.1 La realidad oculta del análisis de datos

Existe un secreto que rara vez se menciona en cursos introductorios de ciencia de datos: **entre el 60% y el 80% del tiempo de un proyecto de datos se dedica a la limpieza y preparación**, no al análisis "glamoroso" ni a la construcción de modelos.

Este módulo aborda esa realidad de frente. Aprenderá a:

- Importar datos de diversas fuentes (CSV, Excel, bases de datos)
- Explorar y diagnosticar la calidad de sus datos
- Limpiar inconsistencias, valores faltantes y errores
- Transformar datos para prepararlos para el análisis
- Combinar múltiples fuentes de información
- Documentar su proceso de manera reproducible

### 1.2 ¿Por qué Python y no solo Excel?

Es probable que se pregunte: *"Ya sé usar Excel. ¿Por qué necesito aprender Python?"*

Esta es una pregunta legítima que merece una respuesta honesta:

| Aspecto | Excel | Python |
|---------|-------|--------|
| **Curva de aprendizaje** | Baja | Media-Alta |
| **Límite de filas** | ~1 millón | Ilimitado (memoria) |
| **Reproducibilidad** | Difícil | Excelente |
| **Automatización** | Limitada | Total |
| **Transparencia** | Opaca (fórmulas ocultas) | Transparente (código visible) |
| **Colaboración** | Versiones conflictivas | Control de versiones (Git) |
| **Integración con otros sistemas** | Limitada | Amplia |

**La verdad matizada**: Excel sigue siendo excelente para exploración rápida, reportes pequeños y comunicación con stakeholders no técnicos. Python no lo reemplaza; lo complementa. El objetivo es que **usted decida** cuándo usar cada herramienta, en lugar de estar limitado por lo que sabe.

### 1.3 Relevancia para docentes universitarios

Como docentes, tienen un rol único en relación con estas herramientas:

1. **Formar profesionales competentes**: Los egresados de economía, administración y contaduría cada vez más necesitan habilidades de manipulación de datos.

2. **Investigación académica**: Muchas revistas ahora exigen código reproducible. Python facilita esta transparencia.

3. **Gestión universitaria**: Desde análisis de rendimiento estudiantil hasta planificación presupuestaria, los datos institucionales requieren procesamiento.

4. **Modelar el aprendizaje continuo**: Al aprender una herramienta nueva frente a sus estudiantes, demuestra que el aprendizaje no termina con un título.

### 1.4 Competencias que desarrollará

| Competencia | Descripción | Nivel esperado |
|-------------|-------------|----------------|
| **Programación básica** | Variables, tipos de datos, estructuras de control en Python | Introductorio |
| **Manipulación con Pandas** | Operaciones fundamentales con DataFrames | Intermedio |
| **Exploración de datos (EDA)** | Técnicas sistemáticas de diagnóstico | Intermedio |
| **SQL básico** | Consultas fundamentales | Introductorio |
| **Pensamiento computacional** | Descomponer problemas en pasos ejecutables | Intermedio |
| **Documentación** | Crear notebooks reproducibles y explicados | Intermedio |

---

## 2. Marco Conceptual: ¿Qué es Data Wrangling?

### 2.1 Definición y alcance

**Data Wrangling** (también llamado data munging, data cleaning, o data preparation) es el proceso de transformar datos "crudos" en datos "limpios" y estructurados, listos para el análisis.

El término "wrangling" proviene del inglés rural estadounidense, donde un *wrangler* es quien arrea y controla caballos salvajes. La metáfora es apta: los datos "en bruto" son frecuentemente caóticos, inconsistentes y difíciles de manejar.

### 2.2 El pipeline de Data Wrangling

```
┌─────────────────────────────────────────────────────────────────┐
│                     PIPELINE DE DATA WRANGLING                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │   ADQUISICIÓN   │
                    │  (Importación)  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   EXPLORACIÓN   │
                    │      (EDA)      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    LIMPIEZA     │
                    │ (Valores faltantes, │
                    │  duplicados, errores) │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ TRANSFORMACIÓN  │
                    │ (Tipos, derivadas, │
                    │   agregaciones)  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   INTEGRACIÓN   │
                    │ (Merge, concat)  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   VALIDACIÓN    │
                    │  (Verificación   │
                    │     final)       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  DATOS LIMPIOS  │
                    │ (Listos para    │
                    │   análisis)     │
                    └─────────────────┘
```

### 2.3 Principios filosóficos del Data Wrangling

#### Principio 1: Tidy Data (Datos ordenados)

Hadley Wickham, científico jefe de RStudio, formalizó el concepto de **tidy data** (datos ordenados):

1. Cada variable forma una columna
2. Cada observación forma una fila
3. Cada tipo de unidad observacional forma una tabla

Este estándar simple tiene implicaciones profundas: cuando los datos están "ordenados", las herramientas de análisis funcionan de manera consistente y predecible.

**Referencia clave**: Wickham, H. (2014). Tidy Data. *Journal of Statistical Software*, 59(10).

#### Principio 2: Reproducibilidad

Cualquier persona (incluyendo usted en el futuro) debería poder:
- Obtener los mismos resultados a partir de los mismos datos originales
- Entender exactamente qué transformaciones se aplicaron
- Modificar el proceso si es necesario

Excel dificulta esto (¿qué fórmula se aplicó en la celda J347?). Los notebooks de Jupyter lo facilitan: el código es la documentación.

#### Principio 3: Conservación de datos originales

**Nunca modifique los datos originales.** Siempre trabaje con copias y documente todas las transformaciones. Los datos crudos son sagrados; las transformaciones son hipótesis que pueden ser incorrectas.

#### Principio 4: Escepticismo saludable

Los datos "vienen con sorpresas". Siempre verifique:
- ¿Los tipos de datos son los esperados?
- ¿Hay valores faltantes donde no debería haberlos?
- ¿Los rangos son razonables?
- ¿Los totales cuadran?

### 2.4 El contexto humano del Data Wrangling

Detrás de cada dataset hay personas y procesos:

- **¿Quién recolectó estos datos?** Sus incentivos y limitaciones importan.
- **¿Con qué propósito?** Los datos recolectados para un fin pueden no servir para otro.
- **¿Qué no se capturó?** La ausencia de datos es información en sí misma.
- **¿Qué errores son probables?** Conocer el proceso de generación ayuda a anticipar problemas.

---

## 3. Conceptos Fundamentales

### 3.1 Python: Fundamentos para Data Wrangling

#### Por qué Python

Python se ha convertido en el lenguaje dominante en ciencia de datos por varias razones:

- **Sintaxis legible**: Diseñado para ser fácil de leer y escribir
- **Ecosistema rico**: Miles de bibliotecas especializadas
- **Comunidad activa**: Abundante documentación y ayuda
- **Versatilidad**: Sirve para análisis, web, automatización, y más
- **Gratuito y abierto**: Sin costos de licencia

#### Conceptos clave de Python

**Variables y tipos de datos**:
```python
# Numéricos
edad = 35              # int (entero)
promedio = 17.5        # float (decimal)

# Texto
nombre = "María"       # str (string)

# Booleanos
activo = True          # bool

# Colecciones
lista = [1, 2, 3]      # list (mutable, ordenada)
conjunto = {1, 2, 3}   # set (mutable, sin duplicados)
diccionario = {"a": 1} # dict (pares clave-valor)
```

**Estructuras de control**:
```python
# Condicionales
if promedio >= 18:
    print("Aprobado con distinción")
elif promedio >= 10:
    print("Aprobado")
else:
    print("Reprobado")

# Bucles
for estudiante in lista_estudiantes:
    print(estudiante)
```

**Funciones**:
```python
def calcular_promedio(notas):
    """Calcula el promedio de una lista de notas."""
    return sum(notas) / len(notas)
```

#### Reflexión metacognitiva sobre aprender a programar

Aprender a programar de adulto puede generar frustración. Algunas reflexiones:

1. **Los errores son normales**: Incluso programadores expertos pasan tiempo depurando código.

2. **La sintaxis es lo de menos**: Lo importante es el pensamiento computacional; la sintaxis se aprende con práctica.

3. **No memorice, comprenda**: Es más importante entender *qué* hace el código que memorizar comandos.

4. **Use los errores como maestros**: Los mensajes de error, aunque crípticos al inicio, contienen información valiosa.

### 3.2 Pandas: La herramienta central

#### ¿Qué es Pandas?

Pandas es una biblioteca de Python para manipulación y análisis de datos. Su nombre proviene de "Panel Data" (datos de panel, término econométrico).

Fue creada por Wes McKinney mientras trabajaba en AQR Capital Management, precisamente porque las herramientas existentes eran inadecuadas para el análisis financiero.

#### El DataFrame: Concepto central

Un **DataFrame** es una estructura de datos bidimensional (filas y columnas), similar a:
- Una hoja de cálculo de Excel
- Una tabla de base de datos
- Un dataset de SPSS/Stata

```python
import pandas as pd

# Crear un DataFrame simple
datos = {
    'estudiante_id': [1, 2, 3, 4],
    'carrera': ['Economía', 'Administración', 'Contaduría', 'RRII'],
    'promedio': [17.5, 15.2, 18.1, 16.8]
}
df = pd.DataFrame(datos)
```

#### Operaciones fundamentales

| Operación | Código | Descripción |
|-----------|--------|-------------|
| Ver primeras filas | `df.head()` | Inspección rápida |
| Ver últimas filas | `df.tail()` | Inspección rápida |
| Dimensiones | `df.shape` | (filas, columnas) |
| Tipos de datos | `df.dtypes` | Tipo de cada columna |
| Estadísticas | `df.describe()` | Resumen estadístico |
| Valores faltantes | `df.isnull().sum()` | Conteo de nulos |
| Seleccionar columna | `df['columna']` | Acceso por nombre |
| Filtrar filas | `df[df['col'] > valor]` | Selección condicional |

#### La importancia de `describe()`

El método `describe()` produce estadísticas resumidas que revelan inmediatamente problemas potenciales:

```
       promedio
count       100    ← ¿Es el n esperado?
mean      15.23    ← ¿Es razonable?
std        3.45    ← ¿Variabilidad esperada?
min        0.00    ← ¿Es posible un 0?
25%       12.50    ← Primer cuartil
50%       15.00    ← Mediana
75%       17.80    ← Tercer cuartil
max       25.00    ← ¿Es posible un 25?
```

### 3.3 Análisis Exploratorio de Datos (EDA)

#### Filosofía del EDA

John Tukey, creador del EDA, enfatizaba:

> "El análisis exploratorio de datos es trabajo de detective... buscando pistas que a menudo nos llevan a nuevas preguntas."

El EDA no es un paso para "pasar rápido" hacia el análisis "real". Es donde ocurren los descubrimientos más importantes.

#### Protocolo sistemático de EDA

**Paso 1: Estructura general**
- ¿Cuántas filas y columnas?
- ¿Qué representa cada fila? (unidad de observación)
- ¿Qué representa cada columna? (variables)

**Paso 2: Tipos de datos**
- ¿Los tipos son correctos? (fechas como fechas, números como números)
- ¿Hay columnas que deberían ser categóricas?

**Paso 3: Valores faltantes**
- ¿Cuántos hay en cada columna?
- ¿Hay patrones? (¿faltan aleatoriamente o sistemáticamente?)
- ¿Qué significan? (¿no aplica, no disponible, error?)

**Paso 4: Distribuciones univariadas**
- Para numéricas: histogramas, boxplots, estadísticas
- Para categóricas: frecuencias, proporciones

**Paso 5: Relaciones bivariadas**
- Correlaciones entre numéricas
- Tablas de contingencia entre categóricas
- Gráficos de dispersión

**Paso 6: Valores atípicos (outliers)**
- ¿Existen valores extremos?
- ¿Son errores o datos legítimos?
- ¿Cómo afectan el análisis?

### 3.4 Limpieza de datos

#### Valores faltantes: Estrategias

| Estrategia | Cuándo usarla | Riesgos |
|------------|---------------|---------|
| **Eliminar filas** | Pocos casos, aleatorios | Pérdida de información, sesgo si no son aleatorios |
| **Eliminar columna** | Muchos faltantes, variable no crítica | Pérdida de información |
| **Imputar con media/mediana** | Variable numérica, distribución simétrica | Reduce varianza, sesga relaciones |
| **Imputar con moda** | Variable categórica | Puede introducir sesgo |
| **Imputación múltiple** | Análisis riguroso | Complejidad técnica |
| **Dejar como categoría** | "Faltante" es información | Solo para categóricas |

**Reflexión crítica**: No existe una "solución correcta" universal para valores faltantes. Cada decisión tiene implicaciones que deben documentarse y justificarse.

#### Duplicados

```python
# Identificar duplicados
df.duplicated().sum()

# Ver cuáles son
df[df.duplicated(keep=False)]

# Eliminar (mantener primero)
df.drop_duplicates(keep='first', inplace=True)
```

**Pregunta clave**: ¿Un "duplicado" es realmente un error o representa múltiples observaciones legítimas?

#### Inconsistencias en texto

Problemas comunes:
- Mayúsculas/minúsculas ("Economía" vs "economía" vs "ECONOMÍA")
- Espacios extra ("  Administración ")
- Caracteres especiales ("Contaduría" vs "Contaduria")

```python
# Limpiar texto
df['carrera'] = df['carrera'].str.strip()        # Eliminar espacios
df['carrera'] = df['carrera'].str.lower()        # Minúsculas
df['carrera'] = df['carrera'].str.title()        # Capitalizar
```

### 3.5 Combinación de datos (Merge y Join)

#### Tipos de combinación

```
INNER JOIN: Solo filas que existen en ambas tablas
LEFT JOIN:  Todas las filas de la izquierda + coincidencias de la derecha
RIGHT JOIN: Todas las filas de la derecha + coincidencias de la izquierda
OUTER JOIN: Todas las filas de ambas tablas
```

Visualmente:

```
Tabla A          Tabla B              INNER        LEFT         OUTER
┌───┬───┐       ┌───┬───┐         ┌───┬───┬───┐  ┌───┬───┬───┐  ┌───┬───┬───┐
│ K │ V1│       │ K │ V2│         │ K │V1 │V2 │  │ K │V1 │V2 │  │ K │V1 │V2 │
├───┼───┤       ├───┼───┤         ├───┼───┼───┤  ├───┼───┼───┤  ├───┼───┼───┤
│ 1 │ a │       │ 1 │ x │   →     │ 1 │ a │ x │  │ 1 │ a │ x │  │ 1 │ a │ x │
│ 2 │ b │       │ 3 │ y │         │ 3 │ c │ y │  │ 2 │ b │NaN│  │ 2 │ b │NaN│
│ 3 │ c │       │ 4 │ z │                        │ 3 │ c │ y │  │ 3 │ c │ y │
└───┴───┘       └───┴───┘                        └───┴───┴───┘  │ 4 │NaN│ z │
                                                                └───┴───┴───┘
```

#### En Pandas

```python
# Merge con clave común
resultado = pd.merge(df1, df2, on='estudiante_id', how='inner')

# Merge con diferentes nombres de columna
resultado = pd.merge(df1, df2,
                     left_on='id_estudiante',
                     right_on='estudiante_id',
                     how='left')

# Diagnóstico con indicator
resultado = pd.merge(df1, df2, on='id', how='outer', indicator=True)
# La columna _merge indica: 'left_only', 'right_only', o 'both'
```

### 3.6 SQL: El lenguaje universal de datos

#### Por qué aprender SQL

SQL (Structured Query Language) es el lenguaje estándar para interactuar con bases de datos relacionales. Aunque usemos Pandas, SQL sigue siendo relevante porque:

1. **Ubicuidad**: Casi toda organización tiene datos en bases SQL
2. **Eficiencia**: Para datos muy grandes, SQL puede ser más eficiente que Pandas
3. **Estandarización**: La sintaxis es similar entre sistemas (MySQL, PostgreSQL, SQLite, etc.)
4. **Demanda laboral**: Es una habilidad casi universalmente requerida

#### Operaciones fundamentales

```sql
-- Selección básica
SELECT columna1, columna2
FROM tabla
WHERE condicion;

-- Agregación
SELECT carrera, COUNT(*) as cantidad, AVG(promedio) as prom_medio
FROM estudiantes
GROUP BY carrera
HAVING AVG(promedio) > 15;

-- Join (combinación)
SELECT e.nombre, c.nombre_carrera
FROM estudiantes e
INNER JOIN carreras c ON e.carrera_id = c.id;

-- Ordenamiento
SELECT *
FROM estudiantes
ORDER BY promedio DESC
LIMIT 10;
```

#### SQL en Python con SQLite

```python
import sqlite3
import pandas as pd

# Conectar a base de datos
conn = sqlite3.connect('universidad.db')

# Ejecutar consulta y obtener DataFrame
query = """
SELECT carrera, AVG(promedio) as promedio_medio
FROM estudiantes
GROUP BY carrera
"""
df = pd.read_sql_query(query, conn)

# Cerrar conexión
conn.close()
```

---

## 4. Metaaprendizaje: El Docente como Aprendiz de Código

### 4.1 Enfrentando la frustración del principiante

Aprender a programar de adulto puede ser particularmente desafiante porque:

1. **Estamos acostumbrados a ser competentes**: Como docentes expertos en nuestras disciplinas, volver a ser "principiantes" puede ser incómodo.

2. **El feedback es inmediato y despiadado**: El código funciona o no funciona. No hay puntos parciales.

3. **Los errores son públicos**: Un mensaje de error rojo puede sentirse como un juicio.

4. **La curva inicial es empinada**: Hay mucho que aprender antes de hacer algo "útil".

**Estrategias para navegar esta frustración**:

- **Celebre victorias pequeñas**: Su primer gráfico, su primera limpieza exitosa, son logros reales.
- **Normalice los errores**: Incluso expertos pasan horas depurando. Es parte del proceso.
- **Tome descansos**: La fatiga mental reduce la capacidad de resolver problemas.
- **Busque ayuda**: Google, Stack Overflow, ChatGPT, y compañeros son recursos legítimos.

### 4.2 Mentalidad de crecimiento en programación

Carol Dweck distingue entre:

- **Mentalidad fija**: "No soy bueno para programar" (habilidad como rasgo estable)
- **Mentalidad de crecimiento**: "Aún no soy bueno para programar" (habilidad desarrollable)

En programación, la mentalidad de crecimiento es especialmente importante porque:

- La curva de aprendizaje es larga (años, no semanas)
- Siempre habrá nuevas herramientas que aprender
- Los "errores" son la forma principal de aprender

**Reframe sugeridos**:

| En lugar de... | Intente... |
|----------------|------------|
| "No entiendo este error" | "Este error me está enseñando algo" |
| "Esto es muy difícil" | "Esto requiere más práctica" |
| "Nunca lo lograré" | "Aún no lo he logrado" |
| "Fulano es naturalmente bueno" | "Fulano ha practicado mucho" |

### 4.3 Estrategias de aprendizaje efectivas para código

**1. Escriba código, no lo lea solamente**

La programación es como aprender un instrumento musical: ver videos no es suficiente. Necesita practicar activamente.

**2. Modifique antes de crear**

Antes de escribir código desde cero:
- Tome código existente (del curso, de ejemplos)
- Modifíquelo (cambie valores, agregue líneas)
- Observe qué sucede

**3. Descomponga problemas**

Ante un problema complejo:
1. Divídalo en subproblemas
2. Resuelva cada subproblema por separado
3. Combine las soluciones

**4. Use el método "rubber duck"**

Explique su código (o su problema) a un objeto inanimado (un pato de goma, tradicionalmente). El acto de verbalizar frecuentemente revela el error.

**5. Documente mientras programa**

Los comentarios no son solo para otros; son para usted en el futuro. Escriba comentarios que expliquen *por qué*, no solo *qué*.

### 4.4 Transferencia a la enseñanza

Este módulo le ofrece una oportunidad única: **observar el aprendizaje desde adentro**. Mientras aprende a programar, preste atención a:

- ¿Qué explicaciones le ayudan más?
- ¿Qué ejemplos resuenan con usted?
- ¿Cuándo se siente más frustrado?
- ¿Qué tipo de feedback necesita?

Estas observaciones son valiosas para mejorar su propia docencia, independientemente de si enseña programación o no.

---

## 5. Conexiones con la Práctica Docente

### 5.1 Para docentes de Economía

#### Aplicaciones del Data Wrangling

| Tarea | Herramientas del módulo |
|-------|-------------------------|
| Analizar series de inflación del BCV | Importar CSV, manejar fechas, valores faltantes |
| Comparar indicadores entre países LATAM | Merge de múltiples datasets |
| Construir índices compuestos | Transformaciones y variables derivadas |
| Limpiar encuestas económicas | EDA, valores atípicos, inconsistencias |

#### Caso de estudio: Datos del BCV

Los datos económicos venezolanos presentan desafíos únicos:

- **Series discontinuas**: Cambios metodológicos, períodos sin publicación
- **Reconversiones monetarias**: Necesidad de ajustar series históricas
- **Múltiples fuentes**: BCV, INE, OPEC con metodologías diferentes

Estos desafíos hacen del data wrangling no un lujo, sino una necesidad.

#### Reflexión pedagógica

*¿Qué tan explícitamente enseña a sus estudiantes a lidiar con datos imperfectos? ¿O asumen que los datos de los libros de texto reflejan la realidad?*

### 5.2 Para docentes de Administración

#### Aplicaciones del Data Wrangling

| Tarea | Herramientas del módulo |
|-------|-------------------------|
| Analizar encuestas de clima organizacional | EDA de escalas Likert, valores faltantes |
| Integrar datos de ventas y CRM | Merge de múltiples fuentes |
| Preparar datos para dashboard gerencial | Transformaciones, agregaciones |
| Auditar calidad de datos operativos | Detección de duplicados, inconsistencias |

#### Caso de estudio: Integración de sistemas

Las organizaciones modernas tienen datos dispersos en múltiples sistemas:
- ERP (operaciones)
- CRM (clientes)
- HRIS (recursos humanos)
- Contabilidad

La capacidad de **integrar** estas fuentes (data wrangling aplicado) es crucial para la gestión basada en evidencia.

#### Reflexión pedagógica

*¿Sus estudiantes aprenden a trabajar con datos reales (imperfectos) o solo con casos de libro (limpios)? ¿Cómo podría incorporar el "desorden" real en sus ejercicios?*

### 5.3 Para docentes de Contaduría

#### Aplicaciones del Data Wrangling

| Tarea | Herramientas del módulo |
|-------|-------------------------|
| Reconciliar estados financieros | Merge y validación cruzada |
| Detectar anomalías en transacciones | EDA, outliers, patrones inusuales |
| Preparar datos para auditoría | Limpieza, documentación |
| Automatizar reportes periódicos | Scripts reproducibles |

#### Caso de estudio: Auditoría de datos

La contabilidad forense y la detección de fraude dependen cada vez más de análisis de datos. Técnicas como:
- **Ley de Benford**: Distribución esperada de primeros dígitos
- **Detección de outliers**: Transacciones inusualmente grandes
- **Análisis de duplicados**: Pagos duplicados, facturas clonadas

Todas requieren habilidades de data wrangling.

#### Reflexión pedagógica

*¿Sus estudiantes aprenden a cuestionar la integridad de los datos que reciben, o asumen que los sistemas contables son perfectos?*

### 5.4 Para docentes de Relaciones Industriales

#### Aplicaciones del Data Wrangling

| Tarea | Herramientas del módulo |
|-------|-------------------------|
| Analizar encuestas de satisfacción | EDA de escalas, análisis de texto |
| Auditar equidad salarial | Transformaciones, agregaciones por grupo |
| Limpiar datos de nómina | Valores faltantes, inconsistencias |
| Integrar evaluaciones de desempeño | Merge de fuentes múltiples |

#### Caso de estudio: Análisis de equidad

Un análisis de brecha salarial de género requiere:
1. Obtener datos de nómina (data acquisition)
2. Verificar calidad y completitud (EDA)
3. Definir "trabajo comparable" (transformación)
4. Calcular diferencias ajustadas (análisis)

Cada paso involucra decisiones metodológicas que deben documentarse.

#### Reflexión pedagógica

*¿Cómo enseña a sus estudiantes a ser críticos con los datos de encuestas que "parecen" objetivos pero pueden tener sesgos de diseño o respuesta?*

---

## 6. Preguntas de Reflexión Metacognitiva

### 6.1 Antes de comenzar el módulo

1. ¿Cuál es mi experiencia previa con programación? ¿Positiva, negativa, inexistente?

2. ¿Qué emoción predomina cuando pienso en "aprender a programar"? ¿De dónde viene esa emoción?

3. ¿Cuánto tiempo realista puedo dedicar a practicar entre sesiones?

4. ¿Qué datos de mi práctica profesional me gustaría poder analizar mejor?

### 6.2 Durante el módulo

5. ¿Qué concepto me ha costado más? ¿Qué estrategia he usado para abordarlo?

6. ¿En qué momento he sentido más frustración? ¿Cómo la manejé?

7. ¿He encontrado paralelismos entre aprender a programar y aprender mi disciplina?

8. ¿Qué error recurrente estoy cometiendo? ¿Qué puedo aprender de él?

### 6.3 Al finalizar el módulo

9. ¿Qué puedo hacer ahora que no podía hacer antes del módulo?

10. ¿Qué aspecto del data wrangling encuentro más relevante para mi trabajo?

11. ¿Cómo ha cambiado mi actitud hacia la programación?

12. ¿Qué quiero seguir aprendiendo después de este módulo?

### 6.4 Diario de errores

Considere mantener un "diario de errores" durante el módulo:

```
Fecha: _________
Error/Problema: _________

¿Qué intentaba hacer?

¿Cuál fue el mensaje de error o síntoma?

¿Cómo lo resolví?

¿Qué aprendí?
```

Este registro es valioso porque:
- Los patrones de errores revelan áreas que necesitan más práctica
- La resolución documentada sirve de referencia futura
- El progreso es visible (errores que antes eran difíciles se vuelven triviales)

---

## 7. Lecturas Fundamentales

### 7.1 Lectura obligatoria principal

**McKinney, W. (2022). *Python for Data Analysis* (3ra edición). O'Reilly Media.**

- **ISBN**: 978-1098104030
- **Páginas**: 579
- **Disponibilidad**: [Amazon](https://www.amazon.com/Python-Data-Analysis-Wes-McKinney/dp/109810403X) | [Acceso parcial gratuito](https://wesmckinney.com/book/)
- **Por qué es fundamental**: Wes McKinney es el creador de Pandas. Este libro es la referencia definitiva, actualizada a la versión más reciente. Los capítulos 5-8 cubren directamente el contenido del módulo.
- **Capítulos prioritarios**: 4 (NumPy Basics), 5 (Getting Started with pandas), 7 (Data Cleaning and Preparation), 8 (Data Wrangling: Join, Combine, and Reshape)

### 7.2 Lectura obligatoria complementaria

**Wickham, H. (2014). Tidy Data. *Journal of Statistical Software*, 59(10), 1-23.**

- **DOI**: [10.18637/jss.v059.i10](https://doi.org/10.18637/jss.v059.i10)
- **Acceso gratuito**: [PDF directo](https://www.jstatsoft.org/article/view/v059i10)
- **Por qué es fundamental**: Este artículo seminal define los principios de "datos ordenados" que subyacen a todo el data wrangling moderno. Aunque usa R, los conceptos son universales.

### 7.3 Lectura recomendada

**Sweigart, A. (2019). *Automate the Boring Stuff with Python* (2da edición). No Starch Press.**

- **ISBN**: 978-1593279929
- **Acceso gratuito**: [automatetheboringstuff.com](https://automatetheboringstuff.com/)
- **Por qué es importante**: Introducción amigable a Python con enfoque práctico. Excelente para quienes nunca han programado. Los primeros capítulos son particularmente útiles.

---

## 8. Lecturas Complementarias

### 8.1 Para profundizar en Python

**VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly Media.**

- **ISBN**: 978-1491912058
- **Acceso gratuito**: [jakevdp.github.io/PythonDataScienceHandbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- **Relevancia**: Cobertura exhaustiva de NumPy, Pandas, Matplotlib y Scikit-learn. Más técnico que McKinney pero excelente como referencia.

**Matthes, E. (2019). *Python Crash Course* (2da edición). No Starch Press.**

- **ISBN**: 978-1593279288
- **Relevancia**: Si necesita más fundamentos de Python antes de Pandas, este libro es ideal.

### 8.2 Para profundizar en SQL

**Beaulieu, A. (2020). *Learning SQL* (3ra edición). O'Reilly Media.**

- **ISBN**: 978-1492057611
- **Relevancia**: Introducción completa a SQL con énfasis en MySQL. Los primeros 6 capítulos cubren lo esencial.

**Molinaro, A., & de Graaf, R. (2020). *SQL Cookbook* (2da edición). O'Reilly Media.**

- **ISBN**: 978-1492077442
- **Relevancia**: Recetas prácticas para problemas comunes de SQL. Útil como referencia cuando enfrente problemas específicos.

### 8.3 Para calidad de datos

**Redman, T. C. (2001). *Data Quality: The Field Guide*. Digital Press.**

- **ISBN**: 978-1555582517
- **Relevancia**: Aunque antiguo, sigue siendo referencia en gestión de calidad de datos. Perspectiva organizacional más que técnica.

**Dasu, T., & Johnson, T. (2003). *Exploratory Data Mining and Data Cleaning*. Wiley.**

- **ISBN**: 978-0471268512
- **Relevancia**: Tratamiento riguroso de técnicas de limpieza de datos. Más técnico, pero los capítulos conceptuales son accesibles.

### 8.4 Artículos académicos clave

**Kandel, S., Heer, J., Plaisant, C., Kennedy, J., van Ham, F., Riche, N. H., ... & Buono, P. (2011). Research directions in data wrangling: Visualizations and transformations for usable and credible data. *Information Visualization*, 10(4), 271-288.**

- **DOI**: [10.1177/1473871611415994](https://doi.org/10.1177/1473871611415994)
- **Relevancia**: Panorama académico del campo del data wrangling. Útil para entender el contexto de investigación.

**Krishnan, S., Wang, J., Wu, E., Franklin, M. J., & Goldberg, K. (2016). ActiveClean: Interactive data cleaning for statistical modeling. *Proceedings of the VLDB Endowment*, 9(12), 948-959.**

- **DOI**: [10.14778/2994509.2994514](https://doi.org/10.14778/2994509.2994514)
- **Relevancia**: Investigación sobre limpieza de datos interactiva. Muestra el estado del arte en automatización.

---

## 9. Recursos Multimedia

### 9.1 Videos esenciales

#### Serie: Corey Schafer - Pandas Tutorials

- **Duración**: ~11 videos, 15-30 min cada uno
- **URL**: [YouTube Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS)
- **Por qué verla**: Tutoriales claros y bien estructurados. Schafer es uno de los mejores educadores de Python en YouTube.

#### Video: Keith Galli - Complete Python Pandas Data Science Tutorial

- **Duración**: ~1 hora
- **URL**: [YouTube](https://www.youtube.com/watch?v=vmEHCJofslg)
- **Por qué verlo**: Tutorial completo en una sola sesión. Ideal para una introducción intensiva o repaso.

#### Serie: Sentdex - Python Programming Tutorials

- **URL**: [pythonprogramming.net](https://pythonprogramming.net/)
- **Por qué verla**: Tutoriales gratuitos que van desde principiante hasta avanzado. Enfoque práctico.

#### Curso: freeCodeCamp - Data Analysis with Python

- **Duración**: ~4 horas
- **URL**: [YouTube](https://www.youtube.com/watch?v=r-uOLxNrNk8)
- **Por qué verlo**: Curso completo gratuito. Cubre desde fundamentos hasta proyectos.

### 9.2 Cursos interactivos gratuitos

**Kaggle Learn - Python**

- **Duración**: ~5 horas
- **URL**: [kaggle.com/learn/python](https://www.kaggle.com/learn/python)
- **Descripción**: Introducción interactiva a Python con ejercicios en el navegador. Ideal para principiantes.

**Kaggle Learn - Pandas**

- **Duración**: ~4 horas
- **URL**: [kaggle.com/learn/pandas](https://www.kaggle.com/learn/pandas)
- **Descripción**: Curso interactivo de Pandas con datasets reales. Complemento perfecto para este módulo.

**DataCamp - Introduction to SQL**

- **Duración**: ~4 horas
- **URL**: [datacamp.com/courses/introduction-to-sql](https://www.datacamp.com/courses/introduction-to-sql)
- **Descripción**: Primer curso es gratuito. Interactivo con práctica en el navegador.

**Mode Analytics SQL Tutorial**

- **URL**: [mode.com/sql-tutorial](https://mode.com/sql-tutorial/)
- **Descripción**: Tutorial interactivo de SQL con datos reales. Gratuito y muy bien estructurado.

### 9.3 Documentación oficial

**Pandas Documentation**

- **URL**: [pandas.pydata.org/docs](https://pandas.pydata.org/docs/)
- **Descripción**: Documentación oficial de Pandas. La sección "User Guide" es particularmente útil.

**Python Documentation**

- **URL**: [docs.python.org](https://docs.python.org/3/)
- **Descripción**: Documentación oficial de Python. El "Tutorial" es excelente para principiantes.

**W3Schools SQL Tutorial**

- **URL**: [w3schools.com/sql](https://www.w3schools.com/sql/)
- **Descripción**: Referencia rápida de SQL con ejemplos ejecutables. Ideal para consulta rápida.

### 9.4 Recursos de práctica

**HackerRank - SQL**

- **URL**: [hackerrank.com/domains/sql](https://www.hackerrank.com/domains/sql)
- **Descripción**: Ejercicios de SQL ordenados por dificultad. Excelente para práctica deliberada.

**LeetCode - Database**

- **URL**: [leetcode.com/problemset/database](https://leetcode.com/problemset/database/)
- **Descripción**: Problemas de SQL más desafiantes. Útil una vez dominados los fundamentos.

**Pandas Exercises**

- **URL**: [github.com/guipsamora/pandas_exercises](https://github.com/guipsamora/pandas_exercises)
- **Descripción**: Colección de ejercicios de Pandas con soluciones. Organizado por tema.

---

## 10. Actividades de Metaaprendizaje

### 10.1 Actividad: Mapeo de mi proceso de datos actual

**Objetivo**: Hacer explícito cómo maneja datos actualmente para identificar oportunidades de mejora.

**Duración**: 45-60 minutos

**Instrucciones**:

1. Piense en un análisis de datos que haya realizado recientemente (para investigación, docencia, o gestión).

2. Documente su proceso respondiendo:
   - ¿De dónde vinieron los datos?
   - ¿En qué formato estaban?
   - ¿Qué "limpieza" hizo? ¿Fue manual?
   - ¿Cuánto tiempo tomó la preparación vs. el análisis?
   - ¿Podría otra persona reproducir exactamente lo que hizo?

3. Identifique:
   - ¿Qué pasos fueron más tediosos?
   - ¿Dónde podrían haber entrado errores?
   - ¿Qué herramientas del módulo podrían ayudar?

4. Conserve este mapeo para comparar al final del programa.

### 10.2 Actividad: Diálogo con el error

**Objetivo**: Transformar la relación con los errores de programación.

**Duración**: Tarea continua durante el módulo

**Instrucciones**:

Cada vez que encuentre un error de código:

1. **Pause** antes de frustrarse.

2. **Lea** el mensaje de error completo (no solo la última línea).

3. **Traduzca** el mensaje a lenguaje simple:
   - `NameError`: "No conozco esta variable"
   - `SyntaxError`: "No entiendo la estructura"
   - `KeyError`: "Esta clave no existe"
   - `TypeError`: "No puedo hacer esta operación con estos tipos"

4. **Pregunte** al error:
   - ¿En qué línea estás?
   - ¿Qué esperabas encontrar?
   - ¿Qué encontraste en cambio?

5. **Documente** en su diario de errores.

### 10.3 Actividad: Enseñar para aprender

**Objetivo**: Consolidar comprensión explicando a otros.

**Duración**: 30-45 minutos después de cada sesión

**Instrucciones**:

Después de cada sesión del módulo:

1. **Seleccione** un concepto que aprendió.

2. **Explíquelo** como si enseñara a un colega que no sabe programar:
   - Use analogías de su disciplina
   - Evite jerga técnica
   - Dé un ejemplo concreto

3. **Grábese** (audio o video, solo para usted) explicando el concepto.

4. **Escuche/vea** la grabación y note:
   - ¿Dónde se trabó?
   - ¿Qué partes no explicó bien?
   - ¿Qué necesita repasar?

### 10.4 Actividad: Refactorización reflexiva

**Objetivo**: Desarrollar capacidad de mejorar código propio.

**Duración**: 20-30 minutos

**Instrucciones**:

1. Tome código que escribió al inicio del módulo (de un ejercicio o laboratorio).

2. Sin mirarlo, reescriba la solución con lo que sabe ahora.

3. Compare ambas versiones:
   - ¿La nueva es más legible?
   - ¿Es más eficiente?
   - ¿Usa mejores prácticas?

4. Documente qué aprendió entre una versión y otra.

### 10.5 Actividad: Transferencia disciplinar

**Objetivo**: Planificar la aplicación de habilidades en su contexto.

**Duración**: 60-90 minutos

**Instrucciones**:

1. Identifique un dataset que use o podría usar en su asignatura.

2. Diseñe un ejercicio de data wrangling para sus estudiantes:
   - ¿Qué datos usarían?
   - ¿Qué problemas de calidad tendrían que resolver?
   - ¿Qué preguntas responderían?
   - ¿Qué aprenderían del proceso?

3. Esboce el notebook que usaría, incluyendo:
   - Instrucciones claras
   - Código de ejemplo
   - Preguntas guía
   - Criterios de evaluación

4. Comparta con el grupo para feedback.

---

## 11. Glosario Técnico-Crítico

### API (Application Programming Interface)
**Definición técnica**: Conjunto de protocolos para que diferentes software se comuniquen.
**En data wrangling**: Frecuentemente usamos APIs para obtener datos de servicios web (ej: API del Banco Mundial).
**Crítica**: Las APIs pueden cambiar sin aviso, rompiendo código que dependía de ellas.

### CSV (Comma-Separated Values)
**Definición técnica**: Formato de archivo de texto donde los valores están separados por comas.
**Ventajas**: Simple, universal, legible por humanos.
**Trampas**: El "separador" varía (comas, punto y coma, tabs). La codificación de caracteres puede causar problemas.

### DataFrame
**Definición técnica**: Estructura de datos bidimensional con filas y columnas etiquetadas.
**Analogía**: Como una hoja de Excel, pero con superpoderes.
**Nota**: Aunque parece una tabla, internamente es más complejo (índices, tipos de datos por columna).

### EDA (Exploratory Data Analysis)
**Definición técnica**: Análisis estadístico orientado a descubrir patrones sin hipótesis previas.
**Filosofía**: "Dejar que los datos hablen" (Tukey).
**Crítica**: La idea de explorar "sin hipótesis" es cuestionable; siempre tenemos supuestos.

### ETL (Extract, Transform, Load)
**Definición técnica**: Proceso de extraer datos de fuentes, transformarlos, y cargarlos en un destino.
**Relación con wrangling**: Data wrangling es similar pero más enfocado en preparación para análisis que en ingeniería de datos.

### Imputación
**Definición técnica**: Proceso de reemplazar valores faltantes con valores estimados.
**Métodos comunes**: Media, mediana, moda, predicción por modelo.
**Crítica**: Toda imputación introduce supuestos. Documentar qué se imputó y cómo es crucial.

### Join
**Definición técnica**: Operación que combina filas de dos tablas basándose en una columna común.
**Tipos**: Inner, Left, Right, Outer, Cross.
**Trampa común**: Joins pueden multiplicar filas si hay duplicados en las claves.

### NaN (Not a Number)
**Definición técnica**: Valor especial que representa datos faltantes en Pandas/NumPy.
**Comportamiento**: NaN ≠ NaN (comparar NaN consigo mismo da False).
**Nota**: Pandas también usa None y NaT (Not a Time) para diferentes tipos de faltantes.

### Outlier (Valor atípico)
**Definición técnica**: Observación que se desvía significativamente del resto.
**Debate**: ¿Es un error a corregir o información valiosa a preservar?
**Regla práctica**: Investigar antes de eliminar. Un outlier podría ser el dato más importante.

### Query
**Definición técnica**: Solicitud de datos a una base de datos o estructura de datos.
**En SQL**: Instrucción SELECT y sus componentes.
**En Pandas**: Método `.query()` o filtrado con corchetes.

### Reproducibilidad
**Definición técnica**: Capacidad de obtener los mismos resultados a partir de los mismos datos y código.
**Importancia**: Fundamental para ciencia rigurosa y auditoría.
**Herramientas**: Notebooks, control de versiones, documentación, ambientes virtuales.

### Tidy Data (Datos ordenados)
**Definición**: Principios de Wickham: cada variable en una columna, cada observación en una fila, cada tipo de unidad en una tabla.
**Crítica**: "Tidy" depende del análisis planeado. Lo que es tidy para un análisis puede no serlo para otro.

### Wrangling
**Etimología**: Del inglés rural, "arreando caballos salvajes".
**En datos**: El proceso de domar datos desordenados hasta que son útiles.
**Sinónimos**: Munging, cleaning, preparation, preprocessing.

---

## 12. Referencias Bibliográficas

### Referencias citadas en esta guía

Dweck, C. S. (2006). *Mindset: The New Psychology of Success*. Random House.

Kandel, S., Heer, J., Plaisant, C., Kennedy, J., van Ham, F., Riche, N. H., ... & Buono, P. (2011). Research directions in data wrangling: Visualizations and transformations for usable and credible data. *Information Visualization*, 10(4), 271-288.

McKinney, W. (2022). *Python for Data Analysis* (3ra edición). O'Reilly Media.

Sweigart, A. (2019). *Automate the Boring Stuff with Python* (2da edición). No Starch Press.

Tukey, J. W. (1977). *Exploratory Data Analysis*. Addison-Wesley.

VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly Media.

Wickham, H. (2014). Tidy Data. *Journal of Statistical Software*, 59(10), 1-23. https://doi.org/10.18637/jss.v059.i10

### Referencias adicionales recomendadas

Beaulieu, A. (2020). *Learning SQL* (3ra edición). O'Reilly Media.

Bruce, P., Bruce, A., & Gedeck, P. (2020). *Practical Statistics for Data Scientists* (2da edición). O'Reilly Media.

Dasu, T., & Johnson, T. (2003). *Exploratory Data Mining and Data Cleaning*. Wiley.

Grus, J. (2019). *Data Science from Scratch* (2da edición). O'Reilly Media.

Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen, P., Cournapeau, D., ... & Oliphant, T. E. (2020). Array programming with NumPy. *Nature*, 585(7825), 357-362.

Lutz, M. (2013). *Learning Python* (5ta edición). O'Reilly Media.

Matthes, E. (2019). *Python Crash Course* (2da edición). No Starch Press.

Molinaro, A., & de Graaf, R. (2020). *SQL Cookbook* (2da edición). O'Reilly Media.

Redman, T. C. (2001). *Data Quality: The Field Guide*. Digital Press.

The Pandas Development Team. (2024). *pandas documentation*. https://pandas.pydata.org/docs/

---

## Nota Final

El data wrangling es, paradójicamente, tanto la parte más tediosa como la más importante del análisis de datos. Es donde se cometen los errores más graves (datos mal fusionados, valores mal interpretados) y donde se hacen los descubrimientos más sorprendentes (patrones inesperados, problemas de calidad que revelan fallas en procesos).

Como docente, usted tiene la oportunidad de transformar esta "parte aburrida" en una fuente de aprendizaje profundo para sus estudiantes. Los datos imperfectos del mundo real son, de hecho, mejores maestros que los datasets limpios de los libros de texto.

*Dominar los datos comienza por respetarlos: entender de dónde vienen, qué representan, y qué nos ocultan.*

---

**Versión**: 1.0
**Fecha**: Marzo 2026
**Programa**: Formación Docente en Ciencia de Datos y BI - FACES UCAB
**Licencia**: CC BY-SA 4.0

