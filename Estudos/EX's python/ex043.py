# desenvolva uma logica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5:Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: sobrepeso
# -Acima de 40: Obesidade Morbida              FORMULA DE IMC : peso/ altura²
peso = float(input("Qual é o seu peso em KG?:"))
altura = float(input("Qual sua Altura em Metros?:"))
IMC = peso/ (altura **2)
if IMC < 18.5:
    print(f"O seu IMC é de {IMC:.2f}, Classificado como Abaixo do Peso")
elif IMC >= 18.5 and IMC < 25:
    print(f"O seu IMC é de {IMC:.2f}, Classificado como Peso ideal")
elif IMC >= 25 and IMC < 30:
    print(f"O seu IMC é de {IMC:.2f}, Classificado como Sobrepeso")
elif IMC >=30 and IMC < 40:
    print(f"O seu IMC é de {IMC:.2f}, Classificado como Obesidade")
else:
    print(f"O seu IMC é de {IMC:.2f}, Classificado como Obesidade Morbida")
