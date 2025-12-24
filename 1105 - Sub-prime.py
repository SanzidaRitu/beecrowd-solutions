while True:
    B, N = map(int, input().split())

    if B == 0 and N == 0:
        break

    balances = list(map(int, input().split()))

    for _ in range(N):
        D, C, V = map(int, input().split())
        balances[D - 1] -= V
        balances[C - 1] += V

    possible = True
    for money in balances:
        if money < 0:
            possible = False
            break

    print("S" if possible else "N")