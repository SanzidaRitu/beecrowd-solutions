import math

def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1

    if n > 1:
        result -= result // n
    return result

N = int(input())
A = list(map(int, input().split()))

max_A = max(A)
x = max_A + 1

while True:
    if phi(x) == N:
        print(x)
        break
    x += 1