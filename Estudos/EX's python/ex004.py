# Faça um programa que leia algo pelo teclado e mostre seu tipo primitivo e todas as informaçoes possiveis sobre ele
x = input("Digite Algo:")
print("{} é um:".format(x),type(x))
print("{} é um numero:".format(x),x.isnumeric())
print("{} são letras:".format(x),x.isalpha())
print("{} são letras e numeros:".format(x),x.isalnum())
print("{} está em minusculo:".format(x),x.islower())
print("{} está em maiusculo:".format(x),x.isupper())
