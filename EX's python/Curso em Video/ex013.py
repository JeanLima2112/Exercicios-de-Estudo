# Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 15 % de aumento
x = float(input("Qual é o salario atual?:"))
y = float(input("Qual a porcentagem de aumento a ser aplicada?:"))
print("com o salario de {}R$ sendo aplicado {}% de aumento resulta em um novo salario de {}R$".format(x,y,x+((x/100)*y)))