x = int(input())
y = int(input())

start = min(x, y) + 1
end = max(x, y)

for i in range(start, end):
    if i % 5 == 2 or i % 5 == 3:
        print(i)