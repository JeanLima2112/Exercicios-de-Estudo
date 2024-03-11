# Escreva um programa que leia a velocidade de um carro.
#se ele ultrapassar 80km/h mostre uma mensagem de que ele foi multado
# a multa vai custar r$7,00 por cada Km acima do limite.

vel = float(input("A que velocidade o carro está?:"))
if vel> 80:
    print("você ultrapassou o Limite de velocidade de 80Km/h voce passou a {:.2f}KM/h e excedeu em {:.2f}KM/h o limite, portando sua multa será de {:.2f}R$".format(vel,vel-80,(vel-80)*7))
else:
    print("Você passou dentro da velocidade Permitida")
