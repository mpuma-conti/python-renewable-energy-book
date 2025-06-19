voltaje = 230          # Entero (int)
corriente = 10.5       # Flotante (float)
equipo = "Generador"   # Cadena de texto (str)
encendido = True       # Booleano (bool)

print(f"Voltaje: {voltaje} V")
print(f"Corriente: {corriente} A")
print(f"Equipo: {equipo}")
print(f"Estado: {'Encendido' if encendido else 'Apagado'}")