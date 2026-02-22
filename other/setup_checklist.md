# Guia de Configuracion del Entorno

## Opcion 1: Google Colab (recomendada para inicio rapido)

1. Ir a [colab.research.google.com](https://colab.research.google.com/)
2. Iniciar sesion con cuenta Google
3. Abrir notebooks directamente desde GitHub:
   - File → Open notebook → GitHub → `gonzalezulises/formacion-docente-bi-faces`
4. No requiere instalacion local

## Opcion 2: Instalacion Local

### Paso 1: Python
- Descargar [Anaconda](https://www.anaconda.com/download) (incluye Jupyter, Pandas, NumPy, Matplotlib, Scikit-learn)
- O instalar [Python 3.10+](https://www.python.org/downloads/) por separado

### Paso 2: Clonar el repositorio
```bash
git clone https://github.com/gonzalezulises/formacion-docente-bi-faces.git
cd formacion-docente-bi-faces
```

### Paso 3: Crear entorno virtual (si no usa Anaconda)
```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
# venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

### Paso 4: Verificar instalacion
```bash
jupyter notebook
```
Abrir cualquier notebook del Modulo 01 y ejecutar la primera celda.

### Paso 5: Power BI Desktop (Modulo 02)
- Solo Windows: Descargar desde [powerbi.microsoft.com/desktop](https://powerbi.microsoft.com/desktop/)
- Mac/Linux: Usar [Power BI Web](https://app.powerbi.com/) con cuenta Microsoft gratuita
- Alternativa multiplataforma: [Google Looker Studio](https://lookerstudio.google.com/)

## Verificacion Rapida

Ejecutar en una celda de Jupyter:
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
print("Todo listo!")
print(f"pandas {pd.__version__}, numpy {np.__version__}, sklearn {sklearn.__version__}")
```

## Problemas Frecuentes

| Problema | Solucion |
|----------|----------|
| `ModuleNotFoundError` | `pip install nombre_del_modulo` |
| Jupyter no abre | `pip install notebook` y reintentar |
| Conflictos de version | Usar entorno virtual limpio |
| Power BI no disponible en Mac | Usar Power BI Web o Looker Studio |
