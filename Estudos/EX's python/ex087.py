from random import *
import time

nums= ['0','1','2','3','4','5','6','7','8','9']
letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
especiais = ['!','@','#','$','%','&','*','ç','Ç']
masculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


senhadigit = input("Digite Uma Senha:")
TAM = len(senhadigit)
chute = []
tentativas = 0

inicio = time.time()
while True:
    for c in range(0,TAM):
        chute.append(choice(nums+letras+especiais+masculas))
        
    val = "".join(chute)
    print(val)
    if val == senhadigit:
        print(f"Descobrimos a senha:{val}\nCom {tentativas} tentativas.")
        break
    chute = []
    tentativas += 1
fim = time.time() - inicio
print(f"Foram necessarios {fim:.2f} tempo para quebrar a senha")
