from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Cargar los datos históricos de la planta
data = pd.read_csv('historial_mantenimiento.csv')

# Características que podrían predecir la necesidad de mantenimiento
features = data[['temperatura', 'vibracion', 'caudal', 'nivel_embalse']]
target = data['necesita_mantenimiento']  # 0 = No, 1 = Sí

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Crear el modelo de regresión logística
model = LogisticRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo
print(classification_report(y_test, y_pred))