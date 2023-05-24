# A confederação nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria de acordo com sua idade
# - até 9 anos: MIRIM
# - até 14 anos: INFANTIL
# - até 19 anos: JUNIOR
# - até 20 anos: SENIOR
# - Acima: MASTER
from datetime import date
datatual = date.today().year
nasc = int(input("Digite o ano de nascimento do atleta:"))
idade = datatual - nasc
if idade < 9:
    print(f"o atleta tem {idade} anos, faz parte da categoria MIRIM")
elif idade >= 9 and idade < 14:
    print(f"o atleta tem {idade}  anos, faz parte  da categoria INFANTIL")
elif idade >= 14 and idade < 19:
    print(f"o atleta tem {idade} anos , faz parte da categoria JUNIOR ")
elif idade >= 19 and idade < 20:
    print(f"o atleta tem {idade} anos, faz parte da categoria SENIOR")
elif idade >= 20 :
    print(f"o atleta tem {idade} anos, faz parte da categoria MASTER")




