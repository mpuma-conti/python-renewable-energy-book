import pulp

# Crear el problema
problema = pulp.LpProblem("Optimización de Iluminación", pulp.LpMinimize)

# Variables de decisión
luz_natural = pulp.LpVariable("Luz Natural", 0, 100)  # En porcentaje
luz_artificial = pulp.LpVariable("Luz Artificial", 0, 100)  # En porcentaje

# Función objetivo: Minimizar el consumo energético
problema += luz_natural * 0.1 + luz_artificial * 0.5, "Consumo Energético"

# Restricciones: Nivel de iluminación necesario y límites
problema += luz_natural + luz_artificial >= 100, "Nivel de Iluminación"
problema += luz_natural <= 80, "Máximo Luz Natural"

# Resolver el problema
problema.solve()
print(f"Luz Natural: {luz_natural.varValue}%")
print(f"Luz Artificial: {luz_artificial.varValue}%")