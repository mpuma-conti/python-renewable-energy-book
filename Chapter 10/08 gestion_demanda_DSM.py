import numpy as np
import matplotlib.pyplot as plt

# Datos simulados: carga inicial por sectores (MW)
sectores = ["Residencial", "Comercial", "Industrial"]
carga_inicial = np.array([30, 50, 70])  # MW
capacidad_max = 120  # Capacidad total disponible

# Ajustar cargas proporcionalmente para no superar la capacidad
factor_ajuste = capacidad_max / carga_inicial.sum()
carga_ajustada = carga_inicial * factor_ajuste

# Visualización
x = np.arange(len(sectores))
plt.bar(x - 0.2, carga_inicial, width=0.4, label="Carga Inicial")
plt.bar(x + 0.2, carga_ajustada, width=0.4, label="Carga Ajustada")
plt.xticks(x, sectores)
plt.ylabel("Carga (MW)")
plt.title("Gestión de Carga por Sectores")
plt.legend()
plt.grid()
plt.show()