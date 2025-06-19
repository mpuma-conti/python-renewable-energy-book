def calcular_energia(potencia, tiempo):
    return potencia * tiempo

energia = calcular_energia(500, 2)  # Potencia en W, tiempo en horas
print(f"Energía generada: {energia} Wh")