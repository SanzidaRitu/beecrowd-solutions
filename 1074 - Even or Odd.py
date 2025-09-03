N = int(input())

for i in range(N):
    n = int(input())
    if n == 0:
        print('NULL')
    elif n % 2 == 0:
        if n > 0:
            print('EVEN POSITIVE')
        else:
            print('EVEN NEGATIVE')
    else:
        if n > 0:
            print('ODD POSITIVE')
        else:
            print('ODD NEGATIVE')