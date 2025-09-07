import matplotlib.pyplot as plt

# Datos de pérdidas
componentes = ["Líneas", "Transformadores", "Pérdidas No Técnicas"]
perdidas = [200, 250, 300]  # Valores en kWh

# Gráfico de barras
plt.bar(componentes, perdidas, color="skyblue")
plt.title("Distribución de Pérdidas Energéticas")
plt.xlabel("Componentes")
plt.ylabel("Pérdidas (kWh)")
plt.show()