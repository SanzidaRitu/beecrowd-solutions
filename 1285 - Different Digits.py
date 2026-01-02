while True:
    try:
        a, b = map(int, input().split())
        count = 0

        for i in range(a, b + 1):
            s = str(i)
            if len(s) == len(set(s)):
                count += 1

        print(count)

    except EOFError:
        break