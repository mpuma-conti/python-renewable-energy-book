import numpy as np
import matplotlib.pyplot as plt

# Parámetros del circuito
V = 10  # voltaje de entrada en voltios
R = 100  # resistencia en ohmios
L = 0.05  # inductancia en henrios
C = 1e-6  # capacitancia en faradios

# Rango de frecuencias
frecuencias = np.linspace(50, 1000, 500)  # en Hz
I_magnitudes = []

for f in frecuencias:
    omega = 2 * np.pi * f
    Z = R + 1j * omega * L - 1j / (omega * C)
    I = V / Z  # corriente en el circuito
    I_magnitudes.append(abs(I))

# Visualización de la respuesta en frecuencia
plt.plot(frecuencias, I_magnitudes)
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud de la Corriente (A)")
plt.title("Análisis en Frecuencia de un Circuito RLC en Serie")
plt.grid()
plt.show()