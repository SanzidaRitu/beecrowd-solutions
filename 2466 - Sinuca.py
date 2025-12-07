n = int(input())
arr = list(map(int, input().split()))

while n >= 2:
    top = []

    for i in range(1, n):
        x = arr[i] + arr[i - 1]
        if x == 0:
            top.append(-1)
        elif x == 2:
            top.append(1)
        elif x == -2:
            top.append(1)

    arr = top
    n -= 1
print('preta' if arr[0] == 1 else 'branca')