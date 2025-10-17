while True:
    try:
        M, N = map(int, input().split())

        matrix = []

        output = [[0 for _ in range(N)] for _ in range(M)]

        for i in range(M):
            x = input()
            row = list(map(int, x.split()))
            matrix.append(row)

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 1:
                    output[i][j] = 9

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    sum = 0

                    if i > 0 and matrix[i - 1][j] == 1:
                        sum += 1

                    if i < M-1 and matrix[i + 1][j] == 1:
                        sum += 1

                    if j > 0 and matrix[i][j - 1] == 1:
                        sum += 1

                    if j < N-1 and matrix[i][j + 1] == 1:
                        sum += 1
                    output[i][j] = sum

        for i in range(M):
            print("".join(map(str, output[i])))

    except EOFError:
        break