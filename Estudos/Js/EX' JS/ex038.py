#Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem:
# o primeiro valor é maior
# o segundo valor é maior
# não existe valor maior os dois são iguais
num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))
if num1 == num2:
    print(f"Os numeros são iguais ambos são {num1}")
elif num1 > num2:
    print(f"{num1} é maior que {num2}")
else:
    print(f"{num2} é maior que {num1}")