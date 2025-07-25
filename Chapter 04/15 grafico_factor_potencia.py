# Ángulos de desfase en grados
phi_degrees = np.linspace(0, 90, 100)
phi_radians = np.radians(phi_degrees)

# Factor de potencia
cos_phi = np.cos(phi_radians)

# Gráfica
plt.figure(figsize=(8, 5))
plt.plot(phi_degrees, cos_phi, label="Factor de Potencia ($\cos(\phi)$)")
plt.xlabel("Ángulo de desfase (°)")
plt.ylabel("Factor de potencia")
plt.title("Relación entre desfase y factor de potencia")
plt.grid()
plt.legend()
plt.show()