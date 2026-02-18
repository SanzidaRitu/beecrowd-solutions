import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    digits = line.replace('.', '').replace('-', '')

    a = list(map(int, digits[:9]))
    b = list(map(int, digits[9:11]))

    s1 = sum((i + 1) * a[i] for i in range(9))
    b1 = s1 % 11
    if b1 == 10:
        b1 = 0

    s2 = sum((9 - i) * a[i] for i in range(9))
    b2 = s2 % 11
    if b2 == 10:
        b2 = 0

    if [b1, b2] == b:
        print("CPF valido")
    else:
        print("CPF invalido")