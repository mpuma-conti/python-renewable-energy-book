import serial

# Configuración del puerto serial
puerto = serial.Serial('/dev/ttyUSB0', 9600)

while True:
    if puerto.in_waiting > 0:
        lectura = puerto.readline().decode('utf-8').strip()
        print(f"Corriente medida: {lectura} A")