# Faça um programa que leia um numero qualquer e mostre o seu fatorial
import math
# usando For
total = num1 = int(input("Digite um numero para saber seu fatorial:"))
for cont in range (num1-1,0,-1):
    total = cont * total
print(f"O fatorial de {num1} é {total}")
# usando While
cnt = num1 -1
tot = num1
while cnt != 1:
    tot = tot * cnt
    cnt = cnt - 1
print(f"O fatorial de {num1} é {tot}")
# usando função
result = math.factorial(num1)
print(f"O fatorial de {num1} é {result}")




