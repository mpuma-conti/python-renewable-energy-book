def ajustar_pitch(velocidad_viento):
    if velocidad_viento < 10:
        return 0  # Ángulo en grados (posición plana)
    elif 10 <= velocidad_viento <= 20:
        return (velocidad_viento - 10) * 2  # Ajuste lineal
    else:
        return 20  # Límite máximo de ajuste

# Simulación
velocidades = [5, 12, 15, 22]  # Velocidades del viento (m/s)

for velocidad in velocidades:
    pitch = ajustar_pitch(velocidad)
    print(f"Velocidad del viento: {velocidad} m/s, Ángulo de las palas: {pitch}°")