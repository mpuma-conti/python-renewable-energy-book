# Parámetros del sistema térmico
masa = 5000  # kg de agua
capacidad_calorifica = 4.18  # kJ/kg·°C
temperatura_inicial = 25  # °C
temperatura_final = 80  # °C

# Cálculo de la energía térmica almacenada
energia_termica = masa * capacidad_calorifica * (temperatura_final - temperatura_inicial)

print(f"Energía térmica almacenada: {energia_termica} kJ")