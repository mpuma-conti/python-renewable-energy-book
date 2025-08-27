import numpy as np
import matplotlib.pyplot as plt

# Datos simulados
dias = np.arange(1, 31)  # 30 días
produccion_solar = np.random.uniform(20, 50, len(dias))  # Producción variable en kWh
demanda_diaria = 40  # Demanda constante en kWh
almacenamiento = 100  # Capacidad del sistema de almacenamiento en kWh
estado_bateria = 50  # Estado inicial de carga en kWh

# Variables para simulación
energia_excedente = []
energia_faltante = []
estado_bateria_dia = []

# Simulación diaria
for produccion in produccion_solar:
    # Energía disponible y déficit
    energia_disponible = produccion + estado_bateria
    deficit = demanda_diaria - energia_disponible

    # Actualización de batería
    if deficit > 0:
        estado_bateria -= abs(deficit)  # Se descarga la batería
        energia_faltante.append(abs(deficit))
        energia_excedente.append(0)
    else:
        energia_excedente.append(abs(deficit))
        estado_bateria = min(almacenamiento, estado_bateria + abs(deficit))  # Se carga la batería
        energia_faltante.append(0)

    estado_bateria_dia.append(estado_bateria)

# Gráficos de resultados
plt.figure(figsize=(10, 6))
plt.plot(dias, produccion_solar, label="Producción Solar (kWh)")
plt.axhline(y=demanda_diaria, color='r', linestyle='--', label="Demanda Diaria (kWh)")
plt.plot(dias, estado_bateria_dia, label="Estado de la Batería (kWh)")
plt.fill_between(dias, 0, energia_excedente, color='green', alpha=0.3, label="Energía Excedente")
plt.fill_between(dias, 0, energia_faltante, color='orange', alpha=0.3, label="Déficit Energético")
plt.title("Simulación de Integración Solar con Almacenamiento")
plt.xlabel("Días")
plt.ylabel("Energía (kWh)")
plt.legend()
plt.grid(True)
plt.show()