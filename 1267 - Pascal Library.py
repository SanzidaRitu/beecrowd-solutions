import sys

for line in sys.stdin:
    N, D = map(int, line.split())

    if N == 0 and D == 0:
        break

    days = []
    for _ in range(D):
        days.append(list(map(int, sys.stdin.readline().split())))

    found = False

    for student in range(N):
        attended_all = True
        for day in range(D):
            if days[day][student] == 0:
                attended_all = False
                break

        if attended_all:
            found = True
            break

    print("yes" if found else "no")