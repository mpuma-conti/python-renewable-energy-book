def calcular_potencia(voltaje, corriente):
    """
    Calcula la potencia eléctrica.
    
    Parámetros:
    voltaje (float): Voltaje en voltios.
    corriente (float): Corriente en amperios.
    
    Retorna:
    float: Potencia en vatios.
    """
    return voltaje * corriente

# Ejemplo de uso
V = 230  # Voltios
I = 5    # Amperios
P = calcular_potencia(V, I)
print(f"Potencia calculada: {P} W")