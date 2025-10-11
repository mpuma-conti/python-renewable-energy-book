import numpy as np
import matplotlib.pyplot as plt

# Generar datos de velocidad del viento
np.random.seed(42)
time = np.arange(0, 24, 0.1)  # Tiempo en horas
wind_speed = 10 + 3 * np.sin(2 * np.pi * time / 24) + np.random.normal(0, 0.5, len(time))

# Potencia generada (relación no lineal con la velocidad del viento)
power_output = np.maximum(0, (wind_speed - 3)**3 / (12 - 3)**3 * 50)  # MW

# Graficar resultados
plt.figure(figsize=(10, 5))
plt.plot(time, wind_speed, label="Velocidad del Viento (m/s)")
plt.plot(time, power_output, label="Potencia Generada (MW)", linestyle="--")
plt.title("Variabilidad del Viento y Generación Eólica")
plt.xlabel("Tiempo (horas)")
plt.ylabel("Velocidad / Potencia")
plt.legend()
plt.grid()
plt.show()