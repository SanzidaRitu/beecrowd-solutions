while True:
    A, D = map(int, input().split())
    if A == 0 and D == 0:
        break

    attackers = list(map(int, input().split()))
    defenders = list(map(int, input().split()))

    min_attacker = min(attackers)

    defenders.sort()
    second_defender = defenders[1]

    if min_attacker < second_defender:
        print("Y")
    else:
        print("N")