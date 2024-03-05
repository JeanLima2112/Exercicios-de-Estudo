#Faça um programa que leia alargura e a altura de uma parede em metros, calcule a sua àrea e a quantidade de tinta necessaria para pinta-la sabendo que cada litro de tinta pinta uma area de 2 m²
alt = float(input("Qual é a Altura em metros da Parede?:"))
larg = float(input("Qual é a Largura em metros da Parede?:"))
x = alt * larg
print("a altura da sua parede é {}m a largura é {}m isso resulta em uma parede de {}m² e para pinta-la você necessitara de {} litros de tinta".format(alt,larg,x,x/2))