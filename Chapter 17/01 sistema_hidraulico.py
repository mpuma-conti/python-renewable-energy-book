import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
rho = 1000  # Densidad del agua (kg/m^3)
g = 9.81  # Aceleración debido a la gravedad (m/s^2)
h = 50  # Altura de caída (m)
A = 5  # Área del conducto (m^2)
v = 2  # Velocidad del agua (m/s)
Q = A * v  # Caudal (m^3/s)

# Cálculo de la energía potencial en el embalse
E_potencial = rho * g * h * Q  # Energía potencial en (J/s o Watts)

# Cálculo de la energía cinética en el flujo
E_cinetica = 0.5 * rho * v**2 * Q  # Energía cinética en (J/s o Watts)

# Energía total disponible para la turbina
E_total = E_potencial + E_cinetica

# Mostrar resultados
print(f"Energía potencial: {E_potencial} W")
print(f"Energía cinética: {E_cinetica} W")
print(f"Energía total disponible: {E_total} W")

# Graficar la energía total en función de la velocidad
velocidades = np.linspace(1, 10, 10)
E_totales = 0.5 * rho * velocidades**2 * Q + rho * g * h * Q

plt.plot(velocidades, E_totales, label="Energía total")
plt.xlabel("Velocidad del flujo (m/s)")
plt.ylabel("Energía total (W)")
plt.title("Energía total disponible para la turbina en función de la velocidad del flujo")
plt.legend()
plt.show()