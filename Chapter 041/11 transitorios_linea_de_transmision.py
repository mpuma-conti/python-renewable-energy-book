import scipy.integrate as spi
import matplotlib.pyplot as plt
import numpy as np

# Parámetros del circuito
R = 10  # Resistencia (ohmios)
L = 0.1  # Inductancia (henrios)
C = 0.001  # Capacitancia (faradios)
V0 = 100  # Voltaje inicial (V)

# Función diferencial: d²v/dt² + (R/L) * dv/dt + (1/LC) * v = 0
def transient_response(v, t):
    dv_dt = v[1]
    d2v_dt2 = -(R/L) * v[1] - (1/(L*C)) * v[0]
    return [dv_dt, d2v_dt2]

# Condiciones iniciales
v0 = [V0, 0]  # [Tensión inicial, Derivada inicial]

# Tiempo de simulación
t = np.linspace(0, 0.01, 1000)  # 10 ms, 1000 puntos

# Solución
v = spi.odeint(transient_response, v0, t)

# Gráfica
plt.figure(figsize=(8, 5))
plt.plot(t, v[:, 0], label="Tensión en la línea $V(t)$")
plt.xlabel("Tiempo (s)")
plt.ylabel("Tensión (V)")
plt.title("Respuesta transitoria en una línea de transmisión")
plt.grid()
plt.legend()
plt.show()