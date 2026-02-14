import sys

case = 1
first = True

while True:
    try:
        n = input().strip()
        if not n:
            continue
        n = int(n)

        line = input().strip()
        shoes = line.split()

        total = 0
        male = 0
        female = 0

        for i in range(0, len(shoes), 2):
            size = int(shoes[i])
            gender = shoes[i + 1]

            if size == n:
                total += 1
                if gender == 'M':
                    male += 1
                else:
                    female += 1

        if not first:
            print()
        first = False

        print(f"Caso {case}:")
        print(f"Pares Iguais: {total}")
        print(f"F: {female}")
        print(f"M: {male}")

        case += 1

    except EOFError:
        break