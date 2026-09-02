import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
num_steps = 100  # Número de pasos de tiempo
V = np.linspace(0, 40, num_steps)  # Rango de voltaje (V)
I = 10 - 0.2 * V  # Curva de corriente (A), ejemplo lineal
P = V * I  # Potencia (W)

# Inicialización del algoritmo P&O
V_prev = 0
P_prev = 0
delta_V = 1  # Incremento de voltaje (V)
V_opt = 0
P_opt = 0

V_trace = []
P_trace = []

for i in range(num_steps):
    # Simulación del punto de operación
    V_current = V_prev + delta_V
    if V_current > V[-1]:
        V_current = V[-1]
    
    # Obtener la potencia en el voltaje actual
    I_current = 10 - 0.2 * V_current  # Curva de corriente (A)
    P_current = V_current * I_current  # Potencia (W)
    
    # Almacenar trazas para visualización
    V_trace.append(V_current)
    P_trace.append(P_current)
    
    # Comparar la potencia actual con la anterior
    if P_current > P_prev:
        V_opt = V_current
        P_opt = P_current
        # Si la potencia aumenta, continuar en la misma dirección
    else:
        # Si la potencia disminuye, cambiar la dirección
        delta_V = -delta_V
        V_current = V_prev + delta_V
        I_current = 10 - 0.2 * V_current
        P_current = V_current * I_current
        V_trace.append(V_current)
        P_trace.append(P_current)
    
    # Actualizar valores para el siguiente paso
    V_prev = V_current
    P_prev = P_current

# Visualización de resultados
plt.figure(figsize=(12, 6))

# Curva de Potencia vs Voltaje
plt.subplot(1, 2, 1)
plt.plot(V, P, label='Curva de Potencia')
plt.scatter(V_opt, P_opt, color='red', label='Punto Óptimo')
plt.title('Curva de Potencia vs Voltaje')
plt.xlabel('Voltaje (V)')
plt.ylabel('Potencia (W)')
plt.legend()
plt.grid(True)

# Trazas del Algoritmo P&O
plt.subplot(1, 2, 2)
plt.plot(V_trace, P_trace, marker='o', linestyle='-', color='green', label='Algoritmo P&O')
plt.scatter(V_opt, P_opt, color='red', label='Punto Óptimo')
plt.title('Evolución del Algoritmo P&O')
plt.xlabel('Voltaje (V)')
plt.ylabel('Potencia (W)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

print(f"Punto de máxima potencia: V = {V_opt:.2f} V, P = {P_opt:.2f} W")