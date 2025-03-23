from scipy.optimize import linprog

c = [200, 100]

A_ub = [[30, 10],   # Restricao de materia-prima
        [5, 2]]     # Restricao de tempo

b_ub = [500, 240]   # Lado direito das desigualdades (limites maximos)

x_bounds = (10, None)
y_bounds = (20, None)

res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[x_bounds, y_bounds], method="highs")

print("resultado:")
print(f"Status da Otimizacao: {res.message}")
print(f"Mesas Produzidas: {res.x[0]:.2f}")
print(f"Cadeiras Produzidas: {res.x[1]:.2f}")
print(f"Custo Minimo Total: R$ {-res.fun:.2f}")