while True:
    try:
        A, B = map(int, input().split())

        month = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        X = days[A] - B

        Y = 0

        for i in range(A + 1, 13):
            Y += days[i]

        C = Y + X
        D = C - 6

        if D == 0:
            print('E natal!')

        elif D == 1:
            print('E vespera de natal!')

        elif 359 >= D > 0:
            print(f"Faltam {D} dias para o natal!")

        else:
            print('Ja passou!')

    except EOFError:
        break