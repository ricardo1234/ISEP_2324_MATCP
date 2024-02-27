
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
[Source Code](src/Exercicio_01.py)
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
[Source Code](src/Exercicio_02.py)
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
[Source Code](src/Exercicio_03.py)
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
[Source Code](src/Exercicio_04.py)
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
[Source Code](src/Exercicio_05.py)
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
[Source Code](src/Exercicio_06.py)
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
[Source Code](src/Exercicio_07.py)
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
[Source Code](src/Exercicio_08.py)
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
[Source Code](src/Exercicio_09.py)
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
[Source Code](src/Exercicio_10.py)
## Exercício 11
``` python
import random

def caraCroa():
    if random.random() < 0.5:
        return "Cara"
    return "Coroa"

def testGame(n):
    coroas = 0
    for i in range(n):
        if caraCroa() == "Coroa":
            coroas += 1
    print(f"O numero de caras foi {coroas} que corresponde a {(coroas/n*100):.2f}%")

testGame(10)
testGame(100)
testGame(1000)
testGame(10000)
testGame(100000)
```
[Source Code](src/Exercicio_11.py)
### Resultados
	O numero de caras foi 6 que corresponde a 60.00%
	O numero de caras foi 47 que corresponde a 47.00%
	O numero de caras foi 470 que corresponde a 47.00%
	O numero de caras foi 5043 que corresponde a 50.43%
	O numero de caras foi 50268 que corresponde a 50.27%

Podemos observar que valor teórico não foi obtido nenhuma vez, mas quanto maior o numero de iterações, mais o valor real se aproxima do teórico. 
## Exercício 12
``` python
import random

def jogar():
    for i in range(4):
        numero = random.randint(1, 6)
        if numero == 6:
            return True
    return False

def jogarXvezes(n):
    vitorias = 0
    for i in range(n):
        if jogar():
            vitorias += 1
    return vitorias

def estatistica(n):
    vitorias = jogarXvezes(n)
    print(f'Vitorias: {vitorias}\t\tProbabilidade: {vitorias / n * 100:.2f}%')

estatistica(100)
estatistica(1000)
estatistica(10000)
estatistica(100000)
```
[Source Code](src/Exercicio_12.py)

### Resultados
	Vitorias: 48            Probabilidade: 48.00%
	Vitorias: 530           Probabilidade: 53.00%
	Vitorias: 5163          Probabilidade: 51.63%
	Vitorias: 51815         Probabilidade: 51.81%


X: De não sair 6 em 4 jogadas 
$P(X) = \frac{5}{6}*\frac{5}{6}*\frac{5}{6}*\frac{5}{6}=0.4822 \Leftrightarrow48.22\%$
Logo a probabilidade de sair pelo menos um 6 em 4 jogadas é de: $1-P(X) = 1-0.4822=0.5178 \Leftrightarrow51.78\%$ 
Mais uma vez quanto maior o numero mais se aproxima do valor teorico.

## Exercício 12
``` python
import random

Artimanhas = 0.05
Bombom = 0.2
Caramelo = 0.25
Diluvio = 0.5

def corrida():
    prob = random.random()
    if prob < Artimanhas:
        return "Artimanhas"
    elif prob < Artimanhas + Bombom:
        return "Bombom"
    elif prob < Artimanhas + Bombom + Caramelo:
        return "Caramelo"
    elif prob < Artimanhas + Bombom + Caramelo + Diluvio:
        return "Diluvio"
    else:
        return "Nada"

def campeonato(n):
    campeonato = []
    for i in range(n):
        campeonato.append(corrida())
    return campeonato

def statsCampeonato(n):
    resultados = campeonato(n)
    print(f"{n}\t\t{resultados.count('Artimanhas')/n*100:.2f}%\t\t{resultados.count('Bombom')/n*100:.2f}%\t\t{resultados.count('Caramelo')/n*100:.2f}%\t\t{resultados.count('Diluvio')/n*100:.2f}")

print("Nº Jogadas\tArtimanhas\tBomba\t\tCaramelo\tDiluvio")
statsCampeonato(100)
statsCampeonato(1000)
statsCampeonato(10000)
statsCampeonato(100000)
```
[Source Code](src/Exercicio_13.py)

### Resultados
	Nº Jogadas      Artimanhas      Bomba           Caramelo        Diluvio
	100             3.00%           24.00%          22.00%          51.00%
	1000            4.80%           20.30%          24.70%          50.20%
	10000           4.72%           20.39%          24.46%          50.43%
	100000          4.98%           20.02%          25.20%          49.80%


X: De não sair 6 em 4 jogadas 
$P(X) = \frac{5}{6}*\frac{5}{6}*\frac{5}{6}*\frac{5}{6}=0.4822 \Leftrightarrow48.22\%$
Logo a probabilidade de sair pelo menos um 6 em 4 jogadas é de: $1-P(X) = 1-0.4822=0.5178 \Leftrightarrow51.78\%$ 
Mais uma vez quanto maior o numero mais se aproxima do valor teórico.