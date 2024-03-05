# Refaça o Desafio 035 dos triãngulos,
# acresentando o recurso de mostrar que tipo de triangulo será formado
# - Equilatero: todos os lados iguais
# - Isóceles: Dois lados iguais
# - Escaleno:todos os lados diferentes
r0 = float(input("Digite o comprimento da primeira reta:"))
r1 = float(input("Da segunda reta"))
r2 = float(input("Da terceira reta:"))
if r0 > r1+r2 or r1>r2+r0 or r2>r1+r0:
    print("{}, {} e {} não formam um triangulo".format(r0,r1,r2))
else:
    if r0 == r1 == r2:
        print("{} {} e {} formam um triangulo Equilatero".format(r0, r1, r2))
    elif r1 == r2 or r2 == r0 or r0 == r1:
        print("{} {} e {} formam um triangulo Isoceles".format(r0, r1, r2))
    else:
        print("{} {} e {} formam um triangulo Escaleno".format(r0, r1, r2))
