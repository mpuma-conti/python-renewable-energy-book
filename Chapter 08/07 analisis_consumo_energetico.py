import pandas as pd
import matplotlib.pyplot as plt

# Datos simulados
datos = {
    "Hora": range(24),
    "Consumo": [300, 280, 250, 220, 200, 210, 230, 300, 400, 500, 550, 580,
                600, 620, 610, 580, 560, 540, 520, 500, 450, 400, 350, 320]
}

# Crear DataFrame
df = pd.DataFrame(datos)

# Análisis de consumo
consumo_total = df["Consumo"].sum()
consumo_promedio = df["Consumo"].mean()
print(f"Consumo total: {consumo_total} kWh")
print(f"Consumo promedio: {consumo_promedio:.2f} kWh/h")

# Gráfica de consumo
plt.plot(df["Hora"], df["Consumo"], marker='o')
plt.title("Consumo Energético por Hora")
plt.xlabel("Hora")
plt.ylabel("Consumo (kWh)")
plt.grid(True)
plt.show()