# Energía generada y capacidad nominal
energia_generada = 2000  # en MWh
capacidad_nominal = 3  # en MW
horas_totales = 1000  # en horas

# Calcular el Factor de Capacidad
factor_capacidad = energia_generada / (capacidad_nominal * horas_totales)
print(f"Factor de Capacidad: {factor_capacidad:.2f}")