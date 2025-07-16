from scipy.integrate import odeint

# Definición de la función del sistema RLC en serie
def rlc(y, t, R, L, C, V_in):
    I, V_C = y
    dI_dt = (V_in - I * R - V_C) / L
    dV_C_dt = I / C
    return [dI_dt, dV_C_dt]

# Condiciones iniciales y parámetros
y_0 = [0.0, 0.0]
t = np.linspace(0, 0.01, 1000)
V_in = 10  # voltaje de entrada

# Resolver el sistema
solucion = odeint(rlc, y_0, t, args=(R, L, C, V_in))
I, V_C = solucion.T

# Visualización de la respuesta
plt.plot(t, I, label="Corriente (I)")
plt.plot(t, V_C, label="Voltaje en el Capacitor (V_C)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Corriente (A) / Voltaje (V)")
plt.legend()
plt.title("Respuesta Temporal del Circuito RLC")
plt.grid()
plt.show()