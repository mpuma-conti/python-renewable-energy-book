import numpy as np
import matplotlib.pyplot as plt

# Definir los parámetros del sistema eólico
rho = 1.225  # Densidad del aire en kg/m³
r = 40       # Radio del rotor en metros
Cp = 0.4     # Coeficiente de potencia
eta = 0.9    # Eficiencia del generador

# Calcular el área barrida por las palas (A = pi * r^2)
A = np.pi * r**2

# Definir una función para calcular la potencia generada
def calcular_potencia(v):
    """
    Calcula la potencia generada por un aerogenerador en función de la velocidad del viento.
    """
    P = 0.5 * rho * A * Cp * v**3  # Potencia eólica (en W)
    P_electrica = P * eta          # Potencia eléctrica (en W)
    return P_electrica

# Definir una gama de velocidades del viento (de 0 a 25 m/s)
velocidades_viento = np.linspace(0, 25, 100)

# Calcular la potencia generada para cada velocidad del viento
potencia_generada = [calcular_potencia(v) for v in velocidades_viento]

# Graficar los resultados
plt.figure(figsize=(8, 5))
plt.plot(velocidades_viento, potencia_generada, label="Potencia generada", color="b")
plt.title("Simulación de la Potencia Generada por un Aerogenerador")
plt.xlabel("Velocidad del Viento (m/s)")
plt.ylabel("Potencia Generada (W)")
plt.grid(True)
plt.legend()
plt.show()