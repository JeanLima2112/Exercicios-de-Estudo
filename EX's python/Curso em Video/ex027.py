# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente

nome = str(input("Digite um Nome:"))
n = nome.split()
print("o nome digitado foi:{} o primeiro nome é {} e o ultimo é {}".format(nome,n[0],n[-1]))