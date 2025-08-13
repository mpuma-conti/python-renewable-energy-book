import numpy as np

# Definir resistencia, capacitancia e inductancia
R = 100  # ohmios
C = 1e-6  # faradios
L = 0.5  # henrios

# Cálculo de impedancia en un circuito RLC en serie a diferentes frecuencias
frecuencias = np.linspace(10, 10000, 100)  # 10 Hz a 10 kHz
Z_RLC = np.sqrt(R**2 + (2 * np.pi * frecuencias * L - 1 / (2 * np.pi * frecuencias * C))**2)

# Visualización de resultados
import matplotlib.pyplot as plt
plt.plot(frecuencias, Z_RLC)
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Impedancia (Ohmios)")
plt.title("Impedancia de un Circuito RLC en Serie")
plt.grid()
plt.show()