while True:
    try:
        A = input()
        B = input()
        C = input()

        print(f"{A}{B}{C}")

        print(f"{B}{C}{A}")

        print(f"{C}{A}{B}")

        print(f"{A[:10]}{B[:10]}{C[:10]}")

    except EOFError:
        break