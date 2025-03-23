from scipy.optimize import linprog

c = [5, 7]

A_ub = [[-400, -600],   
        [-30, -50],     
        [-50, -30]]   

b_ub = [-2000, -150, -180]  

x_bounds = (0, None)
y_bounds = (0, None)

res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[x_bounds, y_bounds], method="highs")

print("resultado:")
print(f"Status da Otimizacao: {res.message}")
print(f"Mesas Produzidas: {res.x[0]:.2f}")
print(f"Cadeiras Produzidas: {res.x[1]:.2f}")
print(f"Custo Minimo Total: R$ {-res.fun:.2f}")