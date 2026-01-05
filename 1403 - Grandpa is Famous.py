while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    freq = {}

    for _ in range(N):
        for p in map(int, input().split()):
            freq[p] = freq.get(p, 0) + 1

    counts = sorted(set(freq.values()), reverse=True)

    second = counts[1]

    result = sorted(p for p in freq if freq[p] == second)

    for p in result:
        print(p, end=" ")
    print()