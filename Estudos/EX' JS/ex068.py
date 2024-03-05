#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
from time import sleep
vitorias = 0
while True:
    while True:
        escolha = input("Deseja PAR ou IMPAR [P/I]").upper().strip()[0]
        if escolha == "P" or escolha == "I":
            break
    while True:
        jogadap = int(input("Você joga quantos Dedos?, 0 a 10:"))
        if jogadap > 0 and jogadap < 10:
            break
    jogadacom = randint(0,10)
    print(f"Sua escolha:{escolha}")
    sleep(1)
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    print("-="*20)
    print(f"Voce joga {jogadap}\nComputador joga {jogadacom}")
    print("-="*20)
    if escolha == "P":
        if (jogadap + jogadacom) % 2 == 0:
            print(f"Total:{jogadap + jogadacom}, você ganhou")
            vitorias +=1
        else:
            print(f"Total:{jogadap + jogadacom}, você perdeu")
            break
    else:
        if (jogadap + jogadacom) % 2 == 1:
            print(f"Total:{jogadap + jogadacom}, você ganhou")
            vitorias += 1
        else:
            print(f"Total:{jogadap + jogadacom}, você perdeu")
            break
print("-="*20)
print(f"Total de Vitorias:{vitorias}")

