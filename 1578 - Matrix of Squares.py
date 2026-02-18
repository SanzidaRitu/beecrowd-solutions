n = int(input())

matrix_number = 4

for case in range(n):
    m = int(input())

    matrix = []

    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append([x * x for x in row])

    widths = []
    for col in range(m):
        max_width = 0
        for row in range(m):
            max_width = max(max_width, len(str(matrix[row][col])))
        widths.append(max_width)

    print(f"Quadrado da matriz #{matrix_number}:")

    for row in range(m):
        for col in range(m):
            value = str(matrix[row][col]).rjust(widths[col])
            if col == 0:
                print(value, end="")
            else:
                print(" " + value, end="")
        print()

    matrix_number += 1

    if case != n - 1:
        print()