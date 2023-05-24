# faça o programa que leia o peso de 5 pessoas .
# no final, mostre qual foi o maior e o menor peso lidos
pesomaior = pesomenor = 0
for cont in range(1,6):
    pesolido = float(input(f"Qual o peso da {cont}° pessoa(KG):"))
    if pesolido > pesomaior :
        pesomaior = pesolido
    if (pesolido < pesomenor) or (cont == 1):
        pesomenor = pesolido
print(f"o Menor peso foi de {pesomenor} KG\nO maior peso foi de {pesomaior} KG")
