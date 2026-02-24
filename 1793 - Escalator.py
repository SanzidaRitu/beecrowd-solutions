while True:
    N = int(input())

    if N == 0:
        break

    times = list(map(int, input().split()))

    total = 0

    for i in range(N - 1):
        total += min(10, times[i + 1] - times[i])

    total += 10

    print(total)