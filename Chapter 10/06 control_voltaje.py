import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
Kp = 0.8  # Ganancia proporcional
Ki = 0.2  # Ganancia integral
setpoint = 1.0  # Voltaje deseado en pu
dt = 0.1  # Paso de tiempo
tiempo = np.arange(0, 10, dt)

# Variables iniciales
error = 0
integral = 0
voltaje_real = np.zeros_like(tiempo)
carga = 0.8 + 0.1 * np.sin(2 * np.pi * 0.2 * tiempo)  # Simulación de carga variable

# Simulación del controlador PI
for i in range(1, len(tiempo)):
    error = setpoint - carga[i]
    integral += error * dt
    control = Kp * error + Ki * integral
    voltaje_real[i] = carga[i] + control

# Visualización
plt.plot(tiempo, carga, label="Carga")
plt.plot(tiempo, voltaje_real, label="Voltaje Controlado")
plt.axhline(setpoint, color="red", linestyle="--", label="Setpoint")
plt.title("Control Automático de Voltaje (PI)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (pu)")
plt.legend()
plt.grid()
plt.show()