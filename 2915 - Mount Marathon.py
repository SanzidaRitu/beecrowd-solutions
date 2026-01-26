N = int(input())
C = list(map(int, input().split()))

INF = 10 ** 9
dp = [INF] * (N + 1)
dp[N] = 0

can_merge = [[False] * N for _ in range(N)]

for i in range(N):
    top = C[i]
    can_merge[i][i] = True
    for j in range(i + 1, N):
        if C[j] <= top:
            top = C[j]
            can_merge[i][j] = True
        else:
            break

for i in range(N - 1, -1, -1):
    for j in range(i, N):
        if can_merge[i][j]:
            dp[i] = min(dp[i], 1 + dp[j + 1])
        else:
            break

print(dp[0])