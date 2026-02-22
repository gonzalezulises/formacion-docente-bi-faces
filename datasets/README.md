# Catalogo de Datasets

Este directorio contiene todos los datasets utilizados en el programa. Los datos del dominio FACES son **simulados pero realistas**, disenados para reflejar patrones y magnitudes verosimiles del contexto universitario y economico venezolano.

---

## Universidad (`universidad/`)

| Archivo | Filas | Columnas | Descripcion | Modulos |
|---------|-------|----------|-------------|---------|
| `matricula_faces.csv` | ~2,000 | periodo, carrera, genero, edad, tipo_ingreso, sede, estatus | Datos de inscripcion por carrera, periodo y genero (2015-2025) | 01, 02 |
| `rendimiento_academico.csv` | ~3,000 | estudiante_id, carrera, semestre, promedio, materias_aprobadas, materias_reprobadas, asistencia_pct, beca, trabaja, edad, genero | Notas y factores sociodemograficos | 02, 03 |
| `presupuesto_facultad.csv` | ~120 | anio, mes, partida, presupuestado, ejecutado, fuente | Series temporales de ejecucion presupuestaria (2015-2025) | 02, 03 |
| `encuesta_docente.csv` | ~200 | docente_id, departamento, antiguedad, dedicacion, satisfaccion_*, formacion, publicaciones, carga_horaria | Encuesta de clima laboral y perfil docente | 02, 03 |

## Economia (`economia/`)

| Archivo | Filas | Columnas | Descripcion | Modulos |
|---------|-------|----------|-------------|---------|
| `indicadores_bcv.csv` | ~120 | fecha, inflacion_mensual, tipo_cambio, liquidez_monetaria, reservas_internacionales, pib_trimestral | Indicadores macroeconomicos mensuales | 02, 03 |
| `inflacion_latam.csv` | ~300 | pais, anio, inflacion_anual, pib_per_capita, desempleo | Comparacion entre 10 paises LATAM (2000-2025) | 02 |
| `comercio_exterior.csv` | ~500 | anio, mes, pais_destino, producto, valor_fob, volumen | Exportaciones e importaciones por sector | 02, 03 |

## Empresarial (`empresarial/`)

| Archivo | Filas | Columnas | Descripcion | Modulos |
|---------|-------|----------|-------------|---------|
| `ventas_retail.csv` | ~5,000 | fecha, tienda, categoria, producto, cantidad, ingreso, costo, region | Ventas diarias de cadena retail (2 anios) | 03 |
| `rrhh_nomina.csv` | ~500 | empleado_id, departamento, cargo, antiguedad, salario, evaluacion, ausencias, genero, edad | Datos de recursos humanos | 02, 03 |
| `estados_financieros.csv` | ~200 | empresa_id, anio, activos, pasivos, patrimonio, ingresos, costos, utilidad_neta, sector | Balances de empresas simuladas | 02, 03 |

## Generales (`generales/`)

| Archivo | Filas | Columnas | Descripcion | Modulos |
|---------|-------|----------|-------------|---------|
| `titanic.csv` | 891 | - | Pasajeros del Titanic — ejemplo clasico de clasificacion | 03 |
| `bikeshare.csv` | ~10,000 | - | Demanda de bicicletas compartidas — regresion | 03 |
| `bank.csv` | ~4,000 | - | Marketing bancario — clasificacion en contexto financiero | 03 |

---

## Notas

- Los datasets de `universidad/`, `economia/` y `empresarial/` son **datos sinteticos** generados con Faker y NumPy. No representan datos reales de ninguna institucion.
- Los datasets de `generales/` provienen de fuentes publicas (Kaggle, seaborn, UCI ML Repository).
- Todos los CSVs usan codificacion UTF-8 y separador coma (`,`).
