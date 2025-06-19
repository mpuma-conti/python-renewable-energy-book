resistencias = [10, 20, 30]  # en ohmios
corriente = 2  # corriente constante en amperios

for R in resistencias:
    potencia = corriente**2 * R
    print(f"Potencia disipada en resistencia {R} ohmios: {potencia} W")