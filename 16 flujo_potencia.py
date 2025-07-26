import numpy as np

# Parámetros de la red
Z01 = 0.05 + 0.1j  # Impedancia Nodo 0-1 (pu)
Z12 = 0.02 + 0.04j  # Impedancia Nodo 1-2 (pu)
Z23 = 0.01 + 0.03j  # Impedancia Nodo 2-3 (pu)

# Potencias de carga (pu)
S1 = 0.5 + 0.3j  # Nodo 1
S2 = 0.4 + 0.2j  # Nodo 2
S3 = 0.3 + 0.15j  # Nodo 3

# Inicialización de tensiones
V0 = 1 + 0j  # Tensión de referencia en la subestación (Nodo 0)
V = np.zeros(4, dtype=complex)  # Tensiones iniciales
V[0] = V0

# Método iterativo de caída de tensión
tolerancia = 1e-6
error = 1
iteraciones = 0
max_iter = 100

while error > tolerancia and iteraciones < max_iter:
    iteraciones += 1
    V_prev = V.copy()
    
    # Cálculo de tensiones en los nodos
    V[3] = V[2] - Z23 * np.conj(S3 / V[2])  # Nodo 3
    V[2] = V[1] - Z12 * np.conj((S2 + S3) / V[1])  # Nodo 2
    V[1] = V[0] - Z01 * np.conj((S1 + S2 + S3) / V[0])  # Nodo 1
    
    # Error relativo
    error = np.max(np.abs(V - V_prev))

# Resultados finales
print("Tensiones en los nodos:")
for i, v in enumerate(V):
    print(f"V{i} = {abs(v):.4f} pu, Ángulo = {np.angle(v, deg=True):.2f}°")