# Parámetros
T = np.linspace(0, 75, 100)  # Temperatura de la celda (°C)
Voc_ref = 0.6  # Voltaje de circuito abierto a 25°C (V)
T_ref = 25  # Temperatura estándar (°C)
beta = 0.0023  # Coeficiente de temperatura (V/°C)

# Cálculo del voltaje
Voc = Voc_ref - beta * (T - T_ref)

# Gráfica
plt.figure(figsize=(8, 5))
plt.plot(T, Voc, label="Voltaje de circuito abierto")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Voltaje (V)")
plt.title("Efecto de la Temperatura en el Voltaje de Circuito Abierto")
plt.grid()
plt.legend()
plt.show()