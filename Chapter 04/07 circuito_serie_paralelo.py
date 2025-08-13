import numpy as np

# Parámetros del circuito
V = 10  # voltaje de la fuente en voltios
R1 = 100  # resistencia en ohmios
R2 = 200  # resistencia en ohmios
R3 = 150  # resistencia en ohmios

# Construcción de la matriz de conductancias
G = np.array([[1/R1 + 1/R2, -1/R2], [-1/R2, 1/R2 + 1/R3]])

# Matriz de voltajes
V_matrix = np.array([V/R1, 0])

# Resolución de las corrientes
I = np.linalg.solve(G, V_matrix)

print(f"Corriente en R1: {I[0]:.4f} A")
print(f"Corriente en R2: {I[0] - I[1]:.4f} A")
print(f"Corriente en R3: {I[1]:.4f} A")