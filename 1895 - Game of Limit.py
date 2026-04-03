N, T, L = map(int, input().split())

stack = [int(input()) for _ in range(N - 1)]

alice = 0
bob = 0

for i in range(N - 1):
    S = stack[i]
    diff = abs(T - S)

    if diff <= L:
        if i % 2 == 0:
            alice += diff
        else:
            bob += diff
        T = S

print(alice, bob)