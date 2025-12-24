while True:
    N, M, S = map(int, input().split())

    if N == 0 and M == 0 and S == 0:
        break

    grid = []
    x = y = 0
    direction = ""

    for i in range(N):
        row = list(input())
        for j in range(M):
            if row[j] in "NSLO":
                x, y = i, j
                direction = row[j]
                row[j] = "."
        grid.append(row)

    commands = input()

    order = ["N", "L", "S", "O"]
    dx = {"N": -1, "S": 1, "L": 0, "O": 0}
    dy = {"N": 0, "S": 0, "L": 1, "O": -1}

    stickers = 0

    for cmd in commands:
        if cmd == "D":
            direction = order[(order.index(direction) + 1) % 4]
        elif cmd == "E":
            direction = order[(order.index(direction) - 1) % 4]
        else:
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != "#":
                x, y = nx, ny
                if grid[x][y] == "*":
                    stickers += 1
                    grid[x][y] = "."

    print(stickers)