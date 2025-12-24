while True:
    A, C = map(int, input().split())

    if A == 0 and C == 0:
        break

    heights = list(map(int, input().split()))

    total_cut = 0
    current_height = A

    for h in heights:
        if h < current_height:
            total_cut += current_height - h
        current_height = h

    print(total_cut)