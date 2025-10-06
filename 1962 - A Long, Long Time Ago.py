N = int(input())

for i in range(N):

    T = int(input())

    d = 2015 - T

    if d < 1:
        print(f"{1 - d} A.C.")
    else:
        print(f"{d} D.C.")