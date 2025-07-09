densidad_aire = 1.225  # kg/m^3 (densidad del aire a nivel del mar)
radio_aspas = 40  # metros
velocidad_viento = 10  # m/s

area_barrida = 3.1416 * radio_aspas**2
potencia_teorica = 0.5 * densidad_aire * area_barrida * velocidad_viento**3
print(f"Potencia teórica del aerogenerador: {potencia_teorica / 1000} kW")