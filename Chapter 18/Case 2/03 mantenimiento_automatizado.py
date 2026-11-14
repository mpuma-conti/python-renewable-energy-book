import pandas as pd
from sklearn.ensemble import IsolationForest

# Cargar datos históricos de turbinas
datos = pd.read_csv('datos_turbinas.csv')

# Entrenar modelo de detección de anomalías
modelo = IsolationForest(contamination=0.01)
modelo.fit(datos[['velocidad_viento', 'direccion_viento']])

# Detectar anomalías en nuevos datos
nuevos_datos = pd.read_csv('nuevos_datos_turbinas.csv')
predicciones = modelo.predict(nuevos_datos[['velocidad_viento', 'direccion_viento']])
nuevos_datos['anomalía'] = predicciones

# Generar órdenes de mantenimiento
for index, row in nuevos_datos.iterrows():
    if row['anomalía'] == -1:
        print(f"Orden de Mantenimiento: Turbina {row['turbina_id']} presenta anomalía.")
        # Aquí se integraría el sistema de gestión de órdenes de trabajo