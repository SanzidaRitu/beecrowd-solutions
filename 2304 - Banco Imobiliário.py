I, N = map(int, input().split())

money = {'D': I, 'E': I, 'F': I}

for _ in range(N):
    op = input().split()

    if op[0] == 'C':
        player = op[1]
        amount = int(op[2])
        money[player] -= amount

    elif op[0] == 'V':
        player = op[1]
        amount = int(op[2])
        money[player] += amount

    elif op[0] == 'A':
        receiver = op[1]
        payer = op[2]
        amount = int(op[3])
        money[receiver] += amount
        money[payer] -= amount

print(money['D'], money['E'], money['F'])