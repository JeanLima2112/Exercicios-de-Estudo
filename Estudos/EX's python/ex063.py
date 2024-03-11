# escreva um programa que leia um numero n inteiro qualquer
# e mostre na tela os n primeiros elementos de uma sequencia de Fibonacci.
n = int(input("Quantos elementos da sequencia de fibonacci você deseja descobrir?:"))
c = 0
atual = anterior = 1
while c < n :
    novo = atual + anterior
    anterior = atual
    atual = novo
    c+=1
    print(novo)


