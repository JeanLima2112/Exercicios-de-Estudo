#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = str(input("Digite um Nome:"))
x = nome.title()
print("Em {} tem o nome Silva?-".format(nome),"Silva" in x)