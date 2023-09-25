while True:
    n= total = float(input("Qual o valor que você deseja sacar?(Digite 0 para encerrar):"))
    if n == 0:
        break
    if n < 0.01:
        print("Não se pode sacar valores tão pequenos")
    ced = 100
    tipo = "Notas"
    contced = 0
    while True:
        if total >= ced:
            while total >= ced:
                total = total - ced
                contced += 1
            print(f"Você podera sacar {contced} {tipo} de {ced}R$")
        if total == 0:
            break
        else:
            if total < 100:
                ced = 50
                if total < 50:
                    ced = 20
                    if total <20:
                        ced = 10
                        if total < 10:
                            ced = 4
                            if total < 4:
                                ced = 2
                                if total < 2:
                                    ced = 1
                                    if total < 1:
                                        tipo = "Moedas"
                                        ced = 0.50
                                        if total < 0.50:
                                            ced = 0.10
                                            if total < 0.10:
                                                ced = 0.05
                                                if total < 0.05:
                                                    ced = 0.01
        contced = 0
