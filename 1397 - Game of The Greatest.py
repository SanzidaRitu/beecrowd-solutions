while True:
    n = int(input())

    if n == 0:
        break

    a_wins = 0
    b_wins = 0

    for _ in range(n):
        a, b = map(int, input().split())

        if a > b:
            a_wins += 1
        elif b > a:
            b_wins += 1

    print(a_wins, b_wins)