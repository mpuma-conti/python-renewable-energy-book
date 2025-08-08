# Datos para la gráfica
categories = ['Ideal', 'Con Pérdidas']
energies = [E_annual, E_actual]

# Gráfica de barras
plt.figure(figsize=(8, 5))
plt.bar(categories, energies, color=['skyblue', 'orange'])
plt.ylabel("Energía Generada (kWh)")
plt.title("Impacto de las Pérdidas en la Energía Generada")
plt.grid(axis='y')
plt.show()