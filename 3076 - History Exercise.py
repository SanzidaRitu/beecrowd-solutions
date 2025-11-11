import sys
import math

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    year = int(line)
    century = (year + 99) // 100
    print(century)