# crie um jogo que faça o computador jogar Jokempô com você
import random
import time
itens = ("Pedra","Papel","Tesoura")
jogadacomp = random.randint(0,2)
jogada = int(input("Escolha sua Jogada:\n[0] PEDRA \n[1]PAPEL \n[2]TESOURA\nSua Jogada:"))
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO")
print("-="*11,f"\nSua jogada foi {itens[jogada]}\nO computador jogou {itens[jogadacomp]}\n","-="*11)
if jogadacomp == 0:
    if jogada == 0:
        print("Empate")
    elif jogada ==1:
        print("Jogador WINS!")
    elif jogada == 2:
        print("Computador WINS!")
    else:
        print("Jogada invalida")
elif jogadacomp == 1:
    if jogada == 0:
        print("Computador WINS!")
    elif jogada ==1:
        print("Empate")
    elif jogada == 2:
        print("Jogador WINS!")
    else:
        print("Jogada invalida")
elif jogadacomp == 2:
    if jogada == 0:
        print("Jogador WINS!")
    elif jogada ==1:
        print("Computador WINS!")
    elif jogada == 2:
        print("Empate")
    else:
        print("Jogada invalida")
else:
    print("Jogada invalida")

