import matplotlib.pyplot as plt

# Datos simulados
meses = ["Enero", "Febrero", "Marzo", "Abril"]
ahorros = [300, 350, 320, 400]  # Ahorros en USD
emisiones_reducidas = [150, 175, 160, 200]  # Reducción en kg CO2

# Gráficos
fig, ax1 = plt.subplots()

# Ahorros
ax1.bar(meses, ahorros, color='skyblue', label='Ahorros (USD)')
ax1.set_xlabel("Mes")
ax1.set_ylabel("Ahorros (USD)", color='blue')

# Emisiones Reducidas
ax2 = ax1.twinx()
ax2.plot(meses, emisiones_reducidas, color='green', marker='o', label='Reducción de CO₂ (kg)')
ax2.set_ylabel("Reducción de CO₂ (kg)", color='green')

plt.title("Impacto Económico y Ambiental")
plt.show()