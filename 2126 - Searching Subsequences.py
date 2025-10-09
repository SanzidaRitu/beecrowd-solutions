case = 1

while True:
    try:
        n1 = input().strip()
        n2 = input().strip()

        count = 0
        last_pos = 0
        pos = n2.find(n1)

        while pos != -1:
            count += 1
            last_pos = pos + 1
            pos = n2.find(n1, pos + 1)

        print(f"Caso #{case}:")

        if count == 0:
            print("Nao existe subsequencia\n")
        else:
            print(f"Qtd.Subsequencias: {count}")
            print(f"Pos: {last_pos}\n")

        case += 1

    except EOFError:
        break