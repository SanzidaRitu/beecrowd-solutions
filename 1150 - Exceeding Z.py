x = int(input())

y = int(input())
while y <= x:
    y = int(input())

s = 0
count = 0
i = x

while s <= y:
    s += i
    i += 1
    count += 1

print(count)