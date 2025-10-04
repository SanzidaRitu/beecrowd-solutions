QT = int(input())

for i in range(QT):

    A1, X1, A2, X2 = input().split()
    N1, N2 = map(int,input().split())

    player1 = {A1:X1}
    player2 = {A2,X2}

    N = N1 + N2

    if N % 2 == 0:
        winner = "PAR"
    else:
        winner = "IMPAR"

    if X1 == winner:
        print(A1)
    else:
        print(A2)