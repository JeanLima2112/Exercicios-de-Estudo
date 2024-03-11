# Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem ou não formar um triangulo
r0 = float(input("Digite o comprimento da primeira reta:"))
r1 = float(input("Da segunda reta"))
r2 = float(input("Da terceira reta:"))
if r0 > r1+r2 or r1>r2+r0 or r2>r1+r0:
    print("{}, {} e {} não formam um triangulo".format(r0,r1,r2))
else:
    print("{} {} e {} formam um triangulo".format(r0,r1,r2))