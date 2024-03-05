# faça um programa que leia um ano qualquer e mostre se ele é bisexto
ano = int(input("Digite um ano para descobrir se ele é ou não bissexto:"))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("{} é um ano Bissexto".format(ano))
else:
    print("{} Não é um ano Bissexto".format(ano))