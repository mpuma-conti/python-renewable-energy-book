# Condicional simple para verificar un nivel de corriente
corriente = 15

if corriente > 10:
    print("Corriente alta")
elif corriente == 10:
    print("Corriente en el límite")
else:
    print("Corriente baja")