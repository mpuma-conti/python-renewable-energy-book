# Pérdidas por línea
lines = ['Línea 0-1', 'Línea 1-2']
losses = [P_loss_01, P_loss_12]

plt.figure(figsize=(8, 5))
plt.bar(lines, losses, color='lightcoral')
plt.xlabel('Líneas')
plt.ylabel('Pérdidas (pu)')
plt.title('Pérdidas en las Líneas')
plt.grid(axis='y')
plt.show()