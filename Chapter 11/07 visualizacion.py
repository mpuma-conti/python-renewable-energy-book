import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# Configuración inicial
corrientes = []

def actualizar(frame):
    corriente = random.uniform(0, 10)  # Simulación de datos en tiempo real
    corrientes.append(corriente)
    if len(corrientes) > 20:  # Limitar a 20 datos en pantalla
        corrientes.pop(0)
    plt.cla()
    plt.plot(corrientes, label="Corriente (A)")
    plt.ylim(0, 10)
    plt.legend(loc='upper left')
    plt.title("Visualización en Tiempo Real")
    plt.xlabel("Tiempo")
    plt.ylabel("Corriente (A)")

ani = FuncAnimation(plt.gcf(), actualizar, interval=500)
plt.show()