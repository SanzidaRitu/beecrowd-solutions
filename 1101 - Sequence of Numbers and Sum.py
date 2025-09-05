while True:
    M, N = map(int, input().split())
    if M <= 0 or N <= 0:
        break
    if M > N:
        M, N = N, M
    total = 0
    for i in range(M, N + 1):
        print(i, end=' ')
        total += i
    print(f'Sum={total}')