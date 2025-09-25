while True:
    n = int(input())
    if n == 0:
        break

    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for l in range((n + 1) // 2):
        value = l + 1
        start = l
        end = n - 1 - l

        for i in range(start, end + 1):
            for j in range(start, end + 1):
                matrix[i][j] = value

    for i in range(n):
        for j in range(n):
            print(f"{matrix[i][j]:3d}", end='')
            if j < n - 1:
                print(" ", end='')
        print()
    print()
