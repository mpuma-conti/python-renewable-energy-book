import numpy as np
import matplotlib.pyplot as plt

# Parámetros del circuito RC
R = 1000  # resistencia en ohmios
C = 1e-6  # capacitancia en faradios
tau = R * C  # constante de tiempo del circuito RC

# Configuración de la simulación
t_final = 0.05  # tiempo final en segundos
dt = 0.0001  # paso de tiempo en segundos
t = np.arange(0, t_final, dt)  # vector de tiempo

# Señal de entrada (voltaje de entrada)
V_in = 5  # voltaje constante en voltios

# Vector de voltaje en el capacitor
V_c = np.zeros_like(t)

# Simulación utilizando un método de Euler
for i in range(1, len(t)):
    dVc_dt = (V_in - V_c[i-1]) / tau
    V_c[i] = V_c[i-1] + dVc_dt * dt

# Visualización de los resultados
plt.figure(figsize=(10, 5))
plt.plot(t, V_c, label="Voltaje en el capacitor $V_c$")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.title("Respuesta del Voltaje en un Circuito RC")
plt.legend()
plt.grid()
plt.show()