import numpy as np

# Parámetros
energia_bateria = 50  # Capacidad total de la batería en kWh
energia_disponible = 20  # Energía inicial disponible en kWh
demanda_red = [0, 5, 10, 15, 10, 5, 0]  # kW por hora durante 7 horas

# Función para decidir flujo de energía
def v2g_control(energia_disponible, demanda_red):
    flujo_energia = []
    for demanda in demanda_red:
        if demanda > 0 and energia_disponible > 0:
            energia_a_entregar = min(demanda, energia_disponible)
            flujo_energia.append(-energia_a_entregar)  # Energía entregada a la red
            energia_disponible -= energia_a_entregar
        else:
            flujo_energia.append(0)  # No hay entrega
    return flujo_energia

# Calcular flujo de energía
flujo = v2g_control(energia_disponible, demanda_red)

# Resultados
print("Flujo de energía hacia la red (kW):", flujo)