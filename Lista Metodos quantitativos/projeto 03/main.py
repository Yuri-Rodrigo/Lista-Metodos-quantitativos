from scipy.optimize import linprog

c = [-500, -300]

A = [[8, 4],  # Restricao de tempo
     [5, 2]]  # Restricao dde materia-prima

b = [1200, 600]

x_bounds = (0, None)
y_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method="highs")

print("resultado:")
print(f"Status da Otimizacao: {res.message}")
print(f"Notebooks Produzidas: {res.x[0]:.2f}")
print(f"Tablets Produzidas: {res.x[1]:.2f}")
print(f"Lucro Maximo: R$ {-res.fun:.2f}")