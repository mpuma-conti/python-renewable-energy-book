# Datos de emisiones
emisiones_red = 0.5  # kg CO2/kWh (intensidad de carbono de la red)
energia_almacenada = 1000  # kWh por año
emisiones_evitas = emisiones_red * energia_almacenada

print(f"Las emisiones evitadas son {emisiones_evitas:.2f} kg de CO2 al año.")