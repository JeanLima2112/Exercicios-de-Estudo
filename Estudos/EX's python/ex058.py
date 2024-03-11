# Melhore o jogo do desafio 028 onde o computador vai pensar
# em um numero entre 0 e 10. só que agora o jogador vai tentar adivinhar até acertar, mostrando no
# final quantos palpites foram necessarios para vencer
import random
y = int(input("Estou pensando em um numero de 0 a 10, em que numero estou pensando?:"))
tentativas = 1
x = random.randint(0,10)
while x != y:
    y = int(input("Você errou, Tente novamente:"))
    tentativas += 1
print(f"Você acertou em {tentativas} tentativas")


