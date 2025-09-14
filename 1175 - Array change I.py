N = []

for _ in range(20):
    value = int(input())
    N.append(value)

N.reverse()

for i in range(20):
    print(f"N[{i}] = {N[i]}")