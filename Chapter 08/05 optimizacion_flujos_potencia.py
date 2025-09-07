import numpy as np
from scipy.optimize import minimize

# Parámetros del sistema
potencia_generadores = np.array([50, 60, 40])  # Potencia de generadores en kW
demanda_total = 130  # Demanda total en kW
costos_generadores = np.array([5, 8, 6])  # Costo por kWh

# Restricción: La suma de las potencias debe igualar la demanda
def restriccion(potencias):
    return np.sum(potencias) - demanda_total

# Función objetivo: Minimizar el costo total
def costo_total(potencias):
    return np.sum(potencias * costos_generadores)

# Restricciones y límites
restricciones = {'type': 'eq', 'fun': restriccion}
limites = [(0, g) for g in potencia_generadores]  # Cada generador no puede superar su capacidad

# Resolver el problema de optimización
resultado = minimize(costo_total, potencia_generadores, constraints=restricciones, bounds=limites)
print(f"Potencias óptimas: {resultado.x}")
print(f"Costo mínimo: {resultado.fun:.2f} $/h")