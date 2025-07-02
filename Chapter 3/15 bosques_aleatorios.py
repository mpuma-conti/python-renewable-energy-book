from sklearn.ensemble import RandomForestRegressor

# Crear y entrenar el modelo de bosque aleatorio
modelo_rf = RandomForestRegressor(n_estimators=100, random_state=42)
modelo_rf.fit(X_train, y_train)

# Realizar predicciones
predicciones_rf = modelo_rf.predict(X_test)
print(predicciones_rf[:5])