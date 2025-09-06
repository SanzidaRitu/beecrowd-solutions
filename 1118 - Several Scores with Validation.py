while True:
    count = 0
    total = 0
    while count < 2:
        n = float(input())
        if 0 <= n <= 10:
            total += n
            count += 1
        else:
            print("nota invalida")
    print(f"media = {total/2:.2f}")

    while True:
        print("novo calculo (1-sim 2-nao)")
        opt = int(input())
        if opt == 1:
            break
        elif opt == 2:
            exit()