# Crie um programam que tenha uma tupla unica com nomes de produtos e seus respectivos preços,
# na sequencia. No final,mostre uma listagem de preços, organizando os dados em forma tabular
valores = ("Caderno",23.45,"Lapis",2.43,
           "Borracha",0.50,"Apontador",3.43,
           "Marca Texto",7.45,"estojo",9.99,"Mochila",50.00)
print("-"*40)
print(f"{'LISTA DE PREÇOS':^40}")
print("-"*40)
for c in range(0,len(valores)):
    if c % 2 == 0:
        print(f"{valores[c]:_<30}",end=" ")
    else:
        print(f"R${valores[c]:>7.2f}")
print("-"*40)
