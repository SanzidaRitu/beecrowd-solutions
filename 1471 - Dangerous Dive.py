while True:
    try:
        N, R = map(int, input().split())
        returned = set(map(int, input().split()))

        all_divers = set(range(1, N + 1))
        missing = sorted(all_divers - returned)

        if not missing:
            print("*")
        else:
            for diver in missing:
                print(diver, end=" ")
            print()

    except EOFError:
        break