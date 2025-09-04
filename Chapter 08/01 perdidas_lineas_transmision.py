# Parámetros del sistema
corriente = 50  # Amperios
resistencia = 0.2  # Ohmios

# Cálculo de pérdidas en la línea
perdida_linea = corriente**2 * resistencia
print(f"Pérdida de potencia en la línea: {perdida_linea:.2f} W")