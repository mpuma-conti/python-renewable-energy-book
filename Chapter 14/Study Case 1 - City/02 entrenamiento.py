from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Crear el modelo Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Entrenar el modelo
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
predictions = model.predict(X_test)

# Evaluar el modelo
mae = mean_absolute_error(y_test, predictions)
print(f'MAE (Error Absoluto Medio): {mae}')