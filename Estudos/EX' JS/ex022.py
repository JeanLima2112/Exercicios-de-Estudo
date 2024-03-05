# Crie um programa que leia o nome completo de uma Pessoa e Mostre
# o nome com todas as letras maiusculas
#o nome com todas as letras minusculas
# quantas letras tem o nome inteiro sem considerar espaços
#Quantas letras tem o Primeiro nome
nome = str(input("Digite seu nome:")).strip()
x = nome.split()
y = x[0]
print("seu nome inteiro é {}\n com todas MAIUSCULAS {}\n Com todas minusculas {}\no nome todo possui {} letras\no primeiro é {} e possui {} letras".format(nome,nome.upper(),nome.lower(),len(nome)-nome.count(" "),y,len(y)))