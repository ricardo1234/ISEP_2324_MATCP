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
