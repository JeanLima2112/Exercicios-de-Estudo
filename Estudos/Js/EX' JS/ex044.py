# elabore um Programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - á vista(Dinheiro / Cheque): 10 % de desconto
# - á vista no cartão: 5 % de desconto -no cartão:
# - em até 2x no cartão: Preço normal
# - 3x ou mais no cartão: 20 % de juros
custo = float(input("Digite o Valor do Produto(R$):"))
pag = int(input("Qual sera a forma de pagamento?\n[1]-Dinheiro \n[2]-Cheque \n[3]-Cartão de Credito\nsua escolha:"))
if pag == 1 or pag == 2:
    print(f"para pagamento a vista será apicado 10% de desconto o valor a pagar é de {custo * 0.90}R$")
elif pag == 3:
    parcela = int(input("Em quantas vezes deseja parcelar?:"))
    if parcela == 1:
        print(f"Em {parcela}° vez no cartão será aplicado 5% de desconto o valor a pagar é de {custo * 0.95}R$")
    elif parcela == 2:
        print(f"em {parcela}° vezes no cartão será cobrado o valor integral de {custo}R$")
    elif parcela >= 3:
        print(f"em {parcela}° vezes no cartão será cobrado 20% de juros o valor a pagar é de {custo * 1.20}R$")
    else:
        print("Não é um valor valido")
else:
    print("Não é um valor valido")
