# Crie um Programa onde o usuário possa digitar cinco
# valores numericos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort())
# No final mostre a lista ordenada na tela
lista = list()
for c in range(1,6):
    aux = int(input("Digite um numero:"))
    if c == 1 or aux > lista[-1]:
        lista.append(aux)
        print(f"Numero {aux} adicionado ao final")
    else:
        pos = 0
        while pos < len(lista):
            if aux <= lista[pos]:
                lista.insert(pos,aux)
                print(f"Numero {aux} adicionado na {pos} posição")
                break
            pos += 1

print(f"Os valores digitados foram {lista}")



