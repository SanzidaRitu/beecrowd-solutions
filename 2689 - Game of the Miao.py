from collections import Counter

p = int(input())

for _ in range(p):
    grid = [list(map(int, input().split())) for _ in range(3)]

    diffs = []
    diff_grid = [[0]*3 for _ in range(3)]

    for i in range(3):
        diff_grid[i][0] = abs(grid[i][0] - grid[i][1])
        diff_grid[i][1] = abs(grid[i][1] - grid[i][0])
        diff_grid[i][2] = abs(grid[i][2] - grid[i][1])
        diffs.extend(diff_grid[i])

    most_common_diff = Counter(diffs).most_common(1)[0][0]

    result = []

    for i in range(3):
        a, b, c = grid[i]
        if abs(a - b) != most_common_diff and abs(a - c) != most_common_diff:
            result.append(a)
        if abs(b - a) != most_common_diff and abs(b - c) != most_common_diff:
            result.append(b)
        if abs(c - a) != most_common_diff and abs(c - b) != most_common_diff:
            result.append(c)

    print("Possiveis maletas: ", end="")
    if result:
        print(", ".join(map(str, result)), end="")
    print(";")