a, b, c = map(int, input().split())

original = [a, b, c]
sorted = sorted(original)

for i in sorted:
    print(i)

print()

for i in original:
    print(i)