import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parámetros de la simulación
fs = 1000  # Frecuencia de muestreo (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # Tiempo de un segundo
f = 50  # Frecuencia de la red (Hz)
V_ref = 230  # Voltaje de referencia (V)

# Señal de entrada (Voltaje CC simulado)
V_cc = 400  # Voltaje CC de entrada al inversor

# Controlador PID para la regulación de voltaje
Kp = 0.1
Ki = 1.0
Kd = 0.01
integral = 0
previous_error = 0

# Generación de la señal de CA con control de voltaje
V_ac = []
for i in range(len(t)):
    # Señal senoidal de referencia
    V_sin = V_ref * np.sin(2 * np.pi * f * t[i])
    
    # Simulación de medición del voltaje
    V_meas = V_ref * np.sin(2 * np.pi * f * t[i] + 0.1)  # Introduce una pequeña desviación
    
    # Cálculo del error
    error = V_ref - V_meas
    integral += error / fs
    derivative = (error - previous_error) * fs
    control_signal = Kp * error + Ki * integral + Kd * derivative
    previous_error = error
    
    # Ajuste del voltaje CC basado en la señal de control
    V_adjusted = V_cc + control_signal
    V_adjusted = np.clip(V_adjusted, 300, 500)  # Limitar el voltaje CC ajustado
    
    # Generación de la señal de CA
    V_out = (V_adjusted / V_cc) * V_sin
    V_ac.append(V_out)

# Visualización de resultados
plt.figure(figsize=(12, 6))

# Señal de referencia vs Señal medida
plt.subplot(2, 1, 1)
plt.plot(t, V_ref * np.sin(2 * np.pi * f * t), label='Referencia (V_ref)', color='orange')
plt.plot(t, V_ac, label='Salida del Inversor (V_ac)', color='blue', alpha=0.7)
plt.title('Control de Voltaje del Inversor')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.legend()
plt.grid(True)

# Respuesta en frecuencia del sistema
plt.subplot(2, 1, 2)
w, mag, phase = signal.bode(signal.TransferFunction([1], [1, 1, 1]))
plt.semilogx(w, mag)  # Magnitud
plt.title('Respuesta en Frecuencia del Controlador PID')
plt.xlabel('Frecuencia (rad/s)')
plt.ylabel('Magnitud (dB)')
plt.grid(True)

plt.tight_layout()
plt.show()