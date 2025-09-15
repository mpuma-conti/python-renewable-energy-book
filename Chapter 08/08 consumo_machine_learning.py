from sklearn.linear_model import LinearRegression
import numpy as np

# Datos de entrenamiento (hora del día y consumo correspondiente)
X = np.array(range(24)).reshape(-1, 1)  # Hora
y = np.array([300, 280, 250, 220, 200, 210, 230, 300, 400, 500, 550, 580,
              600, 620, 610, 580, 560, 540, 520, 500, 450, 400, 350, 320])  # Consumo

# Modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X, y)

# Predicción para las próximas horas
horas_futuras = np.array([24, 25, 26]).reshape(-1, 1)
predicciones = modelo.predict(horas_futuras)

print("Consumo previsto para las próximas horas:", predicciones)