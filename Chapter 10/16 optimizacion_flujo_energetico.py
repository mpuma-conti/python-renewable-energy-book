from pulp import LpProblem, LpVariable, lpSum, LpMinimize

# Crear el modelo
model = LpProblem("Optimización del Flujo de Energía", LpMinimize)

# Variables de decisión (energía suministrada desde cada fuente)
solar = LpVariable("Solar", lowBound=0)
eolica = LpVariable("Eolica", lowBound=0)
red = LpVariable("Red", lowBound=0)

# Restricciones de demanda y capacidad
model += solar + eolica + red == 100  # Demanda energética total (kW)
model += solar <= 50  # Capacidad máxima solar (kW)
model += eolica <= 40  # Capacidad máxima eólica (kW)
model += red <= 20  # Límite de la red principal (kW)

# Función objetivo (minimizar costos operativos)
model += 0.05 * solar + 0.03 * eolica + 0.1 * red

# Resolver el modelo
model.solve()

# Resultados
print(f"Energía Solar: {solar.varValue} kW")
print(f"Energía Eólica: {eolica.varValue} kW")
print(f"Energía de la Red: {red.varValue} kW")