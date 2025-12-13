class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0

    def compute(self, setpoint, measured_value):
        error = setpoint - measured_value
        self.integral += error
        derivative = error - self.prev_error
        self.prev_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative

# Configuración del controlador PID
pid = PIDController(kp=1.0, ki=0.1, kd=0.05)

# Ejemplo de control
setpoint = 100  # Potencia deseada (W)
mediciones = [90, 95, 97, 99, 101, 100]  # Mediciones simuladas

for medida in mediciones:
    control = pid.compute(setpoint, medida)
    print(f"Medida: {medida} W, Salida del controlador: {control:.2f}")