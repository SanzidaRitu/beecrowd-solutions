N, W = map(int, input().split())

for _ in range(N):
    line = input().rstrip()

    name, h = line.rsplit(" ", 1)
    h = int(h)

    if h > W:
        print(name)