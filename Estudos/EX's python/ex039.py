#Faça um programa que leia o ano de nascimento de um jovem,
# de acordo com sua idade:
# - se ele ainda vai se alistar ao serviço militar
# - se é a hora de se alistar
# - Se já passou da hora de se alistar
# seu programa tambem de mostrar o tempo que falta ou que passou do praazo
from datetime import date
datatual = date.today().year
nasc = int(input("Qual é o seu ano de nascimento?:"))
tempo = datatual - nasc
if tempo > 18:
    print(f" Você deveria ter se alistado há {tempo - 18} anos\n o seu ano de alistamento foi em {datatual - (tempo - 18)}")
elif tempo == 18:
    print(f"Você deve se alistar Imediatamente")
elif tempo < 18:
    print(f"Ainda faltam {18 - tempo} anos para você se alistar \no seu ano de alistamento será {datatual + (18-tempo)}")