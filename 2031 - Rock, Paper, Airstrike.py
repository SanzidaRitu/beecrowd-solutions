N = int(input())

for i in range(N):
    signs = {"ataque":2,
            "pedra":1,
            "papel":0
            }

    player1 = input()
    player2 = input()

    if player1 == player2 == "ataque":
        print("Aniquilacao mutua")

    elif player1 == player2 == "papel":
        print("Ambos venceram")

    elif player1 == player2 == "pedra":
        print("Sem ganhador")

    else:
        p1_score = signs[player1]
        p2_score = signs[player2]

        if p1_score > p2_score:
            print("Jogador 1 venceu")

        else:
            print("Jogador 2 venceu")