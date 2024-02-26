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