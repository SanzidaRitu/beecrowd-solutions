T = int(input())
N = [0] * 1000

for i in range(1000):
    N[i] = i % T

for i in range(1000):
    print(f"N[{i}] = {N[i]}")