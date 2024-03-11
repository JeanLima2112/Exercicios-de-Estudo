# Crie um programa que leia 5 valores numericos e guarde-os em uma lista.
# No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
lista = list()
for c in range(0,5):
    lista.append(int(input(f"Digite um numero na posição {c}:")))
    print(f"O maior  da lista foi {max(lista)} na posição {(lista.index(max(lista)))}")
print(f"O menor da lista foi {min(lista)} na posção {lista.index(min(lista))}")