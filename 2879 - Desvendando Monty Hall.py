N = int(input())
wins = 0

for _ in range(N):
    X = int(input())

    if X != 1:
        wins += 1
print(wins)