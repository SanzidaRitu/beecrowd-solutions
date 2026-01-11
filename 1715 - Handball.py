n, m = map(int, input().split())

excellent = 0

for _ in range(n):
    goals = list(map(int, input().split()))
    if all(g > 0 for g in goals):
        excellent += 1

print(excellent)