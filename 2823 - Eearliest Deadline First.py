n = int(input())
total = 0.0

for _ in range(n):
    c, p = map(float, input().split())
    total += c / p

if total <= 1:
    print("OK")
else:
    print("FAIL")