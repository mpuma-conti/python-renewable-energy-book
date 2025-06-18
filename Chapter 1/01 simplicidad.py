import math

# Parámetros del sistema
voltaje = 230  # en volts
corriente = 10  # en amperios
angulo_fase = math.radians(30)  # Convertimos a radianes

# Cálculo de la potencia activa
potencia_activa = voltaje * corriente * math.cos(angulo_fase)
print(f"La potencia activa es: {potencia_activa} W")