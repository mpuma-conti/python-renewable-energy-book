def mppt(potencias, voltajes):
    max_potencia = max(potencias)
    indice = potencias.index(max_potencia)
    voltaje_optimo = voltajes[indice]
    return voltaje_optimo

# Datos simulados
potencias = [50, 60, 75, 80, 70]  # Potencias medidas (W)
voltajes = [18, 19, 20, 21, 22]  # Voltajes correspondientes (V)

voltaje_optimo = mppt(potencias, voltajes)
print(f"Voltaje óptimo para MPPT: {voltaje_optimo} V")