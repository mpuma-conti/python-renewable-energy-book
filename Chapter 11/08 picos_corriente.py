umbral = 8.0  # Umbral de corriente
for corriente in corrientes:
    if corriente > umbral:
        print(f"¡Advertencia! Pico de corriente detectado: {corriente:.2f} A")