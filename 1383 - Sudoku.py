def valid_sudoku(grid):
    for row in grid:
        if set(row) != set(range(1, 10)):
            return False

    for col in range(9):
        column = [grid[row][col] for row in range(9)]
        if set(column) != set(range(1, 10)):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = []
            for x in range(3):
                for y in range(3):
                    block.append(grid[i + x][j + y])
            if set(block) != set(range(1, 10)):
                return False

    return True

T = int(input())

for case in range(1, T + 1):
    grid = [list(map(int, input().split())) for _ in range(9)]

    print(f"Instancia {case}")
    if valid_sudoku(grid):
        print("SIM")
    else:
        print("NAO")
    print()