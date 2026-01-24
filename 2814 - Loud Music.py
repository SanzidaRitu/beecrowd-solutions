import math

N = int(input())

for _ in range(N):
    K, J = map(int, input().split())
    grid = [input().rstrip() for _ in range(J)]

    fr = fc = jr = jc = 0

    for i in range(J):
        for j in range(len(grid[i])):
            if grid[i][j] == 'F':
                fr, fc = i, j
            elif grid[i][j] == 'J':
                jr, jc = i, j

    dx = (fc - jc) * 10
    dy = (fr - jr) * 10
    distance = math.hypot(dx, dy)

    meters = int(distance)
    max_volume = K / (0.99 ** meters)

    print(f"{int(max_volume)} dBs")