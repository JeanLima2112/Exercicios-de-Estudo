# faça um programa que calcule a soma ente todos os numeros impares
# que são multiplos de 3 e que se encontram no intervalo de 1 até 500
s = 0
for cont in range (1,501,2):
        if cont % 3 == 0:
            print(cont)
            s += cont
print(f"O resultado é {s}")
