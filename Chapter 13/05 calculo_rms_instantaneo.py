def calcular_rms(signal, ventana):
    n_muestras = len(signal)
    rms = np.zeros(n_muestras - ventana)
    for i in range(n_muestras - ventana):
        rms[i] = np.sqrt(np.mean(signal[i:i + ventana]**2))
    return rms

ventana = int(frecuencia_muestreo / frecuencia)  # Una ventana de un ciclo (20 ms)
rms = calcular_rms(voltaje, ventana)

# Visualización del RMS
plt.figure(figsize=(10, 4))
plt.plot(tiempo[:len(rms)], rms, label='RMS Instantáneo')
plt.axhline(voltaje_nominal, color='r', linestyle='--', label='Voltaje Nominal')
plt.title('Análisis RMS de Variaciones de Voltaje')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje RMS (V)')
plt.legend()
plt.grid()
plt.show()