import seaborn as sns
import numpy as np

# Datos de ejemplo de eficiencia y capacidad de varios sistemas
datos_eficiencia = np.array([[0.85, 0.75, 0.90], [0.88, 0.80, 0.92], [0.82, 0.78, 0.87]])
sistemas = ['Sistema A', 'Sistema B', 'Sistema C']
metricas = ['Eficiencia', 'Factor de Capacidad', 'COP']

# Crear mapa de calor
sns.heatmap(datos_eficiencia, annot=True, cmap='Blues', xticklabels=sistemas, yticklabels=metricas)
plt.title('Mapa de Calor de Eficiencia en Diferentes Sistemas')
plt.show()