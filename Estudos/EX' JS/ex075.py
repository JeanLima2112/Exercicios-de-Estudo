# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a)Quantas vezes apareceu o valor 9
# B)Em que posição foi digitado o primeiro valor 3
# C)Quais foram os Numeros Pares
flag = False
valores = (int(input("digite o primeiro numero:")),
           int(input("Digite o Segundo Numero:")),
           int(input("Digite o Terceiro Numero:")),
           int(input("Digite o Ultimo Numero:")))
print("o valor 9 apareceu",valores.count(9)," Vezes")
if valores.count(3) != 0:
    print("O primeiro valor 3 foi digitado na posição",valores.index(3)+1)
else:
    print("Não foi digitado o valor 3.")
print("Numeros pares digitados:",end=" ")
for c in valores:
    if c % 2 == 0:
        print(f"{c}",end=" ")
        flag = True
if flag == False:
    print("Não foram digitados valores pares.")



