A, B = map(int, input().split())

if A < B:
    duration = B - A
else:
    duration = 24 - A + B

print(f'O JOGO DUROU {duration} HORA(S)')