import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
num_steps = 1440  # Simulación por minuto durante 24 horas
tiempo = np.arange(0, 24, 24/num_steps)  # Tiempo en horas

# Simulación de la posición solar (ángulos de elevación y azimut)
elevacion = 90 * np.sin(np.pi * (tiempo - 6) / 12)  # Elevación máxima a mediodía
azimut = 180 * (1 + np.sin(np.pi * (tiempo - 6) / 12))  # Azimut desde 0° al amanecer a 360° al atardecer

# Inicialización de los ángulos actuales de los paneles
angulo_elevacion = 0
angulo_azimut = 0
errores_elevacion = []
errores_azimut = []

# Parámetros del controlador PID
Kp = 0.1
Ki = 0.01
Kd = 0.05
error_prev_elev = 0
error_sum_elev = 0
error_prev_azimut = 0
error_sum_azimut = 0

# Registro de ángulos para visualización
registro_elevacion = []
registro_azimut = []

for t in range(num_steps):
    # Calcular el error entre la posición actual del panel y la posición solar
    error_elev = elevacion[t] - angulo_elevacion
    error_sum_elev += error_elev
    delta_error_elev = error_elev - error_prev_elev
    
    error_azimut = azimut[t] - angulo_azimut
    error_sum_azimut += error_azimut
    delta_error_azimut = error_azimut - error_prev_azimut
    
    # Control PID para elevación
    control_elev = Kp * error_elev + Ki * error_sum_elev + Kd * delta_error_elev
    
    # Control PID para azimut
    control_azimut = Kp * error_azimut + Ki * error_sum_azimut + Kd * delta_error_azimut
    
    # Actualizar los ángulos de los paneles
    angulo_elevacion += control_elev
    angulo_azimut += control_azimut
    
    # Limitar los ángulos a rangos físicos (0° a 90° para elevación, 0° a 360° para azimut)
    angulo_elevacion = np.clip(angulo_elevacion, 0, 90)
    angulo_azimut = angulo_azimut % 360
    
    # Registrar los datos
    registro_elevacion.append(angulo_elevacion)
    registro_azimut.append(angulo_azimut)
    
    # Actualizar errores previos
    error_prev_elev = error_elev
    error_prev_azimut = error_azimut

# Visualización de resultados
plt.figure(figsize=(14, 6))

# Elevación solar vs Elevación del panel
plt.subplot(2, 1, 1)
plt.plot(tiempo, elevacion, label='Elevación Solar (°)', color='orange')
plt.plot(tiempo, registro_elevacion, label='Elevación del Panel (°)', color='blue', linestyle='--')
plt.title('Control de Elevación del Panel Solar')
plt.xlabel('Tiempo (horas)')
plt.ylabel('Ángulo de Elevación (°)')
plt.legend()
plt.grid(True)

# Azimut solar vs Azimut del panel
plt.subplot(2, 1, 2)
plt.plot(tiempo, azimut, label='Azimut Solar (°)', color='green')
plt.plot(tiempo, registro_azimut, label='Azimut del Panel (°)', color='red', linestyle='--')
plt.title('Control de Azimut del Panel Solar')
plt.xlabel('Tiempo (horas)')
plt.ylabel('Ángulo de Azimut (°)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()