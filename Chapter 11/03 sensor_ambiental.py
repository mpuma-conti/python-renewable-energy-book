import Adafruit_DHT

# Configuración del sensor
SENSOR = Adafruit_DHT.DHT22
PIN = 4  # Pin GPIO donde está conectado el sensor

# Lectura de temperatura y humedad
humedad, temperatura = Adafruit_DHT.read_retry(SENSOR, PIN)
if humedad is not None and temperatura is not None:
    print(f"Temperatura: {temperatura:.1f}°C, Humedad: {humedad:.1f}%")
else:
    print("Error al leer datos del sensor")