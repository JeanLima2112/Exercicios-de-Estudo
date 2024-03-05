# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# no final, mostre os 10 primeiros termos dessa PA
a1 = int(input("Qual o primeiro termo da PA?:"))
r = int(input("Qual a razão:"))
d = a1 + (10 - 1) * r
print("Os 10 primeiros termos são:")
for cont in range(a1,d,r):
    print(f"{cont}",end="-")
print("FIM")

