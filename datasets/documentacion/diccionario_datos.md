# Diccionario de Datos - Formación Docente BI-FACES

Este documento describe todos los conjuntos de datos disponibles en el programa de formación docente en Business Intelligence para FACES-UCAB.

---

## Índice

1. [Datasets Universitarios](#1-datasets-universitarios)
   - [rendimiento_academico.csv](#11-rendimiento_academico)
   - [matricula_faces.csv](#12-matricula_faces)
   - [encuesta_docente.csv](#13-encuesta_docente)
   - [presupuesto_facultad.csv](#14-presupuesto_facultad)
2. [Datasets Económicos](#2-datasets-económicos)
   - [inflacion_latam.csv](#21-inflacion_latam)
   - [indicadores_bcv.csv](#22-indicadores_bcv)
   - [comercio_exterior.csv](#23-comercio_exterior)
3. [Datasets Empresariales](#3-datasets-empresariales)
   - [ventas_retail.csv](#31-ventas_retail)
   - [estados_financieros.csv](#32-estados_financieros)
   - [rrhh_nomina.csv](#33-rrhh_nomina)
4. [Relaciones entre Datasets](#4-relaciones-entre-datasets)
5. [Uso por Módulo](#5-uso-por-módulo)

---

## 1. Datasets Universitarios

### 1.1 rendimiento_academico

**Descripción:** Registro de rendimiento académico de estudiantes de FACES (datos simulados).

**Archivo:** `datasets/universidad/rendimiento_academico.csv`

**Filas:** ~3,000 registros

**Uso principal:** Módulo 4 (Modelos Predictivos), Proyecto Integrador

| Columna | Tipo | Descripción | Valores Posibles | Notas |
|---------|------|-------------|------------------|-------|
| `estudiante_id` | string | Identificador único del estudiante | EST-0001, EST-0002, ... | Clave primaria |
| `carrera` | string | Carrera en la que está inscrito | Administración, Contaduría, Economía, RRII, Sociología | Categórica nominal |
| `semestre` | int | Semestre actual del estudiante | 1-10 | Ordinal |
| `genero` | string | Género del estudiante | M, F | Categórica binaria |
| `edad` | int | Edad en años | 17-50 | Numérica discreta |
| `promedio` | float | Promedio acumulado de notas | 0.0-20.0 | Escala venezolana |
| `materias_inscritas` | int | Materias inscritas en el período | 1-8 | Numérica discreta |
| `materias_aprobadas` | int | Materias aprobadas | 0-8 | Numérica discreta |
| `materias_reprobadas` | int | Materias reprobadas | 0-8 | Numérica discreta |
| `asistencia_pct` | float | Porcentaje de asistencia | 0.0-100.0 | Porcentaje |
| `beca` | boolean | Tiene beca activa | True, False | Binaria |
| `trabaja` | boolean | Trabaja actualmente | True, False | Binaria |

**Variable objetivo sugerida para ML:** `promedio` (regresión) o `estado` derivado de `promedio >= 10` (clasificación)

---

### 1.2 matricula_faces

**Descripción:** Registro histórico de matrícula por período, carrera y características demográficas.

**Archivo:** `datasets/universidad/matricula_faces.csv`

**Filas:** ~5,000 registros

**Uso principal:** Módulo 3 (BI), Lab de Storytelling

| Columna | Tipo | Descripción | Valores Posibles | Notas |
|---------|------|-------------|------------------|-------|
| `periodo` | string | Período académico | 2015-I, 2015-II, ..., 2024-II | Formato año-semestre |
| `carrera` | string | Carrera | Administración, Contaduría, Economía, RRII, Sociología | |
| `genero` | string | Género | M, F | |
| `edad` | int | Edad al momento de inscripción | 17-60 | |
| `tipo_ingreso` | string | Tipo de ingreso a la universidad | Regular, Equivalencia, Reingreso | |
| `sede` | string | Sede universitaria | Montalbán, La Castellana, ... | |
| `estatus` | string | Estatus actual del estudiante | Activo, Egresado, Retirado, Suspendido | |

**Análisis sugeridos:**
- Tendencia de matrícula por año
- Deserción por carrera
- Distribución demográfica

---

### 1.3 encuesta_docente

**Descripción:** Resultados de encuesta de clima laboral y satisfacción docente.

**Archivo:** `datasets/universidad/encuesta_docente.csv`

**Filas:** ~150 registros

**Uso principal:** Módulo 1 (Fundamentos), Análisis exploratorio

| Columna | Tipo | Descripción | Valores Posibles | Notas |
|---------|------|-------------|------------------|-------|
| `docente_id` | string | Identificador del docente | DOC-001, DOC-002, ... | Anonimizado |
| `departamento` | string | Departamento académico | Administración, Economía, Estadística, ... | |
| `genero` | string | Género | M, F | |
| `edad` | int | Edad en años | 25-70 | |
| `antiguedad` | int | Años de servicio | 1-40 | |
| `dedicacion` | string | Tipo de dedicación | Tiempo Completo, Medio Tiempo, Contratado | |
| `formacion` | string | Nivel de formación | Licenciatura, Maestría, Doctorado | |
| `satisfaccion_general` | int | Satisfacción general | 1-5 (Likert) | 1=Muy insatisfecho, 5=Muy satisfecho |
| `satisfaccion_salarial` | int | Satisfacción con salario | 1-5 (Likert) | |
| `satisfaccion_infraestructura` | int | Satisfacción con infraestructura | 1-5 (Likert) | |
| `satisfaccion_desarrollo` | int | Satisfacción con oportunidades de desarrollo | 1-5 (Likert) | |
| `publicaciones` | int | Número de publicaciones en últimos 5 años | 0-20 | |
| `carga_horaria` | int | Horas de clase semanales | 4-20 | |

**Consideraciones éticas:** Datos anonimizados. No intentar re-identificar.

---

### 1.4 presupuesto_facultad

**Descripción:** Ejecución presupuestaria de la facultad por año y partida.

**Archivo:** `datasets/universidad/presupuesto_facultad.csv`

**Uso principal:** Módulo 3 (BI), Dashboards

| Columna | Tipo | Descripción | Valores Posibles | Notas |
|---------|------|-------------|------------------|-------|
| `año` | int | Año fiscal | 2018-2024 | |
| `trimestre` | int | Trimestre | 1-4 | |
| `partida` | string | Categoría presupuestaria | Personal, Operaciones, Inversiones, ... | |
| `monto_asignado` | float | Presupuesto asignado | > 0 | En USD |
| `monto_ejecutado` | float | Presupuesto ejecutado | >= 0 | En USD |
| `departamento` | string | Departamento | Decanato, Administración, Economía, ... | |

---

## 2. Datasets Económicos

### 2.1 inflacion_latam

**Descripción:** Indicadores económicos de países latinoamericanos.

**Archivo:** `datasets/economia/inflacion_latam.csv`

**Fuente simulada:** Basado en datos del Banco Mundial

| Columna | Tipo | Descripción | Valores Posibles | Notas |
|---------|------|-------------|------------------|-------|
| `pais` | string | País | Venezuela, Colombia, Brasil, Argentina, Chile, México, Perú | |
| `anio` | int | Año | 2000-2023 | |
| `inflacion_anual` | float | Inflación anual (%) | -5 a 1000+ | Venezuela tiene valores extremos |
| `pib_per_capita_usd` | float | PIB per cápita | > 0 | En USD corrientes |
| `desempleo_pct` | float | Tasa de desempleo | 0-30 | Porcentaje |

**Uso sugerido:** Visualización de series de tiempo, comparaciones regionales, manejo de outliers (Venezuela).

---

### 2.2 indicadores_bcv

**Descripción:** Serie histórica de indicadores del Banco Central de Venezuela.

**Archivo:** `datasets/economia/indicadores_bcv.csv`

| Columna | Tipo | Descripción | Valores Posibles | Notas |
|---------|------|-------------|------------------|-------|
| `fecha` | date | Fecha del registro | 2015-01-01 a 2024-12-31 | Mensual |
| `tipo_cambio_oficial` | float | Tipo de cambio oficial BCV | > 0 | VES/USD |
| `tipo_cambio_paralelo` | float | Tipo de cambio paralelo | > 0 | VES/USD |
| `liquidez_m2` | float | Liquidez monetaria M2 | > 0 | En millones VES |
| `reservas_internacionales` | float | Reservas internacionales | > 0 | En millones USD |
| `inflacion_mensual` | float | Inflación mensual | -10 a 500 | Porcentaje |

---

### 2.3 comercio_exterior

**Descripción:** Datos de importaciones y exportaciones.

**Archivo:** `datasets/economia/comercio_exterior.csv`

| Columna | Tipo | Descripción | Valores Posibles | Notas |
|---------|------|-------------|------------------|-------|
| `año` | int | Año | 2015-2023 | |
| `mes` | int | Mes | 1-12 | |
| `tipo` | string | Tipo de operación | Importación, Exportación | |
| `sector` | string | Sector económico | Petrolero, No petrolero | |
| `categoria` | string | Categoría de producto | Alimentos, Manufactura, Química, ... | |
| `pais_destino_origen` | string | País de destino/origen | USA, China, Colombia, ... | |
| `valor_usd` | float | Valor en USD | > 0 | Miles de USD |

---

## 3. Datasets Empresariales

### 3.1 ventas_retail

**Descripción:** Registro de ventas diarias de una cadena de retail ficticia.

**Archivo:** `datasets/empresarial/ventas_retail.csv`

**Filas:** ~10,000 transacciones

| Columna | Tipo | Descripción | Valores Posibles | Notas |
|---------|------|-------------|------------------|-------|
| `fecha` | date | Fecha de la transacción | 2023-01-01 a 2024-06-30 | |
| `tienda` | string | Identificador de tienda | Tienda-01 a Tienda-15 | |
| `region` | string | Región geográfica | Capital, Andes, Llanos, Oriente | |
| `categoria` | string | Categoría de producto | Alimentos, Bebidas, Hogar, Cuidado Personal | |
| `cantidad` | int | Unidades vendidas | > 0 | |
| `ingreso` | float | Ingreso por venta | > 0 | En USD |
| `costo` | float | Costo del producto | > 0 | En USD |

**Métricas derivables:** Margen = (ingreso - costo) / ingreso

---

### 3.2 estados_financieros

**Descripción:** Estados financieros simplificados de empresa ficticia.

**Archivo:** `datasets/empresarial/estados_financieros.csv`

| Columna | Tipo | Descripción | Valores Posibles | Notas |
|---------|------|-------------|------------------|-------|
| `año` | int | Año fiscal | 2018-2024 | |
| `trimestre` | int | Trimestre | 1-4 | |
| `cuenta` | string | Cuenta contable | Ingresos, Costos, Gastos Operativos, ... | |
| `monto` | float | Monto en USD | Positivo o negativo | |
| `categoria` | string | Categoría de cuenta | Activo, Pasivo, Patrimonio, Resultados | |

---

### 3.3 rrhh_nomina

**Descripción:** Datos de nómina de recursos humanos (anonimizados).

**Archivo:** `datasets/empresarial/rrhh_nomina.csv`

| Columna | Tipo | Descripción | Valores Posibles | Notas |
|---------|------|-------------|------------------|-------|
| `empleado_id` | string | Identificador del empleado | EMP-0001, ... | Anonimizado |
| `departamento` | string | Departamento | Ventas, Finanzas, Operaciones, RRHH, TI | |
| `cargo` | string | Cargo | Analista, Coordinador, Gerente, Director | |
| `antiguedad_años` | int | Años en la empresa | 0-30 | |
| `genero` | string | Género | M, F | |
| `edad` | int | Edad | 18-65 | |
| `salario_base` | float | Salario base mensual | > 0 | En USD |
| `bonos` | float | Bonos del período | >= 0 | En USD |
| `evaluacion_desempeño` | float | Última evaluación de desempeño | 1.0-5.0 | |
| `horas_capacitacion` | int | Horas de capacitación en el año | 0-200 | |

---

## 4. Relaciones entre Datasets

### Modelo Relacional Universidad

```
                    ┌─────────────────────┐
                    │   encuesta_docente  │
                    │   (DOC-xxx)         │
                    └─────────────────────┘
                              │
                              │ (departamento)
                              ▼
┌───────────────────┐    ┌─────────────────────┐
│ matricula_faces   │───│   rendimiento       │
│ (período, carrera)│    │   académico         │
└───────────────────┘    │   (EST-xxx)         │
                         └─────────────────────┘
                              │
                              │ (carrera)
                              ▼
                    ┌─────────────────────┐
                    │ presupuesto_facultad│
                    │ (departamento)      │
                    └─────────────────────┘
```

### Posibles JOINs

1. `matricula_faces` + `rendimiento_academico` por `carrera`
2. `encuesta_docente` + `presupuesto_facultad` por `departamento`
3. `ventas_retail` + `estados_financieros` por `año` y `trimestre`

---

## 5. Uso por Módulo

### Módulo 1: Fundamentos

| Dataset | Uso |
|---------|-----|
| `encuesta_docente` | Análisis exploratorio, tipos de variables |
| `rendimiento_academico` | Distribuciones, estadísticas descriptivas |

### Módulo 2: Data Wrangling

| Dataset | Uso |
|---------|-----|
| `rendimiento_academico` | Limpieza, transformaciones |
| `ventas_retail` | Agregaciones, groupby |
| `indicadores_bcv` | Series de tiempo |

### Módulo 3: Business Intelligence

| Dataset | Uso |
|---------|-----|
| `matricula_faces` | Dashboard de matrícula, storytelling |
| `presupuesto_facultad` | Dashboard financiero |
| `ventas_retail` | Dashboard de ventas |

### Módulo 4: Modelos Predictivos

| Dataset | Uso |
|---------|-----|
| `rendimiento_academico` | Proyecto integrador (predecir rendimiento) |
| `rrhh_nomina` | Clasificación de desempeño |
| `ventas_retail` | Predicción de demanda |

---

## Licencia y Uso

Estos datasets son **simulados** y han sido creados exclusivamente para fines educativos. No representan datos reales de ninguna institución.

**Uso permitido:** Educación, investigación, práctica personal.

**Citación sugerida:**
> Formación Docente en BI-FACES (2025). Datasets simulados para análisis de datos. UCAB.

---

*Última actualización: Enero 2025*
