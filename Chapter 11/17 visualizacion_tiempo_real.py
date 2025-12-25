import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configuración inicial
datos_potencia = []

def actualizar(frame):
    global datos_potencia
    potencia = obtener_potencia_actual()  # Función para obtener el último dato de potencia
    datos_potencia.append(potencia)
    if len(datos_potencia) > 20:
        datos_potencia.pop(0)
    plt.cla()
    plt.plot(datos_potencia, label="Potencia (W)")
    plt.legend(loc='upper left')
    plt.title("Potencia Generada en Tiempo Real")
    plt.xlabel("Tiempo")
    plt.ylabel("Potencia (W)")

ani = FuncAnimation(plt.gcf(), actualizar, interval=1000)
plt.show()