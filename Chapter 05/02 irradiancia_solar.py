import numpy as np
import matplotlib.pyplot as plt

# Parámetros
irradiancia = np.linspace(200, 1000, 100)  # Irradiancia en W/m^2
Isc_ref = 5.0  # Corriente de cortocircuito en condiciones estándar (A)
irradiancia_ref = 1000  # Irradiancia estándar (W/m^2)

# Relación corriente-irradiancia
Isc = Isc_ref * (irradiancia / irradiancia_ref)

# Gráfica
plt.figure(figsize=(8, 5))
plt.plot(irradiancia, Isc, label="Corriente vs Irradiancia")
plt.xlabel("Irradiancia (W/m^2)")
plt.ylabel("Corriente (A)")
plt.title("Efecto de la Irradiancia en la Corriente Generada")
plt.grid()
plt.legend()
plt.show()