from sklearn.neural_network import MLPRegressor

# Crear y entrenar el modelo de red neuronal
modelo_nn = MLPRegressor(hidden_layer_sizes=(50, 50), max_iter=1000, random_state=42)
modelo_nn.fit(X_train, y_train)

# Realizar predicciones
predicciones_nn = modelo_nn.predict(X_test)
print(predicciones_nn[:5])