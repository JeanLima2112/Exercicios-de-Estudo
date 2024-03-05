# Escreva um programa que pergunte a quantidade de Km percorridos por um carro e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado
dias = int(input("Por quantos dias o carro ficou alugado:"))
km = float(input("Quantos quilometros foram rodados?:"))
valor = (dias * 60) + (km * 0.15)
print("sendo utilizado por {} dias e rodando {} km o valor a ser pago é de {:.2f} R$".format(dias,km,valor))
