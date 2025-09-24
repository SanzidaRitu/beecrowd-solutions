operation = input()
matrix = []

for _ in range(12):
    row = []
    for _ in range(12):
        row.append(float(input()))
    matrix.append(row)

totalsum = 0
count = 0

for i in range(12):
    for j in range(12):
        if j > i and j > 11 - i:
            totalsum += matrix[i][j]
            count += 1

if operation == 'S':
    print(f"{totalsum:.1f}")
elif operation == 'M':
    if count > 0:
        average = totalsum / count
        print(f"{average:.1f}")
