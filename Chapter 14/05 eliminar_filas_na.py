import pandas as pd

# Cargar el conjunto de datos
df = pd.read_csv('datos_energeticos.csv')

# Eliminar filas con valores faltantes
df_limpio = df.dropna()
