import random

num_jogador = int(input("Quantos jogadores vão jogar? "))
jogadores= []


for i in range(num_jogador):
    nome = input("Digite o nome do jogador:")
    jogadores.append(nome)

ranking = []


for nome in jogadores:
    print(f"\nVez de {nome} jogar!")
    num = random.randint(1, 100)
    sorteNUM = 0


    while sorteNUM != num:
        chute = int(input("Adivinhe o numero de 1 a 100: "))
        sorteNUM += 1
        if chute == num:
            print("Acertou!!!!")
            break
        elif chute < num:
            print("Muito baixo")
        else:
            print("Muito alto")

    ranking.append((nome, sorteNUM))

with open("ranking.txt", "w") as arquivo:
          arquivo.write("---Ranking---\n")
          for nome, sorteNUM in ranking:
               arquivo.write(f"{nome}: {sorteNUM} tentativas\n")

print("\nRanking salvo em 'ranking.txt'")


