while True:
    N = int(input())
    if N == 0:
        break

    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(2**(i + j))
        matrix.append(row)

    maxval = len(str(matrix[N-1][N-1]))

    for i in range(N):
        for j in range(N):
            print(f'{matrix[i][j]:>{maxval}}', end='')
            if j < N - 1:
                print(' ', end='')
        print()
    print()
