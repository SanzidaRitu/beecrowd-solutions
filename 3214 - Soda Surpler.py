def total_sodas(E, F, C):
    bottles = E + F
    sodas = 0

    while bottles >= C:
        new_sodas = bottles // C
        sodas += new_sodas
        bottles = bottles % C + new_sodas

    return sodas


while True:
    try:
        line = input().strip()
        if not line:
            continue

        E, F, C = map(int, line.split())
        print(total_sodas(E, F, C))

    except EOFError:
        break