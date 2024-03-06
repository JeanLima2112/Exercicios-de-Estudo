# crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
import  datetime
maiores = menores = 0
datatual = datetime.date.today().year
for cont in range(1,8):
    pessoa = int(input("Qual é o ano do seu nascimento?:"))
    if  datatual - pessoa >= 18:
        maiores += 1
    else:
        menores += 1
print(f"O numero de Maiores de Idade é de {maiores} pessoas\nO numero de menores de idade é de {menores} pessoas")