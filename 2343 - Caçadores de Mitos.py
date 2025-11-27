from collections import defaultdict

if __name__ == "__main__":
    n = int(input())
    memo = defaultdict(dict)
    chk = 0

    for i in range(n):
        x, y = map(int, input().split())
        if x in memo and y in memo[x]:
            chk = 1
            break
        else:
            memo[x][y] = 1

    if chk == 0:
        print(0)
    else:
        print(1)