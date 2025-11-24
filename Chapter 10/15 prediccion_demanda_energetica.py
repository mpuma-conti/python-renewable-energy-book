import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Cargar datos históricos de consumo energético
data = pd.read_csv("datos_consumo_energetico.csv")

# Seleccionar características y variable objetivo
X = data[['temperatura', 'hora', 'dia', 'mes']]
y = data['demanda']

# Dividir datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluar el modelo
predictions = model.predict(X_test)
error = mean_absolute_error(y_test, predictions)

print(f"Error absoluto medio: {error:.2f} kW")