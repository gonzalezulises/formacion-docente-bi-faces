# Actividad 2 — Lectura y transformación de datos desde PDF

> Material original entregado por el instructor **Gabriel Gómez**.

## Archivos incluidos

| Archivo | Tipo | Uso |
|---------|------|-----|
| [`actividad2.docx`](actividad2.docx) | Documento | Enunciado y rúbrica |
| [`poblacion_provincias_panama.pdf`](poblacion_provincias_panama.pdf) | Dataset fuente | PDF con tabla de población por provincia/año |

## Objetivo

Desarrollar una solución en Python que permita **leer datos desde un archivo PDF**, estructurarlos en un DataFrame y aplicar transformaciones mediante un diccionario de correspondencias para generar nuevas columnas.

## Instrucciones

1. Leer el archivo PDF proporcionado (`poblacion_provincias_panama.pdf`).
2. Extraer las columnas: `year`, `Provincia` y `Valor`.
3. Limpiar los datos (filas incompletas, formatos inconsistentes).
4. Crear un diccionario de clasificación de provincias (por ejemplo: Región).
5. Aplicar el diccionario para crear una nueva columna llamada `Region`.
6. Exportar el resultado a un archivo CSV.

## Diccionario de ejemplo

```python
regiones = {
    'Panamá': 'Centro',
    'Chiriquí': 'Occidente',
    'Darién': 'Oriente',
}
```

## Entregables

- Código Python (`.ipynb` o `.py`).
- Archivo CSV resultante con las columnas `year`, `Provincia`, `Valor`, `Region`.

## Pistas de implementación

```python
# Opción 1: pdfplumber (recomendado para tablas)
!pip install pdfplumber
import pdfplumber
import pandas as pd

rows = []
with pdfplumber.open('poblacion_provincias_panama.pdf') as pdf:
    for page in pdf.pages:
        for table in page.extract_tables():
            rows.extend(table)

df = pd.DataFrame(rows[1:], columns=rows[0])

# Limpieza: quitar filas vacías y convertir tipos
df = df.dropna(how='any').reset_index(drop=True)
df['Valor'] = pd.to_numeric(df['Valor'].str.replace(r'[^\d]', '', regex=True), errors='coerce')
df['year'] = pd.to_numeric(df['year'], errors='coerce').astype('Int64')

# Aplicar diccionario de regiones
regiones = {
    'Panamá': 'Centro', 'Colón': 'Centro', 'Panamá Oeste': 'Centro',
    'Chiriquí': 'Occidente', 'Bocas del Toro': 'Occidente', 'Veraguas': 'Occidente',
    'Coclé': 'Centro', 'Herrera': 'Azuero', 'Los Santos': 'Azuero',
    'Darién': 'Oriente',
}
df['Region'] = df['Provincia'].map(regiones)

# Exportar
df.to_csv('poblacion_provincias_panama_limpio.csv', index=False)
```

---

Mapeo al notebook del repo: [`notebooks/02_04_wrangling_avanzado.ipynb`](../../notebooks/02_04_wrangling_avanzado.ipynb) (sección lectura de fuentes heterogéneas).
