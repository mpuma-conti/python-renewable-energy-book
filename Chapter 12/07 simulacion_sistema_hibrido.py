import numpy as np
import matplotlib.pyplot as plt

# Datos de entrada
horas = np.arange(0, 24, 1)
irradiancia = [0, 0, 0, 50, 200, 400, 600, 800, 900, 950, 1000, 900, 800, 600, 400, 200, 50, 0, 0, 0, 0, 0, 0, 0]  # W/m²
viento = [5, 6, 5, 7, 10, 12, 15, 14, 13, 12, 10, 9, 8, 6, 5, 4, 3, 3, 3, 2, 2, 2, 2, 2]  # m/s
demanda = [1.0, 1.2, 1.5, 2.0, 3.0, 4.5, 6.0, 7.5, 8.0, 7.0, 6.0, 5.0, 4.0, 3.5, 3.0, 2.5, 2.0, 1.8, 1.5, 1.2, 1.0, 0.8, 0.5, 0.2]  # kW

# Parámetros del sistema
area_solar = 75  # m²
eficiencia_solar = 0.2
capacidad_turbina = 5  # kW por turbina
num_turbinas = 2
capacidad_bateria = 50  # kWh
soc = 50  # Estado inicial de la batería (%)
eficiencia_bateria = 0.9

# Variables para almacenar resultados
generacion_solar = []
generacion_eolica = []
uso_bateria = []
energia_desperdiciada = []
energia_no_satisfecha = []

for i in range(24):
    # Generación solar
    solar = irradiancia[i] * area_solar * eficiencia_solar / 1000  # kW
    generacion_solar.append(solar)
    
    # Generación eólica
    if viento[i] < 3 or viento[i] > 25:  # Fuera del rango operativo
        eolica = 0
    else:
        eolica = min(capacidad_turbina * num_turbinas, 0.5 * 1.225 * 20 * eficiencia_bateria * viento[i]**3 / 1000)
    generacion_eolica.append(eolica)
    
    # Energía total generada
    total_generacion = solar + eolica
    
    # Cobertura de la demanda
    if total_generacion > demanda[i]:
        excedente = total_generacion - demanda[i]
        if soc < 100:
            carga = min(excedente * eficiencia_bateria, (100 - soc) * capacidad_bateria / 100)
            soc += carga / capacidad_bateria * 100
        energia_desperdiciada.append(max(0, excedente - carga))
        energia_no_satisfecha.append(0)
    else:
        deficit = demanda[i] - total_generacion
        descarga = min(deficit / eficiencia_bateria, soc * capacidad_bateria / 100)
        soc -= descarga / capacidad_bateria * 100
        energia_no_satisfecha.append(max(0, deficit - descarga))
        energia_desperdiciada.append(0)
    
    uso_bateria.append(soc)

# Gráficos de resultados
plt.plot(horas, demanda, label='Demanda (kW)', linestyle='--')
plt.plot(horas, generacion_solar, label='Solar (kW)')
plt.plot(horas, generacion_eolica, label='Eólica (kW)')
plt.plot(horas, uso_bateria, label='SOC Batería (%)', linestyle='-.')
plt.xlabel('Hora del día')
plt.ylabel('Energía (kW) / SOC (%)')
plt.title('Simulación de Sistema Híbrido para una Comunidad Rural')
plt.legend()
plt.grid()
plt.show()