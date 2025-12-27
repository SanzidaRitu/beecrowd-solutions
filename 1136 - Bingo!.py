while True:
    N, B = map(int, input().split())
    if N == 0 and B == 0:
        break

    balls = list(map(int, input().split()))
    balls.sort()

    possible = [False] * (N + 1)
    possible[0] = True

    for i in range(B):
        for j in range(i + 1, B):
            diff = balls[j] - balls[i]
            if diff <= N:
                possible[diff] = True

    if all(possible):
        print("Y")
    else:
        print("N")