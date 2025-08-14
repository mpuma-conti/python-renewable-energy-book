import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo: demanda de energía (kW) y generación eólica (kW)
demanda = np.array([1000, 1200, 1500, 1700, 1800, 1900, 2000, 1800, 1600, 1400, 1300, 1200])  # Demanda horaria
generacion_eolica = np.array([200, 300, 450, 600, 700, 750, 800, 700, 600, 500, 400, 300])  # Generación horaria

# Calcular el déficit o sobrante de energía
deficit_sobrante = demanda - generacion_eolica

# Asumir que la energía de respaldo proviene de una planta térmica o almacenamiento
energia_respaldo = np.maximum(deficit_sobrante, 0)  # Si hay déficit, usar respaldo

# Visualización
plt.figure(figsize=(10, 6))
plt.plot(demanda, label='Demanda de Energía (kW)', color='b')
plt.plot(generacion_eolica, label='Generación Eólica (kW)', color='g')
plt.plot(energia_respaldo, label='Energía de Respaldo (kW)', color='r', linestyle='--')
plt.title('Integración de Energía Eólica en la Red Eléctrica')
plt.xlabel('Hora del Día')
plt.ylabel('Potencia (kW)')
plt.legend()
plt.grid(True)
plt.show()