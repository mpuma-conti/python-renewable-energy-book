from sklearn.linear_model import LinearRegression

# Crear un modelo de regresión lineal para predecir la producción de energía
X = datos_hidraulicos[['caudal']]
y = datos_hidraulicos['energia']
modelo = LinearRegression()
modelo.fit(X, y)

# Predicción de energía para un caudal dado
caudal_predicho = np.array([[150]])  # Caudal de 150 m³/s
energia_predicha = modelo.predict(caudal_predicho)
print(f"Producción de energía predicha para un caudal de 150 m³/s: {energia_predicha[0]} MWh")