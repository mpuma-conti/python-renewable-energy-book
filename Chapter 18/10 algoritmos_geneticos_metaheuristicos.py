import numpy as np
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms
import random

# Definición del problema: optimizar flujos para maximizar energía generada
def energia_generada(individual):
    return sum(individual),

# Configuración del Algoritmo Genético
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("flow", random.uniform, 0, 200)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.flow, n=5)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", energia_generada)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=10, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Restricción: suma de flujos debe ser <= 500
def suma_flujos(individual):
    return sum(individual) <= 500

toolbox.decorate("evaluate", tools.DeltaPenalty(suma_flujos, 0, 0))

def main():
    random.seed(42)
    pop = toolbox.population(n=50)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("max", np.max)
    
    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.2, ngen=40, stats=stats, halloffame=hof, verbose=True)
    
    return pop, log, hof

if __name__ == "__main__":
    pop, log, hof = main()
    best = hof[0]
    print("Flujos óptimos (m³/s):", best)
    print("Energía máxima generada:", energia_generada(best)[0], "MW")
    
    # Visualización de la evolución de la energía
    fits = [ind.fitness.values[0] for ind in pop]
    plt.hist(fits, bins=20)
    plt.title("Distribución de la Energía Generada en la Población Final")
    plt.xlabel("Energía (MW)")
    plt.ylabel("Frecuencia")
    plt.show()