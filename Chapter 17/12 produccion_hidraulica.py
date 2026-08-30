import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la planta hidroeléctrica
capacidad_bombeo = 100  # MW, capacidad máxima de bombeo
capacidad_generacion = 150  # MW, capacidad máxima de generación
nivel_agua = 500  # Nivel inicial del embalse en metros cúbicos

# Simulación de demanda de la red
tiempo = np.arange(0, 24, 1)  # 24 horas de operación
demanda_red = np.random.normal(loc=100, scale=20, size=len(tiempo))  # Demanda variable

# Simulación de operación
energia_producida = []
nivel_agua_dia = []

for i in tiempo:
    if demanda_red[i] > capacidad_generacion:
        energia_bombeo = (demanda_red[i] - capacidad_generacion) * 0.8  # Energía bombeada
        nivel_agua += energia_bombeo * 0.5  # Aumento en el nivel del agua por bombeo
        energia_producida.append(capacidad_generacion)
    else:
        energia_producida.append(demanda_red[i])
    
    nivel_agua_dia.append(nivel_agua)

# Gráficos
plt.figure(figsize=(10, 6))
plt.plot(tiempo, energia_producida, label='Energía Producida (MW)', color='b')
plt.plot(tiempo, demanda_red, label='Demanda de la Red (MW)', color='r', linestyle='--')
plt.title('Simulación de Integración de Energía Hidráulica')
plt.xlabel('Hora del Día')
plt.ylabel('Potencia (MW)')
plt.legend()
plt.grid(True)
plt.show()