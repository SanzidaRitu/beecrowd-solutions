import sys

for line in sys.stdin:
    n = int(line.strip())
    print(chr(ord('a') + n - 1))