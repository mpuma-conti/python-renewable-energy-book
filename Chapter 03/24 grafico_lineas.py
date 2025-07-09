import pandas as pd

# Datos de ejemplo de eficiencia a lo largo del tiempo
fechas = pd.date_range(start='2023-01-01', periods=10, freq='M')
eficiencia = [0.82, 0.85, 0.80, 0.83, 0.87, 0.89, 0.88, 0.86, 0.90, 0.91]

# Crear gráfico de línea
plt.plot(fechas, eficiencia, marker='o', color='blue')
plt.xlabel('Fecha')
plt.ylabel('Eficiencia Energética')
plt.title('Eficiencia Energética en el Tiempo')
plt.xticks(rotation=45)
plt.show()