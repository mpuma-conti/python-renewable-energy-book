import numpy as np

# Parámetros de la red
Z01 = 0.02 + 0.04j  # Impedancia de la línea 0-1
Z12 = 0.03 + 0.05j  # Impedancia de la línea 1-2

# Potencias inyectadas y consumidas (en pu)
S_gen = -0.5 + 0j  # Generación fotovoltaica en el nodo 1 (P + jQ)
S_load = 1.0 + 0.5j  # Carga en el nodo 2 (P + jQ)

# Tensión inicial en la subestación
V0 = 1.0 + 0j  # Nodo 0

# Inicialización de tensiones en los nodos
V1 = V0
V2 = V0

# Método iterativo
tolerancia = 1e-6
error = 1
iteraciones = 0
max_iter = 100

while error > tolerancia and iteraciones < max_iter:
    iteraciones += 1
    V1_prev, V2_prev = V1, V2

    # Nodo 2 (Carga)
    I2 = np.conj(S_load / V2)
    V2 = V1 - Z12 * I2

    # Nodo 1 (Generador)
    I1 = I2 + np.conj(S_gen / V1)
    V1 = V0 - Z01 * I1

    # Calcular el error relativo
    error = max(abs(V1 - V1_prev), abs(V2 - V2_prev))

# Resultados finales
print(f"Tensiones en los nodos:")
print(f"V0 = {abs(V0):.4f} pu, Ángulo = {np.angle(V0, deg=True):.2f}°")
print(f"V1 = {abs(V1):.4f} pu, Ángulo = {np.angle(V1, deg=True):.2f}°")
print(f"V2 = {abs(V2):.4f} pu, Ángulo = {np.angle(V2, deg=True):.2f}°")

# Corrientes en las líneas
I01 = (V0 - V1) / Z01
I12 = (V1 - V2) / Z12

# Pérdidas en las líneas
P_loss_01 = abs(I01)**2 * Z01.real
P_loss_12 = abs(I12)**2 * Z12.real
total_loss = P_loss_01 + P_loss_12

print(f"\nPérdidas en la red:")
print(f"Pérdidas en la línea 0-1: {P_loss_01:.4f} pu")
print(f"Pérdidas en la línea 1-2: {P_loss_12:.4f} pu")
print(f"Pérdidas totales: {total_loss:.4f} pu")

# Balance de potencia
P_supply = abs(S_gen.real) + total_loss
print(f"\nBalance de potencia:")
print(f"Potencia generada + pérdidas: {P_supply:.4f} pu")
print(f"Potencia consumida: {S_load.real:.4f} pu")