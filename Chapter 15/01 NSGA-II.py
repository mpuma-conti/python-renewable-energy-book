import numpy as np
from scipy.optimize import differential_evolution
import matplotlib.pyplot as plt

# Función de objetivos: costos y emisiones (simplificado)
def objetivos(x):
    costo = 100 * x[0] + 150 * x[1]  # Costo de las plantas de energía (en unidades monetarias)
    emisiones = 200 * x[0] + 100 * x[1]  # Emisiones de CO2 (en toneladas)
    return [costo, emisiones]

# Definir los límites de las variables: [energía solar, energía eólica]
bounds = [(0, 1), (0, 1)]

# Ejecutar optimización multiobjetivo
result = differential_evolution(objetivos, bounds, strategy='best1bin', maxiter=100, popsize=50)

# Mostrar los resultados
print(f"Solución óptima (solar, eólica): {result.x}")
print(f"Objetivos: Costo = {result.fun[0]}, Emisiones = {result.fun[1]}")

# Graficar soluciones de Pareto
costos = []
emisiones = []
for sol in result.x:
    costo, emis = objetivos(sol)
    costos.append(costo)
    emisiones.append(emis)

plt.scatter(costos, emisiones)
plt.xlabel('Costo de Generación (unidades)')
plt.ylabel('Emisiones de CO2 (toneladas)')
plt.title('Soluciones de Pareto en la Optimización de la Mezcla Energética')
plt.show()