import matplotlib.pyplot as plt

# Graficar el histograma del consumo de energía
plt.hist(datos['Consumo_kWh'], bins=5, color='skyblue', edgecolor='black')
plt.xlabel('Consumo de Energía (kWh)')
plt.ylabel('Frecuencia')
plt.title('Distribución del Consumo de Energía')
plt.show()