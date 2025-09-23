# Datos simulados de consumo energético real y objetivo
meses = ["Enero", "Febrero", "Marzo", "Abril"]
consumo_real = [12000, 11500, 13000, 12500]
consumo_objetivo = [11500, 11000, 12000, 11800]

# Cálculo del desempeño
desempeno = [(real - objetivo) / objetivo * 100 for real, objetivo in zip(consumo_real, consumo_objetivo)]

# Visualización de resultados
import matplotlib.pyplot as plt

plt.plot(meses, consumo_real, label="Consumo Real")
plt.plot(meses, consumo_objetivo, label="Consumo Objetivo", linestyle="--")
plt.bar(meses, desempeno, alpha=0.5, label="Desempeño (%)")
plt.axhline(0, color="red", linestyle="--", linewidth=0.8)
plt.title("Desempeño del Consumo Energético")
plt.xlabel("Mes")
plt.ylabel("Consumo (kWh) y Desempeño (%)")
plt.legend()
plt.grid(True)
plt.show()