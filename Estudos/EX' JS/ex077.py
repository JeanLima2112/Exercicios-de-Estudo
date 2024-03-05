# Crie um programa que tenha uma tupla com várias palavras (não usar acentos)
# . Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ("Carro","Moto","Paralelepipedo",
            "Martelo","Trabalho","Gelo","Gordura","Abelha")
for c in palavras:
    c = c.upper()
    print(f"\n{c} Temos:",end =" ")
    for letra in c:
        if letra in "AEIOU":
            print(f"{letra.lower()}",end=" ")



