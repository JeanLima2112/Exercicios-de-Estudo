# Crie um programa que simule o funcionamento de um caixa eletrônico.
# no inicio, pergunte ao usuário qual será o valor a ser sacado (numero inteiro)
# e o programa vai informar quantas cedulas de cad valor serão entregues
n = int(input("Qual o valor que você deseja sacar?:"))
ced = 100
while True:
    if total >= ced:
        while total >= ced:
            total = total - ced
            contced += 1
        print(f"Você podera sacar {contced} notas de {ced}R$")
    if total == 0:
        break
    else:
        if total < 100:
            ced = 50
            if total < 50:
                ced = 20
                if total <20:
                    ced = 10
                    if total < 10:
                        ced = 5
                        if total < 5:
                            ced = 2
                            if total < 2:
                                ced = 1
    contced = 0