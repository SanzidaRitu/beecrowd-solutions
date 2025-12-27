while True:
    n = int(input())
    if n == 0:
        break

    for _ in range(n):
        values = list(map(int, input().split()))
        filled = []

        for i in range(5):
            if values[i] <= 127:
                filled.append(chr(ord('A') + i))

        if len(filled) == 1:
            print(filled[0])
        else:
            print("*")