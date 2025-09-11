T = int(input())

for i in range(T):
    PA, PB, G1, G2 = input().split()
    PA = int(PA)
    PB = int(PB)
    G1 = float(G1)
    G2 = float(G2)

    Years = 0

    while PA <= PB and Years <= 100:
        PA += int(PA * G1 / 100)
        PB += int(PB * G2 / 100)
        Years += 1

    if Years > 100:
        print('Mais de 1 seculo.')
    else:
        print(f'{Years} anos.')