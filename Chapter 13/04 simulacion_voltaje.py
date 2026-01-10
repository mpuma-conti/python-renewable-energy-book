import numpy as np
import matplotlib.pyplot as plt

# Parámetros
frecuencia = 50  # Hz
frecuencia_muestreo = 1000  # Hz
tiempo = np.linspace(0, 1, frecuencia_muestreo, endpoint=False)  # 1 segundo

# Señal de voltaje nominal con variaciones
voltaje_nominal = 230
caida = np.where((tiempo > 0.2) & (tiempo < 0.3), 0.7, 1)  # 70% de caída
sobretension = np.where((tiempo > 0.6) & (tiempo < 0.7), 1.3, 1)  # 130% de sobretensión
fluctuacion = 0.05 * np.sin(2 * np.pi * 10 * tiempo)  # Fluctuaciones (10 Hz)
voltaje = voltaje_nominal * (np.sin(2 * np.pi * frecuencia * tiempo) + fluctuacion) * caida * sobretension

# Visualización de la señal
plt.figure(figsize=(10, 4))
plt.plot(tiempo, voltaje, label='Voltaje')
plt.axhline(230, color='r', linestyle='--', label='Voltaje Nominal')
plt.title('Simulación de Variaciones de Voltaje')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.legend()
plt.grid()
plt.show()