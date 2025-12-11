import serial

# Configuración del puerto serial
puerto = serial.Serial('COM3', baudrate=9600, timeout=1)

print("Iniciando lectura de datos en tiempo real...")

try:
    while True:
        datos = puerto.readline().decode('utf-8').strip()  # Leer y decodificar datos
        if datos:
            print(f"Dato recibido: {datos}")
except KeyboardInterrupt:
    print("Finalizando lectura.")
    puerto.close()