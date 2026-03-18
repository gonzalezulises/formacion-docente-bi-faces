# Guía de Estudio: Módulo 3 - Business Intelligence Aplicado a Decisiones

## El arte de transformar datos en historias que impulsan la acción

---

> *"El propósito de la visualización es la comprensión, no las imágenes."*
> — Ben Shneiderman, pionero en interacción humano-computadora

---

## Tabla de Contenidos

1. [Propósito y Relevancia del Módulo](#1-propósito-y-relevancia-del-módulo)
2. [Marco Conceptual: ¿Qué es Business Intelligence?](#2-marco-conceptual-qué-es-business-intelligence)
3. [Conceptos Fundamentales](#3-conceptos-fundamentales)
4. [Metaaprendizaje: El Docente como Comunicador Visual](#4-metaaprendizaje-el-docente-como-comunicador-visual)
5. [Conexiones con la Práctica Docente](#5-conexiones-con-la-práctica-docente)
6. [Preguntas de Reflexión Metacognitiva](#6-preguntas-de-reflexión-metacognitiva)
7. [Lecturas Fundamentales](#7-lecturas-fundamentales)
8. [Lecturas Complementarias](#8-lecturas-complementarias)
9. [Recursos Multimedia](#9-recursos-multimedia)
10. [Actividades de Metaaprendizaje](#10-actividades-de-metaaprendizaje)
11. [Glosario de Visualización](#11-glosario-de-visualización)
12. [Referencias Bibliográficas](#12-referencias-bibliográficas)

---

## 1. Propósito y Relevancia del Módulo

### 1.1 De datos a decisiones: el eslabón perdido

Usted ya sabe preparar datos (Módulo 2). Pero datos limpios sin comunicación efectiva son como un libro cerrado: contienen valor, pero nadie lo aprovecha.

Este módulo aborda el **eslabón crítico** entre análisis y acción: la capacidad de comunicar hallazgos de manera que generen comprensión, convicción y cambio.

El Business Intelligence (BI) no es simplemente hacer gráficos bonitos. Es un sistema completo para:

- **Monitorear** el estado actual de una organización
- **Diagnosticar** problemas y oportunidades
- **Predecir** tendencias futuras
- **Comunicar** hallazgos a tomadores de decisiones
- **Democratizar** el acceso a información

### 1.2 La paradoja de la abundancia de datos

Vivimos en una época de abundancia de datos sin precedentes. Sin embargo:

- Los ejecutivos reportan sentirse **más abrumados**, no más informados
- Las organizaciones recolectan datos que **nunca analizan**
- Los dashboards proliferan pero las **decisiones no mejoran**
- La visualización se usa para **impresionar**, no para comunicar

Esta paradoja revela que el problema no es la falta de datos o herramientas, sino la falta de **pensamiento crítico sobre comunicación visual**.

### 1.3 Por qué docentes necesitan BI

| Rol | Aplicación de BI |
|-----|------------------|
| **Investigador** | Comunicar hallazgos en artículos y conferencias |
| **Docente** | Crear visualizaciones didácticas para estudiantes |
| **Gestor académico** | Monitorear indicadores de programa, facultad o universidad |
| **Consultor** | Presentar análisis a clientes y stakeholders |

Más allá de aplicaciones específicas, las habilidades de este módulo desarrollan su **capacidad de comunicar complejidad con claridad**—una competencia transferible a cualquier ámbito profesional.

### 1.4 Competencias que desarrollará

| Competencia | Descripción | Nivel esperado |
|-------------|-------------|----------------|
| **Alfabetización visual** | Leer e interpretar visualizaciones críticamente | Intermedio |
| **Diseño de visualizaciones** | Crear gráficos efectivos para diferentes propósitos | Intermedio |
| **Herramientas BI** | Usar Power BI y/o Tableau para dashboards | Intermedio |
| **Definición de KPIs** | Diseñar indicadores significativos | Introductorio |
| **Storytelling con datos** | Construir narrativas persuasivas | Intermedio |
| **Crítica visual** | Identificar problemas en visualizaciones | Avanzado |

---

## 2. Marco Conceptual: ¿Qué es Business Intelligence?

### 2.1 Definición y evolución histórica

**Business Intelligence** es un término paraguas que abarca las estrategias, tecnologías y prácticas usadas para recolectar, integrar, analizar y presentar información empresarial.

#### Breve historia del BI

| Década | Desarrollo | Tecnología representativa |
|--------|------------|---------------------------|
| 1960s | Sistemas de reportes | Mainframes, informes en papel |
| 1970s | Decision Support Systems | Modelos cuantitativos |
| 1980s | Executive Information Systems | Interfaces gráficas |
| 1990s | Data Warehousing, OLAP | Cubos multidimensionales |
| 2000s | Business Intelligence moderno | Dashboards, self-service |
| 2010s | Analytics avanzado | Big Data, machine learning |
| 2020s | BI aumentado | IA generativa, NLP |

### 2.2 El stack de BI moderno

```
┌────────────────────────────────────────────────────────────┐
│                     CAPA DE PRESENTACIÓN                    │
│         Dashboards, Reportes, Alertas, Mobile               │
│              (Power BI, Tableau, Looker)                    │
└────────────────────────────────────────────────────────────┘
                              ▲
                              │
┌────────────────────────────────────────────────────────────┐
│                    CAPA DE ANÁLISIS                         │
│          Métricas, KPIs, Drill-down, Filtros                │
│              (DAX, Calculated Fields)                       │
└────────────────────────────────────────────────────────────┘
                              ▲
                              │
┌────────────────────────────────────────────────────────────┐
│                  CAPA DE MODELADO                           │
│       Modelo de datos, Relaciones, Dimensiones              │
│          (Star Schema, Snowflake Schema)                    │
└────────────────────────────────────────────────────────────┘
                              ▲
                              │
┌────────────────────────────────────────────────────────────┐
│                    CAPA DE DATOS                            │
│           Data Warehouse, Data Lake, APIs                   │
│         (SQL Server, Snowflake, BigQuery)                   │
└────────────────────────────────────────────────────────────┘
                              ▲
                              │
┌────────────────────────────────────────────────────────────┐
│                  FUENTES DE DATOS                           │
│         ERP, CRM, Excel, Web, Sensores, APIs                │
└────────────────────────────────────────────────────────────┘
```

### 2.3 BI vs. Analytics vs. Data Science

Estos términos se usan frecuentemente de manera intercambiable, pero tienen matices:

| Aspecto | Business Intelligence | Analytics | Data Science |
|---------|----------------------|-----------|--------------|
| **Enfoque temporal** | Pasado y presente | Pasado, presente y futuro | Futuro |
| **Pregunta típica** | ¿Qué pasó? ¿Qué está pasando? | ¿Por qué pasó? ¿Qué pasará? | ¿Qué optimizar? |
| **Usuarios típicos** | Ejecutivos, gerentes | Analistas | Científicos de datos |
| **Complejidad técnica** | Baja a media | Media | Alta |
| **Herramientas** | Power BI, Tableau | Excel avanzado, R, Python | Python, ML frameworks |

**Nota**: Estas categorías se superponen cada vez más. Power BI ahora incluye capacidades predictivas; Data Science incluye visualización.

### 2.4 El debate: BI tradicional vs. Self-Service BI

**BI tradicional**: Departamento de TI crea reportes; usuarios los consumen pasivamente.

**Self-Service BI**: Usuarios de negocio crean sus propios análisis con herramientas accesibles.

| Aspecto | BI Tradicional | Self-Service BI |
|---------|---------------|-----------------|
| **Velocidad** | Lento (semanas) | Rápido (horas) |
| **Control** | Alto (TI) | Distribuido |
| **Consistencia** | Alta | Variable |
| **Innovación** | Limitada | Alta |
| **Riesgo de errores** | Bajo | Medio-Alto |
| **Adopción** | Obligatoria | Orgánica |

El modelo actual tiende hacia un **híbrido**: TI provee infraestructura y gobernanza; usuarios crean análisis dentro de ese marco.

---

## 3. Conceptos Fundamentales

### 3.1 Principios de Visualización Efectiva

#### La jerarquía visual

El ojo humano procesa información visual en un orden predecible. Los elementos visuales más destacados se perciben primero:

1. **Posición** (más fuerte)
2. **Color/Saturación**
3. **Tamaño**
4. **Forma**
5. **Orientación** (más débil)

**Implicación para diseño**: Use posición para lo más importante. Reserve color para énfasis, no decoración.

#### Principios Gestalt

Los principios de la psicología Gestalt explican cómo percibimos agrupaciones:

| Principio | Descripción | Aplicación en visualización |
|-----------|-------------|----------------------------|
| **Proximidad** | Elementos cercanos se perciben como grupo | Agrupe datos relacionados espacialmente |
| **Similitud** | Elementos similares se perciben como grupo | Use color/forma consistente para categorías |
| **Continuidad** | Preferimos líneas continuas | Las líneas de tendencia funcionan por esto |
| **Cierre** | Completamos formas incompletas | Podemos sugerir sin mostrar todo |
| **Figura-fondo** | Distinguimos objeto de contexto | Cree contraste entre datos y fondo |

#### Pre-attentive attributes

Ciertos atributos se procesan **antes** de la atención consciente (en menos de 250ms):

- Color
- Tamaño
- Posición
- Orientación
- Movimiento

**Implicación**: Use estos atributos para resaltar lo importante. Un dato crítico en rojo sobre fondo neutro "salta" inmediatamente.

#### El ratio dato-tinta de Tufte

Edward Tufte propuso maximizar el "ratio dato-tinta":

```
Ratio dato-tinta = Tinta usada para mostrar datos / Tinta total
```

**Principio**: Elimine todo elemento que no contribuya a comunicar información.

**Elementos a eliminar**:
- Fondos decorativos
- Líneas de grilla innecesarias
- Efectos 3D sin significado
- Bordes redundantes
- Leyendas que repiten lo obvio

### 3.2 Elección del Gráfico Correcto

#### El problema

El gráfico equivocado puede oscurecer en lugar de iluminar. La elección debe basarse en:

1. **Tipo de datos** (categóricos, numéricos, temporales)
2. **Relación a mostrar** (comparación, distribución, composición, relación)
3. **Audiencia** (técnica, ejecutiva, general)
4. **Contexto** (presentación, reporte, exploración)

#### Guía de selección

| Propósito | Tipos de gráfico recomendados |
|-----------|-------------------------------|
| **Comparación entre categorías** | Barras (horizontal o vertical), Lollipop |
| **Cambio en el tiempo** | Líneas, Área (si pocas series) |
| **Parte del todo** | Barras apiladas 100%, Treemap. (Evitar pie charts) |
| **Distribución** | Histograma, Boxplot, Violin |
| **Correlación** | Scatter plot, Bubble chart |
| **Geográfico** | Mapa coroplético, Mapa de puntos |

#### El caso contra los gráficos de pastel (pie charts)

Los pie charts son populares pero problemáticos:

1. **Difícil comparar ángulos**: El ojo compara mejor longitudes que ángulos
2. **Mala para muchas categorías**: Más de 3-4 sectores confunde
3. **No muestra cambio**: Imposible comparar dos pie charts efectivamente

**Alternativa**: Barras horizontales ordenadas por tamaño comunican lo mismo, mejor.

**Cuándo usar pie chart**: Solo cuando:
- Hay 2-3 categorías
- La composición suma 100%
- Una categoría es claramente dominante
- La audiencia espera un pie chart (tradición)

### 3.3 KPIs (Key Performance Indicators)

#### ¿Qué es un KPI?

Un **KPI** es una métrica cuantificable que refleja qué tan bien una organización está logrando sus objetivos clave.

**No toda métrica es un KPI**. Un KPI debe ser:

| Característica | Descripción | Ejemplo |
|----------------|-------------|---------|
| **Key** (Clave) | Relacionado con objetivos estratégicos | Tasa de graduación (no número de sillas) |
| **Performance** (Desempeño) | Mide resultados, no actividades | Estudiantes empleados (no cursos dictados) |
| **Indicator** (Indicador) | Señala dirección, permite acción | Si baja, sabemos qué investigar |

#### Framework SMART para KPIs

| Letra | Significado | Pregunta clave |
|-------|-------------|----------------|
| S | Specific (Específico) | ¿Qué exactamente medimos? |
| M | Measurable (Medible) | ¿Podemos obtener datos confiables? |
| A | Achievable (Alcanzable) | ¿Es realista la meta? |
| R | Relevant (Relevante) | ¿Importa para los objetivos? |
| T | Time-bound (Temporal) | ¿En qué período? |

#### KPIs para contexto universitario (FACES)

| Área | KPI ejemplo | Fórmula/Definición |
|------|-------------|-------------------|
| **Académico** | Tasa de aprobación | Estudiantes que aprueban / Total inscritos |
| **Académico** | Índice de retención | Estudiantes que continúan / Cohorte inicial |
| **Académico** | Promedio de notas | Media de calificaciones finales |
| **Eficiencia** | Tiempo promedio de graduación | Semestres promedio hasta titulación |
| **Investigación** | Artículos per cápita | Publicaciones / Docentes activos |
| **Satisfacción** | NPS estudiantil | Net Promoter Score de encuestas |
| **Financiero** | Costo por egresado | Presupuesto / Graduados del período |

#### Anti-patrones en KPIs

**1. Vanity metrics**: Métricas que suben pero no importan
- *Ejemplo*: "Número de seguidores en redes" sin engagement

**2. Métricas gaming-able**: Indicadores que se pueden manipular sin mejorar resultados reales
- *Ejemplo*: "Número de publicaciones" sin control de calidad

**3. Métricas lagging sin leading**: Solo indicadores de resultado sin predictores
- *Ejemplo*: Solo medir deserción, no indicadores tempranos de riesgo

**4. Demasiados KPIs**: Si todo es "clave", nada es clave
- *Regla*: 5-7 KPIs máximo por área

### 3.4 Storytelling con Datos

#### El problema con "presentar datos"

Muchas presentaciones de datos fallan porque:

- Muestran **todo** sin jerarquía de importancia
- Carecen de **narrativa** (son colecciones de gráficos)
- No tienen **llamado a la acción** claro
- Asumen que los datos "hablan por sí mismos"

Los datos no hablan por sí mismos. Necesitan un narrador.

#### El framework de Cole Nussbaumer Knaflic

En *Storytelling with Data*, Cole propone un proceso:

**1. Entienda el contexto**
- ¿Quién es su audiencia?
- ¿Qué necesitan saber?
- ¿Qué acción quiere que tomen?

**2. Elija una visualización apropiada**
- Basada en mensaje, no en datos
- Simplifique sin distorsionar

**3. Elimine el desorden (clutter)**
- Aplique ratio dato-tinta
- Cada elemento debe justificarse

**4. Enfoque la atención**
- Use pre-attentive attributes
- Guíe el ojo del lector

**5. Piense como diseñador**
- Considere alineación, espaciado, consistencia
- La estética importa para credibilidad

**6. Cuente una historia**
- Estructura narrativa: contexto → tensión → resolución
- Un mensaje central claro

#### Las 3 C's de la narrativa de datos

| Elemento | Descripción | Ejemplo |
|----------|-------------|---------|
| **Context** (Contexto) | Situación actual, antecedentes | "La deserción ha aumentado 15% en 3 años" |
| **Conflict** (Conflicto) | Problema, tensión, oportunidad | "Si continúa, perderemos 200 estudiantes/año" |
| **Conclusion** (Conclusión) | Resolución, recomendación | "Proponemos programa de alertas tempranas" |

#### Estructura narrativa para presentaciones

```
┌──────────────────────────────────────────────────────────────┐
│  APERTURA (30 seg)                                           │
│  Hook: dato sorprendente, pregunta, provocación              │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│  CONTEXTO (2-3 min)                                          │
│  ¿Por qué estamos aquí? ¿Qué pregunta respondemos?           │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│  HALLAZGOS (5-10 min)                                        │
│  Evidencia que construye hacia la conclusión                 │
│  Ordenada por importancia, no por cronología del análisis    │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│  IMPLICACIONES (2-3 min)                                     │
│  ¿Qué significa esto? ¿Por qué importa?                      │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│  LLAMADO A LA ACCIÓN (1 min)                                 │
│  ¿Qué queremos que haga la audiencia?                        │
└──────────────────────────────────────────────────────────────┘
```

### 3.5 Power BI: Conceptos clave

#### Arquitectura de Power BI

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Power Query    │ ──▶ │  Modelo de      │ ──▶ │  Visualización  │
│  (ETL)          │     │  Datos          │     │  (Reportes)     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
     Obtener y            Relaciones,           Gráficos,
     transformar          DAX                   Interactividad
```

#### Power Query

El editor de Power Query es donde:
- Se conecta a fuentes de datos
- Se aplican transformaciones (limpieza)
- Se crean pasos reproducibles

**Principio clave**: Cada transformación es un "paso" que puede modificarse o eliminarse.

#### DAX (Data Analysis Expressions)

DAX es el lenguaje de fórmulas de Power BI. Permite crear:

- **Columnas calculadas**: Evaluadas fila por fila
- **Medidas**: Evaluadas en contexto de filtros

**Ejemplos básicos**:

```dax
// Columna calculada
Ganancia = [Ingresos] - [Costos]

// Medida simple
Total Ventas = SUM(Ventas[Monto])

// Medida con filtro
Ventas 2024 = CALCULATE(
    SUM(Ventas[Monto]),
    Ventas[Año] = 2024
)

// Medida con porcentaje
% Aprobación =
    DIVIDE(
        COUNTROWS(FILTER(Estudiantes, Estudiantes[Nota] >= 10)),
        COUNTROWS(Estudiantes),
        0
    )
```

#### Modelado dimensional

Power BI funciona mejor con modelos **estrella** (star schema):

```
           ┌─────────────┐
           │ Dim_Fecha   │
           └──────┬──────┘
                  │
┌─────────────┐   │   ┌─────────────┐
│ Dim_Carrera │───┼───│ Dim_Docente │
└─────────────┘   │   └─────────────┘
                  │
           ┌──────┴──────┐
           │ Fact_Notas  │ (tabla de hechos)
           └──────┬──────┘
                  │
           ┌──────┴──────┐
           │ Dim_Estudiante│
           └─────────────┘
```

**Tablas de hechos**: Contienen métricas numéricas (notas, ventas, transacciones)
**Tablas de dimensiones**: Contienen atributos descriptivos (carrera, fecha, estudiante)

### 3.6 Tableau: Conceptos clave

#### Filosofía de Tableau

Tableau fue diseñado con la filosofía de **análisis visual**: el proceso de pensar con visualizaciones.

A diferencia de herramientas que primero piden datos y luego permiten visualizar, Tableau invita a **explorar visualmente** desde el inicio.

#### Dimensiones vs. Medidas

| Tipo | Color | Comportamiento | Ejemplos |
|------|-------|----------------|----------|
| **Dimensión** | Azul | Agrupa, segmenta | Carrera, Año, Género |
| **Medida** | Verde | Agrega (suma, promedio) | Notas, Ventas, Edad |

#### Show Me

El panel "Show Me" sugiere visualizaciones basadas en los campos seleccionados. Es útil para exploración, pero no reemplaza el juicio humano sobre qué visualización es más efectiva para el mensaje.

#### Calculated Fields

Similar a DAX en Power BI, Tableau permite crear campos calculados:

```
// Ejemplo: Categoría de nota
IF [Nota] >= 18 THEN "Excelente"
ELSEIF [Nota] >= 15 THEN "Bueno"
ELSEIF [Nota] >= 10 THEN "Aprobado"
ELSE "Reprobado"
END
```

---

## 4. Metaaprendizaje: El Docente como Comunicador Visual

### 4.1 De consumidor a creador de visualizaciones

La mayoría de nosotros hemos **consumido** miles de visualizaciones pero **creado** muy pocas con intención.

Esta transición requiere desarrollar un "ojo" crítico:

- Ver un gráfico y preguntarse: *¿Cómo lo haría diferente?*
- Notar técnicas efectivas: *¿Por qué funciona esto?*
- Identificar fallas: *¿Qué me confunde aquí?*

### 4.2 Sesgos en visualización

Los sesgos cognitivos que afectan el análisis de datos también afectan la visualización:

**Sesgo de confirmación visual**: Tendemos a crear (y ver) visualizaciones que confirman lo que ya creemos.

**Efecto anclaje**: El primer gráfico que vemos "ancla" nuestra interpretación.

**Sesgo de disponibilidad**: Usamos tipos de gráficos que conocemos, no los más efectivos.

**Sesgo de complejidad**: Asumimos que visualizaciones complejas son más rigurosas.

### 4.3 El síndrome del dashboard infinito

Un fenómeno común en BI es crear dashboards que nadie usa. Causas:

1. **Se construyeron sin consultar usuarios**: Técnicos deciden qué mostrar
2. **Muestran todo lo posible**: Sin jerarquía de importancia
3. **No se actualizan**: Datos obsoletos destruyen confianza
4. **No conectan con decisiones**: Información interesante pero no accionable

**Pregunta clave antes de cada visualización**: ¿Qué decisión cambiará gracias a esto?

### 4.4 Ética de la visualización

Las visualizaciones pueden engañar—intencional o accidentalmente:

| Técnica engañosa | Ejemplo | Cómo detectarla |
|------------------|---------|-----------------|
| **Truncar eje Y** | Comenzar en 95% para exagerar diferencia | Verificar si eje comienza en 0 |
| **Escala inconsistente** | Cambiar escala entre gráficos | Comparar escalas explícitamente |
| **Cherry-picking temporal** | Seleccionar período favorable | Pedir serie completa |
| **Colores manipuladores** | Rojo para oponentes, verde para propios | Cuestionar elección de colores |
| **3D innecesario** | Distorsiona proporciones | Preferir siempre 2D |

**Reflexión ética**: Como comunicadores, tenemos responsabilidad de no engañar, incluso cuando sería "conveniente" para nuestro argumento.

### 4.5 Iteración y feedback

Las mejores visualizaciones son resultado de iteración:

1. **Borrador rápido**: Primera versión sin pulir
2. **Auto-crítica**: ¿Qué no funciona?
3. **Feedback externo**: Mostrar a alguien que no conoce los datos
4. **Revisión**: Incorporar feedback
5. **Refinamiento**: Detalles finales

**Pregunta poderosa para feedback**: "¿Qué te dice este gráfico?" (No "¿Qué te parece?")

---

## 5. Conexiones con la Práctica Docente

### 5.1 Para docentes de Economía

#### Visualizaciones clave en economía

| Tipo de dato | Visualización recomendada | Ejemplo |
|--------------|---------------------------|---------|
| Series temporales | Líneas | PIB, Inflación, Tipo de cambio |
| Comparación entre países | Barras horizontales | PIB per cápita por país |
| Composición del PIB | Área apilada 100% | Sectores económicos |
| Correlación | Scatter | Inflación vs. Desempleo |
| Distribución de ingreso | Histograma, Lorenz | Deciles de ingreso |

#### Dashboard ejemplo: Indicadores macroeconómicos

Un dashboard para economía podría incluir:
- KPIs de cabecera: Inflación actual, Tipo de cambio, Tasa de desempleo
- Tendencia: Serie de inflación últimos 24 meses
- Comparativo: Venezuela vs. países LATAM
- Composición: Exportaciones por sector
- Drill-down: Detalle por estado/región

#### Reflexión pedagógica

*¿Cómo enseña actualmente a sus estudiantes a "leer" gráficos económicos? ¿Les enseña también a crearlos y a criticarlos?*

### 5.2 Para docentes de Administración

#### Visualizaciones clave en administración

| Tipo de dato | Visualización recomendada | Ejemplo |
|--------------|---------------------------|---------|
| Ventas por producto | Barras, Treemap | Ingresos por línea de negocio |
| Embudo de conversión | Funnel | Lead → Oportunidad → Venta |
| Desempeño vs. meta | Bullet chart, Gauge | Ventas actual vs. objetivo |
| Portafolio | Matriz BCG (scatter) | Crecimiento vs. Participación |
| Proceso | Sankey | Flujo de clientes |

#### Dashboard ejemplo: Cuadro de Mando Integral (BSC)

Siguiendo la metodología de Kaplan y Norton:

```
┌─────────────────────────────────────────────────────────────┐
│  PERSPECTIVA FINANCIERA                                      │
│  [ROI actual: 12%]  [Margen: 25%]  [Crecimiento: 8%]         │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│  PERSPECTIVA CLIENTE                                         │
│  [NPS: 45]  [Retención: 85%]  [Satisfacción: 4.2/5]          │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│  PERSPECTIVA PROCESOS                                        │
│  [Eficiencia: 92%]  [Tiempo ciclo: 3.2 días]  [Calidad: 98%] │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│  PERSPECTIVA APRENDIZAJE                                     │
│  [Capacitación: 24h/año]  [Rotación: 8%]  [Innovación: 12]   │
└─────────────────────────────────────────────────────────────┘
```

#### Reflexión pedagógica

*¿Sus estudiantes aprenden a diseñar sistemas de indicadores, o solo a leer los que otros diseñaron? ¿Discuten las limitaciones de los KPIs tradicionales?*

### 5.3 Para docentes de Contaduría

#### Visualizaciones clave en contaduría

| Tipo de dato | Visualización recomendada | Ejemplo |
|--------------|---------------------------|---------|
| Estados financieros | Waterfall | De ingresos a utilidad neta |
| Estructura de costos | Treemap | Desglose de gastos |
| Ratios financieros | Bullet chart | Actual vs. benchmark |
| Tendencia de cuentas | Líneas | Evolución de pasivos |
| Composición | Barras apiladas | Activo circulante/no circulante |

#### Gráficos Waterfall (Cascada)

El gráfico de cascada es particularmente útil para mostrar cómo se llega de un valor a otro:

```
Ingresos totales         ████████████████████  $1,000,000
 (-) Costo de ventas     ██████████           ($400,000)
 = Margen bruto          ██████████████       $600,000
 (-) Gastos operativos   ████████             ($300,000)
 = EBITDA                ██████               $300,000
 (-) Depreciación        ██                   ($50,000)
 = EBIT                  █████                $250,000
 ...
```

#### Reflexión pedagógica

*¿Cómo podría la visualización hacer más accesible la interpretación de estados financieros para no contadores? ¿Qué visualizaciones usaría para presentar a un directorio?*

### 5.4 Para docentes de Relaciones Industriales

#### Visualizaciones clave en RRII

| Tipo de dato | Visualización recomendada | Ejemplo |
|--------------|---------------------------|---------|
| Encuestas Likert | Barras divergentes | Satisfacción por dimensión |
| Brecha salarial | Barras agrupadas | Salario por género/nivel |
| Rotación | Líneas + área | Tendencia de rotación |
| Estructura organizacional | Treemap | Empleados por área |
| Clima laboral | Radar/Spider | Dimensiones de clima |

#### Visualización de escalas Likert

Las escalas Likert (Muy de acuerdo → Muy en desacuerdo) se visualizan mejor con **barras divergentes**:

```
                    En desacuerdo ◄────┼────► De acuerdo
                                       │
"Me siento valorado"      ████████████│███████████████████
"Tengo oportunidades"     ██████████████│██████████████
"La comunicación es buena"███████████████████│██████████
"Mi jefe me apoya"        ██████████│████████████████████
```

El centro representa el punto neutro, facilitando ver dónde hay más acuerdo o desacuerdo.

#### Reflexión pedagógica

*¿Cómo enseña a sus estudiantes a presentar resultados de encuestas de manera que sean accionables, no solo descriptivos?*

---

## 6. Preguntas de Reflexión Metacognitiva

### 6.1 Antes de comenzar el módulo

1. Piense en la última presentación con datos que hizo. ¿Qué funcionó bien? ¿Qué mejoraría?

2. ¿Cuál es su reacción inicial ante herramientas como Power BI o Tableau? ¿Curiosidad, intimidación, escepticismo?

3. ¿Ha recibido alguna vez formación explícita en comunicación visual? ¿De dónde vienen sus "intuiciones" sobre diseño?

4. ¿Qué visualizaciones usa regularmente en su docencia? ¿Las crea usted o las toma de otros?

### 6.2 Durante el módulo

5. ¿Qué principio de visualización le ha resultado más revelador? ¿Por qué?

6. ¿Ha identificado algún gráfico que usa regularmente que podría mejorarse? ¿Cómo?

7. ¿Qué le resulta más desafiante: los aspectos técnicos (herramientas) o los conceptuales (diseño)?

8. ¿Ha notado visualizaciones problemáticas en noticias o redes sociales? ¿Cuáles?

### 6.3 Al finalizar el módulo

9. ¿Cómo ha cambiado su forma de "ver" gráficos y dashboards?

10. ¿Qué herramienta (Power BI, Tableau, otra) se siente más cómodo usando? ¿Por qué?

11. ¿Qué KPI diseñaría para medir el éxito de su propia asignatura?

12. ¿Cómo incorporará principios de storytelling en su próxima presentación con datos?

### 6.4 Diario de observación visual

Durante el módulo, mantenga un registro de visualizaciones que encuentre:

```
Fecha: _________
Fuente: (noticia, reporte, red social, etc.)
URL/Referencia: _________

Tipo de gráfico:

¿Qué intenta comunicar?

¿Qué funciona bien?

¿Qué problemas tiene?

¿Cómo lo mejoraría?

Captura/sketch:
```

---

## 7. Lecturas Fundamentales

### 7.1 Lectura obligatoria principal

**Knaflic, C. N. (2015). *Storytelling with Data: A Data Visualization Guide for Business Professionals*. Wiley.**

- **ISBN**: 978-1119002253
- **Páginas**: 288
- **Disponibilidad**: [Amazon](https://www.amazon.com/Storytelling-Data-Visualization-Business-Professionals/dp/1119002257) | Bibliotecas universitarias
- **Por qué es fundamental**: Este libro es LA referencia para comunicación efectiva con datos. Cole traduce principios de diseño y psicología cognitiva en guías prácticas y ejemplos concretos. Accesible para no diseñadores.
- **Capítulos prioritarios**: 2 (Elegir una visualización efectiva), 3 (Desorden es su enemigo), 5 (Piense como diseñador), 7 (Lecciones de storytelling)

### 7.2 Lectura obligatoria complementaria

**Few, S. (2012). *Show Me the Numbers: Designing Tables and Graphs to Enlighten* (2da edición). Analytics Press.**

- **ISBN**: 978-0970601971
- **Páginas**: 400
- **Disponibilidad**: [Amazon](https://www.amazon.com/Show-Me-Numbers-Designing-Enlighten/dp/0970601972)
- **Por qué es fundamental**: Stephen Few ofrece un tratamiento más técnico y exhaustivo que Knaflic. Excelente para entender el "por qué" detrás de las mejores prácticas.
- **Capítulos prioritarios**: 3 (Diferencias entre tablas y gráficos), 5 (Relaciones entre datos cuantitativos), 8 (Componentes gráficos)

### 7.3 Lectura recomendada

**Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2da edición). Graphics Press.**

- **ISBN**: 978-1930824133
- **Páginas**: 197
- **Disponibilidad**: [Amazon](https://www.amazon.com/Visual-Display-Quantitative-Information/dp/1930824130)
- **Por qué es importante**: Considerado el "libro sagrado" de la visualización de datos. Tufte es polémico pero influyente. Su concepto de "ratio dato-tinta" y sus ejemplos históricos son fundamentales para la alfabetización visual.

---

## 8. Lecturas Complementarias

### 8.1 Para profundizar en diseño visual

**Cairo, A. (2012). *The Functional Art: An Introduction to Information Graphics and Visualization*. New Riders.**

- **ISBN**: 978-0321834737
- **Relevancia**: Cairo, periodista y diseñador, ofrece una perspectiva desde la comunicación y el periodismo de datos. Excelente para entender visualización como comunicación.

**Ware, C. (2012). *Information Visualization: Perception for Design* (3ra edición). Morgan Kaufmann.**

- **ISBN**: 978-0123814647
- **Relevancia**: Tratamiento científico de la percepción visual aplicada a diseño. Más técnico, pero fundamental para entender por qué funcionan ciertos diseños.

### 8.2 Para profundizar en herramientas

**Ferrari, A., & Russo, M. (2019). *The Definitive Guide to DAX* (2da edición). Microsoft Press.**

- **ISBN**: 978-1509306978
- **Relevancia**: LA referencia para DAX en Power BI y Analysis Services. Necesario si quiere dominar Power BI más allá de lo básico.

**Murray, D., & Chabot, C. (2013). *Tableau Your Data!: Fast and Easy Visual Analysis with Tableau Software*. Wiley.**

- **ISBN**: 978-1118612040
- **Relevancia**: Guía práctica para Tableau. Los primeros capítulos son accesibles; los avanzados son útiles como referencia.

### 8.3 Para profundizar en KPIs y métricas

**Parmenter, D. (2015). *Key Performance Indicators: Developing, Implementing, and Using Winning KPIs* (3ra edición). Wiley.**

- **ISBN**: 978-1118925102
- **Relevancia**: Tratamiento exhaustivo de cómo diseñar sistemas de KPIs. Parmenter distingue entre KPIs verdaderos y otras métricas.

**Kaplan, R. S., & Norton, D. P. (1996). *The Balanced Scorecard: Translating Strategy into Action*. Harvard Business School Press.**

- **ISBN**: 978-0875846514
- **Relevancia**: El libro original del Balanced Scorecard. Aunque tiene más de 20 años, sigue siendo relevante para entender cómo conectar métricas con estrategia.

### 8.4 Artículos académicos clave

**Heer, J., & Shneiderman, B. (2012). Interactive dynamics for visual analysis. *Communications of the ACM*, 55(4), 45-54.**

- **DOI**: [10.1145/2133806.2133821](https://doi.org/10.1145/2133806.2133821)
- **Relevancia**: Marco conceptual para entender qué hace que las visualizaciones interactivas sean efectivas.

**Borland, D., & Taylor, R. M. (2007). Rainbow color map (still) considered harmful. *IEEE Computer Graphics and Applications*, 27(2), 14-17.**

- **DOI**: [10.1109/MCG.2007.323435](https://doi.org/10.1109/MCG.2007.323435)
- **Relevancia**: Por qué los mapas de calor "arcoíris" son problemáticos. Fundamental para elegir paletas de colores.

---

## 9. Recursos Multimedia

### 9.1 Videos esenciales

#### Serie: Storytelling with Data - Cole Nussbaumer Knaflic

- **URL**: [YouTube Channel](https://www.youtube.com/c/storytellingwithdata)
- **Descripción**: Cole tiene un canal con videos cortos que ilustran principios de su libro. Ideal para repasar conceptos.
- **Videos recomendados**: "What's wrong with this graph?", "The power of decluttering"

#### Serie: Guy in a Cube (Power BI)

- **URL**: [YouTube Channel](https://www.youtube.com/c/GuyinaCube)
- **Descripción**: Adam Saxton y Patrick LeBlanc (ambos de Microsoft) ofrecen tutoriales de Power BI. Desde básicos hasta avanzados.
- **Videos recomendados para principiantes**: "Power BI Tutorial for Beginners", "DAX 101"

#### Serie: Curbal (Power BI / DAX)

- **URL**: [YouTube Channel](https://www.youtube.com/c/Curbal)
- **Descripción**: Ruth Pozuelo ofrece tutoriales de Power BI con énfasis en DAX. Excelente para aprender fórmulas.

#### Charla: Hans Rosling - 200 Countries, 200 Years

- **URL**: [YouTube](https://www.youtube.com/watch?v=jbkSRLYSojo)
- **Duración**: 4 minutos
- **Por qué verla**: Masterclass de storytelling con datos en vivo. Rosling convierte estadísticas en drama.

#### Charla: David McCandless - The Beauty of Data Visualization

- **URL**: [TED](https://www.ted.com/talks/david_mccandless_the_beauty_of_data_visualization)
- **Duración**: 18 minutos
- **Por qué verla**: McCandless muestra cómo la visualización puede revelar patrones ocultos y contar historias.

### 9.2 Cursos online gratuitos

**Microsoft Learn - Power BI**

- **URL**: [learn.microsoft.com/power-bi](https://learn.microsoft.com/en-us/training/powerplatform/power-bi)
- **Descripción**: Módulos oficiales de Microsoft. Completos y actualizados. El path "Get started with Power BI" es ideal.

**Tableau e-Learning**

- **URL**: [elearning.tableau.com](https://elearning.tableau.com/)
- **Descripción**: Cursos oficiales de Tableau. Los básicos son gratuitos.

**Coursera: Data Visualization with Tableau**

- **URL**: [Coursera](https://www.coursera.org/specializations/data-visualization)
- **Descripción**: Especialización de UC Davis. Se puede auditar gratis.

### 9.3 Recursos de inspiración

**Information is Beautiful**

- **URL**: [informationisbeautiful.net](https://informationisbeautiful.net/)
- **Descripción**: Portafolio de David McCandless con visualizaciones hermosas y bien diseñadas. Excelente para inspiración.

**Flowing Data**

- **URL**: [flowingdata.com](https://flowingdata.com/)
- **Descripción**: Blog de Nathan Yau sobre visualización de datos. Mezcla tutoriales, críticas y ejemplos.

**Makeover Monday**

- **URL**: [makeovermonday.co.uk](https://www.makeovermonday.co.uk/)
- **Descripción**: Desafío semanal de rediseño de visualizaciones. Excelente para practicar y ver diferentes enfoques.

**Viz of the Day (Tableau Public)**

- **URL**: [public.tableau.com/app/discover/viz-of-the-day](https://public.tableau.com/app/discover/viz-of-the-day)
- **Descripción**: Visualización destacada cada día. Ideal para ver qué es posible con Tableau.

### 9.4 Herramientas complementarias

**Datawrapper**

- **URL**: [datawrapper.de](https://www.datawrapper.de/)
- **Descripción**: Herramienta web para crear visualizaciones rápidamente. Ideal para periodismo y reportes sencillos.

**Flourish**

- **URL**: [flourish.studio](https://flourish.studio/)
- **Descripción**: Herramienta web para visualizaciones animadas e interactivas. Fácil de usar.

**RAWGraphs**

- **URL**: [rawgraphs.io](https://rawgraphs.io/)
- **Descripción**: Herramienta open source para tipos de gráficos menos comunes (Alluvial, Beeswarm, etc.).

---

## 10. Actividades de Metaaprendizaje

### 10.1 Actividad: Crítica de visualización

**Objetivo**: Desarrollar ojo crítico para visualizaciones.

**Duración**: 45-60 minutos

**Instrucciones**:

1. Busque 3 visualizaciones de datos (noticias, informes, redes sociales).

2. Para cada una, analice usando esta rúbrica:

| Criterio | 1 (Pobre) | 2 | 3 | 4 | 5 (Excelente) |
|----------|-----------|---|---|---|---------------|
| ¿El tipo de gráfico es apropiado? | | | | | |
| ¿El mensaje es claro? | | | | | |
| ¿Hay desorden innecesario? | | | | | |
| ¿Los colores son efectivos? | | | | | |
| ¿Es honesta (no engañosa)? | | | | | |
| ¿Invita a la acción? | | | | | |

3. Para la peor visualización, diseñe (sketch a mano) una versión mejorada.

4. Comparta en grupo: ¿Qué patrones de errores encontraron?

### 10.2 Actividad: Rediseño antes/después

**Objetivo**: Practicar mejora de visualizaciones propias.

**Duración**: 60-90 minutos

**Instrucciones**:

1. Encuentre una visualización que haya creado en el pasado (para investigación, docencia, presentación).

2. Aplique los principios del módulo para rediseñarla:
   - ¿Es el tipo de gráfico correcto?
   - ¿Qué desorden puedo eliminar?
   - ¿Dónde enfocar la atención?
   - ¿Cuál es el mensaje central?

3. Cree la versión mejorada (en Power BI, Tableau, o herramienta de su elección).

4. Documente:
   - Versión original (captura)
   - Versión mejorada
   - Lista de cambios y por qué los hizo

### 10.3 Actividad: Diseño de KPIs

**Objetivo**: Aplicar framework SMART a su contexto.

**Duración**: 45-60 minutos

**Instrucciones**:

1. Seleccione una unidad a la que pertenece (asignatura, departamento, facultad).

2. Identifique 3 objetivos estratégicos de esa unidad.

3. Para cada objetivo, diseñe un KPI:

| Objetivo | KPI | S | M | A | R | T |
|----------|-----|---|---|---|---|---|
| | | ¿Específico? | ¿Medible? | ¿Alcanzable? | ¿Relevante? | ¿Temporal? |
| | | | | | | |

4. Para un KPI, especifique:
   - Fórmula exacta
   - Fuente de datos
   - Frecuencia de medición
   - Meta y umbrales (rojo/amarillo/verde)
   - Responsable

5. Reflexione: ¿Qué comportamientos incentivaría este KPI? ¿Podría tener efectos no deseados?

### 10.4 Actividad: Storytelling aplicado

**Objetivo**: Practicar la narrativa de datos.

**Duración**: 90-120 minutos

**Instrucciones**:

1. Usando datos del programa (datasets de FACES) o datos propios:

2. Construya una presentación de 5 minutos siguiendo la estructura:
   - Hook (dato sorprendente)
   - Contexto (situación actual)
   - Hallazgos (3 puntos clave)
   - Implicaciones (qué significa)
   - Llamado a la acción (qué hacer)

3. Límites:
   - Máximo 5 visualizaciones
   - Máximo 10 palabras por slide
   - Sin bullet points de texto

4. Presente a un colega o grábese.

5. Pida feedback específico:
   - ¿Cuál fue el mensaje principal?
   - ¿Qué visualización fue más efectiva?
   - ¿Qué acción tomarías?

### 10.5 Actividad: Dashboard personal de aprendizaje

**Objetivo**: Aplicar BI a su propio proceso de aprendizaje.

**Duración**: Tarea continua

**Instrucciones**:

1. Durante el programa, registre diariamente:
   - Horas dedicadas al estudio
   - Temas cubiertos
   - Nivel de comprensión (1-5)
   - Nivel de confianza (1-5)
   - Obstáculos encontrados

2. Cree un dashboard (en Power BI, Tableau, o Excel) que visualice:
   - Tendencia de tiempo dedicado
   - Distribución por tipo de actividad
   - Progreso de comprensión por módulo
   - Correlación tiempo vs. comprensión

3. Use el dashboard para reflexionar:
   - ¿Dónde necesito más tiempo?
   - ¿Qué temas requieren repaso?
   - ¿Mis estrategias están funcionando?

---

## 11. Glosario de Visualización

### Axis (Eje)
**Definición**: Línea de referencia en un gráfico que define la escala de medición.
**Tipos**: Eje X (horizontal, típicamente independiente), Eje Y (vertical, típicamente dependiente).
**Trampa común**: Truncar el eje Y para exagerar diferencias.

### Chart Junk
**Definición**: Elementos visuales que no contribuyen a la comprensión (término de Tufte).
**Ejemplos**: Fondos decorativos, efectos 3D gratuitos, iconos irrelevantes.
**Principio**: Eliminar chart junk mejora la claridad.

### Dashboard
**Definición**: Colección de visualizaciones relacionadas que ofrecen una vista consolidada de indicadores clave.
**Origen**: Analogía con el tablero de un automóvil.
**Trampa**: Un dashboard con todo es un dashboard de nada.

### Data Ink Ratio
**Definición**: Proporción de tinta usada para representar datos vs. tinta total (concepto de Tufte).
**Fórmula**: Tinta de datos / Tinta total.
**Meta**: Maximizar este ratio sin perder claridad.

### Drill-down
**Definición**: Capacidad de navegar de lo general a lo específico en una visualización.
**Ejemplo**: Clic en "Ventas totales" para ver ventas por región, luego por tienda.

### Encoding Visual
**Definición**: Manera en que los datos se representan visualmente.
**Tipos**: Posición, longitud, área, color, forma, ángulo.
**Efectividad**: Posición > Longitud > Área > Color > Forma

### Filter (Filtro)
**Definición**: Control que permite al usuario seleccionar subconjuntos de datos a visualizar.
**Tipos**: Slicers (Power BI), Filters (Tableau), Dropdown.

### KPI (Key Performance Indicator)
**Definición**: Métrica cuantificable que refleja factores críticos de éxito.
**Distinción**: No toda métrica es KPI; un KPI es estratégicamente importante.

### Legend (Leyenda)
**Definición**: Elemento que explica el significado de colores, formas u otros encodings.
**Mejor práctica**: Evitar leyenda si es posible etiquetando directamente.

### Measure vs. Dimension
**Definición**: Medidas son valores numéricos a agregar; dimensiones son categorías para segmentar.
**Ejemplo**: Ventas (medida) por Región (dimensión).

### Pre-attentive Attributes
**Definición**: Propiedades visuales procesadas antes de la atención consciente (<250ms).
**Ejemplos**: Color, tamaño, orientación, movimiento.

### Slicer
**Definición**: Tipo de filtro visual en Power BI que permite selección interactiva.

### Sparkline
**Definición**: Mini-gráfico de línea incrustado en texto o tabla, sin ejes ni etiquetas.
**Uso**: Mostrar tendencia en poco espacio (concepto de Tufte).

### Tooltip
**Definición**: Información emergente que aparece al pasar el cursor sobre un elemento.
**Mejor práctica**: Usar para detalles secundarios, no para información crítica.

### Treemap
**Definición**: Visualización que muestra jerarquías mediante rectángulos anidados, con área proporcional al valor.
**Uso**: Composición jerárquica (ej: presupuesto por área y sub-área).

---

## 12. Referencias Bibliográficas

### Referencias citadas en esta guía

Borland, D., & Taylor, R. M. (2007). Rainbow color map (still) considered harmful. *IEEE Computer Graphics and Applications*, 27(2), 14-17.

Cairo, A. (2012). *The Functional Art: An Introduction to Information Graphics and Visualization*. New Riders.

Few, S. (2012). *Show Me the Numbers: Designing Tables and Graphs to Enlighten* (2da edición). Analytics Press.

Few, S. (2013). *Information Dashboard Design: Displaying Data for At-a-Glance Monitoring* (2da edición). Analytics Press.

Heer, J., & Shneiderman, B. (2012). Interactive dynamics for visual analysis. *Communications of the ACM*, 55(4), 45-54.

Kaplan, R. S., & Norton, D. P. (1996). *The Balanced Scorecard: Translating Strategy into Action*. Harvard Business School Press.

Knaflic, C. N. (2015). *Storytelling with Data: A Data Visualization Guide for Business Professionals*. Wiley.

Parmenter, D. (2015). *Key Performance Indicators: Developing, Implementing, and Using Winning KPIs* (3ra edición). Wiley.

Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2da edición). Graphics Press.

Ware, C. (2012). *Information Visualization: Perception for Design* (3ra edición). Morgan Kaufmann.

### Referencias adicionales recomendadas

Cairo, A. (2019). *How Charts Lie: Getting Smarter about Visual Information*. W.W. Norton & Company.

Ferrari, A., & Russo, M. (2019). *The Definitive Guide to DAX* (2da edición). Microsoft Press.

Kirk, A. (2019). *Data Visualisation: A Handbook for Data Driven Design* (2da edición). SAGE Publications.

Knaflic, C. N. (2019). *Storytelling with Data: Let's Practice!*. Wiley.

Munzner, T. (2014). *Visualization Analysis and Design*. A K Peters/CRC Press.

Nussbaumer Knaflic, C. (2019). *Storytelling with Data: Let's Practice!*. Wiley.

Schwabish, J. (2021). *Better Data Visualizations: A Guide for Scholars, Researchers, and Wonks*. Columbia University Press.

Wexler, S., Shaffer, J., & Cotgreave, A. (2017). *The Big Book of Dashboards: Visualizing Your Data Using Real-World Business Scenarios*. Wiley.

Wong, D. M. (2010). *The Wall Street Journal Guide to Information Graphics*. W.W. Norton & Company.

Yau, N. (2011). *Visualize This: The FlowingData Guide to Design, Visualization, and Statistics*. Wiley.

---

## Nota Final

La visualización de datos es tanto ciencia como arte. La ciencia—psicología de la percepción, estadística, diseño de información—provee principios. El arte está en aplicar esos principios con sensibilidad al contexto, la audiencia y el mensaje.

Como docentes, ustedes tienen una ventaja única: entienden profundamente los dominios que visualizarán (economía, administración, contaduría, relaciones industriales). Las herramientas son medios; el conocimiento disciplinar es lo que hace que una visualización sea verdaderamente significativa.

*El objetivo no es impresionar con la complejidad, sino iluminar con la claridad.*

---

**Versión**: 1.0
**Fecha**: Marzo 2026
**Programa**: Formación Docente en Ciencia de Datos y BI - FACES UCAB
**Licencia**: CC BY-SA 4.0

