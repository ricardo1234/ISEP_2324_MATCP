lista = [[],[]]

for i in range(10):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

lista[0].sort(reverse = True)
lista[1].sort(reverse = True)

print(f"Os valores pares são: {lista}")
