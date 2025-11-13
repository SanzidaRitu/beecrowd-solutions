from functools import lru_cache

moves = [(1, -1, 0), (-1, 1, 0),
         (1, 0, -1), (-1, 0, 1),
         (0, 1, -1), (0, -1, 1)]

@lru_cache(maxsize=None)
def count_walks(x, y, z, steps):
    if steps == 0:
        return 1 if (x, y, z) == (0, 0, 0) else 0
    total = 0
    for dx, dy, dz in moves:
        total += count_walks(x + dx, y + dy, z + dz, steps - 1)
    return total

t = int(input())
for _ in range(t):
    n = int(input())
    print(count_walks(0, 0, 0, n))