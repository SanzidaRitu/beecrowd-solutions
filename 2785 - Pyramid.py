import sys

def solve():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    it = iter(data)
    N = next(it)
    mat = [[next(it) for _ in range(N)] for _ in range(N)]

    prefix = [[0] * (N + 1) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            prefix[i][j+1] = prefix[i][j] + mat[i][j]

    INF = 10**18
    dp = [[INF] * N for _ in range(N)]

    last_len = N
    dp[N - 1][0] = prefix[N - 1][last_len] - prefix[N - 1][0]

    for i in range(N - 2, -1, -1):
        length = i + 1
        next_max_k = N - (i + 2)
        max_j = N - length
        for j in range(0, max_j + 1):
            seg_sum = prefix[i][j + length] - prefix[i][j]
            best_below = INF

            for k in (j - 1, j):
                if 0 <= k <= next_max_k:
                    if dp[i + 1][k] < best_below:
                        best_below = dp[i + 1][k]
            dp[i][j] = seg_sum + best_below

    answer = min(dp[0][0:N])
    print(answer)

if __name__ == "__main__":
    solve()