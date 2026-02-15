import sys

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, sys.stdin.readline().split())))

    count = 0

    if all(sum(row) < M for row in matrix):
        count += 1

    if all(any(matrix[i][j] == 1 for i in range(N)) for j in range(M)):
        count += 1

    if all(sum(matrix[i][j] for i in range(N)) < N for j in range(M)):
        count += 1

    if all(sum(row) > 0 for row in matrix):
        count += 1

    print(count)