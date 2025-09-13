import math

N = int(input())

for _ in range(N):
    x = int(input())
    prime = True

    if x < 2:
        prime = False
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                prime = False
                break

    if prime:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")