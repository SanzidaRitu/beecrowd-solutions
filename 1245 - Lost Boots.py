while True:
    try:
        n = int(input())
        boots = {}

        for _ in range(n):
            size, side = input().split()
            size = int(size)

            if size not in boots:
                boots[size] = {'E': 0, 'D': 0}

            boots[size][side] += 1

        pairs = 0
        for size in boots:
            pairs += min(boots[size]['E'], boots[size]['D'])

        print(pairs)

    except EOFError:
        break