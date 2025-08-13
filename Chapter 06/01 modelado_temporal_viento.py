import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

# Parámetros de la distribución de Weibull
k = 2  # parámetro de forma
lambda_ = 10  # parámetro de escala

# Generar una muestra de 1000 datos de velocidad del viento
wind_speeds = weibull_min.rvs(k, scale=lambda_, size=1000)

# Graficar la distribución de velocidades del viento
plt.hist(wind_speeds, bins=30, density=True, alpha=0.6, color='g')

# Graficar la distribución de Weibull ajustada
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = weibull_min.pdf(x, k, scale=lambda_)
plt.plot(x, p, 'k', linewidth=2)

plt.title('Distribución de la Velocidad del Viento (Weibull)')
plt.xlabel('Velocidad del Viento (m/s)')
plt.ylabel('Densidad de Probabilidad')
plt.show()