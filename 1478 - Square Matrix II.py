while True:
    N = int(input())
    if N == 0:
        break

    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            value = abs(i - j) + 1
            row.append(value)
        matrix.append(row)

    for i in range(N):
        for j in range(N):
            if j == 0:
                print(f'{matrix[i][j]:>3}', end='')
            else:
                print(f' {matrix[i][j]:>3}', end='')
        print()
    print()
