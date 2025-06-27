import matplotlib.pyplot as plt

# Datos de generación de energía en kWh
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
generacion_energia = [100, 150, 200, 250, 300]

# Graficar la generación de energía
plt.plot(dias, generacion_energia, marker='o')
plt.xlabel('Día')
plt.ylabel('Generación de Energía (kWh)')
plt.title('Generación de Energía en el Tiempo')
plt.show()