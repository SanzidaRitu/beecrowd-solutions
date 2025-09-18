op = input().strip()
mat = [float(input()) for _ in range(144)]

total = 0
count = 0
for i in range(12):
    for j in range(12):
        if j < i and j < 11 - i:
            total += mat[i * 12 + j]
            count += 1

print(f"{total:.1f}" if op == "S" else f"{total / count:.1f}")