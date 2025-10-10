while True:
    N = int(input())

    if N == 0:
        break

    for i in range(N):
        people = int(input())

        if people % 2 == 0:
            result = 2 * people - 2

        if people % 2 != 0:
            result = 2 * people - 1

        print(result)