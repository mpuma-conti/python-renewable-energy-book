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

# Simulación del control de flujo de agua
time = np.linspace(0, 10, 100)  # Tiempo en segundos
dt = time[1] - time[0]
flow_desired = 100  # Flow rate desired (m³/s)
flow_actual = 0
flow_history = []
control_history = []

pid = PIDController(Kp=2.0, Ki=0.5, Kd=1.0, setpoint=flow_desired)

for t in time:
    control = pid.update(flow_actual, dt)
    # Simulación de la respuesta del sistema (simple integrador)
    flow_actual += control * dt
    flow_actual = max(flow_actual, 0)  # Flow cannot be negative
    flow_history.append(flow_actual)
    control_history.append(control)

# Visualización de resultados
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time, flow_history, label='Flow Actual (m³/s)')
plt.plot(time, [flow_desired]*len(time), 'r--', label='Flow Desired (m³/s)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Flujo de Agua (m³/s)')
plt.title('Control PID del Flujo de Agua')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(time, control_history, label='Señal de Control')
plt.xlabel('Tiempo (s)')
plt.ylabel('Control Output')
plt.title('Señal de Control PID')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()