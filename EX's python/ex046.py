# faça um programa que mostre uma contagem regressiva para o estouro de fogos de artificio,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles. emoji de fogos
import time
import emoji
for cont in range(10,-1,-1):
    time.sleep(1)
    print(cont)
print(emoji.emojize(":fireworks:"))
print(emoji.emojize(":sparkler:"))