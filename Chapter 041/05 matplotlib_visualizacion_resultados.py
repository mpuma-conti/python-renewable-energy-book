import matplotlib.pyplot as plt

# Ejemplo de visualización de una señal de onda sinusoidal de voltaje
frecuencia = 50  # Hz
amplitud = 10  # voltios
t = np.linspace(0, 0.1, 1000)
V_senal = amplitud * np.sin(2 * np.pi * frecuencia * t)

plt.plot(t, V_senal)
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.title("Señal de Voltaje Sinusoidal")
plt.grid()
plt.show()