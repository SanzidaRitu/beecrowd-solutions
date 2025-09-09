S = 0
x = 1

for i in range(1, 39, 2):
    S += i / x
    x *= 2

print(f'{S:.2f}')