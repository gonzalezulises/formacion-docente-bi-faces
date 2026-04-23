# Clase 1 — Limpieza y transformación de datos

> Materiales originales entregados por el instructor **Gabriel Gómez**.

## Archivos incluidos

| Archivo | Tipo | Uso |
|---------|------|-----|
| [`limpieza_de_datos.docx`](limpieza_de_datos.docx) | Documento | Guía paso a paso — actividad Clase 1 |
| [`ejercicio_limpieza_transformacion.docx`](ejercicio_limpieza_transformacion.docx) | Documento | Ejercicio complementario con `Hipotecas.xlsx` |
| [`Hipotecas.xlsx`](Hipotecas.xlsx) | Dataset | Datos de hipotecas por provincia/distrito |

Dataset adicional usado en la guía: [`matricula_faces.csv`](../../../datasets/universidad/matricula_faces.csv) (ya presente en el repo).

## Actividad 1 — Limpieza de datos (matricula_faces.csv)

```python
# Cargar librerías
import pandas as pd
import matplotlib.pyplot as plt
import io

# Cargar archivo (Colab)
from google.colab import files
uploaded = files.upload()

# Asignar datos del archivo a la variable df
df = pd.read_csv(io.BytesIO(uploaded['matricula_faces.csv']))
print(df)

# Exploración
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
print(df.isnull().sum())
print(df['genero'].unique())
print(df['genero'].value_counts())

# Limpieza
df = df.dropna()
df['genero'] = df['genero'].replace({'M': 'Masculino', 'F': 'Femenino'})
df['edad'] = df['edad'].astype(int)
df = df.drop_duplicates()

# Variable derivada: mayor de edad
df['mayor_edad'] = df['edad'] >= 18
df = df.sort_values(by='edad', ascending=False)

# Agregaciones
print(df.groupby('carrera').size())
print(df.groupby('genero')['edad'].mean())

# Rango etáreo (usando pd.cut)
bins = [0, 17, 25, 30, 40, 60, 100]
labels = ['Menor de edad', '18-25', '26-30', '31-40', '41-60', '60+']
df['rango_etareo'] = pd.cut(df['edad'], bins=bins, labels=labels)
print(df.groupby('rango_etareo').size())

# Rango etáreo (usando función)
def clasificar_edad(edad):
    if edad < 18:
        return 'Menor de edad'
    elif edad <= 25:
        return '18-25'
    elif edad <= 30:
        return '26-30'
    elif edad <= 40:
        return '31-40'
    elif edad <= 60:
        return '41-60'
    else:
        return '60+'

df['rango_etareo'] = df['edad'].apply(clasificar_edad)
```

## Ejercicio complementario — Hipotecas.xlsx

```python
# 1. Cargar librerías
import pandas as pd
import matplotlib.pyplot as plt
import io

# 2. Subir archivo
from google.colab import files
uploaded = files.upload()

# 3. Leer Excel (salta primera fila si hay encabezado decorativo)
df = pd.read_excel(io.BytesIO(uploaded['Hipotecas.xlsx']), skiprows=1)

# 4. Limpiar nombres de columnas (espacios → guion bajo)
df.rename(columns=lambda x: x.strip().replace(" ", "_"), inplace=True)

# 5. Separar "Provincia" en Provincia + Distrito
df[['Provincia', 'Distrito']] = df['Provincia'].str.split(',', expand=True)

# 6. Renombrar columnas
df.rename(columns={'Hipoteca_Finca.1': 'HFincaTot'}, inplace=True)

# 7. Crear columna derivada Porc.de.Total
df['Monto'] = pd.to_numeric(df['Monto'].str.replace(r'[^\d.]', '', regex=True))
df['MontoTotal'] = pd.to_numeric(df['MontoTotal'].str.replace(r'[^\d.]', '', regex=True))
df['Porc.de.Total'] = df['Monto'] / df['MontoTotal']
```

### Preguntas del ejercicio

1. Si tengo una columna llamada `Nombre_empleado` y deseo renombrarla a `Colaborador`, ¿qué línea de código puedo utilizar?
2. Si en `Colaborador` existen caracteres especiales (`@#$`), ¿cómo los removemos?
3. Si en `Colaborador` hay valores como `"Gabriel, Gómez"`, ¿cómo los separo en dos columnas (`colaborador`, `apellido`)?

---

Mapeo al notebook del repo: [`notebooks/02_00_entorno_python.ipynb`](../../notebooks/02_00_entorno_python.ipynb) y [`notebooks/02_04_wrangling_avanzado.ipynb`](../../notebooks/02_04_wrangling_avanzado.ipynb).
