# Datos iniciales
costo_por_kwh = 0.12  # USD/kWh
consumo_actual = 15000  # kWh/mes
consumo_optimizado = 12000  # kWh/mes

# Cálculo de ahorros
ahorro_mensual = (consumo_actual - consumo_optimizado) * costo_por_kwh
ahorro_anual = ahorro_mensual * 12

print(f"Ahorro mensual: ${ahorro_mensual:.2f}")
print(f"Ahorro anual: ${ahorro_anual:.2f}")