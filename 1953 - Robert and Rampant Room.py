import sys

while True:
    try:
        n = int(input())
    except:
        break

    epr = 0
    ehd = 0
    intrusos = 0

    for _ in range(n):
        reg, course = input().split()

        if course == "EPR":
            epr += 1
        elif course == "EHD":
            ehd += 1
        else:
            intrusos += 1

    print(f"EPR: {epr}")
    print(f"EHD: {ehd}")
    print(f"INTRUSOS: {intrusos}")