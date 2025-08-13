import sympy as sp

# Declaración de variables simbólicas
t, R, C, V_in = sp.symbols('t R C V_in')
V_out = sp.Function('V_out')(t)

# Ecuación diferencial del circuito RC
equation = sp.Eq(R * C * V_out.diff(t) + V_out, V_in)

# Solución simbólica de la ecuación diferencial
solucion = sp.dsolve(equation, V_out)
sp.pprint(solucion)