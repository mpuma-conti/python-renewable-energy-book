# Umbrales
limite_inferior = 0.9 * voltaje_nominal
limite_superior = 1.1 * voltaje_nominal

eventos_caida = tiempo[:len(rms)][rms < limite_inferior]
eventos_sobretension = tiempo[:len(rms)][rms > limite_superior]

print(f"Eventos de caída detectados en: {eventos_caida} segundos")
print(f"Eventos de sobretensión detectados en: {eventos_sobretension} segundos")
