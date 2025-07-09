flujo_agua = 500  # m^3/s (flujo de agua en metros cúbicos por segundo)
altura_caida = 100  # metros

potencia_hidroelectrica = 9.81 * flujo_agua * altura_caida
print(f"Potencia generada por la planta hidroeléctrica: {potencia_hidroelectrica / 1000} MW")