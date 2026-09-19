import casadi as ca
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
dt = 1.0  # Tiempo de muestreo (minutos)
N = 10  # Horizonte de predicción (minutos)
flow_total = 500  # Flow rate total disponible (m³/s)
flow_min = 50  # Flow rate mínimo por turbina (m³/s)
flow_max = 150  # Flow rate máximo por turbina (m³/s)
num_turbinas = 3  # Número de turbinas

# Definición de variables
opti = ca.Opti()

# Variables de decisión: flujos a través de cada turbina en cada paso
flows = opti.variable(N, num_turbinas)

# Estado inicial
flow_initial = 100  # Flow rate inicial por turbina (m³/s)

# Definición de las restricciones
for k in range(N):
    # Cada flujo debe estar dentro de los límites
    opti.subject_to(flows[k, :] >= flow_min)
    opti.subject_to(flows[k, :] <= flow_max)
    # Suma de flujos debe ser igual al flujo total disponible
    opti.subject_to(ca.sum1(flows[k, :]) == flow_total)

# Objetivo: minimizar la variación de los flujos
objective = 0
for k in range(N):
    for i in range(num_turbinas):
        if k == 0:
            objective += (flows[k, i] - flow_initial)**2
        else:
            objective += (flows[k, i] - flows[k-1, i])**2

opti.minimize(objective)

# Configuración del solver
opti.solver('ipopt')

# Resolución del problema
sol = opti.solve()

# Extracción de los flujos optimizados
flows_opt = sol.value(flows)

# Visualización de resultados
time = np.arange(1, N+1)

plt.figure(figsize=(12, 6))
for i in range(num_turbinas):
    plt.plot(time, flows_opt[:, i], label=f'Turbina {i+1}')
plt.axhline(y=flow_min, color='r', linestyle='--', label='Flow Min')
plt.axhline(y=flow_max, color='g', linestyle='--', label='Flow Max')
plt.xlabel('Tiempo (min)')
plt.ylabel('Flow Rate (m³/s)')
plt.title('Optimización de Flujos de Agua con Control Predictivo')
plt.legend()
plt.grid(True)
plt.show()