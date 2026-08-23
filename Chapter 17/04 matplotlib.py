import matplotlib.pyplot as plt
import seaborn as sns

# Gráfico de la distribución de caudales
plt.figure(figsize=(10, 6))
sns.histplot(datos_hidraulicos['caudal'], bins=30, kde=True)
plt.title('Distribución de Caudales')
plt.xlabel('Caudal (m³/s)')
plt.ylabel('Frecuencia')
plt.show()