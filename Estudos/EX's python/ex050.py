#Desenvolva um programa que leia 6 numeros inteiros
# e mostre a soma dos valores pares digitados, se for impar desconsidera-lo
s = 0
for c in range(1,7):
    v = int(input("Digite um numero inteiro:"))
    if v % 2 == 0:
        s += v
print(f"A soma dos numeros pares digitados é {s}")