import sys
import math

for line in sys.stdin:
    if not line.strip():
        continue
    H, M = map(int, line.strip().split())

    measurements = list(map(float, sys.stdin.readline().strip().split()))

    QT = len(measurements)
    mean = sum(measurements) / QT
    variance = sum((x - mean) ** 2 for x in measurements) / (QT - 1)
    sigma = math.sqrt(variance)

    print(f"{sigma:.5f}")