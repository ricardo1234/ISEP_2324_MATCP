listNumero = []

while True:
    numero = int(input("Digite um número: "))
    if numero < 0:
        break
    if numero not in listNumero:
        print(f"O número {numero} foi adicionado na lista")
        listNumero.append(numero)

maior = max(listNumero)
menor = min(listNumero)

posicaoMenor = listNumero.index(menor)
posicaoMaior = listNumero.index(maior)

print(f"O maior valor digitado foi #{posicaoMaior} {maior}")
print(f"O menor valor digitado foi #{posicaoMenor} {menor}")

print(listNumero)