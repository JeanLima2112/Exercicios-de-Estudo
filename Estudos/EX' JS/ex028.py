# Escreva um programa que faça o computador "pensar" em um numero entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo omputador. o programa devera escrever na tela se o usuario venceu ou perdeu.
import random
x = random.randint( 0,5)
y = int(input("Estou pensando em um numero de 0 a 5, em que numero estou pensando?:"))
if x == y:
    print("Você acertou estava realmente pensando em {}".format(y))
else:
    print("Você errou não estava pensando em {} na verdade estava pensando em {}".format(y,x))