import pandas as pd

# Cargar datos desde un archivo CSV
datos_hidraulicos = pd.read_csv("datos_hidraulicos.csv")

# Ver las primeras filas del DataFrame
print(datos_hidraulicos.head())