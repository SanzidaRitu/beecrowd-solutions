C = int(input().strip())

for _ in range(C):
    parts = input().split()
    a = int(parts[0])
    op = parts[1]
    b = int(parts[2])
    given = int(parts[4])

    if op == '+':
        real = a + b
    elif op == '-':
        real = a - b
    else:
        real = a * b

    if real != given:
        diff = abs(real - given)
        print("E" + "r" * diff + "ou!")