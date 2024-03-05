# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
# para salarios superiores a R$1.250,00, calcule um aumento de 10%
# para os inferiores ou iguais, o aumento é de 15%
sal = float(input("Qual é o salario:"))
if sal > 1250:
    print("o salario de {:.2f}R$ será aplicada um aumento de 10% ficando {:.2f}R$".format(sal,sal * 1.10))
else:
    print("o salario de {:.2f}R$ será aplicada um aumento de 15 % ficando {:.2f}R$".format(sal,sal*1.15))