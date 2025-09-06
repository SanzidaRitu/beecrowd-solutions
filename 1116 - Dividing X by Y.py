N = int(input())

for i in range(N):
    X, Y = map(int, input().split())
    if Y == 0:
        print(f'divisao impossivel')
    else:
        print(f'{X / Y:.1f}')