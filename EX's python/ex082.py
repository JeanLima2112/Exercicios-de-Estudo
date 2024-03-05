# Crie um programa que vai ler vários numeros e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores impares
# digitados respectivamente ao final mostre o conteudo da três listas geradas
lista = []
listapar = []
listaimpar = []
while True:
    lista.append(int(input("Digite um numero:")))
    resp = input("Deseja continuar?[S/N]").upper().strip()[0]
    if resp == "N":
        break
for c in lista:
    if c % 2 == 0:
        listapar.append(c)
    else:
        listaimpar.append(c)
print(f"lista comum {lista}\nLista dos Pares {listapar}\nLista dos Impares{listaimpar}")
