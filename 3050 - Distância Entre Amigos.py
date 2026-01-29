n = int(input())
arr = list(map(int, input().split()))

best = arr[0] - 0
ans = 0

for j in range(1, n):
    ans = max(ans, best + arr[j] + j)
    best = max(best, arr[j] - j)

print(ans)