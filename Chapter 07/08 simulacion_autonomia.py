# Simulación de autonomía
consumo_horario = 2.5  # kWh
autonomia = capacidad_requerida * DoD * eficiencia / consumo_horario

print(f"El sistema puede sostener la carga por {autonomia:.2f} horas continuas.")