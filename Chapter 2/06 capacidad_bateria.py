energia_exceso = 1000  # en kWh, energía excedente generada
profundidad_descarga = 0.9  # eficiencia de descarga

capacidad_bateria = energia_exceso / profundidad_descarga
print(f"Capacidad requerida de la batería: {capacidad_bateria} kWh")