from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Separar las variables de entrada y salida
X = datos[['Temperatura', 'Humedad', 'Dia_semana', 'Hora_dia']]
y = datos['Consumo_kWh']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Realizar predicciones
predicciones = modelo.predict(X_test)
print(predicciones[:5])