import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la celda solar
Iph = 5.0  # Corriente fotogenerada (A)
I0 = 1e-10  # Corriente de saturación inversa (A)
n = 1.3  # Factor de idealidad del diodo
Rs = 0.01  # Resistencia serie (ohmios)
Rp = 100.0  # Resistencia paralela (ohmios)
T = 298.15  # Temperatura (K)
k = 1.380649e-23  # Constante de Boltzmann (J/K)
q = 1.60217663e-19  # Carga del electrón (C)
Vt = n * (k * T / q)  # Voltaje térmico (V)

# Rango de voltajes
V = np.linspace(0, 0.8, 1000)

# Ecuación de corriente
def calculate_current(V):
    return Iph - I0 * (np.exp((V + Rs * Iph) / Vt) - 1) - (V + Rs * Iph) / Rp

I = calculate_current(V)

# Gráfica de la curva IV
plt.figure(figsize=(8, 5))
plt.plot(V, I, label="Curva IV")
plt.xlabel("Voltaje (V)")
plt.ylabel("Corriente (I)")
plt.title("Curva IV de una Celda Solar")
plt.grid(True)
plt.legend()
plt.show()