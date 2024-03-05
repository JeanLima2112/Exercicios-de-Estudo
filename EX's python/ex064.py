# Crie um programa que leia varios numeros inteiros pelo teclado.
# o programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada.
# no final mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o 999/flag)
num1 = soma = cont = 0
while num1 != 999:
    num1 = int(input("Digite um numero inteiro:"))
    if num1 != 999:
        soma += num1
        cont += 1
print(f"foram digitados {cont} numeros e a soma entre eles é de {soma}")