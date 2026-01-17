# Cálculo de los RMS de cada fase
def calcular_rms(signal):
    return np.sqrt(np.mean(signal**2))

V_A_rms = calcular_rms(fase_A)
V_B_rms = calcular_rms(fase_B)
V_C_rms = calcular_rms(fase_C)

# Calcular el índice de desbalanceo de tensión (IDT)
idt = 100 * max([V_A_rms, V_B_rms, V_C_rms]) / min([V_A_rms, V_B_rms, V_C_rms]) - 100
print(f"Índice de Desbalanceo de Tensión: {idt:.2f}%")