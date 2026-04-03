import sys

while True:
    try:
        N = int(input())
    except:
        break

    grid = [list(map(int, input().split())) for _ in range(N)]

    species_set = set()

    for _ in range(2 * N):
        x, y = map(int, input().split())
        species_set.add(grid[x - 1][y - 1])

    print(len(species_set))