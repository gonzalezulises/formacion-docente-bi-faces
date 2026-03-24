# Módulo Complementario — IA aplicada al análisis de datos

![Tipo](https://img.shields.io/badge/tipo-opcional-lightgrey)
![Modalidad](https://img.shields.io/badge/modalidad-asincrónico-blue)
![Duración](https://img.shields.io/badge/duración_estimada-3_horas-green)

![ChatGPT](https://img.shields.io/badge/ChatGPT-74aa9c?style=flat-square&logo=openai&logoColor=white)
![Claude](https://img.shields.io/badge/Claude-d4a574?style=flat-square&logo=anthropic&logoColor=white)
![GitHub Copilot](https://img.shields.io/badge/GitHub_Copilot-000?style=flat-square&logo=githubcopilot&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Gemini-4285F4?style=flat-square&logo=google&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

---

## Descripción

Este módulo es **opcional y asincrónico**. Explora cómo la inteligencia artificial generativa puede integrarse al flujo de trabajo de análisis de datos que se desarrolla a lo largo del programa.

No reemplaza el pensamiento crítico ni las habilidades analíticas — las amplifica. El objetivo es que cada docente entienda **qué puede hacer la IA por su análisis, qué no puede, y cómo usarla de forma responsable** en el contexto académico.

**Este módulo complementa los Módulos 1-4. Puedes consumirlo en cualquier momento del programa.**

---

## Objetivos de aprendizaje

Al completar este módulo, el participante será capaz de:

1. Entender qué es la IA generativa y cómo se diferencia del machine learning tradicional
2. Usar herramientas de IA como asistente para tareas de análisis de datos (limpieza, exploración, visualización)
3. Escribir prompts efectivos para obtener código Python, interpretaciones y sugerencias analíticas
4. Identificar las limitaciones y riesgos de depender de IA en el análisis de datos
5. Aplicar un marco ético para el uso de IA en la docencia e investigación universitaria

---

## Contenido

### 1. ¿Qué es la IA generativa y por qué importa en datos?

La IA generativa (ChatGPT, Claude, Gemini, Copilot) puede generar código, interpretar resultados y sugerir análisis. Pero no "entiende" los datos — predice texto probable.

**Conceptos clave:**
- LLMs (Large Language Models): qué son y cómo funcionan a alto nivel
- Diferencia entre IA generativa y machine learning predictivo (Módulo 4)
- El rol de la IA: asistente, no analista
- Por qué la IA necesita contexto de dominio — exactamente lo que ustedes tienen

**Analogía para docentes:** La IA es como un asistente de investigación muy rápido que lee todo pero no entiende nada. Tú pones el criterio, el contexto y la pregunta correcta.

---

### 2. IA en el flujo de análisis de datos

Dónde encaja la IA en el flujo que aprendimos en el Módulo 1:

| Fase del flujo | Sin IA | Con IA como asistente |
|----------------|--------|----------------------|
| **Import** | Escribir código de carga manualmente | "Genera código para cargar este CSV con encoding latin-1" |
| **Tidy** | Detectar problemas fila por fila | "Identifica columnas con más del 30% de valores faltantes" |
| **Transform** | Consultar documentación de pandas | "Crea una columna 'grupo_edad' a partir de 'edad' con estos rangos" |
| **Visualize** | Elegir gráfico por prueba y error | "¿Qué gráfico es más adecuado para comparar distribuciones entre 3 grupos?" |
| **Model** | Escribir pipeline completo | "Genera un modelo de regresión logística para predecir deserción" |
| **Communicate** | Redactar interpretación desde cero | "Resume estos hallazgos en 3 bullets para un informe ejecutivo" |

**Regla de oro:** La IA genera el borrador, tú validas con tu conocimiento de dominio.

---

### 3. Prompting efectivo para análisis de datos

Un buen prompt tiene 4 componentes:

1. **Rol:** "Eres un analista de datos educativos"
2. **Contexto:** "Tengo un dataset con 2,847 registros de estudiantes de FACES con columnas: promedio, asistencia, carrera, turno"
3. **Tarea:** "Genera código Python para calcular la tasa de deserción por carrera y turno"
4. **Formato:** "Usa pandas y muestra el resultado como tabla formateada"

#### Ejemplos aplicados al programa

**Exploración de datos (Módulo 2):**
```
Tengo un DataFrame llamado df con columnas: estudiante_id, carrera,
promedio_1er_trim, asistencia_pct, trabaja, turno, deserto.
Genera código pandas para:
1. Estadísticas descriptivas por carrera
2. Tabla cruzada de deserción por turno
3. Identificar columnas con valores faltantes
```

**Visualización (Módulo 3):**
```
Con el DataFrame anterior, genera código matplotlib/seaborn para:
1. Boxplot de promedio por carrera, coloreado por deserción
2. Heatmap de correlación entre variables numéricas
Usa estilo profesional con títulos en español.
```

**Interpretación (todos los módulos):**
```
Estos son los resultados de mi análisis:
- Promedio < 10 en 1er trimestre → 3× más riesgo de deserción
- Asistencia < 60% multiplica el riesgo por 2.1×
- Trabajar NO fue significativo (p=0.34)

Soy docente de Economía en FACES-UCAB. Ayúdame a:
1. Interpretar estos resultados para el Consejo de Escuela
2. Sugerir 3 acciones concretas basadas en la evidencia
```

---

### 4. Lo que la IA NO puede hacer por ti

| La IA puede | La IA NO puede |
|-------------|----------------|
| Generar código rápidamente | Garantizar que el código es correcto |
| Sugerir tipos de análisis | Saber si el análisis responde TU pregunta |
| Limpiar datos con instrucciones | Detectar sesgos en la recolección |
| Producir visualizaciones | Juzgar si el gráfico es honesto |
| Resumir hallazgos | Entender el contexto institucional |
| Citar fuentes (a veces inventadas) | Verificar que las fuentes existen |

**Riesgos específicos en análisis de datos:**
- **Alucinaciones estadísticas:** la IA puede inventar p-values, coeficientes o interpretaciones
- **Sesgo de confirmación amplificado:** si le pides que confirme tu hipótesis, lo hará
- **Código plausible pero incorrecto:** el código puede ejecutarse sin errores pero calcular algo diferente a lo que pediste
- **Pérdida de aprendizaje:** si la IA hace todo, no desarrollas intuición analítica

**Antídoto:** Siempre ejecuta el código, verifica los números, y pregúntate: "¿Esto tiene sentido con lo que sé de mi contexto?"

---

### 5. Marco ético para IA en la academia

#### Principios para docentes-investigadores

1. **Transparencia:** Si usaste IA, repórtalo. En qué etapa, para qué tarea, qué herramienta
2. **Verificación:** Todo output de IA debe ser verificado antes de incluirlo en un trabajo
3. **Propiedad intelectual:** El análisis y las conclusiones son tuyas, no de la IA
4. **Equidad:** No todos los estudiantes tienen el mismo acceso a herramientas de IA
5. **Desarrollo de competencias:** La IA complementa, no reemplaza, el aprendizaje

#### ¿Cuándo SÍ usar IA en el programa?

- Para generar borradores de código que luego modificas y entiendes
- Para explorar enfoques alternativos de análisis
- Para traducir una idea en prosa a código ejecutable
- Para depurar errores en tu código
- Para obtener explicaciones de conceptos que no quedaron claros

#### ¿Cuándo NO usar IA en el programa?

- Para entregar código que no entiendes
- Para generar interpretaciones que no has validado con los datos
- Para "inventar" datos o resultados
- Como sustituto de pensar tu pregunta analítica (Módulo 1)

---

## Recursos de video

### IA generativa — Fundamentos

| Video | Duración | Tema |
|-------|:--------:|------|
| [¿Qué es ChatGPT y cómo funciona? — DotCSV](https://www.youtube.com/watch?v=oFfVt3S51T4) | 15 min | Explicación clara de LLMs para no técnicos |
| [How AI Could Empower Any Business — Andrew Ng (TED)](https://www.youtube.com/watch?v=reUZRyXxUs4) | 18 min | Visión práctica de IA en organizaciones |
| [Intro to Large Language Models — Andrej Karpathy](https://www.youtube.com/watch?v=zjkBMFhNj_g) | 60 min | Explicación técnica accesible del funcionamiento de LLMs |

### IA para análisis de datos

| Video | Duración | Tema |
|-------|:--------:|------|
| [Data Analysis with ChatGPT — Luke Barousse](https://www.youtube.com/watch?v=4VfAK8ezEKk) | 25 min | Flujo práctico de análisis con IA |
| [Claude for Data Science — Anthropic](https://www.youtube.com/watch?v=Aw-rrVraEBk) | 12 min | Uso de Claude para análisis de datos |
| [AI-Powered EDA — Ken Jee](https://www.youtube.com/watch?v=C75TROiiEa0) | 20 min | Análisis exploratorio asistido por IA |

### Ética y limitaciones

| Video | Duración | Tema |
|-------|:--------:|------|
| [The Danger of AI in Research — Sabine Hossenfelder](https://www.youtube.com/watch?v=sByHaN8oNHE) | 15 min | Riesgos de IA en investigación científica |
| [AI Won't Replace Data Analysts — Alex The Analyst](https://www.youtube.com/watch?v=3cMhgsNPy0M) | 10 min | Por qué el criterio humano sigue siendo esencial |

---

## Herramientas recomendadas

| Herramienta | Acceso | Uso principal |
|-------------|--------|---------------|
| [ChatGPT](https://chat.openai.com/) | Gratuito (GPT-3.5) / Pago (GPT-4) | Generación de código, explicaciones, interpretación |
| [Claude](https://claude.ai/) | Gratuito (limitado) / Pago | Análisis de documentos largos, razonamiento detallado |
| [Google Gemini](https://gemini.google.com/) | Gratuito con cuenta Google | Integración con Google Workspace y Colab |
| [GitHub Copilot](https://github.com/features/copilot) | Gratuito para estudiantes y docentes | Autocompletado de código en el editor |
| [Julius AI](https://julius.ai/) | Gratuito (limitado) | Análisis de datos con interfaz visual + IA |

---

## Checklist de exploración

No es evaluativo — es para que explores a tu ritmo:

- [ ] Abre ChatGPT, Claude o Gemini y pídele que explique qué es un DataFrame de pandas
- [ ] Copia un fragmento de código de un notebook del Módulo 2 y pide a la IA que lo explique línea por línea
- [ ] Genera código con IA para cargar y explorar uno de los datasets del programa
- [ ] Ejecuta el código generado en Google Colab — ¿Funcionó a la primera? ¿Qué tuviste que corregir?
- [ ] Pide a la IA que interprete un resultado estadístico. Luego verifica: ¿La interpretación tiene sentido con lo que sabes?
- [ ] Intenta un prompt malo ("analiza mis datos") vs. un prompt estructurado (rol + contexto + tarea + formato). Compara resultados.

---

## Conexión con el programa

| Módulo | Cómo la IA puede ayudarte |
|--------|--------------------------|
| **01 — Pensar con datos** | Explorar preguntas analíticas, clasificar variables, identificar sesgos en un caso |
| **02 — Data Wrangling** | Generar código pandas, depurar errores, documentar transformaciones |
| **03 — Business Intelligence** | Sugerir métricas para dashboards, generar cálculos DAX/medidas |
| **04 — Modelos predictivos** | Escribir pipelines de scikit-learn, interpretar métricas de modelo |
| **Proyecto integrador** | Estructura del informe, revisión de redacción, presentación de resultados |

---

## Nota importante

> "La IA no te hace mejor analista automáticamente. Te hace más rápido si ya sabes qué buscar. Por eso este módulo es complementario — primero el pensamiento (Módulo 1), luego las herramientas (Módulos 2-4), y la IA como acelerador en todo el camino."

---

[← Volver al programa](../README.md)
