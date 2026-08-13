import numpy as np

# Simulación de emisiones de CO2 con diferentes capacidades solares
capacidades_solares = np.linspace(0, 1000, 100)
emisiones_simuladas = capacidades_solares * slope + intercept

plt.plot(capacidades_solares, emisiones_simuladas)
plt.title('Simulación de Emisiones de CO2 según la Capacidad Solar Instalada')
plt.xlabel('Capacidad Solar (MW)')
plt.ylabel('Emisiones de CO2 (toneladas)')
plt.show()