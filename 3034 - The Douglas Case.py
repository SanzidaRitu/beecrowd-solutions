import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

q = int(input())

for _ in range(q):
    n = int(input())
    x = n + 1

    if x % 7 == 0 and x % 2 == 1 and is_prime(x + 2):
        print("Yes")
    else:
        print("No")