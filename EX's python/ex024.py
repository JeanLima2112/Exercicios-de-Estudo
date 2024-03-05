#Crie um Programa que leia um nome de uma cidade e diga se começa com "Santo"


nome = str(input("Digite o nome da Cidade:"))
x = nome.capitalize()
y = x.split()
print("{} começa com a palavra Santo:".format(nome),"Santo" in y[0])
