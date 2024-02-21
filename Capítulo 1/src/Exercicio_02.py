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


