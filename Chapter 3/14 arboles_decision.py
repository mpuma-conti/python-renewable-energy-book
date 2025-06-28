from sklearn.tree import DecisionTreeRegressor

# Crear y entrenar el modelo de árbol de decisión
modelo_arbol = DecisionTreeRegressor(random_state=42)
modelo_arbol.fit(X_train, y_train)

# Realizar predicciones
predicciones_arbol = modelo_arbol.predict(X_test)
print(predicciones_arbol[:5])