import pandas as pd
import matplotlib.pyplot as plt

# Datos simulados: consumo horario (kWh)
data = {
    "Hora": range(24),
    "Consumo (kWh)": [10, 12, 14, 13, 12, 15, 20, 25, 30, 28, 27, 26, 
                      25, 24, 22, 21, 20, 18, 16, 14, 13, 12, 11, 10]
}

df = pd.DataFrame(data)

# Análisis
media_consumo = df["Consumo (kWh)"].mean()
df["Anomalía"] = df["Consumo (kWh)"] > 1.5 * media_consumo

# Visualización
plt.plot(df["Hora"], df["Consumo (kWh)"], label="Consumo")
plt.scatter(df["Hora"][df["Anomalía"]], df["Consumo (kWh)"][df["Anomalía"]],
            color="red", label="Anomalía")
plt.title("Consumo Horario y Anomalías")
plt.xlabel("Hora")
plt.ylabel("Consumo (kWh)")
plt.legend()
plt.grid()
plt.show()