i = 0.0
j = 1
k = 0.0

while i <= 2.0:
    while j <= 3.0:
        if i == int(i):
            print(f'I={int(i)}', end=' ')
        else:
            print(f'I={i:.1f}', end=' ')

        if k == int(k):
            print(f'J={int(j + k)}')
        else:
            print(f'J={j + k:.1f}')

        j += 1

    j = 1
    k += 0.2
    k = round(k, 1)
    i += 0.2
    i = round(i, 1)