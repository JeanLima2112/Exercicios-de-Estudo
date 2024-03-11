# Faça um algoritimo que leia um preço de um produto e mostre o seu novo preço com 5 % de desconto
x = float(input("Qual é o preço atual do produto?:"))
y = float(input("Qual será o desconto aplicado?:"))
print("com o preço de {}R$ sendo aplicado {}% de desconto resultara em um nov preço de {}R$".format(x,y,x-((x/100)*y)))