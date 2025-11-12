import sys

for line in sys.stdin:
    if not line.strip():
        continue

    h, m = map(int, line.split())
    hour = h // 30
    minute = m // 6
    print(f"{hour:02d}:{minute:02d}")