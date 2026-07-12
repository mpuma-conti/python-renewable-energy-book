import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Cargar el conjunto de datos de demanda energética
df = pd.read_csv('demanda_ciudad.csv')

# Preprocesamiento: eliminar valores faltantes
df.fillna(df.mean(), inplace=True)

# Convertir las fechas en variables adicionales: Día de la semana, Hora del día, etc.
df['fecha'] = pd.to_datetime(df['fecha'])
df['dia_semana'] = df['fecha'].dt.dayofweek
df['hora_dia'] = df['fecha'].dt.hour

# Separar las características (X) del objetivo (y)
X = df[['temperatura', 'humedad', 'velocidad_viento', 'dia_semana', 'hora_dia', 'evento_especial']]
y = df['demanda']

# Normalización de las características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)