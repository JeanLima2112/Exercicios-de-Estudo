# crie um programa que leia dois valores e mostre um menu na tela:
# [1] SOMAR
# [2]MULTIPLICAR
# [3]MAIOR
# [4]novos numeros
# [5]Sair do programa
# Seu Programa devera realizar a operação selecionada em cada caso
num1 = float(input("Digite o Primeiro numero:"))
num2 = float(input("Digite o Segundo Numero:"))
resp = int(input("Que Operação Você deseja realizar\n[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]DIGITAR NOVOS NUMEROS\n[5]SAIR DO PROGRAMA\nSua Resposta:"))
while resp != 5:
    if resp == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif resp == 2:
        print(f"{num1} X {num2} = {num1 * num2}")
    elif resp == 3:
        if num1 > num2:
            print(f"{num1} é maior que {num2}")
        elif num1 < num2:
            print(f"{num2} é maior que {num1}")
        else:
            print("São iguais")
    elif resp == 4:
        num1 = float(input("Digite o Primeiro numero:"))
        num2 = float(input("Digite o Segundo Numero:"))
    resp = int(input("Que Operação Você deseja realizar\n[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]DIGITAR NOVOS NUMEROS\n[5]SAIR DO PROGRAMA\nSua Resposta:"))

print("\nPROGRAMA ENCERRADO")