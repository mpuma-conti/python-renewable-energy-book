from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
X = np.array([[1], [2], [3], [4], [5], [6], [7]])  # Horas del día
y = np.array([50, 55, 58, 61, 65, 70, 75])  # Consumo energético (kWh)

# División de los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creación del modelo Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predicción
predictions = model.predict(X_test)

# Graficar los resultados
plt.scatter(X_test, y_test, color='blue')
plt.scatter(X_test, predictions, color='red')
plt.title('Predicción de Consumo Energético con Random Forest')
plt.xlabel('Hora del Día')
plt.ylabel('Consumo Energético (kWh)')
plt.show()