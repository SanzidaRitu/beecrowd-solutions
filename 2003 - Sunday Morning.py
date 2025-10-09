while True:
    try:

        hr, minute = map(int, input().split(':'))

        if hr < 7:
            print(f'Atraso maximo: 0')

        else:
            Xhr = hr - 7
            Xmin = (Xhr * 60) + minute
            print(f'Atraso maximo: {Xmin}')

    except EOFError:
        break