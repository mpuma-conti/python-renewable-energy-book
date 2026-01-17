import numpy as np
import matplotlib.pyplot as plt

# Parámetros
frecuencia = 50  # Hz
frecuencia_muestreo = 1000  # Hz
tiempo = np.linspace(0, 1, frecuencia_muestreo, endpoint=False)  # 1 segundo

# Tensiones trifásicas con un pequeño desbalance
V_nominal = 230
fase_A = V_nominal * np.sin(2 * np.pi * frecuencia * tiempo)
fase_B = V_nominal * np.sin(2 * np.pi * frecuencia * tiempo - np.pi/6)  # Desfase de 30 grados
fase_C = V_nominal * np.sin(2 * np.pi * frecuencia * tiempo + np.pi/3)  # Desfase de -60 grados

# Visualización de las tensiones
plt.figure(figsize=(10, 6))
plt.plot(tiempo, fase_A, label='Fase A')
plt.plot(tiempo, fase_B, label='Fase B')
plt.plot(tiempo, fase_C, label='Fase C')
plt.title('Tensiones Trifásicas con Desbalanceo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.legend()
plt.grid()
plt.show()