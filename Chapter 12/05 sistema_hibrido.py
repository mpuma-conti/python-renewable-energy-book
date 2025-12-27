import numpy as np

# Datos de entrada (perfiles horarios)
horas = np.arange(0, 24, 1)
irradiancia = [0, 0, 0, 50, 200, 400, 600, 800, 900, 950, 1000, 900, 800, 600, 400, 200, 50, 0, 0, 0, 0, 0, 0, 0]  # W/m²
velocidad_viento = [5, 6, 5, 7, 10, 12, 15, 20, 18, 17, 14, 12, 10, 8, 7, 6, 5, 4, 3, 3, 2, 2, 2, 2]  # m/s
demanda = [0.5, 0.6, 0.7, 0.8, 1.0, 1.2, 1.5, 1.8, 2.0, 2.1, 2.3, 2.2, 2.0, 1.8, 1.5, 1.2, 1.0, 0.8, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]  # kW

# Parámetros del sistema
area_panel = 10  # m²
eficiencia_panel = 0.2
area_rotor = 20  # m²
eficiencia_turbina = 0.4
bateria = Bateria(capacidad_total=10, soc_inicial=50, eficiencia=0.9)

# Resultados
generacion_solar = []
generacion_eolica = []
uso_bateria = []
energia_desperdiciada = []
energia_insuficiente = []

for i in range(24):
    solar = potencia_solar(irradiancia[i], eficiencia_panel, area_panel)
    eolica = potencia_eolica(velocidad_viento[i], area_rotor, eficiencia_turbina)
    total_generacion = solar + eolica

    if total_generacion > demanda[i]:
        excedente = total_generacion - demanda[i]
        bateria.cargar(excedente)
        energia_desperdiciada.append(max(0, excedente - (bateria.capacidad_total - bateria.soc / 100 * bateria.capacidad_total)))
        energia_insuficiente.append(0)
    else:
        deficit = demanda[i] - total_generacion
        suministro_bateria = bateria.descargar(deficit)
        energia_insuficiente.append(max(0, deficit - suministro_bateria))
        energia_desperdiciada.append(0)

    generacion_solar.append(solar)
    generacion_eolica.append(eolica)
    uso_bateria.append(bateria.soc)

# Visualización de resultados
import matplotlib.pyplot as plt

plt.plot(horas, generacion_solar, label='Solar (kW)')
plt.plot(horas, generacion_eolica, label='Eólica (kW)')
plt.plot(horas, demanda, label='Demanda (kW)', linestyle='--')
plt.plot(horas, uso_bateria, label='Estado de Batería (%)', linestyle='-.')
plt.xlabel('Hora del día')
plt.ylabel('Energía (kW) / SOC (%)')
plt.title('Simulación de Sistema Híbrido')
plt.legend()
plt.grid()
plt.show()
