# Crie um Programa que leia a idade e o sexo de varias pessoas.
# a cada pessoa cadastrada o programa devera perguntar se o usuario quer ou não continuar.
# no final Mostre
# -a) Quantas Pessoas tem mais de 18 anos
# -b) Quantos homens foram cadastrados
# -c)Quantas Mulheres tem menos de 20 anos
pesmaior= homemcad= mulhermenor = 0
while True:
    print("-="*10)
    print("CADASTRO")
    print("-="*10)
    while True:
        idade = int(input("Qual a idade?:"))
        if idade > 0:
            break
    while True:
        sex = input("Qual é o Sexo?[M/F]:").upper().split()[0]
        if sex == "M" or sex == "F":
            break
    if sex == "M":
        homemcad += 1
    if idade >= 18:
        pesmaior += 1
    if sex == "F" and idade < 20:
        mulhermenor += 1
    while True:
        resp = input("Deseja Continuar?[S/N]:").upper().split()[0]
        if resp == "S" or resp == "N":
            print("-="*10)
            break
    if resp == "N" :
        break
print(f"Existem {pesmaior} pessoas maiores de 18 anos\nForam cadastrados {homemcad} homens\nExistem {mulhermenor} Mulheres com menos de 20 anos")

