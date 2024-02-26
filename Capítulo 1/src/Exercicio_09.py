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