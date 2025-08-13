# Corrientes en las líneas
I01 = (S1 + S2 + S3) / V[0]
I12 = (S2 + S3) / V[1]
I23 = S3 / V[2]

# Pérdidas en las líneas
P_loss = (np.abs(I01)**2 * Z01.real +
          np.abs(I12)**2 * Z12.real +
          np.abs(I23)**2 * Z23.real)

print(f"Pérdidas en la red: {P_loss:.4f} pu")