# Pérdidas en el sistema
losses_temperature = 0.10  # 10% por temperatura
losses_dirt = 0.05  # 5% por suciedad
losses_electrical = 0.03  # 3% por resistencias eléctricas

# Pérdidas totales
total_losses = losses_temperature + losses_dirt + losses_electrical
E_actual = E_annual * (1 - total_losses)

print(f"Energía generada considerando pérdidas: {E_actual:.2f} kWh")