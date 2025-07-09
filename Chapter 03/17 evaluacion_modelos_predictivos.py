from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Calcular el MAE, MSE y R² del modelo de regresión lineal
mae = mean_absolute_error(y_test, predicciones)
mse = mean_squared_error(y_test, predicciones)
r2 = r2_score(y_test, predicciones)

print(f"MAE: {mae}")
print(f"MSE: {mse}")
print(f"R²: {r2}")