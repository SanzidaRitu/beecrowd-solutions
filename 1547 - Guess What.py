t = int(input())

for _ in range(t):
    qt, s = map(int, input().split())
    guesses = list(map(int, input().split()))

    min_diff = abs(guesses[0] - s)
    winner = 1

    for i in range(1, qt):
        diff = abs(guesses[i] - s)
        if diff < min_diff:
            min_diff = diff
            winner = i + 1

    print(winner)