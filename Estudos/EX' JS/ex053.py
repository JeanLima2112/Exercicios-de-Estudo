# crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços
flag = 0
frase = input("Digite uma frase para saber se ela é um palindromo ou não:")
z = frase.lower()
x = "".join(z.split())
y = "".join(reversed(x))
for cont in range(0,len(x)):
    if x[cont] != y[cont]:
        flag += 1
if flag > 0 :
    print(f"{frase} não é u palindromo")
else :
    print(f"{frase} é um palindromo")