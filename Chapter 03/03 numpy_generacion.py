import numpy as np

# Datos de generación de energía en kWh
generacion_energia = np.array([100, 150, 200, 250, 300])

# Calcular promedio y desviación estándar
promedio_generacion = np.mean(generacion_energia)
desviacion_generacion = np.std(generacion_energia)

print(f"Promedio de generación de energía: {promedio_generacion} kWh")
print(f"Desviación estándar de generación: {desviacion_generacion} kWh")