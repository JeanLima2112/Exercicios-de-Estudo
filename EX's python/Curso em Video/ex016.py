# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira
from math import trunc
x = float(input("Digite um numero:"))
# n = trunc(x)
print("o numero digitado foi {} e sua porção inteira é {}".format(x,trunc(x)))

