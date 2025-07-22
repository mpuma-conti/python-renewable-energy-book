import matplotlib.pyplot as plt

# Datos simulados de potencia activa (en kW) a lo largo del tiempo (en horas)
time = np.linspace(0, 24, 100)  # 24 horas, 100 puntos
power = 2 + 1.5 * np.sin(2 * np.pi * time / 24)  # Consumo variable (kW)

# Energía acumulada
energy = np.trapz(power, time)  # Integral numérica (kWh)

# Gráfica de potencia activa
plt.figure(figsize=(8, 5))
plt.plot(time, power, label="Potencia activa (kW)")
plt.fill_between(time, power, alpha=0.2, label=f"Energía acumulada: {energy:.2f} kWh")
plt.xlabel("Tiempo (horas)")
plt.ylabel("Potencia (kW)")
plt.title("Consumo energético diario")
plt.legend()
plt.grid()
plt.show()

# Resultado
print(f"Energía total consumida en 24 horas: {energy:.2f} kWh")