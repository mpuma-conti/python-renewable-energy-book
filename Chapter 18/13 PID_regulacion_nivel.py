import numpy as np
import matplotlib.pyplot as plt

class PIDController:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.integral = 0
        self.prev_error = 0

    def update(self, measurement, dt):
        error = self.setpoint - measurement
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.prev_error = error
        return output

# Simulación del control del nivel del embalse
time = np.linspace(0, 100, 1000)  # Tiempo en minutos
dt = time[1] - time[0]
nivel_desado = 500  # Nivel deseado del embalse (m³)
nivel_actual = 450  # Nivel inicial del embalse
nivel_historia = []
control_historia = []

pid = PIDController(Kp=2.0, Ki=0.1, Kd=1.0, setpoint=nivel_desado)

for t in time:
    control = pid.update(nivel_actual, dt)
    # Simulación de la respuesta del sistema (aumenta o disminuye el flujo de entrada)
    nivel_actual += control * dt
    nivel_actual = max(nivel_actual, 0)  # Evitar niveles negativos
    nivel_historia.append(nivel_actual)
    control_historia.append(control)

# Visualización de resultados
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time, nivel_historia, label='Nivel del Embalse (m³)')
plt.axhline(y=nivel_desado, color='r', linestyle='--', label='Nivel Deseado')
plt.xlabel('Tiempo (min)')
plt.ylabel('Nivel del Embalse (m³)')
plt.title('Control PID del Nivel del Embalse')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(time, control_historia, label='Señal de Control')
plt.xlabel('Tiempo (min)')
plt.ylabel('Control Output')
plt.title('Señal de Control PID')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()