from collections import defaultdict, deque
import sys

def main():
    input_lines = sys.stdin.read().strip().splitlines()
    n = int(input_lines[0])

    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    order = []

    for line in input_lines[1:]:
        parts = list(map(int, line.split()))
        street_id = parts[0]
        order.append(street_id)
        k = parts[1]
        neighbors = parts[2:]
        graph[street_id].extend(neighbors)
        for nbr in neighbors:
            reverse_graph[nbr].append(street_id)

    reachable_from_0 = set()
    queue = deque([0])
    while queue:
        u = queue.popleft()
        if u in reachable_from_0:
            continue
        reachable_from_0.add(u)
        for v in graph[u]:
            if v not in reachable_from_0:
                queue.append(v)

    can_reach_0 = set()
    queue = deque([0])
    while queue:
        u = queue.popleft()
        if u in can_reach_0:
            continue
        can_reach_0.add(u)
        for v in reverse_graph[u]:
            if v not in can_reach_0:
                queue.append(v)

    trapped = []
    unreachable = []

    for street_id in order:
        if street_id == 0:
            continue
        if street_id not in can_reach_0:
            trapped.append(street_id)
        if street_id not in reachable_from_0:
            unreachable.append(street_id)

    if not trapped and not unreachable:
        print("NO PROBLEMS")
        return

    for t in trapped:
        print(f"TRAPPED {t}")
    for u in unreachable:
        print(f"UNREACHABLE {u}")

if __name__ == "__main__":
    main()