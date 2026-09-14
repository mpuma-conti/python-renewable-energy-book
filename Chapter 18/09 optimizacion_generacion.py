import numpy as np
from scipy.optimize import minimize

# Definición de la función de generación de energía
def energia_generada(flows):
    # Supongamos que la energía generada es proporcional al flujo de agua
    return -np.sum(flows)  # Negativo porque minimizamos

# Restricciones: suma de flujos debe ser igual al flujo total disponible
def restriccion(flows):
    flujo_total = 500  # m³/s
    return flujo_total - np.sum(flows)

# Límites para cada flujo (0 <= flow <= 200)
num_turbinas = 5
limites = [(0, 200) for _ in range(num_turbinas)]

# Condiciones iniciales
flujos_iniciales = [100 for _ in range(num_turbinas)]

# Definición de las restricciones
cons = {'type': 'eq', 'fun': restriccion}

# Resolución del problema de optimización
solucion = minimize(energia_generada, flujos_iniciales, bounds=limites, constraints=cons)

print("Flujos óptimos (m³/s):", solucion.x)
print("Energía máxima generada:", -solucion.fun, "MW")