import pandas as pd
import matplotlib.pyplot as plt

# Importar datos de consumo energético desde un archivo CSV
datos_energia = pd.read_csv('consumo_energia.csv')

# Resumen de los primeros registros
print(datos_energia.head())

# Visualizar el consumo energético a lo largo del tiempo
plt.plot(datos_energia['Fecha'], datos_energia['Consumo_kWh'])
plt.xlabel('Fecha')
plt.ylabel('Consumo de Energía (kWh)')
plt.title('Consumo de Energía a lo Largo del Tiempo')
plt.show()