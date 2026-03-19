# Casos de Estudio Reales

Este documento presenta casos de estudio basados en datos y situaciones reales de Venezuela y América Latina, adaptados para uso educativo.

---

## Índice

1. [Caso 1: Inflación y Poder Adquisitivo en Venezuela](#caso-1-inflación-y-poder-adquisitivo-en-venezuela)
2. [Caso 2: Deserción Universitaria en América Latina](#caso-2-deserción-universitaria-en-américa-latina)
3. [Caso 3: Análisis de Encuesta de Clima Laboral](#caso-3-análisis-de-encuesta-de-clima-laboral)
4. [Caso 4: Predicción de Demanda en Retail](#caso-4-predicción-de-demanda-en-retail)

---

## Caso 1: Inflación y Poder Adquisitivo en Venezuela

### Contexto

Venezuela ha experimentado uno de los episodios de hiperinflación más severos de la historia moderna. Entre 2016 y 2021, la inflación acumulada superó el 50,000,000%, afectando dramáticamente el poder adquisitivo de la población.

### Fuentes de Datos

| Fuente | URL | Descripción |
|--------|-----|-------------|
| Banco Central de Venezuela | bcv.org.ve | Datos oficiales (con limitaciones) |
| Banco Mundial | data.worldbank.org | Indicadores macroeconómicos |
| CENDA | cfrfranciscodemirandavzla | Canasta básica |
| ENCOVI | proyectoencovi.com | Encuesta de Condiciones de Vida |

### Datos Disponibles (Simplificados)

```
Año,Inflacion_Anual_Pct,Salario_Minimo_USD,Canasta_Basica_USD,Cobertura_Pct
2015,180,30,250,12
2016,800,15,300,5
2017,2600,8,350,2.3
2018,130000,5,400,1.3
2019,9500,8,450,1.8
2020,2959,3,500,0.6
2021,686,3,350,0.9
2022,234,16,400,4
2023,189,130,500,26
```

### Preguntas de Análisis

#### Módulo 1: Pensamiento Crítico
1. ¿Por qué los datos oficiales de inflación podrían diferir de estimaciones independientes?
2. ¿Qué sesgos podrían afectar la medición de la canasta básica?
3. ¿Cómo interpretar la "cobertura" del salario mínimo sobre la canasta?

#### Módulo 2: Data Wrangling
1. Calcular la variación porcentual año a año
2. Crear variable de "meses de trabajo para cubrir canasta"
3. Manejar valores extremos (inflación 130000%)

#### Módulo 3: Visualización
1. Diseñar gráfico que muestre la pérdida de poder adquisitivo
2. Crear dashboard comparativo con otros países de la región
3. Comunicar el impacto humano de las estadísticas

#### Módulo 4: Modelado (Exploratorio)
1. ¿Se puede predecir la inflación del próximo mes?
2. ¿Qué variables macroeconómicas correlacionan con la inflación?

### Preguntas de Reflexión

1. **Ética de datos:** ¿Es ético usar estos datos sin contexto político?
2. **Comunicación:** ¿Cómo presentar datos tan extremos sin sensacionalismo?
3. **Limitaciones:** ¿Qué historias NO pueden contar estos datos?

---

## Caso 2: Deserción Universitaria en América Latina

### Contexto

La deserción universitaria en América Latina promedia 50% (UNESCO, 2020), significando que la mitad de los estudiantes que ingresan no completan su carrera. Venezuela enfrenta desafíos adicionales por la crisis económica y la emigración.

### Fuentes de Datos

| Fuente | URL | Descripción |
|--------|-----|-------------|
| UNESCO-IESALC | iesalc.unesco.org | Estadísticas de educación superior |
| OPSU Venezuela | opsu.gob.ve | Matrícula universitaria |
| Estudios UCAB | ucab.edu.ve | Investigaciones institucionales |
| ENCOVI | proyectoencovi.com | Migración y educación |

### Datos Comparativos (Simulados basados en tendencias reales)

```
País,Tasa_Desercion_Pct,PIB_Educacion_Pct,Anos_Promedio_Graduacion,Empleabilidad_Graduados_Pct
Venezuela,55,2.1,7.5,45
Colombia,42,4.5,6.2,68
Chile,35,5.2,5.8,75
Mexico,40,4.0,6.0,62
Argentina,60,5.5,8.0,58
Brasil,45,5.0,5.5,65
Peru,38,3.8,5.5,60
```

### Factores de Deserción (Basado en estudios reales)

| Factor | % de desertores que lo mencionan |
|--------|----------------------------------|
| Económico (no puede pagar) | 45% |
| Laboral (necesita trabajar) | 35% |
| Académico (dificultades) | 30% |
| Personal/Familiar | 25% |
| Migración | 20% (Venezuela) |
| Insatisfacción con carrera | 15% |

### Preguntas de Análisis

#### Módulo 1: Pensamiento con Datos
1. ¿Por qué la tasa de deserción no es igual a "fracaso"?
2. ¿Qué variables confusoras podrían explicar la correlación PIB-deserción?
3. ¿Cómo afecta el sesgo de supervivencia a estos datos?

#### Módulo 2: Data Wrangling
1. Integrar datos de múltiples fuentes con diferentes formatos
2. Calcular indicadores derivados (costo por graduado, eficiencia terminal)
3. Limpiar datos con definiciones inconsistentes de "deserción"

#### Módulo 3: Visualización
1. Crear comparativo regional que contextualice a Venezuela
2. Diseñar dashboard de factores de deserción para una facultad
3. Narrar la historia de un "estudiante promedio" con datos

#### Módulo 4: Modelado
1. Predecir probabilidad de deserción por características del estudiante
2. Identificar factores más importantes (feature importance)
3. Diseñar sistema de alerta temprana

### Ejercicio Práctico

**Escenario:** Usted es analista de datos en FACES-UCAB. El Decano le pide un informe sobre deserción para presentar al Consejo Universitario.

**Entregable:** Dashboard de una página + memo ejecutivo de 500 palabras.

**Datos a usar:** `matricula_faces.csv` del repositorio

---

## Caso 3: Análisis de Encuesta de Clima Laboral

### Contexto

Las universidades venezolanas enfrentan desafíos de retención de personal docente debido a la crisis económica. La satisfacción laboral y las condiciones de trabajo son factores críticos para la calidad educativa.

### Fuentes de Datos

| Fuente | Descripción |
|--------|-------------|
| Encuesta interna UCAB (simulada) | Clima laboral docente |
| FAPUV | Estadísticas de profesorado universitario |
| ILDIS | Estudios sobre sector público |

### Estructura de Datos (encuesta_docente.csv)

El dataset simula una encuesta con:
- Variables demográficas: edad, género, antigüedad
- Variables laborales: dedicación, departamento, formación
- Variables de satisfacción: escala Likert 1-5
- Variables de productividad: publicaciones, carga horaria

### Preguntas de Análisis

#### Módulo 1: Diseño de Encuestas
1. ¿Qué problemas podrían tener estas preguntas de encuesta?
2. ¿Cómo afecta la escala Likert al análisis?
3. ¿Qué sesgos de respuesta podrían existir (deseabilidad social, aquiescencia)?

#### Módulo 2: Análisis Exploratorio
```python
# Análisis sugerido
import pandas as pd

df = pd.read_csv('encuesta_docente.csv')

# 1. Satisfacción promedio por departamento
df.groupby('departamento')['satisfaccion_general'].mean()

# 2. Correlación entre variables
df[['satisfaccion_general', 'satisfaccion_salarial',
    'antiguedad', 'publicaciones']].corr()

# 3. Comparación por dedicación
df.groupby('dedicacion').agg({
    'satisfaccion_general': 'mean',
    'publicaciones': 'mean',
    'carga_horaria': 'mean'
})
```

#### Módulo 3: Visualización
1. Crear visualización de satisfacción por dimensión
2. Identificar patrones por antigüedad/dedicación
3. Diseñar informe para presentar a autoridades

#### Módulo 4: Análisis Predictivo
1. ¿Se puede predecir productividad (publicaciones) con satisfacción?
2. ¿Qué factores predicen mayor insatisfacción?

### Consideraciones Éticas

1. **Confidencialidad:** ¿Cómo proteger identidad de respondentes?
2. **Uso de resultados:** ¿Cómo evitar que se use para represalias?
3. **Transparencia:** ¿Se deben compartir resultados con docentes?

---

## Caso 4: Predicción de Demanda en Retail

### Contexto

Una cadena de supermercados en Venezuela necesita optimizar su inventario en un contexto de alta inflación, escasez de productos y cadenas de suministro inestables.

### Desafíos Específicos del Contexto Venezolano

| Desafío | Impacto en Análisis |
|---------|---------------------|
| Inflación alta | Precios cambian diariamente |
| Escasez | Demanda ≠ Ventas (restricción de oferta) |
| Dolarización parcial | Múltiples monedas |
| Migración | Cambios demográficos en clientes |
| Regulaciones de precios | Distorsiones en precios |

### Datos Disponibles (ventas_retail.csv)

```
fecha,tienda,region,categoria,cantidad,ingreso,costo
2023-01-01,Tienda-01,Capital,Alimentos,50,250.00,175.00
2023-01-01,Tienda-01,Capital,Bebidas,30,120.00,72.00
...
```

### Preguntas de Análisis

#### Módulo 2: Preparación de Datos
1. Calcular métricas: margen, ticket promedio, rotación
2. Agregar datos por día/semana/mes
3. Crear features temporales (día de semana, quincena, fin de mes)

```python
# Ejemplo de feature engineering
df['dia_semana'] = pd.to_datetime(df['fecha']).dt.dayofweek
df['es_quincena'] = pd.to_datetime(df['fecha']).dt.day.isin([15, 30, 31])
df['margen'] = (df['ingreso'] - df['costo']) / df['ingreso']
df['semana'] = pd.to_datetime(df['fecha']).dt.isocalendar().week
```

#### Módulo 3: Dashboard de Ventas
1. KPIs: Ventas totales, margen promedio, ticket promedio
2. Análisis por categoría y región
3. Tendencias temporales

#### Módulo 4: Predicción
1. Predecir ventas de la próxima semana por categoría
2. Identificar productos con demanda estacional
3. Detectar anomalías (picos o caídas inusuales)

### Modelo Simplificado

```python
# Predicción de demanda básica
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Features
X = df[['dia_semana', 'es_quincena', 'semana', 'categoria_encoded']]
y = df['cantidad']

# Modelo
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Interpretar
importances = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)
```

### Preguntas de Reflexión

1. **Limitaciones:** ¿Por qué las ventas pasadas podrían no predecir el futuro en contexto de crisis?
2. **Ética:** ¿Es ético optimizar ganancias en contexto de escasez?
3. **Impacto:** ¿Cómo podría usarse este análisis para mejorar acceso a productos básicos?

---

## Recursos Adicionales

### Fuentes de Datos Públicos Venezuela

| Fuente | URL | Tipo de Datos |
|--------|-----|---------------|
| INE Venezuela | ine.gob.ve | Censo, encuestas |
| BCV | bcv.org.ve | Indicadores económicos |
| ENCOVI | proyectoencovi.com | Condiciones de vida |
| Observatorio Venezolano de Conflictividad Social | observatoriodeconflictos.org.ve | Datos sociales |

### Fuentes de Datos Latinoamérica

| Fuente | URL | Tipo de Datos |
|--------|-----|---------------|
| CEPAL | cepal.org | Estadísticas regionales |
| Banco Mundial | data.worldbank.org | Indicadores globales |
| BID | data.iadb.org | Desarrollo |
| UNESCO-IESALC | iesalc.unesco.org | Educación superior |

### Lecturas Recomendadas

1. **Inflación Venezuela:**
   - Reinhart, C. & Savastano, M. (2003). "The Realities of Modern Hyperinflation"
   - Werner, A. (2020). "Outlook for Latin America and the Caribbean" - IMF

2. **Deserción Universitaria:**
   - Tinto, V. (1993). "Leaving College: Rethinking the Causes and Cures of Student Attrition"
   - Ferreyra et al. (2017). "At a Crossroads: Higher Education in Latin America" - World Bank

3. **Análisis de Encuestas:**
   - Groves et al. (2009). "Survey Methodology" - Wiley

---

## Uso Pedagógico

### Sugerencias para Instructores

1. **Contextualización:** Antes de cada caso, discutir el contexto socio-económico
2. **Sensibilidad:** Reconocer que estudiantes pueden tener experiencias personales con estos temas
3. **Crítica:** Fomentar cuestionamiento de fuentes y metodologías
4. **Acción:** Vincular análisis con posibles acciones o políticas

### Adaptación por Nivel

| Nivel | Enfoque |
|-------|---------|
| **Introductorio** | Exploración descriptiva, visualización básica |
| **Intermedio** | Análisis completo, dashboard, narrativa |
| **Avanzado** | Modelado predictivo, interpretación, recomendaciones |

---

*Última actualización: Enero 2025*
