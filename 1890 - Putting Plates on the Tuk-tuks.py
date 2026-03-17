T = int(input())

for _ in range(T):
    C, D = map(int, input().split())

    if C == 0 and D == 0:
        print(0)
    else:
        print((26 ** C) * (10 ** D))