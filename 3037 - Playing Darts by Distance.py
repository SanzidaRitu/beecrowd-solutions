N = int(input())

for i in range(N):
    JOAO = 0
    MARIA = 0

    for i in range(3):
        a, b = map(int, input().split())
        JOAO += a * b

    for i in range(3):
        a, b = map(int, input().split())
        MARIA += a * b

    if JOAO > MARIA:
        print("JOAO")

    if MARIA > JOAO:
        print("MARIA")