while True:
    N = int(input())
    if N == 0:
        break

    suspicion = list(map(int, input().split()))

    max1 = -1
    max2 = -1
    idx1 = -1
    idx2 = -1

    for i in range(N):
        if suspicion[i] > max1:
            max2 = max1
            idx2 = idx1
            max1 = suspicion[i]
            idx1 = i
        elif suspicion[i] > max2:
            max2 = suspicion[i]
            idx2 = i

    print(idx2 + 1)