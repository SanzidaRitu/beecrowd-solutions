d1 = int(input().split()[1])
h1, m1, s1 = map(int, input().split(':'))
d2 = int(input().split()[1])
h2, m2, s2 = map(int, input().split(':'))

differ = (d2 * 86400 + h2 * 3600 + m2 * 60 + s2) - (d1 * 86400 + h1 * 3600 + m1 * 60 + s1)

print(f'{differ // 86400} dia(s)')
differ %= 86400
print(f'{differ // 3600} hora(s)')
differ %= 3600
print(f'{differ // 60} minuto(s)')
print(f'{differ % 60} segundo(s)')