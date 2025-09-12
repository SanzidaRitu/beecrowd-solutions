N = int(input())

for i in range(N):
    X = int(input())
    num = 0

    for j in range(1, X):
        if X % j == 0:
            num += j

    if num == X:
        print(f'{X} eh perfeito')
    else:
        print(f'{X} nao eh perfeito')