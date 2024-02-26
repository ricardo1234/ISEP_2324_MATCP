
- [Teórica](https://moodle.isep.ipp.pt/pluginfile.php/360049/mod_resource/content/1/CAP%C3%8DTULO%201_MATCP_LEI_2023_2024_V2.pdf)
- [Exercicios](https://moodle.isep.ipp.pt/pluginfile.php/360050/mod_resource/content/1/Exercicios_MATCP_Capitulo_1_LEI_2023_24.pdf)

## Exercício 1
``` python
valorEmprestimo = input("Digite o valor do empréstimo: ")
salario = input("Digite o valor do salário: ")
anos = input("Digite a quantidade de anos: ")

valorEmprestimo = float(valorEmprestimo)
salario = float(salario)
anos = int(anos)

valorPrestacao = valorEmprestimo / (anos * 12)

if valorPrestacao > salario * 0.3:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")
    print(f"Valor da prestação: {valorPrestacao:.2f}€")
```

## Exercício 2
``` python
valorCompra = float(input("Digite o valor da compra: "))
print(f"Tipos de Pagamento:\n A - Pronto Pagamento\n B - Pagamento 2x\n C - Pagamento 3x ou mais")
tipoPagamento = input("Digite o tipo de pagamento: ")

if tipoPagamento == "A":
    valorCompra = valorCompra - (valorCompra * 0.1)
    print(f"Valor da compra: {valorCompra:.2f}€")
elif tipoPagamento == "B":
    print(f"Valor da compra: {valorCompra:.2f}€")
elif tipoPagamento == "C":
    valorCompra = valorCompra + (valorCompra * 0.2)
    print(f"Valor da compra: {valorCompra:.2f}€")
else:
    print("Tipo de pagamento inválido")
```

## Exercício 3
``` python
import random

jogadas = 0
vitorias = 0

while jogadas < 10:
	jogadaUsuario = input(f"Digite a sua jogada #{jogadas+1}: ")
    if jogadaUsuario != "tesoura" and jogadaUsuario != "papel" and jogadaUsuario != "pedra":
        continue
    jogadaComputador = random.choice(["pedra", "papel", "tesoura"])
    print(f"Jogada do computador: {jogadaComputador}")

	if jogadaUsuario == "pedra" and jogadaComputador == "tesoura":
        vitorias += 1
    elif jogadaUsuario == "papel" and jogadaComputador == "pedra":
        vitorias += 1
    elif jogadaUsuario == "tesoura" and jogadaComputador == "papel":
        vitorias += 1
    jogadas += 1

print(f"Percentagem de vitórias: {vitorias / 10 * 100:.2f}%")
```


## Exercício 4
``` python
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
```

## Exercício 5
``` python
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
```

## Exercício 6
``` python
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
```

## Exercício 7

``` python
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
```

## Exercício 8
``` python
Alunos = []

while input('Quer continuar? [S/N] ') == 'S':
    Alunos.append([int(input('Numero: ')), input('Nome: '), float(input('Nota 1: ')), float(input('Nota 2: '))])

print("Numero\tNome\tNota 1\tNota 2\tMedia")

for i in range(len(Alunos)):
    print(f'{Alunos[i][0]}\t{Alunos[i][1]}\t{Alunos[i][2]}\t{Alunos[i][3]}\t{(Alunos[i][2] + Alunos[i][3])/2:.2f}')

while True:
    n = int(input('Nº Aluno: '))
    if n == 0:
        break
    print(f'Numero\tNome\tNota 1\tNota 2\tMedia')
    for i in range(len(Alunos)):
        if Alunos[i][0] == n:
            print(f'{Alunos[i][0]}\t{Alunos[i][1]}\t{Alunos[i][2]}\t{Alunos[i][3]}\t{(Alunos[i][2] + Alunos[i][3])/2:.2f}')
            break
    else:
        print('Aluno não encontrado')

```

## Exercício 9

``` python
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    if fim < inicio:
        fim, inicio = inicio, fim
    for c in range(inicio, fim + 1, passo):
        print(f"{c}", end=" ")
    print("")
contador(1, 10, 1)
contador(10, 0, -2)
contador(10, 100, 3)
```

## Exercício 10

``` python
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
```