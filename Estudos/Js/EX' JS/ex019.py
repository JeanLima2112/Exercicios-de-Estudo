# um professor quer sortear um dos seus alunos para apagar o quadro escreva um programa leia o nome deles e escreva o nome do escolhido
import random
x =str(input("Digite o nome do primeiro Aluno:"))
y =str(input("Digite o Nome do Segundo Aluno:"))
z =str(input("Digite o Nome do Terceiro Aluno:"))
a =str(input("Digite o Nome do Quarto Aluno:"))
lista = [x,y,z,a]
esc = random.choice(lista)
print("O escolhido foi {}".format(esc))