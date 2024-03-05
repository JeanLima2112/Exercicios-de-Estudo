#Faça um Programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input("digite um Numero:"))
n2 = float(input("digite outro Numero:"))
n3 = float(input("digite mais um Numero:"))

if n1 > n2 > n3:
    print(" do maior para o menor a ordem é: {} {} {}".format(n1, n2, n3))
if n1 > n3 > n2:
    print(" do maior para o menor a ordem é: {} {} {}".format(n1, n3, n2))
if n2 > n3 > n1:
    print(" do maior para o menor a ordem é: {} {} {}".format(n2, n3, n1))
if n2 > n1 > n3:
    print(" do maior para o menor a ordem é: {} {} {}".format(n2, n1, n3))
if n3 > n2 > n1:
    print(" do maior para o menor a ordem é: {} {} {}".format(n3, n2, n1))
if n3 > n1 > n2:
    print(" do maior para o menor a ordem é: {} {} {}".format(n3, n1, n2))
