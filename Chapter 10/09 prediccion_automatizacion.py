from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Datos simulados: carga en función de la hora y temperatura
X = np.array([[8, 20], [12, 25], [16, 30], [20, 28], [24, 22]])  # Hora y temperatura
y = np.array([50, 60, 80, 70, 55])  # Carga en MW

# Entrenar modelo
modelo = RandomForestRegressor(n_estimators=10, random_state=0)
modelo.fit(X, y)

# Predicción para hora=18 y temperatura=26°C
prediccion = modelo.predict([[18, 26]])
print(f"Carga estimada para las 18:00 a 26°C: {prediccion[0]:.2f} MW")