n = int(input())

factorials = [1]
for i in range(1, 9):
    factorials.append(factorials[-1] * i)

count = 0

for i in range(8, -1, -1):
    while factorials[i] <= n:
        n -= factorials[i]
        count += 1

print(count)