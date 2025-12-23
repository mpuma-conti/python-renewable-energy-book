import Adafruit_DHT
import serial
import time

# Configuración del sensor DHT22
SENSOR_DHT = Adafruit_DHT.DHT22
PIN_DHT = 4  # Pin GPIO del sensor

# Configuración del medidor PZEM-004T (comunicación serial)
puerto = serial.Serial('COM3', baudrate=9600, timeout=1)

# Función para leer datos del medidor
def leer_pzem():
    puerto.write(b'\x01\x03\x00\x00\x00\x02\xC4\x0B')  # Comando de lectura MODBUS
    respuesta = puerto.read(7)
    if len(respuesta) >= 7:
        voltaje = int.from_bytes(respuesta[3:5], 'big') / 10.0
        corriente = int.from_bytes(respuesta[5:7], 'big') / 1000.0
        potencia = voltaje * corriente
        return voltaje, corriente, potencia
    return None, None, None

# Adquisición de datos
while True:
    humedad, temperatura = Adafruit_DHT.read_retry(SENSOR_DHT, PIN_DHT)
    voltaje, corriente, potencia = leer_pzem()
    if humedad and temperatura and voltaje and corriente and potencia:
        print(f"Temperatura: {temperatura:.1f}°C, Humedad: {humedad:.1f}%")
        print(f"Voltaje: {voltaje:.1f} V, Corriente: {corriente:.3f} A, Potencia: {potencia:.1f} W")
    time.sleep(5)