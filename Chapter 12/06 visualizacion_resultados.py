import matplotlib.pyplot as plt

# Datos simulados
horas = range(24)
demanda = [0.5, 0.6, 0.7, 0.8, 1.0, 1.2, 1.5, 1.8, 2.0, 2.1, 2.3, 2.2, 2.0, 1.8, 1.5, 1.2, 1.0, 0.8, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
generacion = [0.4, 0.5, 0.6, 0.8, 1.1, 1.4, 1.6, 1.9, 2.1, 2.2, 2.4, 2.2, 2.1, 1.7, 1.4, 1.1, 0.9, 0.7, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0]
energia_desperdiciada = [0.0, 0.0, 0.0, 0.0, 0.1, 0.2, 0.3, 0.1, 0.0, 0.1, 0.2, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
energia_no_satisfecha = [0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

# Gráfica
plt.plot(horas, demanda, label='Demanda (kW)', linestyle='--')
plt.plot(horas, generacion, label='Generación (kW)')
plt.bar(horas, energia_desperdiciada, label='Energía Desperdiciada (kW)', alpha=0.6)
plt.bar(horas, energia_no_satisfecha, label='Energía No Satisfecha (kW)', alpha=0.6, bottom=energia_desperdiciada)
plt.xlabel('Horas')
plt.ylabel('Energía (kW)')
plt.title('Análisis de Resultados del Sistema Híbrido')
plt.legend()
plt.grid()
plt.show()
