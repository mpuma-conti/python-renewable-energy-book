import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# Parámetros de la señal
frecuencia_fundamental = 50  # Hz
frecuencia_muestreo = 1000  # Hz
tiempo = np.linspace(0, 0.1, frecuencia_muestreo, endpoint=False)  # 0.1 segundos

# Componentes de la señal
senal_fundamental = np.sin(2 * np.pi * frecuencia_fundamental * tiempo)  # Fundamental
senal_armonico_3 = 0.3 * np.sin(2 * np.pi * 3 * frecuencia_fundamental * tiempo)  # Armónico 3
senal_armonico_5 = 0.2 * np.sin(2 * np.pi * 5 * frecuencia_fundamental * tiempo)  # Armónico 5

# Señal total
senal_total = senal_fundamental + senal_armonico_3 + senal_armonico_5

# Visualización en el dominio del tiempo
plt.figure(figsize=(10, 4))
plt.plot(tiempo, senal_total, label='Señal Total')
plt.title('Señal en el Dominio del Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid()
plt.legend()
plt.show()
