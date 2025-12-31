while True:
    n = int(input())
    if n == 0:
        break

    results = list(map(int, input().split()))

    mary = results.count(0)
    john = results.count(1)

    print(f"Mary won {mary} times and John won {john} times")