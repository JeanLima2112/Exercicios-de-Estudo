# Faça um programa que leia o comprimento do cateto oposto e do cateto adsjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
import math
co = float(input("Digite o comprimento em centimetros do Cateto Oposto"))
ca = float(input("Digite o Comprimento em centimetros do Cateto Adsjascente:"))
# Forma Matematica (x² = c² + c²)
hip = (((co ** 2) + (ca ** 2))**0.5)
# Forma Modular
hip = math.hypot(co,ca)
print("Cateto Oposto {}\nCateto Adsjascente {}\nHipotenusa:{}".format(co,ca,hip))