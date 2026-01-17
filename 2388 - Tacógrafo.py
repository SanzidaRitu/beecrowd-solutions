n = int(input().strip())

total_distance = 0

for _ in range(n):
    t, v = map(int, input().split())
    total_distance += t * v

print(total_distance)