L = int(input())
T = input()

row = []
for i in range(12):
    for j in range(12):
        value = float(input())
        if i == L:
            row.append(value)

if T == 'S':
    print(f"{sum(row):.1f}")
else:
    print(f"{(sum(row) / 12):.1f}")