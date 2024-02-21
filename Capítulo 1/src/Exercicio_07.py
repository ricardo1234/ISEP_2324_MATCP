import numpy as np
n = 0

while n < 3:
    n = int(input("Digite a dimensão da matriz: "))

matriz = np.array([[0 for i in range(n)] for j in range(n)])

for i in range(n):
    for j in range(n):
        matriz[i][j] = int(input(f"Digite um valor para [{i},{j}]: "))

print(f"A matriz é \n{matriz}")

soma = 0

for i in range(n):
    for j in range(n):
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]

print(f"A soma dos valores pares é {soma}")

soma = 0

for i in range(n):
    soma += matriz[i][2]

print(f"A soma dos valores da terceira coluna é {soma}")

print(f"O menor valor da segunda linha é {min(matriz[1])}")
