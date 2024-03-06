# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    num = int(input("Digite um Numero para descobrir sua tabuada:"))
    if num < 0 :
        break
    print("===TABUADA===")
    for cont in range(0,11):
        print(f"{cont:2} X {num:2} = {cont * num}")
    print("="*13)
