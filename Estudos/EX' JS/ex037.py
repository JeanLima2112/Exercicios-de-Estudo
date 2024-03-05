# Escreva um Programa que leia um número  inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#-1 para binário
#-2 para octal
#-3 para hexadecimal
num = int(input("Digite um numero Inteiro:"))
r = int(input("Para que base deseja Converter? \n[1]-Binário\n[2]-Octal\n[3]-Hexadecimal\nSua Opção:"))
if r == 1 :
    print(f"O numero {num} convertido para Binário equivale a {bin(num)[2:]} ")
elif r == 2:
    print(f"O numero {num} convertido para Octal equivale a {oct(num)[2:]}")
elif r == 3:
    print(f"O numero {num} convertido para Headecimal equivale a {hex(num)[2:]}")
else:
    print("O numero de conversão Não é valido")
