from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor

# Definir el modelo y el espacio de búsqueda de hiperparámetros
model = RandomForestRegressor()
param_grid = {'n_estimators': [10, 50, 100], 'max_depth': [5, 10, None]}

# Grid search
grid_search = GridSearchCV(model, param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train, y_train)

print(f'Mejores parámetros: {grid_search.best_params_}')