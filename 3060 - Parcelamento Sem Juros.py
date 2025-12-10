V = int(input())
A = int(input())
x = int(V / A)
now = x * A
P = [x] * A

for index, x in enumerate(P):
    if now < V:
        P[index] += 1
        now += 1

for x in P:
    print(x)