area_panel = 1.6  # en metros cuadrados
irradiancia = 1000  # W/m^2 (irradiancia promedio en días soleados)
eficiencia_panel = 0.15  # 15% de eficiencia

potencia_generada = area_panel * irradiancia * eficiencia_panel
print(f"Potencia generada: {potencia_generada} W")