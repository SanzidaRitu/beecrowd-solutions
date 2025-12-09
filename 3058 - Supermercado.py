n = int(input())
lowest = 0
tp, tg = 0, 0

for i in range(n):
    p, g = map(float, input().split())
    a = float(p / g)

    if lowest == 0:
        lowest = a
        tp = p
        tg = g
    elif lowest > a:
        lowest = a
        tp = p
        tg = g

total = tp + ((1000 - tg) * (tp / tg))
print("%.2f" % total)