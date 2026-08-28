from scipy.optimize import linprog

# Definir el modelo de programación lineal para asignar recursos de mantenimiento
# Minimizamos el tiempo de inactividad (costo) sujeto a las restricciones de recursos

# Coeficientes de la función objetivo (costos de mantenimiento)
c = [10, 15, 20]  # costos de mantenimiento para diferentes turbinas

# Restricciones (disponibilidad de recursos)
A = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]  # Un recurso por tarea
b = [1, 1, 1]  # Disponibilidad de recursos

# Resolver el problema de optimización
result = linprog(c, A_eq=A, b_eq=b, method='highs')

print(f"Recursos asignados: {result.x}")