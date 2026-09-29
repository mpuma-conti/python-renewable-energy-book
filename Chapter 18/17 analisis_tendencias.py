import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generación de datos simulados de nivel del embalse a lo largo del tiempo
tiempo = pd.date_range(start='2024-01-01', periods=1000, freq='H')
nivel_embalse = 500 + np.random.normal(loc=0, scale=2, size=1000).cumsum()

datos = pd.DataFrame({'Tiempo': tiempo, 'Nivel Embalse': nivel_embalse})
datos.set_index('Tiempo', inplace=True)

# Análisis de tendencias con medias móviles
datos['Media Móvil 50'] = datos['Nivel Embalse'].rolling(window=50).mean()
datos['Media Móvil 200'] = datos['Nivel Embalse'].rolling(window=200).mean()

# Visualización de resultados
plt.figure(figsize=(12, 6))
plt.plot(datos.index, datos['Nivel Embalse'], label='Nivel del Embalse', alpha=0.5)
plt.plot(datos.index, datos['Media Móvil 50'], label='Media Móvil 50 Horas', color='red')
plt.plot(datos.index, datos['Media Móvil 200'], label='Media Móvil 200 Horas', color='green')
plt.xlabel('Tiempo')
plt.ylabel('Nivel del Embalse (m³)')
plt.title('Análisis de Tendencias en el Nivel del Embalse')
plt.legend()
plt.grid(True)
plt.show()