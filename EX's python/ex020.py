# o mesmo professor do exercicio anterior quer sortear a ordem de apresentação de trabalhos dos alunos faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random
x =str(input("Digite o nome do primeiro Aluno:"))
y =str(input("Digite o Nome do Segundo Aluno:"))
z =str(input("Digite o Nome do Terceiro Aluno:"))
a =str(input("Digite o Nome do Quarto Aluno:"))
lista = [x,y,z,a]
random.shuffle(lista)
print("A ordem de apresentação será: {}".format(lista))