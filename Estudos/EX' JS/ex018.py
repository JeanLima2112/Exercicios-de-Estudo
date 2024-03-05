#Faça um Programa que leia um angulo qualquer e mostre na tela o valor do seno cosseno e tangente desse angulo
import math
x = int(input("Digite um angulo:"))
cos = math.cos(x)
sen = math.sin(x)
tan = math.tan(x)
print("Seno {:.2f}\nCoseno{:.2f}\nTangente{:.2f}".format(sen,cos,tan))