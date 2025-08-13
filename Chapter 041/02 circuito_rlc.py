import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parámetros del circuito RLC
R = 100  # resistencia en ohmios
L = 0.5  # inductancia en henrios
C = 1e-6  # capacitancia en faradios

# Definir la función de voltaje de entrada
def V_in(t):
    return 10 * np.sin(1000 * t)  # voltaje sinusoidal

# Sistema de ecuaciones diferenciales para el circuito RLC
def rlc_circuit(y, t, R, L, C):
    I, V_C = y
    dI_dt = (V_in(t) - I * R - V_C) / L
    dV_C_dt = I / C
    return [dI_dt, dV_C_dt]

# Condiciones iniciales
I_0 = 0.0  # corriente inicial
V_C_0 = 0.0  # voltaje inicial en el capacitor
y_0 = [I_0, V_C_0]

# Tiempo de simulación
t = np.linspace(0, 0.01, 1000)  # tiempo en segundos

# Resolver las ecuaciones diferenciales
solution = odeint(rlc_circuit, y_0, t, args=(R, L, C))
I = solution[:, 0]
V_C = solution[:, 1]

# Visualización de los resultados
plt.figure(figsize=(10, 5))
plt.plot(t, I, label="Corriente (I)")
plt.plot(t, V_C, label="Voltaje en el Capacitor (V_C)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Corriente (A) y Voltaje (V)")
plt.title("Respuesta del Circuito RLC en Serie")
plt.legend()
plt.grid()
plt.show()