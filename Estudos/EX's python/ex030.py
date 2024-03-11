# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar

num = int(input("Digite um numero inteiro:"))
x = num % 2
if x == 1:
    print("O numero {} é impar".format(num))
else:
    print("o numero {} é par".format(num))