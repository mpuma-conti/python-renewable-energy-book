from scipy.optimize import minimize

# Parámetros
costo_energia = [0.12, 0.10, 0.08, 0.15, 0.20, 0.25]  # Precio en $/kWh durante 6 periodos
demanda_carga = 30  # kWh necesarios
horas_disponibles = len(costo_energia)

# Función objetivo: minimizar costo total
def costo_total(carga_horas):
    return sum(costo_energia[i] * carga_horas[i] for i in range(horas_disponibles))

# Restricciones
def restriccion_carga_total(carga_horas):
    return sum(carga_horas) - demanda_carga  # Total debe igualar demanda

bounds = [(0, 10)] * horas_disponibles  # Límite de carga por hora (kWh)
initial_guess = [5] * horas_disponibles  # Suposición inicial

# Optimización
resultado = minimize(costo_total, initial_guess, bounds=bounds,
                     constraints={"type": "eq", "fun": restriccion_carga_total})

print("Horario óptimo de carga (kWh):", resultado.x)
print("Costo total: $", costo_total(resultado.x))