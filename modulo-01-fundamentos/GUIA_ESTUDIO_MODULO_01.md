# Guía de Estudio: Módulo 1 - Pensar con Datos en Ciencias Sociales

## Una invitación a la reflexión epistemológica sobre los datos

---

> *"El objetivo de la educación es mostrar a las personas cómo aprender por sí mismas. El otro concepto de educación es adoctrinamiento."*
> — Noam Chomsky

---

## Tabla de Contenidos

1. [Propósito y Relevancia del Módulo](#1-propósito-y-relevancia-del-módulo)
2. [Marco Epistemológico: ¿Qué significa "pensar con datos"?](#2-marco-epistemológico-qué-significa-pensar-con-datos)
3. [Conceptos Fundamentales](#3-conceptos-fundamentales)
4. [Metaaprendizaje: Reflexiones para el Docente](#4-metaaprendizaje-reflexiones-para-el-docente)
5. [Conexiones con la Práctica Docente](#5-conexiones-con-la-práctica-docente)
6. [Preguntas de Reflexión Metacognitiva](#6-preguntas-de-reflexión-metacognitiva)
7. [Lecturas Fundamentales](#7-lecturas-fundamentales)
8. [Lecturas Complementarias](#8-lecturas-complementarias)
9. [Recursos Multimedia](#9-recursos-multimedia)
10. [Actividades de Metaaprendizaje](#10-actividades-de-metaaprendizaje)
11. [Glosario Crítico](#11-glosario-crítico)
12. [Referencias Bibliográficas](#12-referencias-bibliográficas)

---

## 1. Propósito y Relevancia del Módulo

### 1.1 ¿Por qué comenzar pensando antes que haciendo?

Este módulo constituye el fundamento filosófico y epistemológico de todo el programa. Antes de manipular datos con Python, antes de construir dashboards en Power BI, antes de entrenar modelos predictivos, necesitamos desarrollar algo más fundamental: **una forma de pensar**.

La decisión de comenzar con un módulo conceptual no es arbitraria. Responde a una realidad preocupante en la enseñanza de ciencia de datos: demasiados cursos enseñan *cómo* ejecutar comandos sin enseñar *por qué* esos comandos importan, *cuándo* son apropiados, y *qué limitaciones* tienen.

Como docentes universitarios, ustedes están en una posición privilegiada y responsable: no solo aprenderán estas herramientas, sino que las transmitirán a futuras generaciones de profesionales. Por ello, es imperativo que desarrollen un **pensamiento crítico sobre los datos** antes de desarrollar competencias técnicas.

### 1.2 El contexto latinoamericano y venezolano

En nuestro contexto específico, pensar críticamente con datos adquiere una dimensión adicional. América Latina, y Venezuela en particular, enfrenta desafíos únicos:

- **Escasez de datos oficiales confiables**: La falta de censos actualizados, la discontinuidad de series estadísticas, y la politización de cifras oficiales.
- **Brecha digital y de acceso**: No todos los fenómenos sociales dejan rastros digitales, lo que puede sesgar nuestras conclusiones hacia poblaciones conectadas.
- **Colonialidad del conocimiento**: Muchas metodologías y herramientas fueron desarrolladas en contextos del Norte Global. Aplicarlas acríticamente puede ser problemático.

Este módulo les invita a cuestionar: ¿Qué significa "ser objetivo" cuando los datos mismos son construcciones sociales? ¿Cómo navegamos la tensión entre rigor metodológico y relevancia contextual?

### 1.3 Competencias que desarrollará

Al finalizar este módulo, habrá desarrollado:

| Competencia | Descripción | Nivel de dominio esperado |
|-------------|-------------|---------------------------|
| **Pensamiento estadístico** | Capacidad de razonar probabilísticamente y reconocer variabilidad | Intermedio |
| **Alfabetización de datos** | Habilidad para leer, interpretar y comunicar con datos | Intermedio |
| **Pensamiento crítico** | Identificación de sesgos, falacias y limitaciones | Avanzado |
| **Reflexión epistemológica** | Comprensión de cómo se construye conocimiento con datos | Introductorio |
| **Transferencia pedagógica** | Capacidad de enseñar estos conceptos a estudiantes | Introductorio |

---

## 2. Marco Epistemológico: ¿Qué significa "pensar con datos"?

### 2.1 Datos como construcciones sociales

Los datos no son hechos neutrales que esperan ser "descubiertos". Son **construidos** a través de decisiones humanas:

- **¿Qué se mide?** (y qué no)
- **¿Cómo se categoriza?** (las categorías son convenciones)
- **¿Quién tiene acceso?** (poder y datos están entrelazados)
- **¿Cuándo se recolecta?** (el timing importa)

Esta perspectiva, conocida como **constructivismo social de los datos**, nos recuerda que detrás de cada dataset hay personas tomando decisiones. Como señala Catherine D'Ignazio en *Data Feminism*:

> "Los datos no son un recurso natural que se extrae, sino un producto cultural que se fabrica."

**Reflexión para docentes**: Cuando enseñamos estadística o análisis de datos, ¿transmitimos la idea de que los datos son "objetivos" e incuestionables? ¿Cómo podríamos incorporar esta dimensión crítica en nuestras asignaturas?

### 2.2 El ciclo hermenéutico de los datos

Comprender datos implica un proceso interpretativo circular:

```
    Pregunta inicial
          ↓
    Recolección de datos
          ↓
    Análisis preliminar
          ↓
    Interpretación
          ↓
    Nuevas preguntas
          ↓
    (volver al inicio)
```

Este ciclo hermenéutico nos recuerda que el análisis de datos no es lineal. Nuestras preguntas iniciales moldean qué datos buscamos, y lo que encontramos reformula nuestras preguntas. No llegamos a "la verdad" definitiva, sino a **comprensiones cada vez más refinadas**.

### 2.3 Positivismo vs. Interpretativismo en ciencia de datos

Dos tradiciones epistemológicas compiten en cómo entendemos el análisis de datos:

| Aspecto | Positivismo | Interpretativismo |
|---------|-------------|-------------------|
| **Realidad** | Objetiva, medible | Socialmente construida |
| **Rol del investigador** | Observador neutral | Co-constructor del conocimiento |
| **Meta** | Leyes generalizables | Comprensión contextual |
| **Datos** | Hechos objetivos | Representaciones parciales |
| **Validez** | Replicabilidad, tamaño muestral | Coherencia, triangulación |

La ciencia de datos moderna tiende hacia el positivismo, pero las ciencias sociales han abrazado perspectivas más interpretativas. Como docentes en economía, administración y disciplinas afines, habitamos en esta tensión. Este módulo no busca resolverla, sino **hacerla explícita**.

---

## 3. Conceptos Fundamentales

### 3.1 El Ciclo de Valor de los Datos

#### Descripción del concepto

El ciclo de valor representa el viaje desde una pregunta hasta una acción informada:

**Pregunta → Datos → Análisis → Hallazgo → Acción**

Pero esta representación lineal es simplificada. En la práctica:

- Las preguntas se reformulan al ver los datos
- Los datos disponibles limitan qué preguntas podemos responder
- Los hallazgos pueden ser ignorados si contradicen intereses
- Las acciones generan nuevos datos que reinician el ciclo

#### Por qué importa para docentes

Como formadores, necesitamos enseñar a nuestros estudiantes que **el valor no está en los datos mismos, sino en su uso para tomar mejores decisiones**. Un dataset de millones de registros no tiene valor si nadie formula preguntas inteligentes sobre él.

**Trampa común**: Confundir acceso a datos con capacidad analítica. Tener muchos datos no garantiza mejores decisiones.

#### Conexión con su asignatura

Considere: ¿Qué decisiones toman los profesionales que usted forma? ¿Qué datos necesitarían para tomar esas decisiones de manera más informada?

### 3.2 Clasificación de Variables y Niveles de Medición

#### La escala de Stevens (1946)

Stanley Smith Stevens propuso cuatro niveles de medición que determinan qué operaciones estadísticas son válidas:

| Nivel | Definición | Ejemplo | Operaciones válidas |
|-------|------------|---------|---------------------|
| **Nominal** | Categorías sin orden | Carrera, género, país | Frecuencias, moda |
| **Ordinal** | Categorías ordenadas | Satisfacción (alta/media/baja), nivel educativo | + Mediana, percentiles |
| **Intervalo** | Distancias iguales, cero arbitrario | Temperatura °C, año calendario | + Media, desviación estándar |
| **Razón** | Cero absoluto | Ingreso, edad, peso | + Razones, coeficientes |

#### Crítica contemporánea

La clasificación de Stevens, aunque útil didácticamente, ha sido criticada:

- **Velleman y Wilkinson (1993)** argumentan que el nivel de medición no debe dictar mecánicamente el análisis apropiado.
- En la práctica, variables ordinales (como escalas Likert) frecuentemente se tratan como de intervalo, generando debates metodológicos.

#### Implicación pedagógica

Más que memorizar la clasificación, los estudiantes deben desarrollar **juicio sobre qué análisis es apropiado dado el significado sustantivo de las variables**. La regla no es "ordinal = mediana", sino "¿qué pregunta intento responder y qué supuestos estoy dispuesto a asumir?"

### 3.3 Sesgos Cognitivos y Analíticos

#### El sesgo de confirmación

Tendemos a buscar, interpretar y recordar información que confirma nuestras creencias preexistentes. En análisis de datos esto se manifiesta como:

- Seleccionar variables que "seguramente" serán significativas
- Interpretar resultados ambiguos en favor de la hipótesis
- No publicar o reportar resultados nulos

**Estudio clave**: Nickerson (1998) documentó extensivamente cómo el sesgo de confirmación opera en contextos científicos, incluyendo cómo investigadores reinterpretan datos contradictorios para preservar sus teorías.

#### Sesgo de selección

Ocurre cuando la muestra no representa la población de interés:

- **Sesgo de supervivencia**: Analizamos solo casos que "sobrevivieron" (empresas exitosas, estudiantes que no desertaron)
- **Autoselección**: Los voluntarios difieren de la población general
- **Sesgo de no respuesta**: Quienes no responden encuestas pueden ser sistemáticamente diferentes

**Ejemplo clásico**: Durante la Segunda Guerra Mundial, Abraham Wald demostró que los militares cometían sesgo de supervivencia al analizar daños en aviones que regresaban. Los aviones que no regresaron (los destruidos) no estaban en la muestra.

#### Causalidad espuria

Correlación no implica causalidad. Variables pueden correlacionarse por:

1. **Coincidencia**: Con suficientes variables, algunas correlacionarán por azar
2. **Variable confundente**: Un tercer factor causa ambas
3. **Causalidad inversa**: B causa A, no A causa B
4. **Causalidad genuina**: A realmente causa B

**Recurso memorable**: El sitio [Spurious Correlations](https://tylervigen.com/spurious-correlations) muestra correlaciones absurdas (ej: consumo de queso y muertes por enredo en sábanas) para ilustrar el peligro de inferir causalidad de correlación.

#### Falacia del fiscal (Base Rate Neglect)

Ignorar las tasas base al interpretar probabilidades condicionales. Si una prueba para detectar una condición rara tiene 99% de precisión, un resultado positivo no significa 99% de probabilidad de tener la condición.

**Aplicación en educación**: Si un modelo predice "deserción" con 90% de precisión, pero solo el 5% de estudiantes desertan, la mayoría de predicciones positivas serán falsos positivos.

### 3.4 Tipos de Análisis

#### Taxonomía de Gartner

| Tipo | Pregunta | Complejidad | Valor |
|------|----------|-------------|-------|
| **Descriptivo** | ¿Qué pasó? | Baja | Bajo |
| **Diagnóstico** | ¿Por qué pasó? | Media | Medio |
| **Predictivo** | ¿Qué pasará? | Alta | Alto |
| **Prescriptivo** | ¿Qué deberíamos hacer? | Muy alta | Muy alto |

#### Análisis exploratorio vs. confirmatorio

John Tukey (1977) distinguió entre:

- **Análisis Exploratorio (EDA)**: Buscar patrones sin hipótesis previas. "Dejar que los datos hablen."
- **Análisis Confirmatorio**: Probar hipótesis predefinidas con rigor estadístico.

**Problema frecuente**: Hacer EDA, encontrar un patrón, y luego "confirmar" esa hipótesis con los mismos datos. Esto es **HARKing** (Hypothesizing After Results are Known) y constituye mala práctica científica.

### 3.5 El problema de la replicabilidad

La "crisis de replicación" en ciencias sociales (y otras disciplinas) revela que muchos hallazgos publicados no se sostienen cuando se replican. Causas incluyen:

- **P-hacking**: Manipular análisis hasta obtener p < 0.05
- **Publicación sesgada**: Solo se publican resultados "significativos"
- **Tamaños muestrales insuficientes**
- **Hipótesis vagas que permiten múltiples interpretaciones**

**Estudio clave**: Open Science Collaboration (2015) intentó replicar 100 estudios de psicología publicados en revistas top. Solo 36% se replicaron exitosamente.

**Implicación para docentes**: Debemos enseñar a nuestros estudiantes no solo cómo obtener resultados, sino cómo obtener resultados **confiables y replicables**.

---

## 4. Metaaprendizaje: Reflexiones para el Docente

### 4.1 ¿Qué es el metaaprendizaje?

El metaaprendizaje es "aprender a aprender": la capacidad de reflexionar sobre nuestros propios procesos de aprendizaje, identificar qué estrategias funcionan para nosotros, y adaptar nuestro enfoque según el contexto.

Como docentes, el metaaprendizaje opera en dos niveles:

1. **Personal**: ¿Cómo estoy aprendiendo estos nuevos conceptos? ¿Qué me resulta difícil y por qué?
2. **Pedagógico**: ¿Cómo puedo facilitar el metaaprendizaje en mis estudiantes?

### 4.2 Reconociendo su punto de partida

Antes de avanzar, es valioso reflexionar sobre su relación actual con los datos:

**Inventario de creencias** (responda honestamente):

1. ¿Creo que los números son más "objetivos" que las palabras?
2. ¿Siento que las matemáticas/estadística "no son lo mío"?
3. ¿Asocio "ser bueno con datos" con ser "inteligente"?
4. ¿He evitado cursos o tareas que involucren análisis cuantitativo?
5. ¿Creo que los científicos de datos tienen "la verdad"?

Estas creencias, sean cuales sean sus respuestas, no son "correctas" o "incorrectas". Son su punto de partida. Reconocerlas es el primer paso para transformarlas si es necesario.

### 4.3 Ansiedad matemática y su abordaje

La **ansiedad matemática** es un fenómeno bien documentado que afecta a una proporción significativa de adultos, incluyendo profesionales altamente educados. Si usted la experimenta, sepa que:

1. **No es un reflejo de su inteligencia**. La ansiedad matemática es una respuesta emocional aprendida, frecuentemente originada en experiencias educativas negativas.

2. **Se puede superar**. La investigación de Jo Boaler (Stanford) demuestra que cambiar la mentalidad sobre las matemáticas puede transformar el desempeño, incluso en adultos.

3. **Este programa está diseñado para usted**. El enfoque conceptual antes que técnico busca precisamente construir confianza progresivamente.

**Referencia clave**: Ashcraft, M. H., & Moore, A. M. (2009). Mathematics anxiety and the affective drop in performance. *Journal of Psychoeducational Assessment*, 27(3), 197-205.

### 4.4 El síndrome del impostor

Muchos docentes que incursionan en ciencia de datos experimentan el **síndrome del impostor**: la sensación de no ser "suficientemente técnicos" para hablar de estos temas, de que serán "descubiertos" como fraudes.

Considere esto: **su experiencia disciplinar es invaluable**. Los científicos de datos "puros" frecuentemente carecen de comprensión profunda de los fenómenos sociales, económicos o administrativos que estudian. Usted aporta:

- Conocimiento del dominio (qué variables importan y por qué)
- Comprensión teórica (marcos para interpretar resultados)
- Juicio profesional (qué preguntas vale la pena responder)
- Sensibilidad ética (qué no debe hacerse con los datos)

**No está aprendiendo a ser científico de datos. Está ampliando su repertorio profesional.**

### 4.5 Transferencia de aprendizaje

Un objetivo clave de este módulo es que pueda **transferir** lo aprendido a su contexto docente. La transferencia no es automática; requiere esfuerzo deliberado.

Estrategias para facilitar la transferencia:

1. **Mientras aprende**: Pregúntese constantemente "¿Cómo se aplicaría esto en mi asignatura?"
2. **Busque analogías**: ¿Qué conceptos de su disciplina son análogos a estos?
3. **Diseñe mentalmente**: Imagine cómo enseñaría este tema a sus estudiantes
4. **Identifique obstáculos**: ¿Qué dificultades tendrían sus estudiantes? ¿Qué malentendidos serían comunes?

---

## 5. Conexiones con la Práctica Docente

### 5.1 Para docentes de Economía

#### Conceptos clave y su aplicación

| Concepto del módulo | Aplicación en Economía |
|---------------------|------------------------|
| Ciclo de valor de datos | Política económica basada en evidencia |
| Variables de razón | Indicadores macroeconómicos (PIB, inflación, desempleo) |
| Sesgo de selección | Encuestas económicas y representatividad |
| Series temporales | Datos económicos a través del tiempo |
| Causalidad espuria | Debates sobre política monetaria/fiscal |

#### Caso para reflexión

La **curva de Phillips** (relación inversa inflación-desempleo) pareció ser una "ley" económica en los años 60. La estanflación de los 70 la desafió. ¿Fue causalidad espuria? ¿Cambio estructural? ¿Variables omitidas?

Este caso ilustra cómo patrones empíricos pueden colapsar y por qué es importante enseñar humildad epistemológica.

#### Pregunta generadora

*¿Cómo enseña actualmente a sus estudiantes a distinguir entre correlación y causalidad en fenómenos económicos? ¿Podría incorporar ejercicios prácticos con datos reales?*

### 5.2 Para docentes de Administración

#### Conceptos clave y su aplicación

| Concepto del módulo | Aplicación en Administración |
|---------------------|------------------------------|
| Ciclo de valor de datos | Toma de decisiones gerenciales |
| KPIs | Indicadores de gestión |
| Sesgo de supervivencia | Estudios de empresas "exitosas" |
| Variables nominales/ordinales | Encuestas de clima organizacional |
| Pensamiento estadístico | Control de calidad, Six Sigma |

#### Caso para reflexión

Los libros de "buenas prácticas gerenciales" (como *In Search of Excellence* de Peters y Waterman) frecuentemente sufren de **sesgo de supervivencia**: estudian empresas exitosas e infieren qué las hizo exitosas, ignorando que empresas fracasadas pueden haber tenido las mismas características.

Phil Rosenzweig en *The Halo Effect* (2007) documenta este problema sistemáticamente.

#### Pregunta generadora

*¿Cuántos de los "casos de éxito" que utiliza en clase podrían estar afectados por sesgo de supervivencia? ¿Cómo podría complementarlos con "casos de fracaso"?*

### 5.3 Para docentes de Contaduría

#### Conceptos clave y su aplicación

| Concepto del módulo | Aplicación en Contaduría |
|---------------------|--------------------------|
| Variables de razón | Estados financieros, ratios |
| Precisión vs. exactitud | Diferencia entre registro contable y valor "real" |
| Sesgo de confirmación | Auditoría y detección de fraude |
| Ética de datos | Manipulación de reportes financieros |
| Niveles de medición | Valuación de activos |

#### Caso para reflexión

El escándalo de **Enron** (2001) ilustra cómo datos financieros pueden ser manipulados para crear una imagen falsa de la realidad. Los auditores de Arthur Andersen no carecían de datos; carecían de **independencia y pensamiento crítico**.

#### Pregunta generadora

*¿Enseña a sus estudiantes a cuestionar los números que reciben, o asumen que los estados financieros "dicen la verdad"? ¿Cómo podría incorporar escepticismo profesional desde el inicio?*

### 5.4 Para docentes de Relaciones Industriales

#### Conceptos clave y su aplicación

| Concepto del módulo | Aplicación en RRII |
|---------------------|---------------------|
| Variables ordinales | Escalas de satisfacción laboral |
| Sesgo de no respuesta | Encuestas de clima organizacional |
| Ética de datos | Privacidad de datos de empleados |
| Causalidad | ¿Satisfacción causa productividad o viceversa? |
| Análisis cualitativo vs. cuantitativo | Entrevistas vs. encuestas |

#### Caso para reflexión

Los famosos **estudios de Hawthorne** (1920s-1930s) que fundamentaron la escuela de relaciones humanas han sido criticados metodológicamente. El "efecto Hawthorne" mismo (las personas modifican su comportamiento al ser observadas) ilustra cómo la recolección de datos puede contaminar lo que se mide.

#### Pregunta generadora

*¿Cómo enseña a sus estudiantes a diseñar investigaciones sobre clima organizacional que minimicen sesgos de respuesta? ¿Discuten las limitaciones de los métodos que enseña?*

---

## 6. Preguntas de Reflexión Metacognitiva

### 6.1 Antes de comenzar el módulo

1. ¿Cuál es mi reacción emocional inicial ante la idea de "pensar con datos"? ¿Entusiasmo, ansiedad, indiferencia, escepticismo?

2. ¿Qué espero aprender en este módulo? ¿Qué necesito aprender?

3. ¿Cuál considero que es mi mayor fortaleza como pensador/analista? ¿Y mi mayor debilidad?

4. Si un estudiante me preguntara "¿por qué debería aprender sobre datos?", ¿qué le respondería hoy?

### 6.2 Durante el módulo

5. ¿Qué concepto me ha resultado más desafiante? ¿Por qué creo que es así?

6. ¿Qué conexión he encontrado entre estos conceptos y mi disciplina que no había considerado antes?

7. ¿En qué momento he sentido resistencia o incomodidad? ¿Qué podría estar causándola?

8. ¿Qué estrategia de aprendizaje me está funcionando mejor? ¿Cuál no?

### 6.3 Al finalizar el módulo

9. ¿Cómo ha cambiado mi comprensión de qué son los "datos"?

10. ¿Qué sesgo o falacia he reconocido en mi propio pensamiento o práctica docente?

11. ¿Qué concepto de este módulo definitivamente incorporaré en mi enseñanza?

12. ¿Qué pregunta me queda sin resolver que quiero explorar más adelante?

### 6.4 Registro de aprendizaje sugerido

Considere mantener un **diario de aprendizaje** durante el programa. No necesita ser extenso; una entrada breve después de cada sesión puede ser suficiente:

```
Fecha: _________
Sesión/Tema: _________

¿Qué aprendí hoy? (conceptos clave)

¿Qué me sorprendió o desafió?

¿Cómo se conecta con lo que ya sabía?

¿Cómo podría aplicarlo en mi enseñanza?

¿Qué preguntas me quedaron?
```

---

## 7. Lecturas Fundamentales

Las siguientes lecturas son **esenciales** para una comprensión profunda de los temas del módulo. Se recomienda leerlas en el orden presentado.

### 7.1 Lectura obligatoria principal

**Cairo, A. (2019). *How Charts Lie: Getting Smarter about Visual Information*. W.W. Norton & Company.**

- **ISBN**: 978-1324001560
- **Páginas**: 256
- **Disponibilidad**: [Amazon](https://www.amazon.com/How-Charts-Lie-Getting-Information/dp/1324001569) | Bibliotecas universitarias
- **Por qué es fundamental**: Cairo, profesor de visualización en University of Miami, ofrece una introducción accesible a cómo los gráficos pueden engañar—intencional o accidentalmente. Ideal para docentes sin formación estadística previa.
- **Capítulos prioritarios**: 1 (Cómo los gráficos funcionan), 4 (Cómo los gráficos mienten), 7 (Cómo los gráficos pueden hacernos más sabios)

### 7.2 Lectura obligatoria complementaria

**Rosling, H., Rosling, O., & Rosling Rönnlund, A. (2018). *Factfulness: Ten Reasons We're Wrong About the World—and Why Things Are Better Than You Think*. Flatiron Books.**

- **ISBN**: 978-1250107817
- **Páginas**: 352
- **Disponibilidad**: [Amazon](https://www.amazon.com/Factfulness-Reasons-World-Things-Better/dp/1250107814) | Ampliamente disponible
- **Por qué es fundamental**: Hans Rosling fue maestro en comunicar con datos. Este libro póstumo documenta los sesgos cognitivos sistemáticos que distorsionan nuestra comprensión del mundo y cómo los datos pueden corregirlos.
- **Capítulos prioritarios**: Introducción, Cap. 1 (Instinto de brecha), Cap. 10 (Instinto de urgencia)

### 7.3 Lectura recomendada: Perspectiva crítica

**O'Neil, C. (2016). *Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy*. Crown.**

- **ISBN**: 978-0553418811
- **Páginas**: 272
- **Disponibilidad**: [Amazon](https://www.amazon.com/Weapons-Math-Destruction-Increases-Inequality/dp/0553418815) | Bibliotecas universitarias
- **Por qué es importante**: Cathy O'Neil, matemática y científica de datos, documenta cómo algoritmos y modelos pueden perpetuar discriminación y desigualdad. Esencial para entender las dimensiones éticas de trabajar con datos.
- **Capítulos prioritarios**: Introducción, Cap. 1 (Metralla), Cap. 5 (Justicia encadenada)

---

## 8. Lecturas Complementarias

### 8.1 Para profundizar en pensamiento estadístico

**Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.**

- **ISBN**: 978-0374533557
- **Relevancia**: El psicólogo Nobel documenta décadas de investigación sobre sesgos cognitivos. Los capítulos sobre heurísticas y sesgos son particularmente relevantes para entender por qué interpretamos datos incorrectamente.
- **Acceso gratuito parcial**: [Resumen en Blinkist](https://www.blinkist.com/en/books/thinking-fast-and-slow-en) | PDF disponible en academia.edu

**Wheelan, C. (2013). *Naked Statistics: Stripping the Dread from the Data*. W.W. Norton & Company.**

- **ISBN**: 978-0393347777
- **Relevancia**: Introducción accesible y humorística a conceptos estadísticos. Ideal para quienes sienten ansiedad matemática.

### 8.2 Para profundizar en ética de datos

**D'Ignazio, C., & Klein, L. F. (2020). *Data Feminism*. MIT Press.**

- **ISBN**: 978-0262044004
- **Relevancia**: Propone examinar ciencia de datos a través de una perspectiva feminista, cuestionando quién tiene poder para definir, recolectar y usar datos.
- **Acceso gratuito**: [Versión completa online](https://data-feminism.mitpress.mit.edu/)

**Zuboff, S. (2019). *The Age of Surveillance Capitalism*. PublicAffairs.**

- **ISBN**: 978-1610395694
- **Relevancia**: Análisis exhaustivo de cómo empresas tecnológicas extraen y monetizan datos personales. Importante para entender el contexto económico-político de los "datos".

### 8.3 Para el contexto latinoamericano

**Calderón, F., & Castells, M. (2019). *The New Latin America*. Polity Press.**

- **ISBN**: 978-1509537471
- **Relevancia**: Análisis de transformaciones sociales en América Latina. Capítulos sobre desigualdad y tecnología proveen contexto para análisis de datos en la región.

**CEPAL (2021). *Datos y hechos sobre la transformación digital*. Naciones Unidas.**

- **Acceso gratuito**: [Repositorio CEPAL](https://www.cepal.org/es/publicaciones)
- **Relevancia**: Estadísticas y análisis sobre digitalización en América Latina. Datos oficiales para contextualizar ejercicios.

### 8.4 Artículos académicos clave

**Nickerson, R. S. (1998). Confirmation bias: A ubiquitous phenomenon in many guises. *Review of General Psychology*, 2(2), 175-220.**

- **DOI**: [10.1037/1089-2680.2.2.175](https://doi.org/10.1037/1089-2680.2.2.175)
- **Relevancia**: Artículo seminal sobre sesgo de confirmación. Documenta cómo opera en contextos científicos y cotidianos.

**Open Science Collaboration. (2015). Estimating the reproducibility of psychological science. *Science*, 349(6251), aac4716.**

- **DOI**: [10.1126/science.aac4716](https://doi.org/10.1126/science.aac4716)
- **Relevancia**: El estudio que catalizó la "crisis de replicación". Demuestra que muchos hallazgos publicados no se replican.

**Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). False-positive psychology: Undisclosed flexibility in data collection and analysis allows presenting anything as significant. *Psychological Science*, 22(11), 1359-1366.**

- **DOI**: [10.1177/0956797611417632](https://doi.org/10.1177/0956797611417632)
- **Relevancia**: Artículo influyente que demuestra cómo pequeñas decisiones analíticas (grados de libertad del investigador) pueden producir cualquier resultado deseado.

---

## 9. Recursos Multimedia

### 9.1 Videos esenciales

#### Charla TED: Hans Rosling - "The best stats you've ever seen" (2006)

- **Duración**: 20 minutos
- **URL**: [TED.com](https://www.ted.com/talks/hans_rosling_the_best_stats_you_ve_ever_seen)
- **Por qué verla**: Rosling demuestra cómo visualización y narrativa pueden hacer que los datos cobren vida. Una masterclass en comunicación con datos.

#### Documental BBC: "The Joy of Stats" (2010)

- **Duración**: 60 minutos
- **Disponibilidad**: [YouTube](https://www.youtube.com/results?search_query=joy+of+stats+hans+rosling)
- **Por qué verlo**: Hans Rosling presenta la estadística como herramienta para entender el mundo. Accesible y entusiasta.

#### Curso completo: "Calling Bullshit" - University of Washington

- **Duración**: 16 clases (1 hora cada una)
- **URL**: [callingbullshit.org](https://www.callingbullshit.org/videos.html)
- **Por qué verlo**: Carl Bergstrom y Jevin West enseñan a detectar manipulación con datos y estadísticas. El curso completo está disponible gratuitamente.
- **Clases prioritarias**: 1 (Introducción), 2 (Naturaleza del bullshit), 6 (Visualización de datos), 10 (Big Data)

#### 3Blue1Brown: "Bayes theorem, the geometry of changing beliefs"

- **Duración**: 15 minutos
- **URL**: [YouTube](https://www.youtube.com/watch?v=HZGCoVF3YvM)
- **Por qué verlo**: Grant Sanderson explica el teorema de Bayes visualmente. Fundamental para entender probabilidad condicional.

### 9.2 Podcasts recomendados

**"More or Less: Behind the Statistics" - BBC Radio 4**

- **Frecuencia**: Semanal
- **URL**: [BBC](https://www.bbc.co.uk/programmes/b006qshd)
- **Descripción**: Tim Harford examina estadísticas en las noticias. Cada episodio es una lección en pensamiento crítico con datos.

**"Data Skeptic"**

- **Frecuencia**: Semanal
- **URL**: [dataskeptic.com](https://dataskeptic.com/)
- **Descripción**: Mezcla de episodios introductorios y entrevistas técnicas. Los "mini-episodios" son particularmente accesibles.

### 9.3 Recursos interactivos

**Seeing Theory - Brown University**

- **URL**: [seeing-theory.brown.edu](https://seeing-theory.brown.edu/)
- **Descripción**: Visualizaciones interactivas de conceptos de probabilidad y estadística. Ideal para desarrollar intuición.

**Gapminder Tools**

- **URL**: [gapminder.org/tools](https://www.gapminder.org/tools/)
- **Descripción**: La herramienta que usaba Hans Rosling. Permite explorar indicadores mundiales interactivamente.

**Our World in Data**

- **URL**: [ourworldindata.org](https://ourworldindata.org/)
- **Descripción**: Repositorio de datos y visualizaciones sobre problemas globales. Excelente fuente de ejemplos contextualizados.

**Spurious Correlations**

- **URL**: [tylervigen.com/spurious-correlations](https://tylervigen.com/spurious-correlations)
- **Descripción**: Colección humorística de correlaciones absurdas. Útil para enseñar por qué correlación ≠ causalidad.

---

## 10. Actividades de Metaaprendizaje

### 10.1 Actividad: Auditoría de creencias

**Objetivo**: Hacer explícitas las creencias previas sobre datos y análisis.

**Duración**: 30-45 minutos

**Instrucciones**:

1. Complete las siguientes oraciones sin pensar demasiado (respuestas instintivas):
   - "Los números son más confiables que las opiniones porque..."
   - "Los científicos de datos saben la verdad porque..."
   - "Si un estudio tiene una muestra grande, entonces..."
   - "Los datos no mienten, pero..."
   - "Mi asignatura no necesita más datos porque..."

2. Revise sus respuestas. ¿Qué supuestos revelan?

3. Para cada supuesto identificado, formule una contra-pregunta. Por ejemplo:
   - Supuesto: "Los números son objetivos"
   - Contra-pregunta: "¿Quién decidió qué medir y cómo?"

4. Conserve este ejercicio para comparar sus creencias al final del programa.

### 10.2 Actividad: Caza de sesgos

**Objetivo**: Identificar sesgos en análisis de datos que encuentra en su vida cotidiana.

**Duración**: Tarea continua durante el módulo

**Instrucciones**:

1. Durante una semana, recolecte ejemplos de "datos" que encuentre en:
   - Noticias
   - Redes sociales
   - Conversaciones profesionales
   - Materiales de su asignatura

2. Para cada ejemplo, analice:
   - ¿Qué sesgo podría estar presente?
   - ¿Qué información falta?
   - ¿Qué conclusión diferente podría sacarse?

3. Documente al menos 5 ejemplos con su análisis.

4. Seleccione el ejemplo más ilustrativo para compartir con el grupo.

### 10.3 Actividad: Traducción disciplinar

**Objetivo**: Conectar conceptos del módulo con su práctica docente específica.

**Duración**: 60-90 minutos

**Instrucciones**:

1. Seleccione una asignatura que imparte regularmente.

2. Para cada concepto principal del módulo, complete:

| Concepto | Ejemplo en mi asignatura | Cómo lo enseño actualmente | Cómo podría mejorarlo |
|----------|--------------------------|---------------------------|----------------------|
| Ciclo de valor | | | |
| Tipos de variables | | | |
| Sesgo de confirmación | | | |
| Sesgo de selección | | | |
| Causalidad vs. correlación | | | |
| Tipos de análisis | | | |

3. Identifique: ¿Hay conceptos que nunca ha enseñado explícitamente? ¿Por qué?

4. Diseñe una actividad breve (15-20 min) que pudiera incorporar en su próximo semestre para enseñar uno de estos conceptos.

### 10.4 Actividad: Diálogo con un escéptico

**Objetivo**: Fortalecer la argumentación sobre la importancia del pensamiento con datos.

**Duración**: 20-30 minutos (o roleplay con colega)

**Instrucciones**:

Imagine (o realice con un colega) un diálogo con un "escéptico" que presenta las siguientes objeciones. Formule respuestas fundamentadas:

1. **"Los datos son manipulables, así que no podemos confiar en ningún análisis."**
   - Su respuesta: _______________

2. **"En mi disciplina trabajamos con teorías, no con datos."**
   - Su respuesta: _______________

3. **"Big Data es solo una moda. En cinco años nadie hablará de esto."**
   - Su respuesta: _______________

4. **"Mis estudiantes no necesitan saber de datos, necesitan saber de [su disciplina]."**
   - Su respuesta: _______________

5. **"Ya tenemos suficiente con Excel. ¿Para qué aprender Python?"**
   - Su respuesta: _______________

### 10.5 Actividad: Carta a usted mismo

**Objetivo**: Crear un ancla temporal para evaluar su progreso.

**Duración**: 15-20 minutos

**Instrucciones**:

1. Escriba una carta breve (1 página) dirigida a usted mismo, para ser leída al finalizar el programa completo.

2. Incluya:
   - Sus expectativas actuales
   - Sus miedos o preocupaciones
   - Lo que espera haber aprendido
   - Lo que espera estar haciendo diferente en su docencia

3. Selle la carta (física o digitalmente) y no la abra hasta la última sesión del programa.

4. Al final, compare sus expectativas iniciales con su experiencia real.

---

## 11. Glosario Crítico

Este glosario no solo define términos, sino que invita a problematizarlos.

### Alfabetización de datos (Data Literacy)
**Definición**: Capacidad de leer, interpretar, crear y comunicar con datos.
**Problematización**: ¿Es suficiente la "alfabetización" o necesitamos "fluidez"? ¿Quién define qué cuenta como alfabetización? ¿Se trata de habilidades técnicas o también de postura crítica?

### Análisis Exploratorio de Datos (EDA)
**Definición**: Enfoque de análisis que enfatiza la visualización y resumen de datos sin hipótesis previas, popularizado por John Tukey.
**Problematización**: ¿Es realmente posible explorar datos "sin hipótesis"? ¿Nuestros marcos previos no condicionan qué "vemos"?

### Big Data
**Definición**: Conjuntos de datos demasiado grandes o complejos para ser procesados con métodos tradicionales.
**Problematización**: El término se ha vuelto un buzzword que frecuentemente obscurece más de lo que aclara. Muchas aplicaciones de "big data" funcionarían igual con datos más pequeños y mejor curados.

### Causalidad
**Definición**: Relación donde un evento (causa) produce otro (efecto).
**Problematización**: Establecer causalidad es extremadamente difícil fuera de experimentos controlados. La mayoría de análisis de datos solo establecen asociaciones.

### Correlación
**Definición**: Medida estadística de la relación lineal entre dos variables.
**Problematización**: "Correlación no implica causalidad" es un mantra repetido pero frecuentemente ignorado en la práctica.

### Dato
**Definición**: Representación simbólica de un atributo de una entidad.
**Problematización**: Los datos no son "hechos brutos" sino construcciones que resultan de decisiones sobre qué medir, cómo categorizar y qué registrar. El origen etimológico (latín *datum* = "lo dado") es engañoso.

### Objetividad
**Definición**: Calidad de juicios basados en hechos observables, independientes del observador.
**Problematización**: La "objetividad" absoluta es un ideal inalcanzable. Mejor hablar de intersubjetividad (acuerdo entre observadores) y transparencia metodológica.

### P-hacking
**Definición**: Práctica de manipular análisis hasta obtener resultados estadísticamente significativos (p < 0.05).
**Problematización**: Refleja incentivos perversos en la academia. La búsqueda de "significancia" puede producir hallazgos espurios.

### Sesgo
**Definición**: Desviación sistemática de la verdad o de un estándar.
**Problematización**: Todos tenemos sesgos; el objetivo no es eliminarlos (imposible) sino hacerlos explícitos y mitigar sus efectos.

### Variable
**Definición**: Característica medible que puede tomar diferentes valores.
**Problematización**: La clasificación de variables (nominal, ordinal, intervalo, razón) es útil pero no debe aplicarse mecánicamente. El significado sustantivo importa.

---

## 12. Referencias Bibliográficas

### Referencias citadas en esta guía

Ashcraft, M. H., & Moore, A. M. (2009). Mathematics anxiety and the affective drop in performance. *Journal of Psychoeducational Assessment*, 27(3), 197-205. https://doi.org/10.1177/0734282908330580

Bergstrom, C. T., & West, J. D. (2020). *Calling Bullshit: The Art of Skepticism in a Data-Driven World*. Random House.

Cairo, A. (2019). *How Charts Lie: Getting Smarter about Visual Information*. W.W. Norton & Company.

D'Ignazio, C., & Klein, L. F. (2020). *Data Feminism*. MIT Press. https://data-feminism.mitpress.mit.edu/

Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.

Nickerson, R. S. (1998). Confirmation bias: A ubiquitous phenomenon in many guises. *Review of General Psychology*, 2(2), 175-220. https://doi.org/10.1037/1089-2680.2.2.175

O'Neil, C. (2016). *Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy*. Crown.

Open Science Collaboration. (2015). Estimating the reproducibility of psychological science. *Science*, 349(6251), aac4716. https://doi.org/10.1126/science.aac4716

Rosenzweig, P. (2007). *The Halo Effect: ... and the Eight Other Business Delusions That Deceive Managers*. Free Press.

Rosling, H., Rosling, O., & Rosling Rönnlund, A. (2018). *Factfulness: Ten Reasons We're Wrong About the World—and Why Things Are Better Than You Think*. Flatiron Books.

Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). False-positive psychology: Undisclosed flexibility in data collection and analysis allows presenting anything as significant. *Psychological Science*, 22(11), 1359-1366. https://doi.org/10.1177/0956797611417632

Stevens, S. S. (1946). On the theory of scales of measurement. *Science*, 103(2684), 677-680.

Tukey, J. W. (1977). *Exploratory Data Analysis*. Addison-Wesley.

Velleman, P. F., & Wilkinson, L. (1993). Nominal, ordinal, interval, and ratio typologies are misleading. *The American Statistician*, 47(1), 65-72.

Wheelan, C. (2013). *Naked Statistics: Stripping the Dread from the Data*. W.W. Norton & Company.

### Referencias adicionales recomendadas

Bergstrom, C. T., & West, J. D. (2021). The case for motivated reasoning. *Proceedings of the National Academy of Sciences*, 118(13), e2102505118.

Best, J. (2001). *Damned Lies and Statistics: Untangling Numbers from the Media, Politicians, and Activists*. University of California Press.

Bowker, G. C., & Star, S. L. (1999). *Sorting Things Out: Classification and Its Consequences*. MIT Press.

Huff, D. (1954). *How to Lie with Statistics*. W.W. Norton & Company.

Ioannidis, J. P. A. (2005). Why most published research findings are false. *PLOS Medicine*, 2(8), e124. https://doi.org/10.1371/journal.pmed.0020124

Mayer-Schönberger, V., & Cukier, K. (2013). *Big Data: A Revolution That Will Transform How We Live, Work, and Think*. Houghton Mifflin Harcourt.

Pearl, J., & Mackenzie, D. (2018). *The Book of Why: The New Science of Cause and Effect*. Basic Books.

Silver, N. (2012). *The Signal and the Noise: Why So Many Predictions Fail—But Some Don't*. Penguin Press.

Spiegelhalter, D. (2019). *The Art of Statistics: How to Learn from Data*. Basic Books.

Zuboff, S. (2019). *The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier of Power*. PublicAffairs.

---

## Nota Final

Esta guía de estudio está diseñada para ser un **compañero de viaje**, no un texto para memorizar. Los conceptos aquí presentados cobran sentido cuando se aplican, se cuestionan y se conectan con su experiencia.

Como docente, usted no solo está aprendiendo sobre datos: está modelando para sus futuros estudiantes lo que significa ser un **aprendiz permanente**. Su disposición a explorar territorios nuevos, a admitir lo que no sabe, y a reflexionar sobre su propio aprendizaje es, en sí misma, una lección poderosa.

*Pensar con datos es un viaje, no un destino.*

---

**Versión**: 1.0
**Fecha**: Marzo 2026
**Programa**: Formación Docente en Ciencia de Datos y BI - FACES UCAB
**Licencia**: CC BY-SA 4.0

