# Parámetros del sistema trifásico
V_L = 400  # Tensión de línea (V)
I_L = 15   # Corriente de línea (A)
phi = np.radians(20)  # Ángulo de desfase en radianes (20°)

# Cálculo de potencias
P = np.sqrt(3) * V_L * I_L * np.cos(phi)  # Potencia activa (W)
Q = np.sqrt(3) * V_L * I_L * np.sin(phi)  # Potencia reactiva (var)
S = np.sqrt(P**2 + Q**2)                  # Potencia aparente (VA)

# Resultados
print(f"Potencia activa (P): {P:.2f} W")
print(f"Potencia reactiva (Q): {Q:.2f} var")
print(f"Potencia aparente (S): {S:.2f} VA")