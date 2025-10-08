operation = input().strip()

matrix = []
for i in range(12):
    row = []
    for j in range(12):
        value = float(input())
        row.append(value)
    matrix.append(row)

total = 0.0
count = 0

for i in range(12):
    for j in range(12):
        if i > j:
            total += matrix[i][j]
            count += 1

if operation == 'S':
    print(f"{total:.1f}")
elif operation == 'M':
    print(f"{(total / count):.1f}")