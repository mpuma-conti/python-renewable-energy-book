import pandas as pd

# Cargar los datos ambientales
df = pd.read_csv('datos_ambientales.csv')

# Eliminar filas con datos faltantes
df_clean = df.dropna()

# Convertir unidades de temperatura de Fahrenheit a Celsius
df_clean['Temperatura_C'] = (df_clean['Temperatura_F'] - 32) * 5.0/9.0