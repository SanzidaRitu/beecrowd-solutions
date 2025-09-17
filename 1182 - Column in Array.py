C = int(input())
T = input().strip()

total = 0.0
for i in range(12):
    for j in range(12):
        value = float(input())
        if j == C:
            total += value

if T == 'M':
    total /= 12

print(f"{total:.1f}")