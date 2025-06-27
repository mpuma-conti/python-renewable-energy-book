import pandas as pd

# Cargar datos de consumo de energía desde un archivo CSV
datos_energia = pd.read_csv('consumo_energia.csv')

# Mostrar las primeras filas del conjunto de datos
print(datos_energia.head())

# Calcular el consumo promedio de energía
consumo_promedio = datos_energia['Consumo_kWh'].mean()
print(f"Consumo promedio de energía: {consumo_promedio} kWh")