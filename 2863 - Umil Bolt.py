import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    T = int(line)
    times = []
    for _ in range(T):
        time = float(sys.stdin.readline().strip())
        times.append(time)
    print(f"{min(times):.2f}")