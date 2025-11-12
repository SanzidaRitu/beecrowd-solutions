while True:
    try:
        n = int(input())
        if n == 0:
            break

        gifts = list(map(int, input().split()))

        pair_sums = [gifts[i] + gifts[-i - 1] for i in range(n)]

        print(max(pair_sums), min(pair_sums))

    except EOFError:
        break