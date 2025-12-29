import sys

total = 0
count = 0

lines = sys.stdin.read().strip().splitlines()

for i in range(1, len(lines), 2):
    total += int(lines[i])
    count += 1

average = total / count
print(f"{average:.1f}")