while True:
    h1, m1, h2, m2 = map(int, input().split())

    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break

    start = h1 * 60 + m1
    end = h2 * 60 + m2

    if end <= start:
        end += 24 * 60

    print(end - start)