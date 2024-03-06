# Desenvolva um programa que pergunte a distancia de uma viagem em Km  calcule o preço da passagem, cobrando r$0,50 por Km para viagens de até 200km e |R$0,45 para viagens mais longas
dist = float(input("Qual foi a distancia percorrida em Km:"))
if dist > 200:
    print("você utilizará a tarifa de longas viagens portanto o valor a pagar é de R${:.2f} ".format(dist * 0.45))
else:
    print("você utilizará a tarifa de viagens curtas portanto o valor a pagar é de {:.2f}".format(dist * 0.50))
