#Crie um programa que leia números inteiros pelo teclado. O programa só vai
# parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
num1 = soma = cont = 0
while True:
    num1 = int(input("Digite um numero inteiro:"))
    if num1 == 999:
        break
    soma += num1
    cont += 1
print(f"foram digitados {cont} numeros e a soma entre eles é de {soma}")