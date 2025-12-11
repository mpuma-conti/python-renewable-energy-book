import Adafruit_ADS1x15

# Configuración del ADC
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1  # Configuración de ganancia

# Lectura del sensor de corriente en el canal 0
valor_adc = adc.read_adc(0, gain=GAIN)
corriente = valor_adc * 0.001  # Conversión basada en la calibración del sensor
print(f"Corriente medida: {corriente:.2f} A")