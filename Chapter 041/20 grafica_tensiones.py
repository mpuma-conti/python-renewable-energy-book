import matplotlib.pyplot as plt

# Tensiones en cada nodo
nodes = ['Nodo 0', 'Nodo 1', 'Nodo 2']
voltages = [abs(V0), abs(V1), abs(V2)]

plt.figure(figsize=(8, 5))
plt.bar(nodes, voltages, color='lightblue')
plt.xlabel('Nodos')
plt.ylabel('Tensión (pu)')
plt.title('Tensiones en los Nodos')
plt.ylim(0.9, 1.05)
plt.grid(axis='y')
plt.show()