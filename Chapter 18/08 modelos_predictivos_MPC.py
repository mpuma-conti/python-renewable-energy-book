import numpy as np
import matplotlib.pyplot as plt
from casadi import *

# Parámetros del sistema
dt = 1.0  # Tiempo de muestreo
N = 10  # Horizonte de predicción
flow_desired = 100  # Flow rate desired (m³/s)

# Definición de variables
x = SX.sym('x')  # Flow actual
u = SX.sym('u')  # Control (adjustment to flow)
x_next = x + u * dt  # Modelo simple de flujo

# Definición del problema de optimización
model = Function('model', [x, u], [x_next])

# Definición del problema de MPC
opti = Opti()
X = opti.variable(N+1)
U = opti.variable(N)
X0 = opti.parameter()
opti.subject_to(X[0] == X0)

for k in range(N):
    opti.subject_to(X[k+1] == model(X[k], U[k]))
    opti.subject_to(U[k] >= -10)  # Límites de control
    opti.subject_to(U[k] <= 10)

# Objetivo: minimizar la desviación del flujo deseado
opti.minimize(sum1((X[1:N+1] - flow_desired)**2) + sum1(U**2))

# Configuración del solver
opti.solver('ipopt')

# Simulación del sistema
sim_time = 50
flow_actual = 90  # Estado inicial
flow_history = [flow_actual]
control_history = []

for t in range(sim_time):
    opti.set_value(X0, flow_actual)
    sol = opti.solve()
    u_opt = sol.value(U[0])
    flow_actual = sol.value(X[1])
    flow_history.append(flow_actual)
    control_history.append(u_opt)
    opti.set_initial(X, sol.value(X))
    opti.set_initial(U, sol.value(U))

# Visualización de resultados
time = np.arange(0, sim_time+1, 1)
control_time = np.arange(0, sim_time, 1)

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time, flow_history, label='Flow Actual (m³/s)')
plt.plot(time, [flow_desired]*len(time), 'r--', label='Flow Desired (m³/s)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Flujo de Agua (m³/s)')
plt.title('Control MPC del Flujo de Agua')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(control_time, control_history, label='Señal de Control')
plt.xlabel('Tiempo (s)')
plt.ylabel('Control Output')
plt.title('Señal de Control MPC')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()