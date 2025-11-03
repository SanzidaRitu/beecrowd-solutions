import sys

data = sys.stdin.read().strip().split()
i = 0

while i < len(data):
    x = int(data[i])
    y = int(data[i + 1])
    n = int(data[i + 2])
    i += 3
    result = []

    for _ in range(n):
        w = int(data[i]);
        h = int(data[i + 1])
        i += 2
        if (w <= x and h <= y) or (h <= x and w <= y):
            result.append("Sim")

        else:
            result.append("Nao")

    print("\n".join(result))