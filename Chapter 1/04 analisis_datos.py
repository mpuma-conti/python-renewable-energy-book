import pandas as pd

# Lectura de datos de rendimiento desde un archivo CSV
datos = pd.read_csv("rendimiento_fotovoltaico.csv")

# Análisis básico
promedio_energia = datos['energia_generada'].mean()
print(f"Energía promedio generada: {promedio_energia} kWh")