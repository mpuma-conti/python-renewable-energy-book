import numpy as np
import matplotlib.pyplot as plt

# Parámetros de simulación
num_vehiculos = 50
carga_por_vehiculo = 7.4  # kW (cargador típico)
horas_carga = np.random.normal(20, 2, num_vehiculos)  # Hora de inicio de carga (media: 8 PM)
duracion_carga = 4  # Horas de carga por vehículo
horas = np.arange(0, 24, 1)  # Horas del día
carga_total = np.zeros_like(horas)

# Calcular carga acumulada
for hora in horas_carga:
    inicio = int(max(hora, 0))
    fin = int(min(inicio + duracion_carga, 24))
    carga_total[inicio:fin] += carga_por_vehiculo

# Visualización
plt.plot(horas, carga_total, label="Demanda de VE")
plt.axhline(300, color="red", linestyle="--", label="Capacidad del transformador (kW)")
plt.title("Simulación de Carga de Vehículos Eléctricos")
plt.xlabel("Hora del día")
plt.ylabel("Demanda (kW)")
plt.legend()
plt.grid()
plt.show()