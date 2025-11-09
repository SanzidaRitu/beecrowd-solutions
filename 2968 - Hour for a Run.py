V, N = map(int, input().split())

total_signs = V * N

results = []
for p in range(10, 100, 10):
    signs = (total_signs * p + 99) // 100
    results.append(signs)

print(*results)