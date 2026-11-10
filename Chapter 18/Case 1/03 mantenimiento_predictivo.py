import pandas as pd
from sklearn.ensemble import IsolationForest

# Cargar datos históricos de sensores
datos = pd.read_csv('datos_paneles.csv')

# Entrenar modelo de detección de anomalías
modelo = IsolationForest(contamination=0.01)
modelo.fit(datos[['temperatura', 'eficiencia']])

# Detectar anomalías en nuevos datos
nuevos_datos = pd.read_csv('nuevos_datos_paneles.csv')
predicciones = modelo.predict(nuevos_datos[['temperatura', 'eficiencia']])
nuevos_datos['anomalía'] = predicciones

# Alertar sobre anomalías
for index, row in nuevos_datos.iterrows():
    if row['anomalía'] == -1:
        print(f"Alerta: Anomalía detectada en el panel {row['panel_id']}")