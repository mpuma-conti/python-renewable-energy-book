from PySpice.Probe.Plot import plot
from PySpice.Spice.Library import SpiceLibrary
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

# Definición del circuito
circuit = Circuit('RC Circuit')
circuit.V(1, 'input', circuit.gnd, 10 @ u_V)  # Fuente de voltaje
circuit.R(1, 'input', 'output', 1 @ u_kΩ)     # Resistor de 1 kΩ
circuit.C(1, 'output', circuit.gnd, 1 @ u_uF) # Capacitor de 1 µF

# Simulación en el tiempo
simulacion = circuit.simulator(temperature=25, nominal_temperature=25)
resultado = simulacion.transient(step_time=1 @ u_ms, end_time=10 @ u_ms)

# Graficar resultados
plot(resultado['input'], resultado['output'])
plt.title('Respuesta de un Circuito RC')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.grid()
plt.show()