from scipy.optimize import minimize

# Función objetivo: pérdidas de potencia en función de la corriente
def perdidas(corriente):
    resistencia = 0.5  # Resistencia en ohmios
    return resistencia * corriente**2

# Restricciones (ejemplo: corriente máxima)
limite_corriente = {'type': 'ineq', 'fun': lambda x: 10 - x}

# Solución de optimización
resultado = minimize(perdidas, x0=1, constraints=limite_corriente)
print(f"Corriente óptima para minimizar pérdidas: {resultado.x[0]} A")