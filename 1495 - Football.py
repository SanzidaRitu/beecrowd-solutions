import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    N, G = map(int, line.split())
    scored = []
    conceded = []

    draws = 0
    losses = []
    points = 0

    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        if a > b:
            points += 3
        elif a == b:
            draws += 1
            points += 1
        else:
            losses.append(b - a)

    while draws > 0 and G > 0:
        draws -= 1
        G -= 1
        points += 2

    losses.sort()
    for diff in losses:
        if G >= diff + 1:
            G -= (diff + 1)
            points += 3
        elif G == diff:
            G -= diff
            points += 1
        else:
            break

    print(points)