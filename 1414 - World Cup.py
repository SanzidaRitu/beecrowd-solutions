import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    T, N = map(int, line.split())
    if T == 0:
        break

    total_points = 0
    for _ in range(T):
        parts = sys.stdin.readline().split()
        team_name = parts[0]
        pts = int(parts[1])
        total_points += pts

    draws = (3 * N) - total_points
    print(draws)