# Datos iniciales
energia_ahorrada = 3000  # kWh/mes
factor_emision = 0.5  # kg CO2/kWh

# Cálculo de emisiones reducidas
emisiones_reducidas_mensual = energia_ahorrada * factor_emision
emisiones_reducidas_anual = emisiones_reducidas_mensual * 12

print(f"Emisiones reducidas mensualmente: {emisiones_reducidas_mensual:.2f} kg de CO₂")
print(f"Emisiones reducidas anualmente: {emisiones_reducidas_anual:.2f} kg de CO₂")