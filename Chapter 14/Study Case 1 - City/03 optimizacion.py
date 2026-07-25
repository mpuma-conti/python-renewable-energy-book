from sklearn.model_selection import GridSearchCV

# Definir los parámetros a evaluar
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10]
}

# Realizar la búsqueda en cuadrícula
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Imprimir los mejores parámetros y el rendimiento
print(f'Best parameters: {grid_search.best_params_}')
print(f'Best score: {grid_search.best_score_}')