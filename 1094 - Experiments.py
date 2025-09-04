N = int(input())
C = R = S =0

for i in range(N):
    A, B = input().split()
    A = int(A)
    if B == 'C':
        C += A
    elif B == 'R':
        R += A
    else:
        S += A

total = C + R + S

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {C}')
print(f'Total de ratos: {R}')
print(f'Total de sapos: {S}')
print(f'Percentual de coelhos: {(C/total) * 100:.2f} %')
print(f'Percentual de ratos: {(R/total) * 100:.2f} %')
print(f'Percentual de sapos: {(S/total) * 100:.2f} %')