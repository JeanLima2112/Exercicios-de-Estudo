n1 = int(input("Digite o numero N1:"))
n2 = int(input("Digite o numero N2:"))
cont = 0
aux = n1
while True:
    if aux - n2 > 0:
        aux -= n2
    else:
        print(f"o Resto da divisão de {n1} por {n2} é {aux}")
        break

