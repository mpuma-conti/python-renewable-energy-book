from scipy.optimize import minimize

# Función de costo: minimización de costos operativos
def cost_function(x):
    solar, wind, diesel = x
    return solar * 20 + wind * 15 + diesel * 50  # Costos en $/MWh

# Restricciones: balance de demanda y límites de generación
def demand_constraint(x):
    solar, wind, diesel = x
    return solar + wind + diesel - 100  # Demanda de 100 MW

bounds = [(0, 50), (0, 50), (0, 100)]  # Límites de generación
initial_guess = [30, 30, 40]  # Suposición inicial

# Resolver optimización
result = minimize(cost_function, initial_guess, bounds=bounds,
                  constraints={"type": "eq", "fun": demand_constraint})

print(f"Generación óptima: Solar={result.x[0]:.2f} MW, "
      f"Eólica={result.x[1]:.2f} MW, Diésel={result.x[2]:.2f} MW")