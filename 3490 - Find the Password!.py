import sys

for line in sys.stdin:
    a, b, c, d = map(int, line.split())
    print(f"{a}{b}{c}{d}")