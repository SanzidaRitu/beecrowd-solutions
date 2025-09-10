n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    if x % 2 == 0:
        x += 1

    total = 0
    count = 0

    while count < y:
        total += x
        x += 2
        count += 1

    print(total)