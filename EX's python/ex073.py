# Crie um tupla preenchida com 20 os 20 primeiro colocados da tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação.Depois Mostre:
# a)Apenas os 5 primeiros colocados
# b)os 4 ultimos colocados da tabela
# c)Uma lista com os times em ordem Alfabetica
# D)Em que posição na tabela está o time do Corinthians
coloc = 1
tabela = ("Botafogo","Palmeiras","Fluminense","Athletico-PR","Cruzeiro",
          "Fortaleza","Sâo Paulo","Atlético-MG","Santos","Gremio","Internacional",
          "Flamengo","Bahia","Vasco da Gama","Bragantino","Corinthians",
          "Cuiaba","Goias","Coritiba","America-MG")
print(f"\nOs 5 primeiros colocados\n{tabela[0:5]}")
print(f"\nA zona de rebaixamento\n{tabela[16:20]}")
print(f"\nOs times em ordem Alfabetica {sorted(tabela)}\n")
print(f"Corinthians está na posição {tabela.index('Corinthians')+1}°")

