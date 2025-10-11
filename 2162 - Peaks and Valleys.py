n = int(input())
heights = list(map(int, input().split()))

if n < 2:
    print(0)
else:
    is_alternating = True

    if heights[0] == heights[1]:
        is_alternating = False
    else:
        last_direction = 1 if heights[1] > heights[0] else -1

        for i in range(1, n - 1):
            if heights[i] == heights[i + 1]:
                is_alternating = False
                break

            current_direction = 1 if heights[i + 1] > heights[i] else -1

            if current_direction == last_direction:
                is_alternating = False
                break

            last_direction = current_direction

    print(1 if is_alternating else 0)