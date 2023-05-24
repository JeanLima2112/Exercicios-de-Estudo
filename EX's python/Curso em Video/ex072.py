# Crie um Programa Que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. seu programa deverá ler um número pelo tecldo (entre 0 e 20 ) e mostrá-lo por extenso
num = ("Zero","Um","Dois","Três","Quatro","Cinco",
       "Seis","Sete","Oito","Nove","Dez","Onze",
       "Doze","Treze","Quatorze","Quinze","Dezesseis",
       "Dezessete","Dezoito","Dezenove","Vinte")
while True:
    n = int(input("Digite um numero entre 0 e 20:"))
    if n >= 0 and n <= 20:
        break
    print("Numero invalido")
print(f"o numero digitado foi {n} por extenso {num[n]}")
