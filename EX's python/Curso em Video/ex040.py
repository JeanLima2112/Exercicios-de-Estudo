# crie um programa que leia duas notas de um aluno e calcule sua media,
# mostrando uma mensagem no final, de acordo com a media atingida
# - media abaixo de 5 reprovado
# - media entre 5.0 e 6.9 recuperação
# - media 7 ou superior aprovado
n1 = float(input("Digite a  primeira nota do aluno:"))
n2 = float(input("Digite a segunda nota do aluno:"))
media = (n1 + n2)/2
if  media < 5:
    print(f" a sua nota foi {media:.1f} portanto você está reprovado")
elif (media > 5) and (media < 6.9):
    print(f"a sua nota foi {media:.1f} portanto você está de recuperação")
else:
    print(f"a sua nota foi {media:.1f}, Você foi aprovado")
