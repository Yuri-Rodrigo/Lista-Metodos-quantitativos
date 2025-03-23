from scipy.optimize import linprog

c = [-4, -5]

A = [[0.5, 1],
     [0.5, 1]]

b = [8, 16]

x_bounds = (0, None)
y_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method="highs")

print("resultado:")
print(f"Status da Otimizacao: {res.message}")
print(f"Camisas Produzidas: {res.x[0]:.2f}")
print(f" Calcas Produzidas: {res.x[1]:.2f}")
print(f"Lucro Maximo: R$ {-res.fun:.2f}")