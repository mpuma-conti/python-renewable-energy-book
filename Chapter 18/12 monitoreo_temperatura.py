import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Generación de datos simulados de temperatura
np.random.seed(42)
temperatura_normal = np.random.normal(loc=75, scale=5, size=1000)
temperatura_anomalous = np.random.normal(loc=100, scale=5, size=50)
temperatura = np.concatenate([temperatura_normal, temperatura_anomalous])

# Preparación de los datos
X = temperatura.reshape(-1, 1)

# Entrenamiento del modelo de Isolation Forest
model = IsolationForest(contamination=0.05)
model.fit(X)

# Predicción de anomalías
predictions = model.predict(X)
anomalías = X[predictions == -1]

# Visualización de resultados
plt.figure(figsize=(12, 6))
plt.hist(temperatura, bins=50, alpha=0.7, label='Temperaturas')
plt.scatter(anomalías, np.zeros_like(anomalías), color='red', label='Anomalías', marker='x')
plt.title('Detección de Anomalías en Datos de Temperatura')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()