import sys
from collections import Counter

for line in sys.stdin:
    N, M = map(int, line.split())

    if N == 0 and M == 0:
        break

    tickets = list(map(int, sys.stdin.readline().split()))

    freq = Counter(tickets)

    fake_count = sum(1 for v in freq.values() if v > 1)

    print(fake_count)