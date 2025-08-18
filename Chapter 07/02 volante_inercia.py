# Parámetros del volante de inercia
momento_inercia = 10  # kg·m²
velocidad_angular = np.linspace(0, 300, 100)  # rad/s

# Cálculo de la energía almacenada
energia = 0.5 * momento_inercia * velocidad_angular**2

# Visualización
plt.figure(figsize=(10, 5))
plt.plot(velocidad_angular, energia, label="Energía Almacenada")
plt.xlabel("Velocidad Angular (rad/s)")
plt.ylabel("Energía (Joules)")
plt.title("Energía Almacenada en un Volante de Inercia")
plt.legend()
plt.grid()
plt.show()