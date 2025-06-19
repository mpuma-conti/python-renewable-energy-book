from sklearn.linear_model import LinearRegression
import numpy as np

# Datos de entrenamiento (temperatura y demanda)
X = np.array([[30], [35], [40], [45]])  # Temperatura en grados Celsius
y = np.array([100, 150, 200, 250])  # Demanda en kW

# Entrenamiento del modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Predicción para una nueva temperatura
temperatura_nueva = np.array([[50]])
demanda_predicha = modelo.predict(temperatura_nueva)
print(f"Demanda predicha para 50°C: {demanda_predicha[0]} kW")