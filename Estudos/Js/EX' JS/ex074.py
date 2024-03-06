# Crie um programa que vai gerar 5 números aleatorios
# e colocar em uma tupla. Depois disso, Mostre a listagem de numeros
# gerados e tambem indique o menor e o maior valor que estão na tupla
from random import randint
numeros = (randint(0,10),randint(0,10),randint(0,10),
           randint(0,10),randint(0,10))
print("Numeros sorteados.",end=" ")
for n in numeros:
    print(f"{n}",end=" ")
print(f"\nO maior numero sorteado {max(numeros)}")
print(f"O menor numero sorteado {min(numeros)}")

