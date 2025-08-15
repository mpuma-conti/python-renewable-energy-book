import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la batería
capacidad = 100  # Capacidad en kWh
soc_inicial = 0.8  # Estado inicial de carga (80%)
eficiencia = 0.95  # Eficiencia de carga/descarga

# Tasa de carga/descarga (kW)
carga = np.linspace(-20, 20, 50)

# Cálculo del estado de carga después de una hora
soc = soc_inicial + (carga / capacidad) * eficiencia

# Limitar el SoC entre 0 y 1
soc = np.clip(soc, 0, 1)

# Visualización
plt.figure(figsize=(10, 5))
plt.plot(carga, soc, label="Estado de Carga (SoC)")
plt.axhline(1, color='r', linestyle='--', label="Carga Máxima")
plt.axhline(0, color='b', linestyle='--', label="Carga Mínima")
plt.xlabel("Tasa de carga/descarga (kW)")
plt.ylabel("Estado de Carga (SoC)")
plt.title("Estado de Carga en una Batería de 100 kWh")
plt.legend()
plt.grid()
plt.show()