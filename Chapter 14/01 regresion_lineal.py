from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo (horas del día vs consumo energético)
X = np.array([[1], [2], [3], [4], [5], [6], [7]])  # Horas del día
y = np.array([50, 55, 58, 61, 65, 70, 75])  # Consumo energético (kWh)

# Creación del modelo
model = LinearRegression()
model.fit(X, y)

# Predicción
predictions = model.predict(X)

# Graficar los resultados
plt.scatter(X, y, color='blue')
plt.plot(X, predictions, color='red')
plt.title('Predicción de Consumo Energético')
plt.xlabel('Hora del Día')
plt.ylabel('Consumo Energético (kWh)')
plt.show()