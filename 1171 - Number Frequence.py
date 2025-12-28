n = int(input())

freq = {}

for _ in range(n):
    x = int(input())
    freq[x] = freq.get(x, 0) + 1

for key in sorted(freq):
    print(f"{key} aparece {freq[key]} vez(es)")