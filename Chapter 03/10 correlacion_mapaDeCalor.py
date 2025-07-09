import seaborn as sns
import numpy as np

# Datos de ejemplo
datos = pd.DataFrame({
    'Consumo_kWh': [100, 120, 150, 130, 160, 170, 180, 200, 220, 210],
    'Temperatura_C': [15, 16, 17, 15, 18, 19, 20, 21, 22, 23]
})

# Calcular la matriz de correlación
correlacion = datos.corr()

# Graficar el mapa de calor de la matriz de correlación
sns.heatmap(correlacion, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Calor de Correlación entre Variables')
plt.show()