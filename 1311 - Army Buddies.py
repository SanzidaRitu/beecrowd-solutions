import sys

for line in sys.stdin:
    S, B = map(int, line.split())
    if S == 0 and B == 0:
        break

    left = [0] * (S + 2)
    right = [0] * (S + 2)

    for i in range(1, S + 1):
        left[i] = i - 1
        right[i] = i + 1

    left[1] = 0
    right[S] = 0

    for _ in range(B):
        L, R = map(int, sys.stdin.readline().split())

        l_survivor = left[L]
        r_survivor = right[R]

        if l_survivor == 0:
            print("*", end=" ")
        else:
            print(l_survivor, end=" ")

        if r_survivor == 0:
            print("*")
        else:
            print(r_survivor)

        if l_survivor != 0:
            right[l_survivor] = r_survivor
        if r_survivor != 0:
            left[r_survivor] = l_survivor

    print("-")