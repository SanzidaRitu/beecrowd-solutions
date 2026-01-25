import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    M, N = map(int, line.split())

    total = 0
    for _ in range(M):
        total += sum(map(int, sys.stdin.readline().split()))

    sacks = total // 60
    liters = total % 60

    print(f"{sacks} saca(s) e {liters} litro(s)")