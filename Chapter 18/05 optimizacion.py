import numpy as np
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms
import random

# Definición del problema: optimizar pitch y yaw para maximizar la potencia generada
# Supongamos que la potencia P es una función del pitch (θ) y yaw (φ)
def potencia(theta, phi, velocidad_viento, direccion_viento):
    # Función de potencia simplificada
    # P = 0.5 * rho * A * V^3 * Cp(theta, phi)
    # Donde Cp es el coeficiente de potencia dependiente de theta y phi
    rho = 1.225  # Densidad del aire (kg/m³)
    A = 100  # Área del rotor (m²)
    V = velocidad_viento
    Cp = max(0, 0.5 * np.cos(theta) * np.cos(phi))  # Ejemplo simplificado de Cp
    return 0.5 * rho * A * V**3 * Cp

# Parámetros de la simulación
velocidad_viento = 12  # m/s
direccion_viento = 180  # grados

# Definición del espacio de búsqueda
BOUND_LOW, BOUND_UP = 0, 90  # Pitch y Yaw en grados

# Configuración del Algoritmo Genético
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("pitch", random.uniform, BOUND_LOW, BOUND_UP)
toolbox.register("yaw", random.uniform, BOUND_LOW, BOUND_UP)
toolbox.register("individual", tools.initCycle, creator.Individual, (toolbox.pitch, toolbox.yaw), n=1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Función de evaluación
def evaluate(individual):
    theta, phi = individual
    P = potencia(theta, phi, velocidad_viento, direccion_viento)
    return (P,)

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=15, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Ejecutar el Algoritmo Genético
def main():
    random.seed(42)
    pop = toolbox.population(n=50)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("max", np.max)
    
    algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.2, ngen=40, stats=stats, halloffame=hof, verbose=True)
    
    return pop, stats, hof

if __name__ == "__main__":
    pop, stats, hof = main()
    best_ind = hof[0]
    print(f"\nMejor individuo: Pitch = {best_ind[0]:.2f}°, Yaw = {best_ind[1]:.2f}°")
    print(f"Potencia máxima: {evaluate(best_ind)[0]:.2f} W")

    # Visualización de la evolución de la potencia
    fits = [ind.fitness.values[0] for ind in pop]
    plt.hist(fits, bins=20)
    plt.title("Distribución de Potencia Generada en la Población Final")
    plt.xlabel("Potencia (W)")
    plt.ylabel("Frecuencia")
    plt.show()