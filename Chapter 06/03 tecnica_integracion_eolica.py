from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo: velocidad del viento (m/s) y potencia generada (kW)
viento = np.array([3, 5, 7, 9, 11, 13, 15])  # Velocidad del viento
potencia = np.array([30, 150, 450, 700, 850, 950, 1000])  # Potencia generada

# Crear un modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(viento.reshape(-1, 1), potencia)

# Predecir la potencia para nuevas velocidades del viento
viento_nuevo = np.array([4, 6, 8, 10, 12])
potencia_predicha = modelo.predict(viento_nuevo.reshape(-1, 1))

# Visualización
plt.scatter(viento, potencia, color='blue', label='Datos históricos')
plt.plot(viento_nuevo, potencia_predicha, color='red', label='Predicción')
plt.xlabel('Velocidad del Viento (m/s)')
plt.ylabel('Potencia Generada (kW)')
plt.title('Predicción de Potencia Generada por un Aerogenerador')
plt.legend()
plt.show()