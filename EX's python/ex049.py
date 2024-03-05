# refaça o desafio 009, usando o laço for
num = int(input("Digite um Numero para descobrir sua tabuada:"))
print("===TABUADA===")
for cont in range(0,11):
    print(f"{cont:2} X {num:2} = {cont * num}")
print("="*13)
