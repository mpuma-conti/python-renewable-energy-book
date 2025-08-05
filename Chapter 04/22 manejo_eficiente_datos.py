import pandas as pd

# Datos del sistema
data = {
    "Nodo": [0, 1, 2],
    "Tensión (pu)": [1.0, 0.98, 0.95],
    "Carga (P, Q)": [(0, 0), (0.5, 0), (1.0, 0.5)]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Guardar datos
df.to_csv("datos_simulacion.csv", index=False)

# Cargar datos
df_cargado = pd.read_csv("datos_simulacion.csv")
print(df_cargado)