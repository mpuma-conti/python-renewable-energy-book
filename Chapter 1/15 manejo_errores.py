def calcular_corriente(voltaje, resistencia):
    try:
        return voltaje / resistencia
    except ZeroDivisionError:
        print("Error: Resistencia no puede ser cero.")
        return None

corriente = calcular_corriente(120, 0)