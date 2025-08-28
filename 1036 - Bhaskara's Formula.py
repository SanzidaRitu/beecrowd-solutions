import math

A, B, C = map(float, input().split())
D = B ** 2 - 4 * A * C

if A == 0 or D < 0:
    print('Impossivel calcular')

else:
    X = (-B + math.sqrt(D)) / (2 * A)
    Y = (-B - math.sqrt(D)) / (2 * A)
    print(f'R1 = {X:.5f}')
    print(f'R2 = {Y:.5f}')