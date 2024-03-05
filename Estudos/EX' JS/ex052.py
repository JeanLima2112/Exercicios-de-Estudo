# faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo
num = int(input("Digite um numero inteiro para saber se é primo ou não:"))
div = 0
for cont in range(num,0,-1):
    if num % cont == 0:
        div += 1
if div > 2:
    print (f"{num} Não é um numero Primo")
else:
    print(f" {num} É um numero primo ")
