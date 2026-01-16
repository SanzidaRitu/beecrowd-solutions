import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    m = int(data[1])
    A = int(data[2])
    B = int(data[3])

    adj = [[] for _ in range(n)]
    idx = 4
    for _ in range(m):
        x = int(data[idx]) - 1
        y = int(data[idx+1]) - 1
        idx += 2
        adj[x].append(y)
        adj[y].append(x)

    deg = [len(adj[i]) for i in range(n)]

    active = [True]*n
    current_size = n

    buckets = [[] for _ in range(n+1)]
    for i in range(n):
        buckets[deg[i]].append(i)

    def threshold(size):
        return size - 1 - B

    thr = threshold(current_size)

    q = deque()

    for i in range(n):
        if deg[i] < A:
            q.append(i)

    for d in range(thr+1, n+1):
        for v in buckets[d]:
            if deg[v] == d:
                q.append(v)

    while q:
        v = q.popleft()
        if not active[v]:
            continue

        if A <= deg[v] <= thr:
            continue

        active[v] = False
        current_size -= 1
        old_thr = thr
        thr = threshold(current_size)

        for nei in adj[v]:
            if active[nei]:
                old_deg = deg[nei]
                deg[nei] -= 1
                new_deg = deg[nei]
                if new_deg < A:
                    q.append(nei)
                buckets[new_deg].append(nei)

        if thr < old_thr:
            limit = old_thr
            new_limit = thr
            for d in range(limit, new_limit, -1):
                if 0 <= d <= n:
                    for x in buckets[d]:
                        if active[x] and deg[x] == d:
                            q.append(x)

    ans = sum(active)
    print(ans)

if __name__ == "__main__":
    solve()