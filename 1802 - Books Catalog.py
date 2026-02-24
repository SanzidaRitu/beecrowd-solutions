import sys

P, *port = map(int, input().split())
M, *math_ = map(int, input().split())
F, *phys = map(int, input().split())
Q, *chem = map(int, input().split())
B, *bio = map(int, input().split())
K = int(input())

sums = []

for p in port:
    for m in math_:
        for f in phys:
            for q in chem:
                for b in bio:
                    sums.append(p + m + f + q + b)

sums.sort(reverse=True)

print(sum(sums[:K]))