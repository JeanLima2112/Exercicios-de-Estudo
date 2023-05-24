# Escreva um programa para aprovar o emprestimo bancario para compra de uma casa.
# o programa vai perguntar o valor da casa, o salario do comprador e em quanto anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado
valor = float(input("Qual o Valor da casa?:"))
sal = float(input("Qual o salario Mensal do Comprador?:"))
tempo = int(input("Em quantos anos pretende Pagar?:"))
prest = (valor/(tempo * 12))
psal = ((prest * 100)/sal)
if psal > 30 :
    print(f"o valor mensal da prestação ficou em {prest:.2f}R$ o que representa {psal:.2f}% do salario portanto o emprestimo está negado")
else:
    print(f"o valor mensal da prestação será de {prest:.2f} R$")
