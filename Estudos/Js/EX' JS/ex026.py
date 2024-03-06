# Um programa que leia uma frase pelo teclado e mostre
#Quantas vezes aparece a letra "A"
# em que posição ela aparece a primeira vez
# em que posição ela aparece a ultima vez

frase = str(input("Digite uma frase:"))
frase = frase.strip()
frase = frase.lower()
print("A frase digitada foi:{}\nExistem {} letras a\nA primeira está na posição {}\nA ultima está na posição {}".format(frase,frase.count("a"),frase.find("a"),frase.rfind("a")))