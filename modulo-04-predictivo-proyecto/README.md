# Módulo 04 — Modelos predictivos simples y proyecto integrador

![Duración](https://img.shields.io/badge/duración-8_horas-blue)
![Nivel](https://img.shields.io/badge/nivel-avanzado-red)
![Instructor](https://img.shields.io/badge/instructor-Ricardo_Navarro-green)
![Fechas](https://img.shields.io/badge/fechas-5,_7,_12,_14_may-lightgrey)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Regresión](https://img.shields.io/badge/regresión_lineal-2c3e50?style=flat-square)
![Clasificación](https://img.shields.io/badge/clasificación_binaria-e74c3c?style=flat-square)
![Statsmodels](https://img.shields.io/badge/Statsmodels-4C72B0?style=flat-square)

---

## Descripcion

Este modulo combina la introduccion a modelos predictivos simples con el proyecto integrador del programa. En la primera mitad, los docentes aprenden a construir e interpretar modelos de regresion y clasificacion. En la segunda mitad, aplican todo lo aprendido en los modulos 1-4 en un proyecto completo de analisis de datos vinculado a su catedra.

---

## Objetivos de Aprendizaje

Al completar este modulo, el docente sera capaz de:

1. Construir e interpretar un modelo de regresion lineal simple y multiple
2. Evaluar la calidad de un modelo con metricas como R², MSE y RMSE
3. Aplicar clasificacion binaria (regresion logistica) a problemas educativos
4. Ejecutar el flujo completo end-to-end: Importar → Limpiar → Explorar → Modelar → Evaluar → Comunicar
5. Comunicar hallazgos de un modelo en lenguaje no tecnico
6. Integrar las competencias de los modulos 1-3 en un proyecto autonomo

---

## Contenidos por Sesion

| Sesion | Fecha | Tema | Duracion |
|--------|-------|------|----------|
| 7 | 5 mayo | Regresion lineal y evaluacion de modelos | 2h |
| 8 | 7 mayo | Clasificacion binaria y flujo completo end-to-end | 2h |
| 9 | 12 mayo | Trabajo guiado en proyecto integrador | 2h |
| 10 | 14 mayo | Presentaciones y evaluacion por pares | 2h |

---

## Estructura de Archivos

```
modulo-04-predictivo-proyecto/
├── README.md                          # Este archivo
├── notebooks/
│   ├── 04_01_regresion_lineal.ipynb           # Regresion simple y multiple
│   ├── 04_02_evaluacion_modelos.ipynb         # Metricas y validacion train/test
│   ├── 04_03_clasificacion_binaria.ipynb      # Regresion logistica
│   └── 04_04_flujo_completo.ipynb             # Flujo end-to-end (nuevo)
├── laboratorios/
│   ├── lab_07_regresion_ejercicios.ipynb      # Practica guiada: regresion
│   ├── lab_07_regresion_soluciones.ipynb      # Soluciones
│   ├── lab_08_clasificacion_ejercicios.ipynb  # Practica guiada: clasificacion
│   └── lab_08_clasificacion_soluciones.ipynb  # Soluciones
└── proyecto-integrador/
    ├── rubrica_evaluacion.md                  # Criterios de evaluacion (actualizada)
    ├── guia_presentacion_resultados.md        # Como presentar hallazgos
    ├── peer_review.md                         # Formato de revision por pares
    ├── fuentes_datos_publicos.md              # Datasets sugeridos
    ├── ejemplo_proyecto_completo.ipynb        # Notebook de referencia
    ├── proyecto_administracion.md             # Guia por carrera
    ├── proyecto_contaduria.md                 # Guia por carrera
    ├── proyecto_economia.md                   # Guia por carrera
    └── proyecto_relaciones_industriales.md    # Guia por carrera
```

---

## Prerequisitos

- **Modulos 1, 2 y 3 completados**: este modulo asume dominio de Python/pandas (Modulo 1), analisis exploratorio y visualizacion (Modulo 2), y fundamentos estadisticos (Modulo 3).
- Entorno de trabajo configurado (Google Colab o instalacion local).

---

## Evaluacion

La evaluacion de este modulo se compone de tres entregables:

| Componente | Peso | Descripcion |
|------------|------|-------------|
| Portafolio de analisis de datos | 40% | Dataset limpio + notebook con proceso documentado |
| Dashboard de BI | 30% | Dashboard funcional + explicacion de uso |
| Proyecto de curso con modelo | 30% | Pregunta + modelo aplicado + hallazgos comunicados |

Ver detalle completo en [`proyecto-integrador/rubrica_evaluacion.md`](proyecto-integrador/rubrica_evaluacion.md).

---

## Nota

Este modulo fusiona contenido simplificado de modelado predictivo (originalmente en el Modulo 3) con el proyecto integrador (originalmente en el Modulo 4). El objetivo es que los docentes aprendan las tecnicas de modelado y las apliquen inmediatamente en su proyecto final, reforzando el aprendizaje practico.

---

[Volver al programa principal](../README.md)
