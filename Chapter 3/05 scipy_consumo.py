from scipy.optimize import minimize

# Función de consumo energético
def consumo_energia(x):
    return x**2 + 10 * x + 25

# Optimización para minimizar el consumo
resultado = minimize(consumo_energia, x0=0)
print(f"Consumo mínimo de energía en x = {resultado.x[0]}")