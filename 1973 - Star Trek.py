n = int(input())
x = list(map(int, input().split()))
total = sum(x)

a = [0] * n
i = 0

while 0 <= i < n:
    l = x[i] % 2

    if x[i] > 0:
        x[i] -= 1
        a[i] = 1
        total -= 1

    if l:
        i += 1
    else:
        i -= 1

a = a.count(1)
print(a, total)