from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

# Supongamos que ya tenemos los valores reales (y_test) y las predicciones (y_pred)
y_test = np.array([150, 200, 250, 300, 350])
y_pred = np.array([145, 195, 240, 310, 340])

# MSE, RMSE, MAE y R²
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'MSE: {mse}')
print(f'RMSE: {rmse}')
print(f'MAE: {mae}')
print(f'R²: {r2}')