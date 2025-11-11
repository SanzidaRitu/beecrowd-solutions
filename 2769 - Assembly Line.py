import sys

data = list(map(int, sys.stdin.read().strip().split()))
idx = 0

while idx < len(data):
    N = data[idx]; idx += 1
    e1, e2 = data[idx], data[idx+1]; idx += 2

    a1 = data[idx:idx+N]; idx += N
    a2 = data[idx:idx+N]; idx += N

    if N > 1:
        t12 = data[idx:idx+N-1]; idx += N-1
        t21 = data[idx:idx+N-1]; idx += N-1
    else:
        t12 = []
        t21 = []

    x1, x2 = data[idx], data[idx+1]; idx += 2

    f1 = [0] * N
    f2 = [0] * N

    f1[0] = e1 + a1[0]
    f2[0] = e2 + a2[0]

    for i in range(1, N):
        f1[i] = min(f1[i-1] + a1[i], f2[i-1] + t21[i-1] + a1[i])
        f2[i] = min(f2[i-1] + a2[i], f1[i-1] + t12[i-1] + a2[i])

    result = min(f1[-1] + x1, f2[-1] + x2)
    print(result)