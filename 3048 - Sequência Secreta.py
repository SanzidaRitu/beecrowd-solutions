n = int(input())

count = 0
previous = None

for _ in range(n):
    current = int(input())
    if current != previous:
        count += 1
        previous = current

print(count)