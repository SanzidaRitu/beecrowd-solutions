T = int(input())

for _ in range(T):
    N = int(input())
    sheep = list(map(int, input().split()))

    distinct_colors = len(set(sheep))

    print(distinct_colors)