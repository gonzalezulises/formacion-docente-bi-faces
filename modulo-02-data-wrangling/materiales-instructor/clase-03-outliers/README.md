# Clase 3 — Detección de outliers

> Materiales originales entregados por el instructor **Gabriel Gómez**.

## Archivos incluidos

| Archivo | Tipo | Uso |
|---------|------|-----|
| [`deteccion_outlier_knn.docx`](deteccion_outlier_knn.docx) | Documento | Guía KNN sobre serie temporal |
| [`deteccion_outliers_isolation_forest.docx`](deteccion_outliers_isolation_forest.docx) | Documento | Guía Isolation Forest sobre dataset de joyería |
| [`tserie.csv`](tserie.csv) | Dataset | Serie temporal (valores cada 30 min) |

## Parte A — KNN sobre serie temporal (`tserie.csv`)

Referencia bibliográfica: *Tarek A. Atwan — "Time Series Analysis with Python Cookbook" (Packt, 2022), pág. 522.*

```python
# 1. Instalar PyOD
!pip install pyod

# 2. Importar librerías
from pyod.models.knn import KNN
import pandas as pd
import matplotlib.pyplot as plt

# 3. Cargar serie temporal (frecuencia 30 min)
tser = pd.read_csv('tserie.csv', index_col='timestamp', parse_dates=True)
tser.index.freq = '30T'

# 4. Configurar modelo KNN
knn = KNN(contamination=0.03, method='mean', n_neighbors=5)
knn.fit(tser)

# 5. Predecir outliers
predicted = pd.Series(knn.predict(tser), index=tser.index)
print('Número de outliers =', predicted.sum())

# 6. Filtrar outliers
outliers = predicted[predicted == 1]
outliers = tser.loc[outliers.index]

# 7. Función para graficar
def plot_outliers(outliers, data, method='KNN',
                  halignment='right', valignment='top', labels=False):
    ax = data.plot(alpha=0.6)
    if labels:
        for i in outliers['values'].items():
            plt.plot(i[0], i[1], 'v', markersize=8,
                     markerfacecolor='none', markeredgecolor='k')
            plt.text(i[0], i[1] - (i[1] * 0.04),
                     f'{i[0].strftime("%m/%d")}',
                     horizontalalignment=halignment,
                     verticalalignment=valignment)
    else:
        data.loc[outliers.index].plot(ax=ax, style='rx', markersize=9)
    plt.title(f'Serie de tiempo - {method}')
    plt.xlabel('fecha'); plt.ylabel('# de pasajeros')
    plt.legend(['Serie de tiempo', 'outliers'])
    plt.show()

plot_outliers(outliers, tser, 'KNN')

# 9-12. Reagrupar por día y repetir detección
tser = pd.read_csv('tserie.csv', parse_dates=['timestamp'])
tser['timestamp'] = pd.to_datetime(tser['timestamp'])
tser['date'] = tser['timestamp'].dt.to_period('D').astype(str)
result = tser.groupby('date', as_index=False)['value'].sum()
result.rename(columns={'date': 'timestamp'}, inplace=True)
tser = result.reset_index(drop=True)
tser.set_index('timestamp', inplace=True)

# (Repetir pasos 4-6 con el dataframe diario)

# 13-15. Etiquetar y concatenar
data = predicted[predicted == 0]
data = tser.loc[data.index]
data['Tipo'] = 'Regular'
outliers['Tipo'] = 'outliers'
Tseries = pd.concat([data, outliers], axis=0)
```

## Parte B — Isolation Forest (`jewellery.csv`)

```python
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# 1. Cargar dataset
url = "https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/jewellery.csv"
df = pd.read_csv(url)

# 2. Explorar
print(df.head())
print(df.info())

# 3. Separar numéricas / categóricas y aplicar one-hot
df_numeric = df.select_dtypes(include=['int64', 'float64'])
df_categorical = df.select_dtypes(include=['object'])
df_encoded = pd.get_dummies(df_categorical, drop_first=True)
df_final = pd.concat([df_numeric, df_encoded], axis=1)

# 4. Imputar nulos
df_final = df_final.fillna(df_numeric.mean())

# 5. Escalar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_final)

# 6-7. Entrenar Isolation Forest
model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
model.fit(X_scaled)

# 8-9. Predecir (-1 = anomalía, 1 = normal) y obtener score
df['anomaly'] = model.predict(X_scaled)
df['anomaly_score'] = model.decision_function(X_scaled)

# 10-11. Resultados
print(df['anomaly'].value_counts())
anomalies = df[df['anomaly'] == -1]
print("Anomalías detectadas:\n", anomalies.head())
```

---

Mapeo al notebook del repo: [`notebooks/02_01_eda_exploratorio.ipynb`](../../notebooks/02_01_eda_exploratorio.ipynb) (sección outliers) y [`notebooks/02_04_wrangling_avanzado.ipynb`](../../notebooks/02_04_wrangling_avanzado.ipynb).
