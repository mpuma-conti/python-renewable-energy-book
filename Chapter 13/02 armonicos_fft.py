# Transformada Rápida de Fourier (FFT)
fft_resultado = fft(senal_total)
frecuencias = np.fft.fftfreq(len(senal_total), d=1/frecuencia_muestreo)
magnitudes = np.abs(fft_resultado) / len(senal_total)

# Filtrar frecuencias positivas
frecuencias_positivas = frecuencias[frecuencias >= 0]
magnitudes_positivas = magnitudes[frecuencias >= 0]

# Visualización en el dominio de la frecuencia
plt.figure(figsize=(10, 4))
plt.stem(frecuencias_positivas, magnitudes_positivas, use_line_collection=True)
plt.title('Espectro de Frecuencia (Análisis FFT)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.grid()
plt.xlim(0, 300)  # Mostrar hasta 300 Hz
plt.show()
