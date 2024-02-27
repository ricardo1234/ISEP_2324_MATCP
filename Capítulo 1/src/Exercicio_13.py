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
    print(f"{n}\t\t{resultados.count('Artimanhas')/n*100:.2f}%\t\t{resultados.count('Bombom')/n*100:.2f}%\t\t{resultados.count('Caramelo')/n*100:.2f}%\t\t{resultados.count('Diluvio')/n*100:.2f}%")

print("Nº Jogadas\tArtimanhas\tBomba\t\tCaramelo\tDiluvio")
statsCampeonato(100)
statsCampeonato(1000)
statsCampeonato(10000)
statsCampeonato(100000)