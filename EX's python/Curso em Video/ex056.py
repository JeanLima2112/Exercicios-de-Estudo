# desenvolva um programa que leia nome, idade e sexo de 4 pessoas. no final do programa, mostre:
# - a media de idade do grupo -
# - qual o nome do homem mais velho
# - Quantas mulheres tem menos de 20 anos
homemvelho= mulhernova = soma = 0
for cont in range(1,5):
    nome = str(input(f"Digite o Nome do {cont}° individuo:"))
    sex = int(input(f"{nome} é do sexo\n [1]-Masculino\n [2]-Feminino\nSua Resposta:"))
    idade = float(input(f"Quantos anos tem {nome}?:"))
    soma += idade
    if sex == 1: 
        if idade > homemvelho :
            homemvelho = idade
            nomehomemvelho = nome
    if sex == 2:
        if idade < 20:
            mulhernova += 1
print(f"A media de idade das pessoas é de {soma/4}")
print(f"O homem mais velho tem {homemvelho} anos e se chama {nomehomemvelho}\nexistem {mulhernova} mulheres com idade menor que 20 anos")

