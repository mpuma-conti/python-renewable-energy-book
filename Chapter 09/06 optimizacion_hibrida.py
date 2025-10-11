from scipy.optimize import minimize

# Función de costo: minimizar uso de diésel
def cost_function(x):
    solar, wind, diesel = x
    return diesel * 0.5  # Costo relativo del diésel

# Restricciones: balance generación-demanda
def constraint(x):
    solar, wind, diesel = x
    return solar + wind + diesel - 50  # Demanda de 50 MW

# Límites de cada fuente
bounds = [(0, 30), (0, 30), (0, 50)]  # Límites de solar, eólica y diésel
initial_guess = [20, 20, 10]

# Resolver optimización
result = minimize(cost_function, initial_guess, bounds=bounds, constraints={"type": "eq", "fun": constraint})
print(f"Distribución óptima: Solar={result.x[0]:.2f} MW, Eólica={result.x[1]:.2f} MW, Diésel={result.x[2]:.2f} MW")