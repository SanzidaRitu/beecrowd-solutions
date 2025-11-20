import sys
import threading
def main():
    import sys
    sys.setrecursionlimit(3000000)

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    class Fenwick:
        def __init__(self, n):
            self.n = n
            self.fw = [0] * (n + 1)

        def add(self, i, v):
            while i <= self.n:
                self.fw[i] += v
                i += i & -i

        def range_add(self, l, r, v):
            self.add(l, v)
            if r + 1 <= self.n:
                self.add(r + 1, -v)

        def query(self, i):
            s = 0
            while i > 0:
                s += self.fw[i]
                i -= i & -i
            return s

    class SegTree:
        def __init__(self, arr):
            self.n = len(arr) - 1
            self.seg = [0] * (4 * self.n)
            self.build(arr, 1, 1, self.n)

        def build(self, arr, idx, l, r):
            if l == r:
                self.seg[idx] = arr[l]
            else:
                m = (l + r) // 2
                self.build(arr, idx * 2, l, m)
                self.build(arr, idx * 2 + 1, m + 1, r)
                self.seg[idx] = gcd(self.seg[idx * 2], self.seg[idx * 2 + 1])

        def update(self, idx, l, r, pos, v):
            if l == r:
                self.seg[idx] += v
            else:
                m = (l + r) // 2
                if pos <= m:
                    self.update(idx * 2, l, m, pos, v)
                else:
                    self.update(idx * 2 + 1, m + 1, r, pos, v)
                self.seg[idx] = gcd(self.seg[idx * 2], self.seg[idx * 2 + 1])

        def query(self, idx, l, r, ql, qr):
            if qr < l or r < ql:
                return 0
            if ql <= l and r <= qr:
                return abs(self.seg[idx])
            m = (l + r) // 2
            return gcd(
                self.query(idx * 2, l, m, ql, qr),
                self.query(idx * 2 + 1, m + 1, r, ql, qr)
            )

    input_data = sys.stdin.read().strip().split()
    ptr = 0

    out = []

    while ptr < len(input_data):
        N = int(input_data[ptr]); ptr += 1
        Q = int(input_data[ptr]); ptr += 1

        arr = [0] * (N + 1)
        for i in range(1, N + 1):
            arr[i] = int(input_data[ptr])
            ptr += 1

        diff = [0] * (N + 1)
        for i in range(1, N + 1):
            diff[i] = arr[i] - (arr[i-1] if i > 1 else 0)

        fenw = Fenwick(N)
        seg = SegTree(diff)

        for _ in range(Q):
            t = int(input_data[ptr]); ptr += 1

            if t == 1:
                A = int(input_data[ptr]); ptr += 1
                B = int(input_data[ptr]); ptr += 1
                V = int(input_data[ptr]); ptr += 1

                fenw.range_add(A, B, V)
                seg.update(1, 1, N, A, V)
                if B + 1 <= N:
                    seg.update(1, 1, N, B + 1, -V)

            else:
                A = int(input_data[ptr]); ptr += 1
                B = int(input_data[ptr]); ptr += 1

                valA = arr[A] + fenw.query(A)

                if A == B:
                    out.append(str(abs(valA)))
                else:
                    g = seg.query(1, 1, N, A + 1, B)
                    out.append(str(abs(gcd(valA, g))))

    print("\n".join(out))

threading.Thread(target=main).start()