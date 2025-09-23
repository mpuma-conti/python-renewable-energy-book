import pandas as pd

# Datos simulados de consumo energético
datos = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "Consumo (kWh)": [12000, 11500, 13000, 12500]
}

df = pd.DataFrame(datos)

# Cálculo de estadísticas básicas
consumo_total = df["Consumo (kWh)"].sum()
consumo_promedio = df["Consumo (kWh)"].mean()

print(f"Consumo total: {consumo_total} kWh")
print(f"Consumo promedio mensual: {consumo_promedio:.2f} kWh")