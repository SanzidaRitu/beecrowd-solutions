N = int(input())
for i in range(N):
    X, Y = map(int, input().split())
    if X > Y:
        X, Y = Y, X
    total = 0
    for j in range(X + 1, Y):
        if j % 2 != 0:
            total += j
    print(total)