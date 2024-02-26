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
