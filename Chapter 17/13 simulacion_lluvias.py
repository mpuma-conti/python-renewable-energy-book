import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la planta hidroeléctrica
capacidad_generacion = 500  # MW
capacidad_bombeo = 400  # MW
nivel_agua = 1000000  # m³, nivel inicial del embalse
volumen_por_MWh = 3000  # m³ de agua por MWh
nivel_minimo_embalse = 200000  # m³, nivel mínimo de agua para evitar agotamiento

# Simulación de la demanda de energía (función seno para variar la demanda)
tiempo_dia = np.arange(0, 24, 1)  # 24 horas del día
demanda = 200 + 300 * np.sin(np.pi * tiempo_dia / 12)  # Demanda que varía a lo largo del día (en MW)

# Generación de lluvias aleatorias que aumentan el nivel del embalse
lluvias = np.random.normal(0, 0.1, len(tiempo_dia))  # Cambio estocástico en el nivel del embalse

# Variables para el registro
generacion = np.zeros_like(tiempo_dia)  # Energía generada cada hora (en MW)
bombeo = np.zeros_like(tiempo_dia)  # Energía bombeada cada hora (en MW)
nivel_agua_hist = [nivel_agua]  # Historial del nivel del embalse

# Simulación de la operación de la planta durante 24 horas
for t in range(24):
    # Simulación de lluvias (aumento del nivel del embalse)
    lluvia = lluvias[t]
    nivel_agua += lluvia * 10000  # Incremento del nivel del embalse por lluvias (escala arbitraria)
    
    # Control de nivel de agua (no debe bajar del nivel mínimo)
    if nivel_agua < nivel_minimo_embalse:
        nivel_agua = nivel_minimo_embalse  # Nivel mínimo de agua para no agotar la fuente

    # Determinar la cantidad de energía a generar y bombear
    if demanda[t] > 0:
        energia_generada = min(demanda[t], capacidad_generacion)  # La energía generada no puede superar la capacidad
        nivel_agua -= energia_generada * volumen_por_MWh / 1000  # Disminuir el nivel del embalse según la energía generada
    else:
        energia_generada = 0

    # Bombeo de agua durante la baja demanda
    if energia_generada < capacidad_generacion:
        energia_bombeada = min(capacidad_bombeo, (capacidad_generacion - energia_generada))  # Bombear el excedente
        nivel_agua += energia_bombeada * volumen_por_MWh / 1000  # Aumentar el nivel del embalse por bombeo
    else:
        energia_bombeada = 0
    
    # Registro de datos para análisis
    generacion[t] = energia_generada
    bombeo[t] = energia_bombeada
    nivel_agua_hist.append(nivel_agua)

# Visualización de los resultados
plt.figure(figsize=(12, 8))

# Gráfico de la demanda de energía
plt.subplot(3, 1, 1)
plt.plot(tiempo_dia, demanda, label='Demanda de Energía (MW)', color='orange')
plt.xlabel('Hora del Día')
plt.ylabel('Demanda (MW)')
plt.title('Demanda de Energía en 24 Horas')
plt.grid(True)

# Gráfico de la energía generada y bombeada
plt.subplot(3, 1, 2)
plt.plot(tiempo_dia, generacion, label='Generación de Energía (MW)', color='blue')
plt.plot(tiempo_dia, bombeo, label='Bombeo de Energía (MW)', color='green')
plt.xlabel('Hora del Día')
plt.ylabel('Energía (MW)')
plt.title('Generación y Bombeo de Energía en 24 Horas')
plt.legend()
plt.grid(True)

# Gráfico del nivel de agua en el embalse
plt.subplot(3, 1, 3)
plt.plot(tiempo_dia, nivel_agua_hist[:-1], label='Nivel del Embalse (m³)', color='red')
plt.xlabel('Hora del Día')
plt.ylabel('Nivel del Embalse (m³)')
plt.title('Nivel de Agua en el Embalse durante 24 Horas')
plt.grid(True)

plt.tight_layout()
plt.show()