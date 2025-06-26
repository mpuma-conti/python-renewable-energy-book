from sklearn.linear_model import LinearRegression
import numpy as np

# Datos de ejemplo (temperatura y demanda)
X = np.array([[20], [25], [30], [35]])  # Temperatura en grados Celsius
y = np.array([100, 150, 200, 250])  # Demanda en kWh

# Entrenamiento del modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Predicción de demanda para una nueva temperatura
temperatura_nueva = np.array([[40]])
demanda_predicha = modelo.predict(temperatura_nueva)
print(f"Demanda predicha para 40°C: {demanda_predicha[0]} kWh")