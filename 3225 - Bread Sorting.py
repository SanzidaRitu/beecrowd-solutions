import sys

def inversion_parity(arr, n):
    BIT = [0] * (n + 1)

    def update(i):
        while i <= n:
            BIT[i] += 1
            i += i & -i

    def query(i):
        s = 0
        while i > 0:
            s += BIT[i]
            i -= i & -i
        return s

    inv = 0
    for i, x in enumerate(arr):
        inv += i - query(x)
        update(x)

    return inv % 2

def solve():
    data = sys.stdin.read().strip().split()
    n = int(data[0])

    start = list(map(int, data[1:n+1]))
    target = list(map(int, data[n+1:2*n+1]))

    if inversion_parity(start, n) == inversion_parity(target, n):
        print("Possible")
    else:
        print("Impossible")

if __name__ == "__main__":
    solve()