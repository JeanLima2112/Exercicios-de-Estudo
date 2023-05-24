# Crie um programa onde o usuario possa digitar varios
# valores numericos e cadastre-os em uma lista.
# caso o número já exista lá dentro ele não será adicionado.
# No final, serão exibidos todos os valores unícos digitados em ordem crescente
lista = []
while True:
    aux =(int(input("Digite um valor para se adicionado na lista:")))
    if aux in lista:
        print("Este numero Já foi adicionado.")
    else:
        lista.append(aux)
        print(f"Numero {aux} adicionado com sucesso.")
    resp = input("Deseja continuar?[S/N]").upper().strip()[0]
    if resp == "N":
        print(f"Os numeros digitados foram: {sorted(lista)}")
        break


