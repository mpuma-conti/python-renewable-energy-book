import numpy as np

# Parámetros del sistema
V = 230  # Tensión en voltios (V)
I = 10   # Corriente en amperios (A)
phi = np.radians(30)  # Ángulo de desfase en radianes (30°)

# Cálculo de potencias
P = V * I * np.cos(phi)  # Potencia activa (W)
Q = V * I * np.sin(phi)  # Potencia reactiva (var)
S = V * I               # Potencia aparente (VA)

# Resultados
print(f"Potencia activa (P): {P:.2f} W")
print(f"Potencia reactiva (Q): {Q:.2f} var")
print(f"Potencia aparente (S): {S:.2f} VA")