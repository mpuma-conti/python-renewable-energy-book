import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
horas = np.arange(0, 24, 1)  # 24 horas
radiacion_solar = [0, 0, 0, 50, 200, 400, 600, 800, 900, 950, 1000, 900, 800, 600, 400, 200, 50, 0, 0, 0, 0, 0, 0, 0]
velocidad_viento = [5, 6, 5, 7, 10, 12, 15, 20, 18, 17, 14, 12, 10, 8, 7, 6, 5, 4, 3, 3, 2, 2, 2, 2]

# Modelos de generación (simples)
potencia_solar = [r * 0.2 for r in radiacion_solar]  # Paneles solares con eficiencia del 20%
potencia_eolica = [v**3 * 0.5 if v > 3 else 0 for v in velocidad_viento]  # Potencia proporcional al cubo de la velocidad

# Suma de la generación
potencia_total = [solar + eolica for solar, eolica in zip(potencia_solar, potencia_eolica)]

# Visualización
plt.plot(horas, potencia_solar, label='Solar (kW)')
plt.plot(horas, potencia_eolica, label='Eólica (kW)')
plt.plot(horas, potencia_total, label='Total (kW)', linestyle='--')
plt.xlabel('Hora del día')
plt.ylabel('Potencia (kW)')
plt.title('Simulación de Generación Híbrida')
plt.legend()
plt.grid()
plt.show()