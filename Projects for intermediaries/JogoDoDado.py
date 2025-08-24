import random

num_jogador = int(input("Numero de jogadores: "))
jogadores = []
for i in  range(num_jogador):
    nome = input("Digite o nome:")
    jogadores.append(nome)

rankingDADO = []

for nome in jogadores:
    print(f"\nVez do {nome}")
    soma = 0
    for i in range(3):
        dado = random.randint(1, 6)
        print(f"Lançamento {i +1}")
        soma += dado
    print(f"Total de pontos de {nome}: {soma}")
    rankingDADO.append((nome, soma))

    rankingDADO.sort(key=lambda x: x[1], reverse= True)

with open("rankingDADO.txt", "w") as arquivo:
    arquivo.write("---Ranking---\n")
    for pos, (nome, pontos) in enumerate(rankingDADO, start =1):
        arquivo.write(f"{pos}= {nome}: {pontos} pontos\n")

print("\n Vencedor:", rankingDADO[0][0], "com", rankingDADO [0][1],"pontos!")
print("Ranking salvo em rankingDADO.txt")