listNumero = []

for i in range(5):
    numero = int(input("Digite um número: "))
    index = len(listNumero)
    for j in range(len(listNumero)):
        if numero < listNumero[j]:
            index = j
            break
    listNumero.insert(index, numero)
    print(listNumero)