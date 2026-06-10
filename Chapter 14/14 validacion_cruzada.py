from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

# Modelo de regresión lineal como ejemplo
model = LinearRegression()

# Validación cruzada con 5 folds
scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')
print(f'Métricas de validación cruzada: {-scores}')
print(f'Mean MSE: {-scores.mean()}')