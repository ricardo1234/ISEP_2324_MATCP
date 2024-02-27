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