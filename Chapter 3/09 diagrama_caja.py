import seaborn as sns

# Graficar el diagrama de caja del consumo de energía
sns.boxplot(x=datos['Consumo_kWh'])
plt.xlabel('Consumo de Energía (kWh)')
plt.title('Diagrama de Caja del Consumo de Energía')
plt.show()