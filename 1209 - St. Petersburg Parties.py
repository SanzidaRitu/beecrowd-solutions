import sys
from collections import deque

data = sys.stdin
readline = data.readline

while True:
    line = readline()
    if not line:
        break

    N, M, K = map(int, line.split())

    adj = [[] for _ in range(N + 1)]
    degree = [0] * (N + 1)

    for _ in range(M):
        u, v = map(int, readline().split())
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1

    removed = [False] * (N + 1)
    q = deque()

    for i in range(1, N + 1):
        if degree[i] < K:
            removed[i] = True
            q.append(i)

    while q:
        u = q.popleft()
        for v in adj[u]:
            if not removed[v]:
                degree[v] -= 1
                if degree[v] < K:
                    removed[v] = True
                    q.append(v)

    res = []
    for i in range(1, N + 1):
        if not removed[i]:
            res.append(str(i))

    if res:
        sys.stdout.write(" ".join(res) + "\n")
    else:
        sys.stdout.write("0\n")