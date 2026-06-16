from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd

# Cargar el conjunto de datos de demanda energética
df = pd.read_csv('demanda_energetica.csv')

# Dividir los datos en características (X) y objetivo (y)
X = df.drop('demanda', axis=1)
y = df['demanda']

# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Entrenar el modelo
model.fit(X_train, y_train)

# Predecir la demanda en el conjunto de prueba
predictions = model.predict(X_test)

# Evaluar el modelo
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_test, predictions)
print(f'MAE (Error Absoluto Medio): {mae}')