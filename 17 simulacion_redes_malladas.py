from scipy.optimize import fsolve

# Parámetros de la red (simplificados)
Ybus = np.array([[10 - 20j, -10 + 20j],  # Matriz de admitancia
                 [-10 + 20j, 10 - 20j]])

# Potencias conocidas (en pu)
S_known = np.array([1.0 + 0.5j, 0.8 + 0.3j])

# Función de flujo de potencia
def flujo_potencia(V):
    V_complex = V[:len(V)//2] + 1j * V[len(V)//2:]
    I = Ybus @ V_complex
    S_calculated = V_complex * np.conj(I)
    mismatch = np.hstack([np.real(S_calculated - S_known), np.imag(S_calculated - S_known)])
    return mismatch

# Solución inicial
V0 = np.array([1.0, 1.0, 0.0, 0.0])  # Tensiones iniciales en magnitud y ángulo

# Resolviendo flujo de potencia
solution = fsolve(flujo_potencia, V0)
V_final = solution[:len(solution)//2] + 1j * solution[len(solution)//2:]

# Resultados
print("Tensiones finales:")
for i, v in enumerate(V_final):
    print(f"Nodo {i+1}: |V| = {abs(v):.4f} pu, Ángulo = {np.angle(v, deg=True):.2f}°")