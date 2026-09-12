import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Generación de datos simulados de vibración
np.random.seed(42)
normal_data = np.random.normal(loc=0.0, scale=1.0, size=1000)
anomalous_data = np.random.normal(loc=5.0, scale=1.0, size=50)
vibration_data = np.concatenate([normal_data, anomalous_data])

# Preparación de los datos para el modelo
X = vibration_data.reshape(-1, 1)

# Entrenamiento del modelo de Isolation Forest
model = IsolationForest(contamination=0.05)
model.fit(X)

# Predicción de anomalías
predictions = model.predict(X)
anomalies = X[predictions == -1]

# Visualización de resultados
plt.figure(figsize=(12, 6))
plt.hist(vibration_data, bins=50, alpha=0.7, label='Datos de Vibración')
plt.scatter(anomalies, np.zeros_like(anomalies), color='red', label='Anomalías', marker='x')
plt.title('Detección de Anomalías en Datos de Vibración')
plt.xlabel('Vibración')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()