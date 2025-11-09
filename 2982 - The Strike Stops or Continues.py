N = int(input())

funds = 0
expenses = 0

for _ in range(N):
    T, C = input().split()
    C = int(C)
    if T == 'V':
        funds += C
    elif T == 'G':
        expenses += C

if funds >= expenses:
    print("A greve vai parar.")
else:
    print("NAO VAI TER CORTE, VAI TER LUTA!")