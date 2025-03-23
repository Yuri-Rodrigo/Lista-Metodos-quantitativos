from scipy.optimize import linprog

c = [-5, -3]

A = [[2, 1],
     [1, 2]]

b = [40, 30]

x_bounds = (0, None)
y_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method="highs")

print("resultado:")
print(f"Status da Otimizacao: {res.message}")
print(f"Camisas Produzidas: {res.x[0]:.2f}")
print(f" Calcas Produzidas: {res.x[1]:.2f}")
print(f"Lucro Maximo: R$ {-res.fun:.2f}")