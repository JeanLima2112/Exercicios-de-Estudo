# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'
# Caso esteja errado peça para ser digitado novament até que o valor esteja correto
resp = str(input("Qual seu sexo [M] ou [F]:")).upper()
while (resp != "M") and (resp != "F"):
    resp = str(input("Digite Novamente [M] ou [F]:")).upper()
print(f"sexo {resp} registrado com sucesso")