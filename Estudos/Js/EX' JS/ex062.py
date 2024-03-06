# Melhore o desafio061, perguntando se o usuario quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos
a1 = int(input("Qual o primeiro termo da PA?:"))
r = int(input("Qual a razão:"))
cont = 0
print("Os 10 primeiros termos são:")
while cont < 10:
    print(f"{a1}",end="-")
    cont += 1
    a1 += r
while True:
    resp = int(input("\nDeseja mostrar mais quantos termos?:"))
    cont = 1
    if resp == 0:
        break
    while cont < resp +1:
        print(f"{a1}", end="-")
        cont += 1
        a1 += r
print("FIM")