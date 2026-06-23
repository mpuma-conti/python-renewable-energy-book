import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# Cargar el conjunto de datos de energía solar
df = pd.read_csv('energia_solar.csv')

# Preprocesamiento: escalado de los datos
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df['produccion'].values.reshape(-1, 1))

# Crear secuencias de datos para LSTM
def create_sequences(data, seq_length=24):
    sequences = []
    labels = []
    for i in range(len(data) - seq_length):
        sequences.append(data[i:i+seq_length])
        labels.append(data[i+seq_length])
    return np.array(sequences), np.array(labels)

X, y = create_sequences(scaled_data)

# Dividir en conjunto de entrenamiento y prueba
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Crear el modelo LSTM
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(LSTM(units=50))
model.add(Dense(units=1))

# Compilar y entrenar el modelo
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Predecir la producción solar
predictions = model.predict(X_test)

# Convertir las predicciones a la escala original
predictions = scaler.inverse_transform(predictions)

# Evaluar el modelo
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, predictions)
print(f'MSE (Error Cuadrático Medio): {mse}')