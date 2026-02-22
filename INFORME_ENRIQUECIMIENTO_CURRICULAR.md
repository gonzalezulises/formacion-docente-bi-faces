# Informe de Enriquecimiento Curricular

## Programa de Formacion Docente en Ciencia de Datos y BI — UCAB-FACES

**Fecha**: 2026-02-22
**Autor**: Analisis automatizado sobre 6 repositorios de libros de referencia
**Version**: 1.0

---

## Resumen Ejecutivo

El programa actual consta de **31 notebooks** y **9 laboratorios** distribuidos en 4 modulos (32 horas). La calidad del contenido existente es alta (8.3/10 promedio), con excelente contextualizacion al entorno universitario venezolano y buena progresion pedagogica.

Sin embargo, el analisis revela **3 gaps criticos** y **8 gaps importantes** que limitan la efectividad del programa:

1. **Ratio notebooks:labs desbalanceado** — Solo el 58% de los notebooks tienen lab correspondiente. Los modulos 2 y 3 tienen notebooks sin practica guiada dedicada.
2. **Ausencia de temas puente** — No hay cobertura de valores faltantes, feature engineering, ni cross-validation como temas independientes, lo que genera saltos abruptos entre modulos.
3. **Labs sin soluciones en Modulo 3** — Los 4 labs del modulo 3 son exercise-only sin notebooks de soluciones, a diferencia de los modulos 1 y 2.

El enriquecimiento propuesto agrega **11 nuevos materiales** con un esfuerzo estimado de **60-80 horas** de desarrollo, priorizados en 3 fases.

---

## Analisis por Modulo

### Modulo 1: Fundamentos de Ciencia de Datos y BI

#### Estado Actual

| Dimension | Valor |
|-----------|-------|
| Notebooks | 5 |
| Laboratorios | 4 (2 ejercicios + 2 soluciones) |
| Ratio NB:Lab | 5:2 (bueno) |
| Calidad | 8.2/10 |
| Ejercicios inline | 13 |
| Datasets usados | matricula_faces, rendimiento_academico |

**Fortalezas**: Excelente scaffolding para principiantes absolutos. Notebooks de etica (01_04) y pensamiento analitico (01_05) son unicos y de alta calidad. Contextualizacion venezolana impecable.

#### Gaps Identificados

| # | Gap | Severidad | Dimension |
|---|-----|-----------|-----------|
| 1.1 | Sin cobertura de valores faltantes (.fillna, .dropna) | Importante | Cobertura tematica |
| 1.2 | Sin operaciones merge/join (prerequisito de Modulo 2) | Importante | Progresion |
| 1.3 | Sin metodos .str para Series | Nice-to-have | Cobertura tematica |
| 1.4 | Sin mini-proyecto acumulativo | Nice-to-have | Evaluacion formativa |
| 1.5 | Sin referencias en espanol en bibliografia | Nice-to-have | Contextualizacion |

#### Propuestas de Enriquecimiento

##### Propuesta 1.1: Seccion de Valores Faltantes en 01_03

- **Gap que cubre**: 1.1
- **Fuente**: VanderPlas → `PythonDataScienceHandbook` → `notebooks/03.04-Missing-Values.ipynb`
- **URL**: https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.04-Missing-Values.ipynb
- **Descripcion del material original**: Notebook de 66 celdas (30 codigo, 36 markdown) que cubre None vs NaN, deteccion con .isnull()/.notnull(), .dropna() con parametros axis/how/thresh, .fillna() con multiples estrategias (valor fijo, ffill, bfill). Incluye tipado nullable de Pandas.
- **Adaptacion requerida**:
  - Cambio de dataset: de ejemplos genericos a rendimiento_academico.csv con NaN simulados
  - Cambio de narrativa: de referencia tecnica a "que hacer cuando faltan datos en la encuesta docente"
  - Simplificacion tecnica: eliminar seccion de nullable dtypes (avanzado para esta audiencia)
  - Adicion de reflexion pedagogica: "como la ausencia de datos afecta conclusiones sobre rendimiento estudiantil"
- **Esfuerzo estimado**: Bajo (2-3 horas)
- **Prioridad**: Alta
- **Ubicacion sugerida**: Agregar como Seccion 8 al final de `01_03_pandas_basico.ipynb` (antes de ejercicios)

##### Propuesta 1.2: Seccion de Merge/Join Introductorio en 01_03

- **Gap que cubre**: 1.2
- **Fuente**: VanderPlas → `PythonDataScienceHandbook` → `notebooks/03.07-Merge-and-Join.ipynb`
- **URL**: https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.07-Merge-and-Join.ipynb
- **Descripcion del material original**: Notebook de 84 celdas con fundamentos de algebra relacional, one-to-one/many-to-one/many-to-many joins, pd.merge() con los 4 tipos (inner/outer/left/right), ejemplo real con datos de estados de EEUU.
- **Adaptacion requerida**:
  - Cambio de dataset: usar matricula_faces + rendimiento_academico (merge natural por estudiante)
  - Cambio de narrativa: "combinar datos de inscripcion con datos de rendimiento para analisis integral"
  - Simplificacion tecnica: cubrir solo inner y left join (los mas comunes), dejar outer para Modulo 2
  - Solo introducir pd.merge(), dejar pd.concat() para 02_02
- **Esfuerzo estimado**: Medio (3-4 horas)
- **Prioridad**: Alta
- **Ubicacion sugerida**: Agregar como Seccion 9 al final de `01_03_pandas_basico.ipynb` o como seccion de apertura en `02_02_combinacion_datos.ipynb`

---

### Modulo 2: Analisis y Visualizacion de Datos

#### Estado Actual

| Dimension | Valor |
|-----------|-------|
| Notebooks | 6 |
| Laboratorios | 5 (2 ejercicios + 2 soluciones + 1 SQL ejercicios) |
| Ratio NB:Lab | 6:3 (50% cobertura) |
| Calidad | 8.0/10 (B+) |
| Ejercicios inline | 18 |
| Datasets usados | 5 (matricula, rendimiento, presupuesto, indicadores_bcv, inflacion_latam) |

**Fortalezas**: SQL introductorio es excelente (ejecutable en Jupyter via SQLite). EDA y visualizacion tienen labs completos con soluciones. Storytelling tiene buen marco teorico (3 C's, Gestalt, Tufte).

#### Gaps Identificados

| # | Gap | Severidad | Dimension |
|---|-----|-----------|-----------|
| 2.1 | 02_02 (combinacion datos) sin lab dedicado | Critico | Densidad de practica |
| 2.2 | 02_06 (storytelling) sin lab dedicado | Importante | Densidad de practica |
| 2.3 | 02_05 (Power BI) no es ejecutable end-to-end | Importante | Diversidad de formatos |
| 2.4 | Lab SQL sin notebook de soluciones | Importante | Evaluacion formativa |
| 2.5 | Sin funciones ventana/CTEs en SQL | Nice-to-have | Cobertura tematica |

#### Propuestas de Enriquecimiento

##### Propuesta 2.1: Lab de Combinacion de Datos

- **Gap que cubre**: 2.1
- **Fuentes**:
  - Pandas Exercises → `05_Merge/Housing_Market/Exercises.ipynb`
  - Pandas Exercises → `05_Merge/Fictitous_Names/Exercises.ipynb`
- **URLs**:
  - https://github.com/guipsamora/pandas_exercises/tree/master/05_Merge/Housing_Market
  - https://github.com/guipsamora/pandas_exercises/tree/master/05_Merge/Fictitous_Names
- **Descripcion del material original**: Dos sets de ejercicios progresivos. Housing Market tiene 7 pasos sobre concat (filas/columnas) y reindexacion. Fictitious Names cubre los 4 tipos de join (inner, left, right, outer) con referencia explicita a semantica SQL.
- **Adaptacion requerida**:
  - Cambio de dataset: usar matricula_faces + rendimiento_academico + presupuesto_facultad
  - Cambio de narrativa: "Construir un perfil integral del estudiante combinando multiples fuentes"
  - Ejercicio 1: concat vertical (combinar datos de multiples periodos)
  - Ejercicio 2: merge inner (inscripcion + rendimiento)
  - Ejercicio 3: merge left (todos los inscritos, con o sin notas)
  - Ejercicio 4: merge multiple (3+ DataFrames encadenados)
  - Ejercicio 5: diagnostico con indicator=True
  - Ejercicio 6: caso integrador con datos reales
- **Esfuerzo estimado**: Bajo (3-4 horas)
- **Prioridad**: Critica
- **Ubicacion sugerida**: `modulo-02-analisis-visualizacion/laboratorios/lab_03b_combinacion_ejercicios.ipynb`

##### Propuesta 2.2: Lab de Storytelling con Datos

- **Gap que cubre**: 2.2
- **Fuente**: VanderPlas → `PythonDataScienceHandbook` → `notebooks/04.14-Visualization-With-Seaborn.ipynb` (seccion Marathon, celdas 31-60)
- **URL**: https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/04.14-Visualization-With-Seaborn.ipynb
- **Descripcion del material original**: Analisis narrativo completo de tiempos de maraton. Demuestra arco narrativo con datos: observar patron → crear metrica derivada (split_frac) → segmentar por categoria → comparar distribuciones → generar insight accionable. Usa jointplots, violin plots, KDE por grupos.
- **Adaptacion requerida**:
  - Cambio de dataset: usar matricula_faces (tendencia historica de inscripcion FACES)
  - Cambio de narrativa: "La historia de FACES en numeros: construir una presentacion ejecutiva para el Decanato"
  - Estructura del lab:
    - Ejercicio 1: Elegir historia (declive de matricula, brecha de genero, eficiencia presupuestaria)
    - Ejercicio 2: Crear visualizacion "antes" (grafico basico sin narrativa)
    - Ejercicio 3: Aplicar principios de storytelling (titulo, contexto, color intencional)
    - Ejercicio 4: Crear visualizacion "despues" (mismos datos, mejor comunicacion)
    - Ejercicio 5: Redactar parrafo ejecutivo (3-5 oraciones con dato, insight, recomendacion)
    - Ejercicio 6: Construir secuencia narrativa de 3 graficos (setup → conflicto → resolucion)
- **Esfuerzo estimado**: Medio (4-5 horas)
- **Prioridad**: Alta
- **Ubicacion sugerida**: `modulo-02-analisis-visualizacion/laboratorios/lab_05b_storytelling_ejercicios.ipynb`

##### Propuesta 2.3: Soluciones para Lab SQL

- **Gap que cubre**: 2.4
- **Fuente**: Contenido propio basado en lab_05_sql_ejercicios.ipynb existente
- **Descripcion**: Crear `lab_05_sql_soluciones.ipynb` con las consultas resueltas y comentadas
- **Esfuerzo estimado**: Bajo (2 horas)
- **Prioridad**: Alta
- **Ubicacion sugerida**: `modulo-02-analisis-visualizacion/laboratorios/lab_05_sql_soluciones.ipynb`

---

### Modulo 3: Modelado Predictivo y ML Aplicado

#### Estado Actual

| Dimension | Valor |
|-----------|-------|
| Notebooks | 7 |
| Laboratorios | 4 (solo ejercicios, sin soluciones) |
| Ratio NB:Lab | 7:4 (57% cobertura) |
| Calidad | 8.5/10 |
| Ejercicios inline | 19 |
| Datasets usados | 7 (rendimiento, presupuesto, encuesta, indicadores_bcv, ventas, estados_financieros, bikeshare) |

**Fortalezas**: Progresion natural regresion → clasificacion → clustering → series temporales → interpretabilidad. SHAP notebook es completo y bien estructurado. Labs son rigurosos con 6 ejercicios cada uno.

#### Gaps Identificados

| # | Gap | Severidad | Dimension |
|---|-----|-----------|-----------|
| 3.1 | 03_07 (SHAP/interpretabilidad) sin lab dedicado | Critico | Densidad de practica |
| 3.2 | Sin lab de arboles/ensemble dedicado (cubierto parcialmente en lab_07) | Importante | Cobertura tematica |
| 3.3 | Sin cross-validation como practica independiente | Importante | Progresion |
| 3.4 | Sin feature engineering entre pandas y ML | Importante | Progresion |
| 3.5 | Labs sin notebooks de soluciones | Importante | Evaluacion formativa |
| 3.6 | Sin proyecto end-to-end como puente a Modulo 4 | Nice-to-have | Progresion |

#### Propuestas de Enriquecimiento

##### Propuesta 3.1: Lab de Interpretabilidad y SHAP

- **Gap que cubre**: 3.1
- **Fuentes**:
  - Practical Statistics → `python/notebooks/Chapter 6 - Statistical Machine Learning.ipynb` (interpretabilidad de arboles)
  - Geron → `07_ensemble_learning_and_random_forests.ipynb` (feature importance de Random Forests)
- **URLs**:
  - https://github.com/gedeck/practical-statistics-for-data-scientists/blob/master/python/notebooks/Chapter%206%20-%20Statistical%20Machine%20Learning.ipynb
  - https://github.com/ageron/handson-ml3/blob/main/07_ensemble_learning_and_random_forests.ipynb
- **Descripcion del material original**: Practical Stats tiene explicaciones accesibles de interpretabilidad basada en impureza (Gini) y particionamiento recursivo. Geron tiene codigo de feature_importances_ con visualizacion de barras horizontales.
- **Adaptacion requerida**:
  - Cambio de dataset: usar rendimiento_academico (prediccion de riesgo estudiantil)
  - Estructura propuesta:
    - Ejercicio 1: Entrenar RandomForest + extraer feature_importances_ nativas
    - Ejercicio 2: Calcular permutation importance y comparar con nativas
    - Ejercicio 3: SHAP TreeExplainer + summary plot (global)
    - Ejercicio 4: SHAP bar plot + interpretacion escrita
    - Ejercicio 5: Waterfall plot para un estudiante especifico ("por que este estudiante esta en riesgo")
    - Ejercicio 6: Redactar recomendacion para coordinacion academica basada en SHAP
  - Simplificacion: no cubrir KernelExplainer (lento, innecesario para docentes)
- **Esfuerzo estimado**: Medio (5-6 horas)
- **Prioridad**: Critica
- **Ubicacion sugerida**: `modulo-03-modelado-predictivo/laboratorios/lab_10_interpretabilidad_ejercicios.ipynb`

##### Propuesta 3.2: Lab de Arboles de Decision y Ensemble

- **Gap que cubre**: 3.2
- **Fuente**: ISLR-Python → `Notebooks/ch8_tree_based_methods_labs.ipynb`
- **URL**: https://github.com/a-martyn/ISL-python/blob/master/Notebooks/ch8_tree_based_methods_labs.ipynb
- **Descripcion del material original**: Lab estructurado con 6 secciones: ajuste de arboles, poda (pruning), visualizacion, bagging, random forest, boosting. Usa datasets de clasificacion y regresion. 48 celdas, formato lab listo para adaptar.
- **Adaptacion requerida**:
  - Cambio de dataset: de Carseats/Boston a encuesta_docente (clasificacion) y rendimiento_academico (regresion)
  - Simplificacion: eliminar boosting (avanzado para esta audiencia), enfocar en arboles + random forest
  - Agregar visualizacion de arboles con plot_tree() (sklearn, mas accesible que la version ISLR)
  - Estructura:
    - Ejercicio 1: Arbol de clasificacion con profundidad limitada + visualizacion
    - Ejercicio 2: Efecto de max_depth en overfitting (grafico train vs test accuracy)
    - Ejercicio 3: Random Forest vs arbol individual (comparacion de accuracy)
    - Ejercicio 4: Feature importance del bosque + grafico de barras
    - Ejercicio 5: Prediccion individual + explicacion ("por que este docente fue clasificado asi")
    - Ejercicio 6: Comparacion con regresion logistica del lab_07
- **Esfuerzo estimado**: Medio (4-5 horas)
- **Prioridad**: Alta
- **Ubicacion sugerida**: `modulo-03-modelado-predictivo/laboratorios/lab_07b_arboles_ejercicios.ipynb`

##### Propuesta 3.3: Lab de Cross-Validation

- **Gap que cubre**: 3.3
- **Fuente**: ISLR-Python → `Notebooks/ch5_resampling_methods_applied.ipynb`
- **URL**: https://github.com/a-martyn/ISL-python/blob/master/Notebooks/ch5_resampling_methods_applied.ipynb
- **Descripcion del material original**: 31 ejercicios aplicados sobre k-fold CV, leave-one-out CV, y bootstrap. Usa datasets Default (credito) y Weekly (retornos). Nivel beginner-intermediate.
- **Adaptacion requerida**:
  - Cambio de dataset: usar rendimiento_academico y estados_financieros
  - Simplificacion: eliminar bootstrap y LOOCV, enfocar en k-fold y stratified k-fold
  - Estructura:
    - Ejercicio 1: Train/test split simple y su variabilidad (repetir 10 veces, mostrar varianza)
    - Ejercicio 2: 5-fold CV con cross_val_score()
    - Ejercicio 3: StratifiedKFold para datasets desbalanceados
    - Ejercicio 4: Comparar 3 modelos con CV (logistica, arbol, RF)
    - Ejercicio 5: Elegir mejor modelo + justificar
    - Ejercicio 6: Reflexion sobre overfitting vs generalizacion
- **Esfuerzo estimado**: Medio (4-5 horas)
- **Prioridad**: Alta
- **Ubicacion sugerida**: Integrar como seccion expandida en `03_02_evaluacion_modelos.ipynb` o crear lab separado

##### Propuesta 3.4: Soluciones para Labs 06-09

- **Gap que cubre**: 3.5
- **Fuente**: Contenido propio basado en labs existentes
- **Descripcion**: Crear 4 notebooks de soluciones comentadas para los labs existentes:
  - `lab_06_regresion_soluciones.ipynb`
  - `lab_07_clasificacion_soluciones.ipynb`
  - `lab_08_clustering_soluciones.ipynb`
  - `lab_09_series_temporales_soluciones.ipynb`
- **Esfuerzo estimado**: Medio (8-10 horas total, 2-2.5h cada uno)
- **Prioridad**: Alta
- **Ubicacion sugerida**: `modulo-03-modelado-predictivo/laboratorios/`

---

### Modulo 4: Proyectos Integradores

#### Estado Actual

| Dimension | Valor |
|-----------|-------|
| Templates de proyecto | 4 (una por carrera) |
| Documentos de apoyo | 5 (rubrica, guia, peer review, fuentes, integracion) |
| Notebooks ejecutables | 0 |
| Calidad | 7.5/10 |

**Fortalezas**: Templates bien diferenciados por carrera. Rubrica completa con 5 criterios ponderados. Fuentes de datos publicos bien curado.

#### Gaps Identificados

| # | Gap | Severidad | Dimension |
|---|-----|-----------|-----------|
| 4.1 | Sin notebook-ejemplo de proyecto completo | Importante | Diversidad de formatos |
| 4.2 | Sin checklist de autoevaluacion para docentes | Nice-to-have | Evaluacion formativa |

#### Propuestas de Enriquecimiento

##### Propuesta 4.1: Notebook Ejemplo de Proyecto End-to-End

- **Gap que cubre**: 4.1
- **Fuente**: Geron → `02_end_to_end_machine_learning_project.ipynb` (estructura, NO contenido completo)
- **URL**: https://github.com/ageron/handson-ml3/blob/main/02_end_to_end_machine_learning_project.ipynb
- **Descripcion del material original**: Notebook de 286 celdas (1.3MB) que cubre el ciclo completo: formulacion → obtencion → limpieza → EDA → feature engineering → modelado → evaluacion → presentacion. Usa California Housing dataset. Es excesivamente largo para usar directamente.
- **Adaptacion requerida**:
  - NO copiar el notebook — es demasiado extenso y avanzado
  - Crear un notebook condensado (40-50 celdas) que siga la misma estructura pero con:
    - Dataset: rendimiento_academico.csv (prediccion de promedio)
    - Pregunta clara: "Que factores predicen el exito academico en FACES?"
    - 6 secciones: Pregunta → Datos → EDA → Modelo → Evaluacion → Presentacion
    - Cada seccion completada como ejemplo, con comentarios pedagogicos
  - Servira como "norte" para los proyectos de los docentes
- **Esfuerzo estimado**: Alto (8-10 horas)
- **Prioridad**: Alta
- **Ubicacion sugerida**: `modulo-04-proyectos-integradores/templates/ejemplo_proyecto_completo.ipynb`

---

## Matriz de Priorizacion

| # | Propuesta | Modulo | Gap | Fuente Principal | Esfuerzo | Prioridad |
|---|-----------|--------|-----|-----------------|----------|-----------|
| 1 | Lab combinacion datos | M2 | 2.1 | Pandas Exercises 05_Merge | Bajo | **Critica** |
| 2 | Lab interpretabilidad SHAP | M3 | 3.1 | Practical Stats Ch6 + Geron 07 | Medio | **Critica** |
| 3 | Soluciones labs M3 (x4) | M3 | 3.5 | Contenido propio | Medio | **Alta** |
| 4 | Lab storytelling | M2 | 2.2 | VanderPlas 04.14 Marathon | Medio | **Alta** |
| 5 | Lab arboles/ensemble | M3 | 3.2 | ISLR Ch8 Labs | Medio | **Alta** |
| 6 | Seccion valores faltantes | M1 | 1.1 | VanderPlas 03.04 | Bajo | **Alta** |
| 7 | Soluciones lab SQL | M2 | 2.4 | Contenido propio | Bajo | **Alta** |
| 8 | Notebook ejemplo proyecto | M4 | 4.1 | Geron 02 (estructura) | Alto | **Alta** |
| 9 | Lab cross-validation | M3 | 3.3 | ISLR Ch5 Applied | Medio | **Alta** |
| 10 | Seccion merge introductorio | M1 | 1.2 | VanderPlas 03.07 | Medio | **Media** |
| 11 | Metodos .str para Series | M1 | 1.3 | VanderPlas 03.10 | Medio | **Baja** |

---

## Dependencias y Consideraciones

### Secuenciacion

1. **Propuestas 1 y 2 son independientes** — pueden desarrollarse en paralelo
2. **Propuesta 3 (soluciones M3) es independiente** — puede hacerse en cualquier momento
3. **Propuesta 6 (valores faltantes) debe ir antes que Propuesta 10 (merge)** — el merge asume que se sabe manejar NaN resultantes de outer joins
4. **Propuesta 5 (arboles lab) debe ir antes que Propuesta 2 (SHAP lab)** — el lab SHAP usa modelos de arboles como base
5. **Propuesta 9 (CV lab) idealmente antes de Propuestas 2 y 5** — CV es fundamento para evaluar los modelos de esos labs

### Prerrequisitos Tecnicos

- Todas las propuestas usan librerias ya incluidas en `requirements.txt` (pandas, sklearn, matplotlib, seaborn, shap, statsmodels)
- No se requiere instalar nuevas dependencias
- Los datasets existentes son suficientes para todas las propuestas

### Licencias

| Repo | Licencia | Uso Permitido |
|------|----------|---------------|
| VanderPlas | Texto CC-BY-NC-ND, Codigo MIT | Codigo adaptable libremente; texto requiere atribucion |
| McKinney (pydata-book) | MIT | Libre |
| Geron (handson-ml3) | Apache 2.0 | Libre con atribucion |
| Pandas Exercises | BSD-3 | Libre |
| ISLR-Python | Varía | Uso educativo |
| Practical Statistics | Codigo disponible | Uso educativo |

### Restriccion de Tiempo

Cada modulo tiene 8 horas. Las propuestas **no agregan sesiones nuevas** — enriquecen las sesiones existentes:

- Propuestas 1, 4: nuevos labs para practicar durante sesiones 3 y 4
- Propuestas 2, 5: nuevos labs para sesion 6
- Propuestas 6, 10: secciones agregadas a notebooks existentes (5-10 min cada una)
- Propuesta 8: material de referencia para sesion 7, no requiere tiempo de clase adicional

---

## Siguiente Paso Recomendado

**Fase 1 (semana 1-2): Gaps criticos — 15-20 horas**

1. Crear `lab_03b_combinacion_ejercicios.ipynb` (Gap 2.1) — 3-4h
2. Crear `lab_10_interpretabilidad_ejercicios.ipynb` (Gap 3.1) — 5-6h
3. Crear `lab_05_sql_soluciones.ipynb` (Gap 2.4) — 2h
4. Agregar seccion de valores faltantes a `01_03_pandas_basico.ipynb` (Gap 1.1) — 2-3h

**Fase 2 (semana 3-4): Gaps importantes — 25-30 horas**

5. Crear 4 notebooks de soluciones para labs M3 (Gap 3.5) — 8-10h
6. Crear `lab_05b_storytelling_ejercicios.ipynb` (Gap 2.2) — 4-5h
7. Crear `lab_07b_arboles_ejercicios.ipynb` (Gap 3.2) — 4-5h
8. Expandir cross-validation en 03_02 o crear lab separado (Gap 3.3) — 4-5h

**Fase 3 (semana 5-6): Enriquecimiento adicional — 20-30 horas**

9. Crear `ejemplo_proyecto_completo.ipynb` para Modulo 4 (Gap 4.1) — 8-10h
10. Agregar merge introductorio a Modulo 1 (Gap 1.2) — 3-4h
11. Agregar metodos .str (Gap 1.3) — 3-4h

**Razon de esta secuenciacion**: La Fase 1 resuelve los gaps que afectan directamente la experiencia del docente durante las sesiones presenciales. La Fase 2 agrega profundidad de practica. La Fase 3 pule el programa para futuras cohortes.

---

## Repositorios Consultados

| Repo | Archivos Revisados | Resultado |
|------|-------------------|-----------|
| VanderPlas (PythonDataScienceHandbook) | 03.04, 03.07, 03.08, 03.10, 04.14 | 4 propuestas derivadas |
| McKinney (pydata-book) | ch05, ch07, ch08, ch09, ch13 | Material de referencia |
| Geron (handson-ml3) | 02, 03, 06, 07, 09 | 3 propuestas derivadas |
| Pandas Exercises | 05_Merge (3 carpetas), 10_Deleting | 1 propuesta derivada |
| ISLR-Python | ch5 (resampling), ch8 (trees) | 2 propuestas derivadas |
| Practical Statistics | Ch1 (EDA), Ch5, Ch6 (ML), Ch7 | 1 propuesta derivada |
