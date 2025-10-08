op = input().strip()

matrix = []
for i in range(12):
    row = []
    for j in range(12):
        row.append(float(input()))
    matrix.append(row)

total = 0.0
count = 0

for i in range(12):
    for j in range(12):
        if i + j > 11:
            total += matrix[i][j]
            count += 1

if op == 'S':
    print(f"{total:.1f}")
elif op == 'M':
    print(f"{total / count:.1f}")