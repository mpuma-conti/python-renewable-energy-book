import numpy as np

# Parámetros del sistema
capacidad_bateria = 100  # Capacidad total en kWh
soc = 50  # Estado inicial de carga (kWh)
soc_min = 20  # Límite mínimo del SOC
soc_max = 80  # Límite máximo del SOC
produccion_renovable = np.random.uniform(10, 50, 24)  # Producción renovable simulada (kWh/h)
demanda = np.random.uniform(20, 40, 24)  # Demanda simulada (kWh/h)

# Gestión inteligente
soc_historico = []
acciones = []

for i in range(len(produccion_renovable)):
    energia_disponible = produccion_renovable[i] - demanda[i]

    if energia_disponible > 0 and soc < soc_max:  # Carga la batería
        carga = min(energia_disponible, soc_max - soc)
        soc += carga
        accion = f"Carga {carga:.2f} kWh"
    elif energia_disponible < 0 and soc > soc_min:  # Descarga la batería
        descarga = min(abs(energia_disponible), soc - soc_min)
        soc -= descarga
        accion = f"Descarga {descarga:.2f} kWh"
    else:
        accion = "Sin acción"

    soc_historico.append(soc)
    acciones.append(accion)

# Resultados
for i, accion in enumerate(acciones):
    print(f"Hora {i+1}: {accion} - SOC: {soc_historico[i]:.2f} kWh")