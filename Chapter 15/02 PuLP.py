from pulp import LpMinimize, LpProblem, LpVariable

# Definir el problema de optimización
prob = LpProblem("Optimización_Mezcla_Energética", LpMinimize)

# Variables de decisión: cantidad de energía generada por cada fuente
x_solar = LpVariable("Energía_Solar", lowBound=0, upBound=400, cat='Continuous')
x_eolica = LpVariable("Energía_Eólica", lowBound=0, upBound=500, cat='Continuous')
x_termica = LpVariable("Energía_Térmica", lowBound=0, upBound=300, cat='Continuous')

# Función objetivo: minimizar el costo total
prob += 0.05 * x_solar + 0.03 * x_eolica + 0.10 * x_termica, "Costo_Total"

# Restricciones
prob += x_solar + x_eolica + x_termica == 1000, "Demanda_Total"
prob += x_solar <= 400, "Capacidad_Solar"
prob += x_eolica <= 500, "Capacidad_Eólica"
prob += x_termica <= 300, "Capacidad_Térmica"

# Resolver el problema
prob.solve()

# Mostrar la solución
print(f"Energía solar a generar: {x_solar.varValue} kWh")
print(f"Energía eólica a generar: {x_eolica.varValue} kWh")
print(f"Energía térmica a generar: {x_termica.varValue} kWh")
print(f"Costo total: ${prob.objective.value()}")