import numpy as np
import matplotlib.pyplot as plt

# Simulación de datos de voltaje en tiempo real
time = np.linspace(0, 10, 1000)  # Tiempo en segundos
voltage = 230 + 5 * np.sin(2 * np.pi * 50 * time)  # Voltaje con ruido

# Graficar los datos simulados
plt.plot(time, voltage)
plt.title("Voltaje Monitoreado por Sensores en la Red")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid()
plt.show()