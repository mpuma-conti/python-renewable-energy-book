import networkx as nx

# Crear grafo de la red eléctrica
G = nx.Graph()
G.add_edges_from([
    ("Subestación A", "Transformador 1"),
    ("Subestación A", "Transformador 2"),
    ("Transformador 1", "Carga 1"),
    ("Transformador 2", "Carga 2"),
])

# Simulación de fallo en un nodo
G.remove_node("Transformador 1")

# Evaluar conectividad
is_connected = nx.is_connected(G)
critical_nodes = list(nx.articulation_points(G))

print(f"¿Red conectada? {'Sí' if is_connected else 'No'}")
print(f"Nodos críticos: {critical_nodes}")