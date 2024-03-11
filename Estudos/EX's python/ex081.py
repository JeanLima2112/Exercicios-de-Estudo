# Crie um programa que vai ler vários números e colocar em uma lista. depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores ordenada de forma decrescente
# C)Se o valor 5 foi digitado e se está ou não na lista
lista = []
while True:
    lista.append(int(input("Digite um numero:")))
    resp = input("Deseja continuar?[S/N]").strip().upper()[0]
    if resp == "N":
        break
lista.sort(reverse=True)
print(f"Foram digitados {len(lista)} elementos.")
print(f"Em ordem decrescente a lista fica {lista}")
if 5 in lista:
    print("O numero 5 foi digitado na lista")
else:
    print("Não existe 5 na lista.")