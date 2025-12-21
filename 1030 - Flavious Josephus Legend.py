t = int(input())

for case in range(1, t + 1):
    n, k = map(int, input().split())

    survivor = 0
    for i in range(2, n + 1):
        survivor = (survivor + k) % i

    print(f"Case {case}: {survivor + 1}")