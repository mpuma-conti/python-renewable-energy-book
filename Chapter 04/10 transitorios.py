import numpy as np
import matplotlib.pyplot as plt

# Parámetros del circuito
V = 5  # Voltaje de la fuente (V)
R = 1000  # Resistencia (ohmios)
C = 0.001  # Capacitancia (faradios)
tau = R * C  # Constante de tiempo

# Tiempo de simulación
t = np.linspace(0, 0.01, 1000)  # 10 ms, 1000 puntos

# Tensión en el capacitor
Vc = V * (1 - np.exp(-t / tau))

# Visualización
plt.figure(figsize=(8, 5))
plt.plot(t, Vc, label="Tensión en el capacitor $V_c(t)$")
plt.axhline(V, color='r', linestyle='--', label="Voltaje de la fuente ($V$)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Tensión (V)")
plt.title("Carga de un capacitor en un circuito RC")
plt.legend()
plt.grid()
plt.show()