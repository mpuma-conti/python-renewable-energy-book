flujo_agua_geotermica = 200  # kg/s
diferencia_temperatura = 150  # °C (diferencia de temperatura aprovechable)

calor_geotermico = flujo_agua_geotermica * 4.18 * diferencia_temperatura
print(f"Energía térmica generada: {calor_geotermico / 1000} kW")