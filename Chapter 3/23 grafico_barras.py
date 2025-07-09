import matplotlib.pyplot as plt

# Datos de ejemplo para diferentes sistemas
sistemas = ['Sistema A', 'Sistema B', 'Sistema C']
eer_sistemas = [0.85, 0.78, 0.92]

# Crear gráfico de barras
plt.bar(sistemas, eer_sistemas, color='skyblue')
plt.xlabel('Sistema')
plt.ylabel('EER')
plt.title('Comparación de Eficiencia Energética (EER) de Diferentes Sistemas')
plt.show()