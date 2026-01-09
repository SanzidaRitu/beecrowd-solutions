import math

while True:
    A, B, C = map(int, input().split())
    if A == 0 and B == 0 and C == 0:
        break

    volume = A * B * C
    edge = int(math.floor(volume ** (1 / 3)))

    print(edge)