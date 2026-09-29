import os
import numpy as np
import matplotlib

if os.environ.get("DISPLAY", "") == "":
    matplotlib.use("Agg")

import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Generación de datos simulados
np.random.seed(42)
datos_normales = np.random.normal(loc=50, scale=5, size=1000)
datos_anomalos = np.random.normal(loc=70, scale=5, size=50)
datos = np.concatenate([datos_normales, datos_anomalos])

# Preparación de los datos
X = datos.reshape(-1, 1)

# Entrenamiento del modelo de Isolation Forest
modelo = IsolationForest(contamination=0.05)
modelo.fit(X)

# Predicción de anomalías
predicciones = modelo.predict(X)
anomalías = X[predicciones == -1]

# Visualización de resultados
plt.figure(figsize=(12, 6))
plt.hist(datos, bins=50, alpha=0.7, label='Datos de Operación')
plt.scatter(anomalías, np.zeros_like(anomalías), color='red', label='Anomalías', marker='x')
plt.title('Detección de Anomalías en Datos de Operación')
plt.xlabel('Valor Operativo')
plt.ylabel('Frecuencia')
plt.legend()
plt.tight_layout()
plt.savefig('deteccion_anomalias.png', dpi=150, bbox_inches='tight')
plt.close()