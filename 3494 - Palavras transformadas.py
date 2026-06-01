s = input().strip()
t = input().strip()

cost = 0

for cs, ct in zip(s, t):
    diff = abs(ord(cs) - ord(ct))
    cost += min(diff, 26 - diff)

print(cost)