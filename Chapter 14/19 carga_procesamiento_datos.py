import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Cargar el conjunto de datos de demanda energética
df = pd.read_csv('datos_energeticos.csv')

# Preprocesamiento: eliminar valores faltantes
df.fillna(df.mean(), inplace=True)

# Convertir variables categóricas (por ejemplo, días de la semana) a numéricas
df['dia_semana'] = pd.to_datetime(df['fecha']).dt.dayofweek

# Separar las características (X) del objetivo (y)
X = df[['temperatura', 'humedad', 'velocidad_viento', 'dia_semana']]  # Características
y = df['demanda']  # Objetivo (demanda energética)

# Normalización de características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)