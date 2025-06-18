from PySpice.Probe.Plot import plot
from PySpice.Spice.Library import SpiceLibrary
from PySpice.Spice.Netlist import Circuit
from PySpice.Simulation import Transient
import matplotlib.pyplot as plt

# Definición del circuito
circuit = Circuit("RC Circuit")
circuit.V(1, "input", circuit.gnd, 10)  # Fuente de voltaje de 10V
circuit.R(1, "input", "output", 1@u_kΩ)  # Resistencia de 1kΩ
circuit.C(1, "output", circuit.gnd, 1@u_uF)  # Capacitancia de 1uF

# Simulación transitoria
simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.transient(step_time=1@u_ms, end_time=10@u_ms)

# Graficar la respuesta en el tiempo
plt.plot(analysis.time, analysis["output"])
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.title("Respuesta en el tiempo del circuito RC")
plt.show()