def solve():
    try:
        while True:
            line = input().strip()
            if not line:
                continue
            E, D = map(int, line.split())

            if E > D:
                print("Eu odeio a professora!")
            elif D - E >= 3:
                print("Muito bem! Apresenta antes do Natal!")
            else:
                print("Parece o trabalho do meu filho!")
                if E + 2 < 24:
                    print("TCC Apresentado!")
                else:
                    print("Fail! Entao eh nataaaaal!")
    except EOFError:
        pass

if __name__ == "__main__":
    solve()