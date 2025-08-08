import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
P_nom = 5.0  # Capacidad nominal del sistema (kW)
efficiency = 0.85  # Eficiencia del sistema

# Irradiancia a lo largo del día (en W/m^2)
time = np.linspace(0, 24, 100)  # Tiempo en horas
irradiance = np.maximum(0, 1000 * np.sin(np.pi * time / 24))  # Simulación de irradiancia

# Potencia generada (kW)
P_gen = (irradiance / 1000) * P_nom * efficiency

# Energía generada (kWh)
E = np.trapz(P_gen, time)

# Gráfica de potencia generada
plt.figure(figsize=(8, 5))
plt.plot(time, P_gen, label="Potencia Generada (kW)")
plt.fill_between(time, P_gen, alpha=0.3, label=f"Energía Generada: {E:.2f} kWh")
plt.xlabel("Tiempo (horas)")
plt.ylabel("Potencia (kW)")
plt.title("Potencia Generada a lo Largo del Día")
plt.legend()
plt.grid()
plt.show()

print(f"Energía total generada en un día: {E:.2f} kWh")