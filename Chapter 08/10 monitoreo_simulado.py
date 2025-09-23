import numpy as np

# Simulación de datos de consumo por hora
horas = np.arange(24)
consumo_horario = np.random.uniform(100, 500, 24)

# Identificación de picos de consumo
pico_consumo = consumo_horario.max()
hora_pico = horas[consumo_horario.argmax()]

print(f"Consumo máximo: {pico_consumo:.2f} kWh a la hora {hora_pico}")