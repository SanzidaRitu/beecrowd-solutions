while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break

    bills = [2, 5, 10, 20, 50, 100]

    diff = M - N
    possible = 0

    for i in range(len(bills)):
        for j in range(len(bills)):
            s = bills[i] + bills[j]

            if s == diff:
                possible += 1

    if possible > 0:
        print("possible")
    else:
        print("impossible")