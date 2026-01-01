import itertools

while True:
    p = list(map(int, input().split()))
    if p == [0, 0, 0, 0, 0]:
        break

    princess = p[:3]
    prince = p[3:]

    used = set(p)
    answer = -1

    for card in range(1, 53):
        if card in used:
            continue

        prince_cards = prince + [card]
        princess_wins = False

        for pr_perm in itertools.permutations(princess):
            wins = 0

            for pc_perm in itertools.permutations(prince_cards):
                w = 0
                for i in range(3):
                    if pr_perm[i] > pc_perm[i]:
                        w += 1
                if w >= 2:
                    wins += 1
                    break
            if wins:
                princess_wins = True
                break

        if not princess_wins:
            answer = card
            break

    print(answer)