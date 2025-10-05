from simple_pid import PID

# Configuración del controlador PID
pid = PID(1, 0.1, 0.05, setpoint=50)
output = pid(45)  # Entrada de medición actual
print(f"Control de salida para mantener la frecuencia: {output}")