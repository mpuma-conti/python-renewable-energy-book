from sklearn.linear_model import Lasso

# Lasso para selección de características
model = Lasso(alpha=0.1)
model.fit(X_train, y_train)
print(f'Coeficientes del modelo: {model.coef_}')