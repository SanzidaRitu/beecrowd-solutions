N, S, P = map(int, input().split())
type_S = list(map(int, input().split()))

P_list = list(map(int, input().split()))

album = list(range(1, N + 1))

excluded = set(album) - set(P_list)

remaining = set(excluded) - set(type_S)

answer = len(excluded) - len(remaining)
print(answer)