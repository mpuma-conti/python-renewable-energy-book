import RPi.GPIO as GPIO
import time

# Configuración del pin del actuador
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)  # Pin conectado al motor del ajuste de pitch

# Control del motor
def mover_motor(angulo):
    print(f"Ajustando ángulo a {angulo} grados...")
    GPIO.output(18, GPIO.HIGH)
    time.sleep(angulo / 10)  # Simulación del tiempo requerido
    GPIO.output(18, GPIO.LOW)

# Simulación de ajustes
for angulo in [0, 10, 20]:
    mover_motor(angulo)