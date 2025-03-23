from scipy.optimize import linprog

c = [4, 6, 9, 5, 4, 7]

A_eq = [
        [1, 0, 0, 1, 0, 0],  
        [0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1]
        ]     

b_eq = [80, 70, 100]

A_ub = [
        [1, 1, 1, 0, 0, 0,],
        [0, 0, 0, 1, 1, 1,]
        ]

b_ub = [100, 150]

bounds = [(0, None)] * 6

res = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")

print("resultado:")
print(f"Status da Otimizacao: {res.message}")
print(f"Custo Minimo Total: R$ {res.fun:.2f}")
print("Quantidade enviada de cada fabrica para cada centro:")
print(f"Fabrica A → Centro 1: {res.x[0]:.2f} unidades")
print(f"Fabrica A → Centro 2: {res.x[1]:.2f} unidades")
print(f"Fabrica A → Centro 3: {res.x[2]:.2f} unidades")
print(f"Fabrica B → Centro 1: {res.x[3]:.2f} unidades")
print(f"Fabrica B → Centro 2: {res.x[4]:.2f} unidades")
print(f"Fabrica B → Centro 3: {res.x[5]:.2f} unidades")