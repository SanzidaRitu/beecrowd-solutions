while True:
    n = int(input())
    if n == 0:
        break

    a = list(map(int, input().split()))
    count = 0

    for i in range(n):
        prev = a[(i - 1) % n]
        curr = a[i]
        next_ = a[(i + 1) % n]

        if (curr > prev and curr > next_) or (curr < prev and curr < next_):
            count += 1

    print(count)