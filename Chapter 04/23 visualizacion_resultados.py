import matplotlib.pyplot as plt

# Datos simulados
nodos = ['Nodo 0', 'Nodo 1', 'Nodo 2']
tensiones = [1.0, 0.98, 0.95]

# Gráfico
plt.figure(figsize=(8, 5))
plt.bar(nodos, tensiones, color='skyblue')
plt.xlabel('Nodos')
plt.ylabel('Tensión (pu)')
plt.title('Tensiones en los nodos')
plt.ylim(0.9, 1.05)
plt.grid(axis='y')
plt.show()