# Crie um programa que leia o nome e o preço de varios produtos.
# o programa deverá perguntar se o usuario vai continuar No final, mostre:
# A) Qual é o Total gasto na compra
# B) Quantos produtos custam mais de R$ 1000
# C) Qual é o nome do produto mais barato
total= prod1000 = prodb = 0
print("="*20,"\nMercado do seu Jorge")
print("="*20)
while True:
    print("NOVO PRODUTO")
    print("="*20)
    nome = input("Qual o nome do produto?:")
    while True:
        preço = float(input("Qual o Preço do produto?:"))
        if preço > 0 :
            break
    total += preço
    if preço > 1000:
        prod1000 += 1
    if preço < prodb or prodb == 0:
        prodb = preço
        nprodb = nome
    while True:
        resp = input("Deseja Continuar?[S/N]:").upper().strip()[0]
        if resp == "S" or resp == "N":
            break
    if resp == "N":
        break
print(f"O total Gasto Foi {total}R$\nExistem {prod1000} produtos custando mais de 1000R$\nO produto mais barato é {nprodb} custando {prodb}R$")

