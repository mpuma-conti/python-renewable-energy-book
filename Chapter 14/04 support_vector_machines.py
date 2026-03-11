from sklearn.svm import SVR
import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
X = np.array([[1], [2], [3], [4], [5], [6], [7]])  # Horas del día
y = np.array([50, 55, 58, 61, 65, 70, 75])  # Consumo energético (kWh)

# Creación del modelo SVR
model = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=0.01)
model.fit(X, y)

# Predicción
predictions = model.predict(X)

# Graficar los resultados
plt.scatter(X, y, color='blue')
plt.plot(X, predictions, color='red')
plt.title('Predicción de Consumo Energético con SVM')
plt.xlabel('Hora del Día')
plt.ylabel('Consumo Energético (kWh)')
plt.show()