import sys

while True:
    N, V = map(int, sys.stdin.readline().split())
    if N == 0 and V == 0:
        break

    possible = False

    for S in range(1, V + 1):
        position = 0

        for speed in range(S, 0, -1):
            for _ in range(speed):
                position += speed
                if position == N:
                    possible = True
                    break
            if possible or position > N:
                break

        if possible:
            break

    if possible:
        print("possivel")
    else:
        print("impossivel")