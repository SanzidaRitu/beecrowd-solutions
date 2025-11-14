import sys

sys.setrecursionlimit(10 ** 7)

def main():
    input = sys.stdin.readline

    n = int(input())
    children = [[] for _ in range(n + 1)]
    demand = [0] * (n + 1)
    cap = [10 ** 18] * (n + 1)

    for i in range(1, n + 1):
        p, r, c = map(int, input().split())
        children[p].append(i)
        demand[i] = r
        cap[i] = c

    def dfs(v):
        dp = [0]

        for ch in children[v]:
            child_dp = dfs(ch)

            new_dp = [10 ** 18] * (len(dp) + len(child_dp) - 1)
            for i in range(len(dp)):
                for j in range(len(child_dp)):
                    new_dp[i + j] = min(new_dp[i + j], dp[i] + child_dp[j])
            dp = new_dp

        if v != 0:
            new_dp = [10 ** 18] * (len(dp) + 1)

            for k in range(len(dp)):
                new_dp[k] = dp[k]

            for k in range(len(dp)):
                new_dp[k + 1] = min(new_dp[k + 1], dp[k] + demand[v])
            dp = new_dp

            for k in range(len(dp)):
                if dp[k] > cap[v]:
                    dp[k] = 10 ** 18

        return dp

    dp_root = dfs(0)

    ans = max(i for i, val in enumerate(dp_root) if val < 10 ** 18)
    print(ans)

if __name__ == "__main__":
    main()