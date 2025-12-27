def potencia_eolica(velocidad, area_rotor, eficiencia):
    if velocidad < 3 or velocidad > 25:  # Fuera del rango operativo
        return 0
    else:
        densidad_aire = 1.225  # kg/m³
        potencia = 0.5 * densidad_aire * area_rotor * eficiencia * velocidad**3
        return potencia / 1000  # Convertir a kW
