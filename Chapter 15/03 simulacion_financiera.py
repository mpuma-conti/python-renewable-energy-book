import numpy as np
import matplotlib.pyplot as plt

# Parámetros del proyecto
inversion_inicial = 5000000  # Inversión inicial en USD
costos_operativos_anuales = 200000  # Costos operativos anuales en USD
precio_energia = 0.07  # Precio de venta de la electricidad (USD/kWh)
produccion_anual = 100000  # Producción anual de energía (kWh)

# Flujos de efectivo anuales (ingresos - costos operativos)
ingresos_anuales = precio_energia * produccion_anual
flujos_efectivos = ingresos_anuales - costos_operativos_anuales

# Simulación de Monte Carlo para variabilidad en la producción de energía y el precio
n_simulaciones = 1000
produccion_simulada = np.random.normal(loc=produccion_anual, scale=0.1 * produccion_anual, size=n_simulaciones)
precio_simulado = np.random.normal(loc=precio_energia, scale=0.01 * precio_energia, size=n_simulaciones)

# Cálculo de los flujos de efectivo simulados
flujos_efectivos_simulados = (produccion_simulada * precio_simulado - costos_operativos_anuales)

# Cálculo del VAN para cada simulación
tasa_descuento = 0.08  # Tasa de descuento
vans = np.array([np.sum(flujos_efectivos_simulados / (1 + tasa_descuento)**np.arange(1, 21)) - inversion_inicial for _ in range(n_simulaciones)])

# Visualización de los resultados
plt.hist(vans, bins=50, color='blue', edgecolor='black')
plt.title('Distribución de VANs para el Proyecto de Energía Solar')
plt.xlabel('Valor Actual Neto (USD)')
plt.ylabel('Frecuencia')
plt.show()

# Análisis de la probabilidad de VAN positivo
probabilidad_van_positivo = np.sum(vans > 0) / n_simulaciones
print(f'Probabilidad de VAN positivo: {probabilidad_van_positivo * 100:.2f}%')