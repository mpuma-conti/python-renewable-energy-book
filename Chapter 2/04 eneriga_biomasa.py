masa_biomasa = 1000  # kg (biomasa disponible)
poder_calorifico = 18  # MJ/kg (poder calorífico promedio de la biomasa)

energia_biomasa = masa_biomasa * poder_calorifico
print(f"Energía disponible en la biomasa: {energia_biomasa / 1000} GJ")