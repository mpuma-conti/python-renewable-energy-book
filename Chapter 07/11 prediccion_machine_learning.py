from sklearn.linear_model import LinearRegression
import numpy as np

# Datos simulados
horas = np.array(range(1, 25)).reshape(-1, 1)  # Horas del día
produccion = produccion_renovable  # Producción renovable simulada

# Modelo de predicción
modelo = LinearRegression()
modelo.fit(horas, produccion)

# Predicción para las próximas 6 horas
horas_futuras = np.array(range(25, 31)).reshape(-1, 1)
prediccion = modelo.predict(horas_futuras)

print("Producción renovable prevista:", prediccion)