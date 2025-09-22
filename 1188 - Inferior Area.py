op = input().strip()
matrix = []

for _ in range(12):
    row = [float(input()) for _ in range(12)]
    matrix.append(row)

total = 0.0
count = 0

for i in range(7, 12):
    for j in range(12):
        if 11 - i < j < i:
            total += matrix[i][j]
            count += 1

if op == 'S':
    print(f"{total:.1f}")
else:
    print(f"{(total / count):.1f}")