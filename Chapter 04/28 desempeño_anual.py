# Parámetros anuales
days = 365  # Días en un año
E_daily = E  # Energía generada en un día (kWh)

# Energía anual
E_annual = E_daily * days

# Factor de capacidad
T = 24 * days  # Tiempo total en horas
CF = E_annual / (P_nom * T)

print(f"Energía total generada en un año: {E_annual:.2f} kWh")
print(f"Factor de capacidad del sistema: {CF:.2%}")