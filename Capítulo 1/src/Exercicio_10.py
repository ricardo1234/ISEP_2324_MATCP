def maior(*numeros):
    if len(numeros) == 0:
        return 0
    maior = numeros[0]
    for valor in numeros:
        if valor > maior:
            maior = valor
    return maior

numeros = []

while True:
    valor = int(input("Digite um valor [0 - sair, -1 - nova lista]: "))
    if valor == 0:
        break
    if valor == -1:
        print(f"o maior numero é {maior(*numeros)}")
        numeros.clear()
        continue
    numeros.append(valor)
