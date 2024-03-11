# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while
a1 = int(input("Qual o primeiro termo da PA?:"))
r = int(input("Qual a razão:"))
d = a1 + (11 - 1) * r
result = a1
print("Os 10 primeiros termos são:")
while result != d:
    print(f"{result}",end="-")
    result += r
print("FIM")