nome = []
valorcompra = []
valorvenda = []
lucro = []
tam = 5

for c in range(0,tam):
    nome.append(str(input("Qual o nome da Mercadoria?:")))
    valorcompra.append(float(input(f"Qual foi o Valor de compra de {nome[c]}?:")))
    valorvenda.append(float(input(f"Qual o valor de venda de {nome[c]}?:")))
    lucro.append(((valorvenda[c]-valorcompra[c])/valorcompra)* 100)

print (lucro)
