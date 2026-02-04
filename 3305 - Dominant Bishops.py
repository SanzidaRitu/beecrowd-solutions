import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().strip().split()
    idx = 0

    while idx < len(data):
        N = int(data[idx])
        idx += 1

        diag1 = defaultdict(int)
        diag2 = defaultdict(int)
        bishops = []

        for _ in range(N):
            x = int(data[idx])
            y = int(data[idx + 1])
            idx += 2
            bishops.append((x, y))
            diag1[x - y] += 1
            diag2[x + y] += 1

        dominant = 0
        for x, y in bishops:
            if diag1[x - y] == 1 and diag2[x + y] == 1:
                dominant += 1

        print(dominant)

if __name__ == "__main__":
    main()