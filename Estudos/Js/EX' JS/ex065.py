# Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução,
# mostre a Média entre todos os valores e qual foi o maior e o menor valores lidos .
# o programa deve perguntar ao usuario se ele quer ou não continuar a digitar mais valores
resp = "sim"
cont = soma = maiorlido = menorlido = 0
while resp == "sim":
    n = int(input("Digite um numero inteiro:"))
    cont += 1
    soma += n
    if n > maiorlido:
        maiorlido = n
    if n < menorlido or cont ==1:
        menorlido = n
    resp = input("Deseja continuar(sim ou não)")
print(f"O maior numero digitado foi {maiorlido}\nO Menor numero digitado foi {menorlido}\nA media entre os numeros digitados é {soma/cont}")
