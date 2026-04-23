# Clase 2 — Análisis exploratorio y gráficos

> Materiales originales entregados por el instructor **Gabriel Gómez**.

## Archivos incluidos

| Archivo | Tipo | Tamaño | Uso |
|---------|------|--------|-----|
| [`actividad_graficos.docx`](actividad_graficos.docx) | Documento | 17 KB | Guía de visualización |
| [`insurance_claims.csv.gz`](insurance_claims.csv.gz) | Dataset comprimido | 640 KB (11.7 MB sin comprimir) | Datos de siniestros vehiculares |

## Dataset — Insurance claims

El dataset original (`Insurance claims.csv`, 11.7 MB) se incluye en formato **comprimido gzip** (`insurance_claims.csv.gz`, 640 KB). Pandas lo lee de forma nativa sin necesidad de descomprimirlo manualmente:

```python
import pandas as pd
Auto = pd.read_csv('insurance_claims.csv.gz')   # auto-detecta gzip por la extensión
```

Si prefieres descomprimirlo:

```bash
gunzip -k insurance_claims.csv.gz    # -k conserva el .gz
```

Fuente alternativa (Kaggle): [Car Insurance Claim Data](https://www.kaggle.com/datasets/ifteshanajnin/carinsuranceclaimprediction-classification).

## Código — Análisis exploratorio con boxplot, IQR e histograma

```python
# 1. Cargar librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import io

# 2a. Opción local: leer el archivo .csv.gz directamente (recomendado)
Auto = pd.read_csv('insurance_claims.csv.gz')

# 2b. Opción Colab: subir el archivo manualmente
# from google.colab import files
# uploaded = files.upload()
# Auto = pd.read_csv(io.BytesIO(uploaded['insurance_claims.csv.gz']))

# 4. Variable objetivo categórica y selección de columnas
Auto['claim_status'] = Auto['claim_status'].astype('str')
Auto = Auto[[
    'subscription_length', 'customer_age', 'vehicle_age', 'model',
    'fuel_type', 'cylinder', 'region_code', 'region_density',
    'is_tpms', 'is_parking_sensors', 'is_parking_camera', 'claim_status'
]]

# 5. Boxplot por grupo
sns.boxplot(x='model', y='customer_age', data=Auto)
plt.title("Boxplot por grupo")
plt.show()

# 6. Detectar outliers con regla IQR
Q1 = Auto['customer_age'].quantile(0.25)
Q3 = Auto['customer_age'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = Auto[(Auto['customer_age'] < lower_bound) | (Auto['customer_age'] > upper_bound)]
print("Outliers:\n", outliers)

# 7. Histograma
plt.hist(Auto['customer_age'], bins=10, color='skyblue', edgecolor='black')
plt.title("Histograma de edad del cliente")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()

# 8. Filtro por tercera edad
Tercera_edad = Auto[Auto['customer_age'] > 70]
print(Tercera_edad.count())

# 9. Gráfico Stem
fig, ax = plt.subplots()
ax.stem(Auto['model'], Auto['customer_age'])
ax.set(xlim=(0, 12), xticks=np.arange(1, 12),
       ylim=(0, 100), yticks=np.arange(1, 8))
plt.show()
```

## Actividad

Utilizando la galería oficial de Matplotlib, generar **al menos 4 gráficos** diferentes y explicar la relación entre las variables utilizadas:

https://matplotlib.org/stable/plot_types/index.html

---

Mapeo al notebook del repo: [`notebooks/02_01_eda_exploratorio.ipynb`](../../notebooks/02_01_eda_exploratorio.ipynb).
