x = int(input())
z = int(input())

while z <= x:
    z = int(input())

s = 0
count = 0
i = x

while s <= z:
    s += i
    i += 1
    count += 1

print(count)