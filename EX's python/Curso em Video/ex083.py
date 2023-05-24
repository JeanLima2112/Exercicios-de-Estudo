# Crie um programa que o usuario digite uma expressão matematica que use parenteses.
# seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta.
lista = []
abre = fecha = 0
lista = input("Digite a expressão matematica:")
for c in lista:
    if c == "(":
        abre += 1
    if c == ")":
        fecha += 1
print("A expresão é valida" if abre == fecha else "Expressão incorreta")
