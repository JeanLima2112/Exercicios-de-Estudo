def soma_intervalo(a,b):
    soma = 0
    if a > b:
        aux = b
        b = a
        a = aux
    for c in range(a+1,b):
        soma += c
    print(f"O A soma entre os numeros no intervalo de {a} até {b} é {soma}")

soma_intervalo(5,8)








