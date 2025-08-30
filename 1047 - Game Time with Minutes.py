h1, m1, h2, m2 = map(int, input().split())

start = h1 * 60 + m1
end = h2 * 60 + m2

duration = (end - start) % (24 * 60) or 24 * 60

print(f'O JOGO DUROU {duration // 60} HORA(S) E {duration % 60} MINUTO(S)')