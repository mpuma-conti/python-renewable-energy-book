# Factores del sistema
DoD = 0.8  # Profundidad de descarga
eficiencia = 0.9  # Eficiencia

# Capacidad real
capacidad_requerida = demanda_total / (DoD * eficiencia)
print(f"Capacidad requerida del sistema: {capacidad_requerida:.2f} kWh")