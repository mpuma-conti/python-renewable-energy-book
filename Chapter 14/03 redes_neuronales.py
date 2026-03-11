from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
X = np.array([[1], [2], [3], [4], [5], [6], [7]])  # Horas del día
y = np.array([50, 55, 58, 61, 65, 70, 75])  # Consumo energético (kWh)

# Creación del modelo de red neuronal
model = Sequential()
model.add(Dense(10, input_dim=1, activation='relu'))  # Capa de entrada
model.add(Dense(1))  # Capa de salida

# Compilación del modelo
model.compile(loss='mean_squared_error', optimizer='adam')

# Entrenamiento del modelo
model.fit(X, y, epochs=500, verbose=0)

# Predicción
predictions = model.predict(X)

# Graficar los resultados
plt.scatter(X, y, color='blue')
plt.plot(X, predictions, color='red')
plt.title('Predicción de Consumo Energético con Redes Neuronales')
plt.xlabel('Hora del Día')
plt.ylabel('Consumo Energético (kWh)')
plt.show()