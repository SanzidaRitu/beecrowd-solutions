N = int(input())

for t in range(N):
    M = int(input())
    nums = list(map(int, input().split()))

    odds = [x for x in nums if x % 2 == 1]

    if odds:
        odds.sort()
        result = []
        i, j = len(odds) - 1, 0
        take_from_end = True

        while j <= i:
            if take_from_end:
                result.append(odds[i])
                i -= 1
            else:
                result.append(odds[j])
                j += 1
            take_from_end = not take_from_end

        print(" ".join(map(str, result)))
    else:
        print()